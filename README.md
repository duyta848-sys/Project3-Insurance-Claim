# Project 3 — Insurance Claim Dataset

Bộ bài hoàn chỉnh Mid-Term 2 học phần Khoa học dữ liệu. Báo cáo, notebook, mã phân tích và thư mục kết quả sử dụng cùng một bộ dữ liệu và kết quả phân tích.

[Kho GitHub của nhóm](https://github.com/duyta848-sys/Project3-Insurance-Claim) · [Mở trên Colab](https://colab.research.google.com/github/duyta848-sys/Project3-Insurance-Claim/blob/main/Project3_MidTerm2.ipynb) · [Xem báo cáo PDF](Project3_MidTerm2_Report.pdf)

## Các tệp trong bộ bài cuối

| Tệp hoặc thư mục | Nội dung |
|---|---|
| [Project3_MidTerm2.ipynb](Project3_MidTerm2.ipynb) | Notebook hoàn chỉnh gồm 15 ô mã, có chú thích và diễn giải kết quả. |
| [Project3_MidTerm2_Report.pdf](Project3_MidTerm2_Report.pdf) | Báo cáo theo định dạng tiểu luận, chữ trong bảng màu đen. |
| [Project3_MidTerm2_Report.docx](Project3_MidTerm2_Report.docx) | Bản Word để nhóm bổ sung thông tin trên bìa. |
| [analysis.py](analysis.py) | Mã phân tích tương đương notebook. |
| [Insurance.csv](Insurance.csv) | Dữ liệu gốc: 1.338 dòng, 8 cột. |
| [requirements.txt](requirements.txt) | Danh sách thư viện sử dụng. |
| [outputs/](outputs/) | 28 tệp kết quả cuối: 19 CSV và 9 hình PNG. |
| [DATA_SOURCE.md](DATA_SOURCE.md) | Nguồn dữ liệu và giới hạn thông tin của bộ dữ liệu. |
| [Doi_chieu_tai_lieu.md](Doi_chieu_tai_lieu.md) | Đối chiếu các thao tác với tài liệu học phần đã cung cấp. |

## Chạy trên Colab

1. Nhấn **Mở trên Colab** ở đầu trang.
2. Chọn **Runtime → Run all** để chạy toàn bộ notebook trong một phiên mới.
3. Xem bảng, hình và phần diễn giải ngay trong notebook. Các tệp kết quả được xuất vào thư mục làm việc của phiên Colab.

Notebook chứa nguyên văn CSV gốc trong ô đọc dữ liệu, dùng `StringIO` và `pd.read_csv`. Có thể chạy độc lập, không cần tải thêm dữ liệu từ Kaggle hoặc Google Drive. `analysis.py` đọc `Insurance.csv` cùng thư mục và tạo các kết quả tương đương. Bản kết quả đã lưu trong kho nằm ở `outputs/`.

## Kết quả chính

- Dữ liệu gốc có 1.338 dòng, 8 cột và không có ô thiếu. Sau khi bỏ một dòng trùng còn 1.337 dòng.
- Nhãn 1 có 782 dòng, chiếm 58,49%; nhãn 0 có 555 dòng.
- Tỷ lệ nhãn 1 trong nhóm hút thuốc là 90,88%, trong nhóm không hút thuốc là 50,14%.
- Tập train/test gồm 1.069/268 dòng, chia có phân tầng với `random_state=42`.
- Random Forest 10 cây đạt accuracy 92,16%, precision nhãn 1 là 97,89%, recall nhãn 1 là 88,54% và ROC-AUC 0,9849 trên tập test.

## Phạm vi phương pháp và kiểm tra

Các giả định được đối chiếu với thống kê mô tả của mẫu. Bốn mô hình và tham số sử dụng theo bài thực hành tuần 15. Ngoại lệ IQR được giữ vì chưa xác định là lỗi; `charges` được loại khỏi mô hình chính do chưa rõ thời điểm quan sát.

Toàn bộ 15 ô mã đã được chạy liên tục trong một tiến trình Python mới. Mã `analysis.py` cũng đã được chạy riêng với CSV gốc; 28 bảng và hình của hai cách chạy được đối chiếu và giống hệt nhau.

Báo cáo Word và PDF có cùng nội dung. Nhóm tự bổ sung thông tin còn trống trên bìa trước khi nộp.
