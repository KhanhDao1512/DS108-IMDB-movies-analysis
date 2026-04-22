# DS107---IMDB-movies-

### 1. Nhiệm vụ Phân tích Đơn biến (Univariate Tasks)
* **Xử lý cột `num_votes` & `log_votes`:**
    * [ ] Vẽ biểu đồ Boxplot cho cột `num_votes` để trực quan hóa độ lệch phải.
    * [ ] Vẽ biểu đồ Histogram (kèm đường cong KDE) cho cột `log_votes` để kiểm tra hình dáng phân phối chuẩn.
    * [ ] Xác định ngưỡng cắt bằng phương pháp IQR (Interquartile Range) hoặc Z-score trên cột `log_votes`.
    * [ ] Viết lệnh lọc (filter) để đánh dấu hoặc loại bỏ các dòng nằm ngoài ngưỡng đã chọn.
* **Xử lý cột `rating_diff`:**
    * [ ] Vẽ biểu đồ Histogram cho cột `rating_diff`.
    * [ ] Quan sát hai đuôi của phân phối và quyết định khoảng giá trị chấp nhận được (ví dụ: chỉ giữ lại các phim có độ lệch từ -2 đến +2). Cắt bỏ phần còn lại.
* **Làm sạch Dữ liệu Chuỗi (Data Quality):**
    * [ ] Chạy lệnh `value_counts()` trên cột `director` để liệt kê toàn bộ đạo diễn.
    * [ ] Viết các biểu thức chính quy (Regex) hoặc hàm replace trong Pandas để sửa lỗi encoding (ví dụ: biến `"beyoncÃ©"` thành `"beyonce"` hoặc loại bỏ hẳn nếu là dữ liệu rác).

### 2. Nhiệm vụ Phân tích Đa biến (Multivariate Tasks)
* **Xử lý Nhiễu ngữ cảnh (Rating vs. Votes):**
    * [ ] Vẽ biểu đồ Scatter Plot với trục X là `log_votes` và trục Y là `average_rating`.
    * [ ] Quan sát góc trên cùng bên trái của biểu đồ. Xác định ngưỡng "Votes tối thiểu" (Ví dụ: phim phải có ít nhất log_votes > 3 mới được tính là uy tín).
    * [ ] Lọc bỏ các dòng có `average_rating` cao nhưng `log_votes` nằm dưới ngưỡng tối thiểu này.
* **Kiểm tra tính logic của thuật toán IMDB:**
    * [ ] Vẽ biểu đồ Scatter Plot giữa `average_rating` và `weighted_rating`.
    * [ ] Kẻ thêm một đường thẳng $y = x$ lên biểu đồ.
    * [ ] Lọc bỏ các điểm phân tán quá xa khỏi đường thẳng này (những phim bị thuật toán phạt hoặc thưởng một cách bất thường).

### 3. Nhiệm vụ Chốt hạ & Báo cáo (Finalization)
* [ ] Dùng lệnh `df.shape` để ghi nhận lại số lượng bộ phim trước khi bắt đầu quy trình lọc.
* [ ] Thực thi toàn bộ các tập lệnh cắt bỏ (Drop) Outlier ở phần 1 và phần 2.
* [ ] Dùng lại lệnh `df.shape` để ghi nhận số lượng bộ phim còn lại sau khi lọc.
* [ ] Tính toán tỷ lệ phần trăm dữ liệu đã bị loại bỏ (để đưa vào slide báo cáo chứng minh quá trình làm sạch dữ liệu).
* [ ] Lưu DataFrame đã sạch thành file `silver_layer_cleaned.csv` chuẩn bị cho bước Vector hóa (TF-IDF).

