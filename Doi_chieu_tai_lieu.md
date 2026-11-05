# Đối chiếu phương pháp với tài liệu học phần

Chỉ số ô dưới đây bắt đầu từ 0 trong tệp bài giảng; số ô mã của notebook dự án bắt đầu từ 1. Các thao tác đã học được ghép lại để xử lý đúng bộ Insurance.csv.

| Thao tác trong dự án | Tài liệu đã cung cấp | Ô mã dự án |
|---|---|---|
| `pd.read_csv` đọc CSV, đọc bằng URL | `T6_nhập_và_lưu_trữ_dữ_liệu_Python.ipynb`, ô 7-8; bản `6. Nhập_và_lưu_trữ_dữ_liệu_Python.ipynb` | 2 |
| `StringIO` chuyển văn bản thành nguồn đọc | `T7_nhập_và_lưu_trữ_dữ_liệu.ipynb`, ô 24; kết hợp với `read_csv` của T6 để đọc CSV nguyên văn | 2 |
| Xem kiểu dữ liệu, kiểm tra thiếu | `T8_Làm sạch và chuẩn bị dữ liệu.ipynb`, phần kiểm tra giá trị thiếu, ô 10 và 24-25 | 3 |
| `duplicated`, `drop_duplicates` | `T8_Làm sạch và chuẩn bị dữ liệu.ipynb`, ô 35 | 3-4 |
| Tứ phân vị, IQR, `describe` | `T8_Làm sạch và chuẩn bị dữ liệu.ipynb`, phần Robust Scaler, ô 45-47; bài thực hành tuần 15, ô 8 | 4-5 |
| Chọn dòng bằng điều kiện và `loc` | `T10_Sắp xếp và biến đổi dữ liệu.ipynb`, ô 14, 20, 24; `T8_Làm sạch và chuẩn bị dữ liệu.ipynb`, ô 50 | 7 |
| `groupby`, `count`, `sum`, `mean`, `agg` | `T10_Sắp xếp và biến đổi dữ liệu.ipynb`, ô 33-34, 92-93; `Giới thiệu về Khoa học dữ liệu.ipynb`, ô 43 | 7-9 |
| Bar, histogram, scatter, boxplot, subplot | `Data_Viz_KHDL.ipynb`; `T12_Trực quan hoá dữ liệu.ipynb`; `T13_Trực quan hoá dữ liệu.ipynb`; `Giới thiệu về Khoa học dữ liệu.ipynb`, ô 45, 56, 58, 63 | 4-10 |
| One-hot với `pd.get_dummies` | `T9_Làm sạch và chuẩn bị dữ liệu.ipynb`, ô 38; `T8_Làm sạch và chuẩn bị dữ liệu.ipynb`, ô 65 | 11 |
| Chia train/test có phân tầng | `T15_Thực hành các mô hình học máy có giám sát.ipynb`, ô 16 và 37 | 11 |
| Fit StandardScaler trên train, transform test | `T15_Thực hành các mô hình học máy có giám sát.ipynb`, ô 18 | 11 |
| Logistic Regression, KNN k=5, Decision Tree sâu 3, Random Forest 10 cây | `T15_Thực hành các mô hình học máy có giám sát.ipynb`, ô 39 | 12 |
| Accuracy, precision, recall, confusion matrix | `T15_Thực hành các mô hình học máy có giám sát.ipynb`, ô 39 | 12-13 |
| ROC, AUC, so sánh các mô hình trên cùng biểu đồ | `T15_Thực hành các mô hình học máy có giám sát.ipynb`, ô 46 và 49 | 14 |
| Biến, danh sách, điều kiện, vòng lặp, hàm | Các PDF lập trình cơ bản, rẽ nhánh, vòng lặp và các notebook Python đã cung cấp | Xuyên suốt |

Phần đối chiếu giả thuyết được thực hiện theo mô tả trong `Mid-term-2.pdf`: đối chiếu số liệu với các giả định ban đầu. Các nhận định giới hạn ở mẫu hiện có. Báo cáo không dùng thuật ngữ bác bỏ H0 hoặc có ý nghĩa thống kê để gọi một chênh lệch mô tả.

Tệp dựng Word/PDF và công cụ đóng gói không được đưa vào mã phân tích của người học. `analysis.py` và notebook là hai biểu diễn của cùng quy trình; dữ liệu trong ô đọc CSV của notebook là nguyên văn tệp gốc.
