# Say It Right - Responsible AI for Online Conversations  🌐🤖

---


## 🚀 Giới Thiệu

Trên mạng xã hội, ngôn từ thô tục và tiêu cực vẫn đang lan tràn, gây ảnh hưởng đến văn hóa giao tiếp và nhận thức cộng đồng, đặc biệt là giới trẻ. Say It Right là một tiện ích mở rộng (browser extension) sử dụng AI có trách nhiệm (Responsible AI) để phát hiện và chuyển đổi các câu bình luận độc hại thành những câu văn minh hơn mà vẫn giữ nguyên ý nghĩa gốc. Điều này giúp xây dựng một môi trường mạng lành mạnh, nơi mọi người có thể bày tỏ quan điểm một cách lịch sự và tôn trọng.

📌 Nền tảng hỗ trợ: Chrome, Firefox, Edge📌 Mô hình AI sử dụng: CafeBERT, ViT5-base📌 Ngôn ngữ: Tiếng Việt 🇻🇳

🛠️ Công Nghệ & Kiến Trúc

📌 Mô hình AI cốt lõi

- CafeBERT - Transformer model chuyên nhận diện ngôn từ độc hại.

- ViT5-base - Seq2Seq model chuyển đổi câu toxic thành nhẹ nhàng hơn.

📌 Hạ tầng và công cụ phát triển

- Google Colab - Chạy mô hình AI trên cloud.

- GitHub - Quản lý mã nguồn.

- Hugging Face - Lưu trữ và thử nghiệm mô hình AI.

- FastAPI / Flask - Xây dựng API backend.

- Docker - Đóng gói và triển khai hệ thống linh hoạt.

- Chrome Extension API - Tích hợp AI vào trình duyệt.

- WebSocket - Tăng tốc độ phản hồi từ AI đến người dùng.

---

## 💡 Vấn Đề & Giải Pháp

🔥 Thực Trạng Hiện Nay

60% người dùng từng gặp bình luận tiêu cực hoặc gây kích động.

30% nội dung trong các hội nhóm Facebook chứa lời lẽ công kích, bạo lực.

TikTok là nền tảng có tỷ lệ ngôn từ tiêu cực cao nhất (nhóm tuổi 13-24).

✅ Giải Pháp Của Chúng Tôi

✔ Phát hiện & nhận diện ngôn từ độc hại trước khi bình luận được đăng tải.

✔ Tự động chuyển đổi câu văn sang phiên bản nhẹ nhàng hơn, giữ nguyên ý nghĩa nhưng giảm cường độ tiêu cực.

✔ Tạo thói quen giao tiếp văn minh, giảm nguy cơ bị báo cáo hoặc kiểm duyệt từ nền tảng.

🔥 Ưu Điểm Cạnh Tranh

✅ Hỗ trợ tiếng Việt chuyên sâu - Nhận diện và xử lý ngôn ngữ tự nhiên hiệu quả.

✅ Kết hợp cả phát hiện & tái tạo nội dung - Không chỉ kiểm duyệt mà còn giúp người dùng giữ được quan điểm.

✅ Triển khai dễ dàng & linh hoạt - Chỉ cần cài đặt extension, không yêu cầu hạ tầng mạnh.

✅ Ứng dụng công nghệ tiên tiến - Kết hợp CafeBERT & ViT5 để tối ưu xử lý ngôn ngữ.

✅ Tối ưu chi phí triển khai - Chạy trên cloud, không tốn tài nguyên người dùng.

⚠️ Thách Thức & Hạn Chế

❌ Giới hạn về nhân lực & kinh phí - Không thể xây dựng dataset từ đầu, cần tái gán nhãn từ tập dữ liệu có sẵn.

❌ Gán nhãn dataset phụ thuộc nhiều vào AI - Có thể dẫn đến sai sót khi fine-tune mô hình Seq2Seq.

❌ Xử lý ngữ cảnh phức tạp - Một số câu toxic có ý nghĩa ẩn dụ, khó xử lý chính xác.

❌ Thay đổi nhanh chóng của ngôn ngữ mạng - Cần cập nhật liên tục để theo kịp các biến thể mới.

❌ Cạnh tranh với các hệ thống kiểm duyệt lớn - Facebook, TikTok có thể phát triển hệ thống riêng.


---

## 📅 Lộ Trình Phát Triển

🏁 Giai Đoạn 1: Nghiên Cứu & Chuẩn Bị Dữ Liệu

- Thu thập, làm sạch dữ liệu.

- EDA & chuẩn bị tập huấn luyện cho CafeBERT và ViT5-base.

🔬 Giai Đoạn 2: Fine-Tune Mô Hình

- Huấn luyện CafeBERT để phân loại toxic/non-toxic.

- Huấn luyện ViT5 để chuyển đổi câu toxic thành nhẹ nhàng hơn.

- Đánh giá model (F1-score, Precision, Recall).

🖥️ Giai Đoạn 3: Xây Dựng Web Demo

- Xây dựng API backend (FastAPI/Flask).

- Phát triển giao diện web demo (Streamlit/React).

- Triển khai lên Hugging Face Spaces / Google Cloud / AWS.

🧩 Giai Đoạn 4: Phát Triển Chrome Extension

- Viết content script để lấy nội dung bình luận từ ô nhập.

- Gọi API kiểm tra toxic/non-toxic.

- Cảnh báo & tự động chuyển đổi bình luận nếu cần.

- Bảo vệ extension bằng mật khẩu.

- Test trên Facebook, YouTube, Threads...

🚀 Giai Đoạn 5: Triển Khai & Đánh Giá

- Đóng gói & đăng ký trên Chrome Web Store.

- Chờ xét duyệt (1 - 7 ngày).

- Thu thập phản hồi & cải tiến liên tục.

---

## 📚 Dataset & Mô Hình Được Sử Dụng

### 📌 Dataset

**ViHOS - Vietnamese Hate Offensive Speech**

- Github: https://github.com/phusroyal/ViHOS 

- Hugging Face: https://huggingface.co/datasets/htdung167/ViHOS

**ViTHSD - Vietnamese Toxic & Hate Speech Detection**

- Github: https://github.com/bakansm/ViTHSD

- Paper: https://arxiv.org/abs/2404.19252

**ViHSD - Vietnamese Hate Speech Detection**

- Github: https://github.com/sonlam1102/vihsd

- Hugging Face: https://huggingface.co/datasets/htdung167/ViHSD

### 📌 Pre-trained Language Models (PLMs)
CafeBERT - Pre-trained Transformer model for Vietnamese NLP

- Paper: https://arxiv.org/abs/2403.15882

- Hugging Face: https://huggingface.co/uitnlp/CafeBERT

ViT5-base - Vietnamese T5 model for text generation

- Github: https://github.com/vietai/ViT5

- Hugging Face: https://huggingface.co/VietAI/vit5-base

- Paper: https://arxiv.org/abs/2205.06457

---

## 📬 Liên Hệ

Team Anti-Toxic Squad

*Ung Hoàng Long - Leader*

*Lương Đắc Nguyên*

*Bùi Trương Thái Sơn*

*Lê Vy*

Email: 23520892@gm.uit.edu.vn
