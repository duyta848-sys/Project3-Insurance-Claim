# Project 3 Insurance Claim Dataset

Bộ nộp Mid-Term 2 học phần Khoa học dữ liệu. Báo cáo, notebook, script, CSV và chín hình sử dụng cùng kết quả phân tích. Bìa được giữ nguyên để nhóm tự bổ sung.

Repository của nhóm: https://github.com/duyta848-sys/Project3-Insurance-Claim

[Mở notebook trên Colab sau khi tải bộ file lên GitHub](https://colab.research.google.com/github/duyta848-sys/Project3-Insurance-Claim/blob/main/Project3_MidTerm2.ipynb)

## Các tệp chính

| Tệp | Nội dung |
|---|---|
| `Project3_MidTerm2_Report.pdf` | Báo cáo chính thức theo định dạng tiểu luận, chữ trong bảng màu đen. |
| `Project3_MidTerm2_Report.docx` | Bản Word để chỉnh bìa và các thông tin nhóm. |
| `Project3_MidTerm2_Report.md` | Bản nội dung để đối chiếu nhanh, có đường dẫn tới hình. |
| `Project3_MidTerm2.ipynb` | Notebook 15 ô mã, mỗi ô có chú thích; mỗi hình có diễn giải số liệu. |
| `analysis.py` | Mã phân tích tương đương notebook, đọc CSV cùng thư mục. |
| `Insurance.csv` | Dữ liệu gốc gồm 1.338 dòng và 8 cột. |
| `outputs/Insurance_clean.csv` | Dữ liệu sau khi bỏ đúng một dòng trùng, gồm 1.337 dòng và 8 cột gốc. |
| `outputs/` | 28 tệp CSV và PNG được tạo từ cả notebook và script. |
| `Doi_chieu_tai_lieu.md` | Đối chiếu thao tác chính với tài liệu đã cung cấp. |
| `validation.json` | Kết quả kiểm tra thực thi, đối chiếu số liệu và đồng bộ bộ file. |
| `MANIFEST.sha256` | Mã kiểm tra nội dung của từng tệp trong bộ nộp. |

## Chạy trên Colab

1. Tải `Project3_MidTerm2.ipynb` lên Colab hoặc mở bằng liên kết phía trên sau khi tải lên GitHub.
2. Chọn **Runtime → Run all**. Nên dùng một runtime mới để tránh giữ biến từ lần chạy cũ.
3. Notebook chứa nguyên văn CSV gốc trong ô đọc dữ liệu, không cần Kaggle, Google Drive hoặc giải nén dữ liệu.
4. Đọc phần phân tích ngay sau từng hình. Các bảng và hình được xuất vào thư mục làm việc của phiên Colab.

Ô đọc dữ liệu dùng `StringIO` và `pd.read_csv`, dựa trên thao tác nhập dữ liệu đã có trong tài liệu. Có thể thay dòng đọc bằng URL raw của `Insurance.csv` nếu muốn đọc trực tiếp từ GitHub. Script `analysis.py` đọc `Insurance.csv` trong cùng thư mục và tạo cùng các bảng/hình.

## Tải lên GitHub bằng giao diện

1. Giải nén `Project3_MidTerm2_Full.zip`, mở thư mục `Project3_MidTerm2` bên trong.
2. Mở repository của nhóm bằng tài khoản có quyền ghi. Với kho trống, chọn **uploading an existing file**; với kho đã có tệp, chọn **Add file → Upload files**.
3. Tải các tệp và thư mục bên trong thư mục dự án lên, giữ notebook và PDF ở thư mục gốc. Chọn **Commit changes**.
4. Mở lại notebook và PDF trong danh sách tệp, kiểm tra repository ở chế độ **Public** và liên kết Colab mở đúng notebook.

URL trong báo cáo trỏ tới kho công khai chính thức của nhóm. Các tệp trong kho gồm notebook, báo cáo PDF/Word, dữ liệu, mã phân tích và kết quả đồng bộ.

## Kết quả chính

- Dữ liệu gốc: 1.338 dòng, 8 cột, không có ô thiếu; bỏ một dòng trùng còn 1.337 dòng.
- Nhãn 1: 782 dòng, chiếm 58,49%; nhãn 0: 555 dòng.
- Tỷ lệ nhãn 1 của smoker=1 là 90,88%, của smoker=0 là 50,14%.
- Train/test: 1.069/268 dòng, phân tầng, random_state=42.
- Random Forest 10 cây: accuracy test 92,16%, precision nhãn 1 là 97,89%, recall nhãn 1 là 88,54%, ROC-AUC 0,9849.
- Kết quả này thay cho các điểm số của phiên bản dùng kỹ thuật ngoài tài liệu. Không trộn điểm số cũ với bộ file hiện tại.

## Phạm vi phương pháp

Phần giả thuyết đối chiếu các giả định với số liệu mô tả theo diễn đạt của đề, không khẳng định ý nghĩa thống kê bằng p-value. Mô hình sử dụng bốn thuật toán và tham số của bài thực hành tuần 15. Bước điền thiếu không áp dụng vì không có ô thiếu; ngoại lệ IQR được giữ vì chưa xác định là lỗi. charges không đưa vào mô hình chính vì chưa rõ thời điểm quan sát.

## Kiểm tra thực thi

Người học đã xác nhận kiểm tra trên Colab trước đợt đồng bộ này. Sau khi sửa phương pháp, toàn bộ 15 ô mã của bản mới đã được chạy liên tục trong một tiến trình Python mới, không có CSV bên ngoài. Script cũng được chạy riêng với CSV gốc; 28 bảng/hình được đối chiếu và giống hệt nhau. Đây là kiểm tra thực thi của bản mới, không phải tuyên bố đã điều khiển giao diện Colab của người học.

Báo cáo Word/PDF và ZIP được cập nhật từ cùng bộ kết quả. Bìa không được chỉnh sửa trong đợt đồng bộ này.

## Đường dẫn tương thích

`Project3_Insurance_Claim.ipynb` là bản giống hệt notebook chính. `Project3_Bao_cao_Insurance_Claim.pdf` là bản giống hệt PDF chính; các đường dẫn đã chia sẻ trước đây tiếp tục mở đúng nội dung hiện tại.
