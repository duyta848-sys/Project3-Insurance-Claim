# Project 3: Insurance Claim Dataset

Bài được chỉnh theo đúng phạm vi tài liệu đã cung cấp: Python/pandas cơ bản, làm sạch dữ liệu, thống kê nhóm, biểu đồ và bốn mô hình phân loại trong T14-T15.

## Tệp chính

| Tệp | Nội dung |
|---|---|
| Project3_Bao_cao_Insurance_Claim.pdf | Báo cáo 14 trang, bốn giai đoạn, 8 hình có số liệu và diễn giải |
| Project3_Insurance_Claim.ipynb | 26 ô, gồm 13 ô mã đã chạy tuần tự không lỗi |
| analysis.py | Mã phân tích xuất từ đúng các ô mã notebook |
| Insurance.csv | Dữ liệu gốc giữ nguyên từ archive.zip |
| Insurance_clean.csv | Dữ liệu sau khi bỏ một bản sao, còn 1.337 dòng |
| Bang_*.csv; Bang_nhom_*.csv | Các bảng số liệu để kiểm chứng nhận định |
| Ma_tran_*.csv | Bốn ma trận nhầm lẫn |
| Hinh_01 đến Hinh_08 | Tám hình được dùng trong báo cáo |
| Doi_chieu_tai_lieu.md | Bảng đối chiếu lệnh/phương pháp với Sources |
| requirements.txt | Các thư viện dùng cho mã phân tích |

## Chạy trên Colab

1. Tải và mở Project3_Insurance_Claim.ipynb trong Google Colab.
2. Trong bảng Files bên trái, dùng nút Upload để tải Insurance.csv vào thư mục làm việc. Giữ nguyên tên tệp. Cần tải lại CSV khi phiên Colab mới xóa dữ liệu tạm.
3. Chọn Runtime > Run all. Không cần gắn Google Drive hoặc thêm lệnh tải dữ liệu.
4. Kết quả hiện ngay trong notebook; các bảng CSV và hình PNG được tạo tại thư mục làm việc.

Đã kiểm tra toàn bộ 13 ô mã chạy theo thứ tự trong Python với CSV được cung cấp, không lỗi. Chưa kiểm tra trực tiếp giao diện Colab. Notebook cần có Insurance.csv trong thư mục làm việc, như các ví dụ read_csv trong tài liệu lớp.

## Các quyết định trong bài

- Không có ô thiếu nên không điền mean/median chỉ để đủ bước xử lý.
- Bỏ một bản sao trùng toàn bộ theo T8-T9; thiếu ID nên chưa xác nhận trùng người.
- Dùng describe và boxplot để xem giá trị bất thường; không bổ sung phép tính ngưỡng xóa chưa được hướng dẫn.
- Đối chiếu giả thuyết bằng thống kê mô tả trong mẫu. Đây không phải kiểm định suy luận; không có p-value hoặc kết luận ý nghĩa thống kê. Nếu giảng viên yêu cầu kiểm định chính thức, cần có tài liệu hướng dẫn tương ứng đã học.
- Mô hình theo T15: train/test 80/20, random_state=42, stratify; one-hot theo T8-T9; đồng bộ cột với align theo ví dụ giá nhà; StandardScaler chỉ học trên train.
- Đánh giá Accuracy, Precision, Recall với nhãn dương 1 và ma trận nhầm lẫn. Dùng đúng bộ tham số minh họa của T15, không tinh chỉnh sau khi xem test.
- Không đưa charges vào đặc trưng vì chưa rõ thời điểm ghi nhận. Không tự gán đơn vị tiền, tên giới tính/vùng hay quan hệ nhân quả.
- Không đưa mã tạo PDF vào bài nộp: công cụ dàn trang không phải phần kiến thức phân tích.

## GitHub

Kho công khai: [Project3-Insurance-Claim](https://github.com/duyta848-sys/Project3-Insurance-Claim). Kho lưu báo cáo PDF, notebook, mã phân tích, dữ liệu và các bảng/hình của bài.

## Nguồn

Chỉ sử dụng Mid-term-2.pdf, archive.zip/Insurance.csv và các tài liệu được cung cấp trong Sources. URL bộ dữ liệu có sẵn trong đề: https://www.kaggle.com/datasets/yasserh/insurance-claim-dataset . Không tra cứu hoặc đưa thêm phương pháp từ nguồn ngoài.
