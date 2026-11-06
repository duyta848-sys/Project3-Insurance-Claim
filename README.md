# Project 3 — Insurance Claim Dataset

Bài Project 3 – Insurance Claim Dataset (Mid-Term 2, Khoa học dữ liệu).

[Kho GitHub của nhóm](https://github.com/duyta848-sys/Project3-Insurance-Claim) · [Mở trên Colab](https://colab.research.google.com/github/duyta848-sys/Project3-Insurance-Claim/blob/main/Project3_MidTerm2.ipynb) · [Xem báo cáo PDF](Project3_MidTerm2_Report.pdf)

## Các tệp trong bộ bài

| Tệp hoặc thư mục | Nội dung |
|---|---|
| [Project3_MidTerm2.ipynb](Project3_MidTerm2.ipynb) | Notebook gồm 15 phần mã, có chú thích và diễn giải kết quả. |
| [Project3_MidTerm2_Report.pdf](Project3_MidTerm2_Report.pdf) | Báo cáo dạng tiểu luận. |
| [Project3_MidTerm2_Report.docx](Project3_MidTerm2_Report.docx) | Bản Word để bổ sung thông tin trên bìa. |
| [analysis.py](analysis.py) | Mã phân tích tương đương notebook. |
| [Insurance.csv](Insurance.csv) | Dữ liệu gốc: 1.338 dòng, 8 cột. |
| [requirements.txt](requirements.txt) | Danh sách thư viện. |
| [outputs/](outputs/) | 28 tệp kết quả: 19 CSV và 9 hình PNG. |
| [DATA_SOURCE.md](DATA_SOURCE.md) | Nguồn dữ liệu. |
| [Doi_chieu_tai_lieu.md](Doi_chieu_tai_lieu.md) | Đối chiếu thao tác với tài liệu học phần. |

## Chạy trên Colab

1. Nhấn **Mở trên Colab** ở đầu trang.
2. Chọn **Runtime → Run all**.
3. Xem bảng, hình và phần diễn giải trong notebook. File kết quả xuất ra thư mục làm việc của phiên Colab.

Notebook chứa sẵn CSV gốc trong ô đọc dữ liệu (`StringIO` + `pd.read_csv`), nên chạy độc lập được. `analysis.py` đọc `Insurance.csv` cùng thư mục. Kết quả đã lưu nằm ở `outputs/`.

## Kết quả chính

- Dữ liệu gốc: 1.338 dòng, 8 cột, không có ô thiếu. Sau khi bỏ 1 dòng trùng còn 1.337 dòng.
- Nhãn 1: 782 dòng (58,49%); nhãn 0: 555 dòng.
- Tỷ lệ nhãn 1 ở nhóm hút thuốc: 90,88%; nhóm không hút thuốc: 50,14%.
- Train/test: 1.069/268 dòng, phân tầng, `random_state=42`.
- Random Forest (10 cây): accuracy test 92,16%, precision nhãn 1 97,89%, recall nhãn 1 88,54%, ROC-AUC 0,9849.

## Ghi chú phương pháp

Giả định được đối chiếu với thống kê mô tả của mẫu. Bốn mô hình lấy theo bài thực hành tuần 15. Ngoại lệ IQR giữ nguyên vì chưa chắc là lỗi; `charges` không đưa vào mô hình chính vì chưa rõ thời điểm quan sát so với nhãn.

Notebook và `analysis.py` cho kết quả giống nhau. Báo cáo Word và PDF cùng nội dung; bổ sung thông tin còn trống trên bìa trước khi nộp.
