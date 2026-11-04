# Đối chiếu mã và phương pháp với tài liệu đã cung cấp

Số ô dưới đây tính riêng các ô mã, theo thứ tự chạy 1-13.

| Ô mã | Lệnh/phương pháp chính | Tài liệu và phần tham chiếu |
|---|---|---|
| 1 | import pandas, NumPy, Matplotlib, Seaborn; read_csv, shape, head, info, describe | T6-T7 đọc CSV; T15 ô 4, 6-8 |
| 2 | DataFrame, dtypes, isna, sum; value_counts, sort_index; so sánh số và to_csv | T8 mục phát hiện missing; T15 ô 33; T6 mục lưu CSV |
| 3 | duplicated(keep=False), drop_duplicates, copy, mean | T8 mục trùng dữ liệu, ô 34-35; T9 Bài 2.1 |
| 4 | describe, subplots, sns.boxplot, savefig | T12 trực quan hóa; Giới thiệu về Khoa học dữ liệu ô 56, 58; T15 subplots |
| 5 | groupby, count, sum, mean; plot.bar | T10-T11 nhóm và tỷ trọng; Giới thiệu về Khoa học dữ liệu; T12 cột |
| 6 | mean, median, min, max; sns.histplot | T8 và T15 describe/mean/median; T12 histogram; T15 ô 10 |
| 7 | loc và điều kiện; groupby; biểu đồ cột và boxplot | T8 ví dụ loc; T10-T11; T12; Giới thiệu về Khoa học dữ liệu |
| 8 | plot.bar, tỷ lệ theo nhóm | T12 phần đồ thị cột; T10 tỷ trọng |
| 9 | groupby, mean/median; sns.scatterplot và sns.boxplot | T10; T12 scatter; Giới thiệu về Khoa học dữ liệu ô 56, 58, 63 |
| 10 | loc và phép trừ, round, print để đối chiếu nhận định | Python cơ bản và T8 truy cập dữ liệu; không thêm kiểm định suy luận |
| 11 | train_test_split, get_dummies, align, StandardScaler, fit_transform, transform | T15 ô 37; T8 ô 65; Giới thiệu về Khoa học dữ liệu ô 60, 63 |
| 12 | LogisticRegression, KNeighborsClassifier, DecisionTreeClassifier, RandomForestClassifier; fit, predict; accuracy_score, precision_score, recall_score | T15 ô 39, 42; giữ nguyên bộ tham số minh họa; nhãn dương đổi thành 1 cho bài toán này |
| 13 | confusion_matrix, sns.heatmap, enumerate, subplots, DataFrame, to_csv | T15 ô 39; bố cục đổi 2x2 cho dễ đọc, vẫn dùng cùng các lệnh vẽ |

## Các điều chỉnh phạm vi so với bản trước

Không còn phần kiểm định SciPy, hiệu chỉnh nhiều kiểm định, khoảng tin cậy Wilson, cross-validation, Pipeline/ColumnTransformer, DummyClassifier, permutation importance hoặc dữ liệu nén/nhúng trong mã. Không còn lệnh quantile/cut/corr chưa được hướng dẫn. Mã đọc CSV theo cách cơ bản và không cần lệnh giải nén hay kiểm tra mã băm.

Phần giả thuyết chỉ đối chiếu số liệu trong mẫu. Nội dung này chưa thay thế kiểm định thống kê suy luận nếu giảng viên yêu cầu theo nghĩa chặt. Các kết luận không khẳng định quan hệ nhân quả.

Công cụ dùng nội bộ để viết notebook, chạy kiểm tra và dàn trang PDF không được đưa vào phần mã phân tích của bộ nộp.
