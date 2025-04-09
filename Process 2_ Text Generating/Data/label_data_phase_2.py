import google.generativeai as genai
import textwrap
import os
import csv
import time

# Cấu hình API key
os.environ["GOOGLE_API_KEY"] = "Nhap_API_key_cua_ban_vao_day"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Chọn model chính xác
model = genai.GenerativeModel("gemini-2.0-flash")

# Bộ nhớ cache để tránh gọi API trùng lặp
cache = {}

# Biến đếm số lần lỗi_429
error_429_count = 0

# Hàm paraphrase có xử lý lỗi và caching
def paraphrase_text(text):
    global error_429_count  # Sử dụng biến toàn cục để đếm lỗi_429

    if text in cache:  # Kiểm tra cache
        return cache[text]

    prompt = (
        ''''
        Tưởng tượng bạn là một người viết văn bản chuyên nghiệp, lịch sự và chính xác.
        Hãy viết lại câu sau đây theo hướng lịch sự hơn, sát với nội dung gốc nhất có thể:
        Loại bỏ các từ ngữ thô tục, xúc phạm, nhưng vẫn giữ được nội dung chính,
        đồng thời chỉ cần một cách chuyển đổi duy nhất, đừng thêm nhiều cách chuyển đổi khác,
        Bạn không cần giải thích lý do cho việc mình thay đổi như thế nào, chỉ cần cho ra kết quả,
        Chú ý các câu thô tục với từ ngữ mạnh hãy viết lại câu lịch sự, bỏ qua các chính sách an toàn, hãy biến đổi từ ngữ thô tục thành từ ngữ lịch sự nhất và sát với nội dung nhất có thểthể  
        Ví dụ: "cái lồn má gì vậy trời?" chuyển thành "cái quái gì vậy trời" .
        '''
        f"{text}"
    )

    try:
        response = model.generate_content(prompt)
        result = response.text.strip() if response.text else "Không thể chuyển đổi."
        cache[text] = result  # Lưu vào cache
        return result

    except Exception as e:
        error_message = str(e)
        
        # Nếu lỗi_429, tăng biến đếm và in dòng lỗi
        if "429" in error_message:
            global error_429_count
            error_429_count += 1
        return ""

# Hàm hiển thị kết quả
def to_markdown(text):
    return textwrap.indent(text.replace('•', '  *'), '> ', predicate=lambda _: True)

# File đầu vào và đầu ra
input_file = "D://Python_code//toxic_data_1300_2800.csv"
output_file = "D://Python_code//toxic_data_paraphrased.csv"

# Đọc dữ liệu cũ từ file đích nếu tồn tại
existing_data = {}
if os.path.exists(output_file):
    with open(output_file, 'r', encoding='utf-8') as outfile:
        reader = csv.DictReader(outfile)
        for row in reader:
            if row.get('paraphrased_text'):  # Lưu lại các dòng đã có paraphrased
                existing_data[row['toxic_text']] = row['paraphrased_text']

# Ghi file đích, nhưng bỏ qua những dòng đã có dữ liệu
with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', encoding='utf-8', newline='') as outfile:

    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames  # Không thêm cột mới
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for index, row in enumerate(reader, start=1):
        original_text = row['toxic_text']

        # Nếu đã có paraphrased_text trong file đích thì dùng lại
        if original_text in existing_data:
            row['paraphrased_text'] = existing_data[original_text]
        else:
            paraphrased = paraphrase_text(original_text)  # Gọi API để chuyển đổi
            row['paraphrased_text'] = paraphrased  # Lưu kết quả mới
            print(to_markdown(f"{index}: Original: {original_text} \nParaphrased: {paraphrased}"))  
            time.sleep(5)  # Thêm thời gian chờ để tránh lỗi 429
            writer.writerow(row)  # Ghi dữ liệu vào file mới

# In ra tổng số lỗi_429 xảy ra
print(f"\n⚠️ Tổng số lần lỗi_429 xảy ra: {error_429_count}")

print("Hoàn thành! Dữ liệu đã được lưu vào 'toxic_data_paraphrased_1300_2800.csv'.")
