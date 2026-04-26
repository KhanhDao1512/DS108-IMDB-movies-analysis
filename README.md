# TMDb Movie Analysis: Data Preprocessing & EDA Pipeline

## Kiến trúc luồng dữ liệu (Data Pipeline)
Dự án áp dụng mô hình **Medallion Architecture** để quản lý vòng đời dữ liệu:
1.  **`preprocessed.csv`:** Dữ liệu thô ban đầu bao gồm metadata cơ bản (tiêu đề, thể loại, đạo diễn, điểm số, lượt bình chọn).
2.  **`eda_preprocessed_outliers_removed.csv`:** Dữ liệu đã được làm sạch, loại bỏ nhiễu (outliers), xử lý lỗi định dạng và nhất quán hóa logic.
3.  **`features.csv`:** Dữ liệu đặc trưng đã qua xử lý văn bản, tối ưu hóa số chiều, sẵn sàng cho thuật toán TF-IDF và tính toán Cosine Similarity.

---

## Quy trình Tiền xử lý

Quy trình trong file `eda_preprocessed.ipynb`:

### 1. Phân tích Đơn biến & Làm sạch Nhiễu (Univariate Cleaning)
* **Biến đổi Logarit & IQR cho `num_votes`:** Do lượt tương tác tuân theo định luật Pareto (phân phối lệch phải nặng), phương pháp Z-score sẽ bị vô hiệu hóa. Giải pháp: sử dụng phép biến đổi Logarit (`log_votes`) để đưa dữ liệu về phân phối tiệm cận chuẩn, sau đó áp dụng **IQR (Interquartile Range)** để xác định và loại bỏ các phim có lượt tương tác quá thấp, không đủ độ tin cậy.
* **Hard Threshold cho `rating_diff`:** Thiết lập ngưỡng chặn tuyệt đối trong khoảng [-2, 2] cho sự chênh lệch giữa điểm trung bình và điểm trọng số TMDB. Điều này giúp loại bỏ tận gốc các trường hợp bị **Review Bombing** hoặc sai lệch thuật toán nghiêm trọng.
* **Kiểm soát chất lượng văn bản (Regex):** Xử lý lỗi mã hóa **Mojibake** (vd: chuyển `beyoncé` thành `beyonce`) thông qua Regular Expression để đảm bảo tính toàn vẹn của thực thể định danh trước khi đưa vào mô hình NLP.

### 2. Phân tích Đa biến & Loại bỏ nhiễu ngữ cảnh
* **Triệt tiêu "Ảo điểm" (Contextual Outliers):** Thông qua biểu đồ phân tán (Scatter Plot) giữa `log_votes` và `average_rating`, loại bỏ các phim có điểm số cao tuyệt đối nhưng lượt bình chọn cực thấp. Việc này đảm bảo hệ thống chỉ đề xuất những tác phẩm đã được cộng đồng kiểm chứng (Verified quality).
* **Kiểm định logic thuật toán:** Đối chiếu tính nhất quán giữa điểm số thô và điểm trọng số dựa trên đường phân giác y=x, đảm bảo đặc trưng `weighted_rating` phản ánh đúng giá trị thực của bộ phim.

### 3. Tối ưu hóa Không gian Dữ liệu
* **Xử lý Metadata thưa (Sparsity Handling):** Giải pháp để tránh Curse of Dimensionality là gom nhóm hàng ngàn đạo diễn chỉ xuất hiện một lần vào nhãn `unknown_director`, điều này giúp nén không gian Vector TF-IDF, tối ưu tài nguyên tính toán mà không làm mất đi giá trị nội dung của phim.

---

## Kết quả nghiệm thu dữ liệu
* **Số lượng phim ban đầu:** 9,993
* **Số lượng phim sau làm sạch:** 9666
* **Số lượng Outliers bị loại bỏ:** ~327
* **Tỷ lệ giữ lại dữ liệu:** 96.73% 

---
