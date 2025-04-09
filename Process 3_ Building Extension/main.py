from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, AutoModelForSequenceClassification
import torch

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tách biệt device cho từng model
device_classifier = "cpu"  # Luôn chạy trên CPU để tiết kiệm VRAM
device_seq2seq = "cuda" if torch.cuda.is_available() else "cpu"

# Load model phân loại (trên CPU)
CLASSIFIER_NAME = "UngLong/cafebert-classification-ft"
tokenizer_classifier = AutoTokenizer.from_pretrained(CLASSIFIER_NAME)
model_classifier = AutoModelForSequenceClassification.from_pretrained(CLASSIFIER_NAME)
model_classifier.to(device_classifier)  # Đẩy model phân loại vào CPU

# Load model seq2seq (trên GPU nếu có)
SEQ2SEQ_NAME = "Nosiath/ViT5-base-finetuned"
tokenizer_seq2seq = AutoTokenizer.from_pretrained(SEQ2SEQ_NAME)
model_seq2seq = AutoModelForSeq2SeqLM.from_pretrained(SEQ2SEQ_NAME)
model_seq2seq.to(device_seq2seq)  # Đẩy model seq2seq vào GPU/CPU

class TextInput(BaseModel):
    text: str

def predict_label(text: str):
    # Tokenize và xử lý trên CPU
    inputs = tokenizer_classifier(text, return_tensors="pt").to(device_classifier)
    with torch.no_grad():
        outputs = model_classifier(**inputs)
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    return 1 if probabilities[0, 1] > 0.5 else 0

@app.post("/predict/")
async def predict(input_data: TextInput):
    text = input_data.text
    
    # Kiểm tra phân loại (chạy trên CPU)
    label = predict_label(text)
    
    if label == 1:
        # Xử lý bằng model seq2seq (trên GPU/CPU)
        inputs = tokenizer_seq2seq(
            text, 
            return_tensors="pt", 
            max_length=200, 
            truncation=True
        ).to(device_seq2seq)  # Đảm bảo inputs cùng device với model
        
        outputs = model_seq2seq.generate(
            **inputs,
            max_length=200,
            no_repeat_ngram_size=3,
            num_beams=10,  # Giảm num_beams từ 20 -> 10 để tiết kiệm bộ nhớ
            early_stopping=True,
            length_penalty=30.0,
            min_length=5,
            repetition_penalty=1.5
        )
        polite_text = tokenizer_seq2seq.decode(outputs[0], skip_special_tokens=True)
    else:
        polite_text = text
    
    return {"original": text, "polite": polite_text}

if __name__ == "__main__":
    model_size = sum(p.numel() * p.element_size() for p in model_classifier.parameters())
    print(f"Kích thước mô hình classifier (trên RAM): {model_size / (1024 * 1024):.2f} MB")
    model_size = sum(p.numel() * p.element_size() for p in model_seq2seq.parameters())
    print(f"Kích thước mô hình seq2seq (trên RAM): {model_size / (1024 * 1024):.2f} MB")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)