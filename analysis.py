# %% 01 Nhập thư viện
# Nhập các thư viện đã dùng trong tài liệu học phần.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn.metrics import roc_curve, roc_auc_score

# Đặt phông có dấu tiếng Việt và màu chữ của hình.
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['text.color'] = 'black'
plt.rcParams['axes.labelcolor'] = 'black'
plt.rcParams['xtick.color'] = 'black'
plt.rcParams['ytick.color'] = 'black'


# %% 02 Đọc dữ liệu gốc
# Đọc tệp CSV trong cùng thư mục với analysis.py.
df_goc = pd.read_csv('Insurance.csv')
print('Kích thước dữ liệu gốc:', df_goc.shape)
print(df_goc.head().to_string(index=False))


# %% 03 Kiểm tra chất lượng dữ liệu
# Kiểm tra kiểu dữ liệu, số ô thiếu và miền giá trị của từng cột.
kiem_tra = pd.DataFrame({
    'bien': df_goc.columns,
    'kieu_du_lieu': df_goc.dtypes.astype(str).values,
    'so_o_thieu': df_goc.isna().sum().values,
    'nho_nhat': df_goc.min().values,
    'lon_nhat': df_goc.max().values
})
kiem_tra.to_csv('Bang01_Kiem_tra_du_lieu.csv', index=False)
print(kiem_tra.to_string(index=False))

# Lưu cả hai dòng giống nhau làm minh chứng, nhưng chỉ một dòng là lặp vượt bản đầu.
dong_trung = df_goc[df_goc.duplicated(keep=False)]
dong_trung.to_csv('Bang02_Dong_trung.csv', index_label='chi_so_dong')
print('Tổng ô thiếu:', df_goc.isna().sum().sum())
print('Số dòng lặp vượt bản đầu:', df_goc.duplicated().sum())
print(dong_trung.to_string())


# %% 04 Ngoại lệ và làm sạch
# Tính IQR cho biến định lượng; không áp dụng cho mã sex, smoker, region hoặc nhãn.
ngoai_le = []
for cot in ['age', 'bmi', 'children', 'charges']:
    q1 = df_goc[cot].describe()['25%']
    q3 = df_goc[cot].describe()['75%']
    iqr = q3 - q1
    duoi = q1 - 1.5 * iqr
    tren = q3 + 1.5 * iqr
    so_danh_dau = ((df_goc[cot] < duoi) | (df_goc[cot] > tren)).sum()
    ngoai_le.append([cot, q1, q3, iqr, duoi, tren, so_danh_dau])
ngoai_le = pd.DataFrame(ngoai_le, columns=['bien', 'Q1', 'Q3', 'IQR', 'nguong_duoi', 'nguong_tren', 'so_danh_dau'])
ngoai_le.to_csv('Bang03_Ngoai_le_IQR.csv', index=False)
print(ngoai_le.to_string(index=False))

# Vẽ bằng chứng ngoại lệ của BMI và chi phí trên dữ liệu gốc.
fig, axes = plt.subplots(1, 2, figsize=(10, 3.4))
for ax, cot in zip(axes, ['bmi', 'charges']):
    sns.boxplot(x=df_goc[cot], ax=ax, color='#c4dfe2')
    ax.set_title('Ngoại lệ: ' + cot)
    ax.set_xlabel(cot)
plt.tight_layout()
plt.savefig('Hinh01_Ngoai_le.png', dpi=180)
plt.show()
plt.close()

# Không điền thiếu vì dữ liệu không có ô thiếu; giữ các giá trị IQR đánh dấu.
# Bỏ đúng một dòng lặp hoàn toàn, trước khi chia tập huấn luyện và kiểm tra.
df = df_goc.drop_duplicates().copy()
df.to_csv('Insurance_clean.csv', index=False)
print('Kích thước sau xử lý:', df.shape)
print('Số dòng trùng còn lại:', df.duplicated().sum())


# %% 05 Phân bố nhãn và thống kê mô tả
# Thống kê nhãn và các biến định lượng sau khi bỏ dòng trùng.
nhan = df['insuranceclaim'].value_counts().sort_index().rename_axis('nhan').reset_index(name='so_ban_ghi')
nhan['ty_le_phan_tram'] = nhan['so_ban_ghi'] / len(df) * 100
nhan.to_csv('Bang04_Phan_bo_nhan.csv', index=False)
mo_ta = df[['age', 'bmi', 'children', 'charges']].describe().T
mo_ta.to_csv('Bang05_Thong_ke_mo_ta.csv', index_label='bien')
print(nhan.to_string(index=False))
print(mo_ta.to_string())

# Vẽ cột phân bố nhãn, ghi rõ cả số lượng và tỷ lệ.
plt.figure(figsize=(7, 4))
bars = plt.bar(['Không yêu cầu (0)', 'Có yêu cầu (1)'], nhan['so_ban_ghi'], color=['#377f88', '#d39838'])
for bar, n, ty_le in zip(bars, nhan['so_ban_ghi'], nhan['ty_le_phan_tram']):
    plt.text(bar.get_x() + bar.get_width()/2, n + 8, f'{n}\n{ty_le:.2f}%', ha='center', color='black')
plt.ylim(0, 900)
plt.ylabel('Số bản ghi')
plt.title('Phân bố nhãn sau khi bỏ dòng trùng')
plt.tight_layout()
plt.savefig('Hinh02_Phan_bo_nhan.png', dpi=180)
plt.show()
plt.close()


# %% 06 Phân bố biến định lượng
# Vẽ histogram của bốn biến định lượng, không thay đổi dữ liệu gốc.
fig, axes = plt.subplots(2, 2, figsize=(9.5, 6.2))
for ax, cot in zip(axes.flat, ['age', 'bmi', 'children', 'charges']):
    ax.hist(df[cot], bins=20, color='#377f88', edgecolor='white')
    ax.set_title('Phân bố ' + cot)
    ax.set_xlabel(cot)
    ax.set_ylabel('Số bản ghi')
plt.tight_layout()
plt.savefig('Hinh03_Phan_bo_bien.png', dpi=180)
plt.show()
plt.close()


# %% 07 So sánh hút thuốc, tuổi, BMI và người phụ thuộc
# Phân nhóm theo ngưỡng được xác định trước khi đọc kết quả so sánh.
df['nhom_tuoi'] = '45-64'
df.loc[df['age'] <= 29, 'nhom_tuoi'] = '18-29'
df.loc[(df['age'] >= 30) & (df['age'] <= 44), 'nhom_tuoi'] = '30-44'
df['nhom_bmi'] = '>=40'
df.loc[df['bmi'] < 25, 'nhom_bmi'] = '<25'
df.loc[(df['bmi'] >= 25) & (df['bmi'] < 30), 'nhom_bmi'] = '25-<30'
df.loc[(df['bmi'] >= 30) & (df['bmi'] < 35), 'nhom_bmi'] = '30-<35'
df.loc[(df['bmi'] >= 35) & (df['bmi'] < 40), 'nhom_bmi'] = '35-<40'

# Tóm tắt từng nhóm, luôn đọc tỷ lệ cùng với cỡ mẫu.
nhom = {}
for cot in ['smoker', 'nhom_tuoi', 'nhom_bmi', 'children', 'sex', 'region']:
    bang = df.groupby(cot, observed=True)['insuranceclaim'].agg(['count', 'sum', 'mean']).reset_index()
    bang.columns = [cot, 'so_ban_ghi', 'so_nhan_1', 'ty_le_nhan_1']
    if cot == 'nhom_bmi':
        bang = bang.set_index(cot).loc[['<25', '25-<30', '30-<35', '35-<40', '>=40']].reset_index()
    bang['ty_le_nhan_1'] = bang['ty_le_nhan_1'] * 100
    nhom[cot] = bang
    bang.to_csv('Bang06_Nhom_' + cot + '.csv', index=False)
    print('\nTheo', cot)
    print(bang.to_string(index=False))

# Vẽ tỷ lệ có nhãn 1 theo bốn đặc điểm; không dùng khoảng tin cậy ngoài tài liệu.
fig, axes = plt.subplots(2, 2, figsize=(10, 6.5))
for ax, cot in zip(axes.flat, ['smoker', 'nhom_tuoi', 'nhom_bmi', 'children']):
    bang = nhom[cot]
    ax.bar(bang[cot].astype(str), bang['ty_le_nhan_1'], color='#377f88')
    ax.set_ylim(0, 105)
    ax.set_title('Theo ' + cot)
    ax.set_ylabel('Tỷ lệ nhãn 1 (%)')
    for i, n in enumerate(bang['so_ban_ghi']):
        ax.text(i, bang.iloc[i]['ty_le_nhan_1'] + 2, 'n=' + str(n), ha='center', fontsize=8, color='black')
plt.tight_layout()
plt.savefig('Hinh04_So_sanh_nhom.png', dpi=180)
plt.show()
plt.close()


# %% 08 So sánh mã giới tính và vùng cư trú
# So sánh nhóm sex và region bằng tỷ lệ, không coi mã region là số đo liên tục.
fig, axes = plt.subplots(1, 2, figsize=(9.5, 3.8))
for ax, cot in zip(axes, ['region', 'sex']):
    bang = nhom[cot]
    ax.bar(bang[cot].astype(str), bang['ty_le_nhan_1'], color='#7793b0')
    ax.set_title('Theo mã ' + cot)
    ax.set_xlabel('Mã ' + cot)
    ax.set_ylim(0, 90)
    ax.set_ylabel('Tỷ lệ nhãn 1 (%)')
    for i, n in enumerate(bang['so_ban_ghi']):
        ax.text(i, bang.iloc[i]['ty_le_nhan_1'] + 2, 'n=' + str(n), ha='center', color='black')
plt.tight_layout()
plt.savefig('Hinh05_Vung_Gioi.png', dpi=180)
plt.show()
plt.close()


# %% 09 Chi phí y tế và thời điểm thông tin
# Thống kê charges theo nhãn, giữ nguyên đơn vị gốc của CSV.
chi_phi = df.groupby('insuranceclaim')['charges'].agg(['count', 'mean', 'median']).reset_index()
chi_phi.to_csv('Bang07_Chi_phi_theo_nhan.csv', index=False)
print(chi_phi.to_string(index=False))

# Vẽ chi phí theo nhãn và quan hệ BMI-chi phí theo nhóm hút thuốc.
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
sns.boxplot(data=df, x='insuranceclaim', y='charges', color='#c4dfe2', ax=axes[0])
axes[0].set_title('Chi phí theo nhãn')
axes[0].set_xlabel('Nhãn yêu cầu bảo hiểm')
axes[0].set_ylabel('charges (đơn vị gốc)')
sns.scatterplot(data=df, x='bmi', y='charges', hue='smoker', alpha=0.5,
                palette=['#377f88', '#d39838'], ax=axes[1])
axes[1].set_title('BMI, chi phí và hút thuốc')
axes[1].set_ylabel('charges (đơn vị gốc)')
plt.tight_layout()
plt.savefig('Hinh06_Chi_phi.png', dpi=180)
plt.show()
plt.close()


# %% 10 Quan sát mối liên hệ và đối chiếu giả định
# Quan sát đồng thời tuổi, BMI và nhãn, rồi đọc phân bố số người phụ thuộc theo nhãn.
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
sns.scatterplot(data=df, x='age', y='bmi', hue='insuranceclaim', alpha=0.4,
                palette=['#377f88', '#d39838'], ax=axes[0])
axes[0].set_title('Tuổi, BMI và nhãn')
sns.boxplot(data=df, x='insuranceclaim', y='children', color='#c4dfe2', ax=axes[1])
axes[1].set_title('Người phụ thuộc theo nhãn')
axes[1].set_xlabel('Nhãn yêu cầu bảo hiểm')
axes[1].set_ylabel('Số người phụ thuộc')
plt.tight_layout()
plt.savefig('Hinh07_Moi_lien_he.png', dpi=180)
plt.show()
plt.close()

# Đối chiếu giả định bằng số liệu mô tả, không dùng kết luận bác bỏ H0.
print('Hút thuốc: đọc tỷ lệ nhãn 1 của smoker=0 và smoker=1 trong Bang06_Nhom_smoker.csv.')
print('Tuổi: so sánh ba nhóm 18-29, 30-44, 45-64; kiểm tra có tăng đều hay không.')
print('BMI: so sánh tỷ lệ giữa các khoảng BMI và quan sát hai nhãn trên scatter plot.')
print('Chi phí: đọc trung bình và trung vị theo nhãn trong Bang07_Chi_phi_theo_nhan.csv.')
print('Các nhận xét chỉ áp dụng cho bộ dữ liệu đang phân tích; chưa phải kiểm định suy luận.')


# %% 11 Mã hóa và chia tập dữ liệu
# One-hot mã vùng vì các mã 0, 1, 2, 3 không có khoảng cách định lượng.
X = pd.get_dummies(df[['age', 'bmi', 'children', 'sex', 'smoker', 'region']],
                   columns=['region'], drop_first=True)
y = df['insuranceclaim']

# Chia phân tầng giống cách thực hành trong tài liệu tuần 15.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                 random_state=42, stratify=y)

# Chỉ học tham số chuẩn hóa từ train, tránh dùng thông tin của test.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print('Train:', X_train.shape, 'Test:', X_test.shape)
print('Các đặc trưng:', list(X.columns))
print('Tỷ lệ nhãn 1 trên test:', y_test.mean())


# %% 12 Huấn luyện và so sánh bốn mô hình
# Khởi tạo đúng bốn mô hình cơ bản và các tham số minh họa của tuần 15.
models = {
    'Logistic Regression': LogisticRegression(random_state=42),
    'KNN': KNeighborsClassifier(n_neighbors=5),
    'Decision Tree': DecisionTreeClassifier(max_depth=3, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=10, random_state=42)
}

# Đánh giá cùng một cách chia để các điểm số có thể so sánh.
ket_qua = []
du_doan = pd.DataFrame({'chi_so_dong': y_test.index, 'nhan_thuc_te': y_test.values})
ma_tran = {}
for ten, model in models.items():
    model.fit(X_train_scaled, y_train)
    pred_train = model.predict(X_train_scaled)
    pred = model.predict(X_test_scaled)
    proba = model.predict_proba(X_test_scaled)[:, 1]
    acc_train = accuracy_score(y_train, pred_train)
    acc = accuracy_score(y_test, pred)
    prec = precision_score(y_test, pred, pos_label=1)
    rec = recall_score(y_test, pred, pos_label=1)
    auc = roc_auc_score(y_test, proba)
    ket_qua.append([ten, acc_train, acc, prec, rec, auc])
    du_doan[ten] = pred
    ma_tran[ten] = confusion_matrix(y_test, pred)
    pd.DataFrame(ma_tran[ten], index=['Thuc_te_0', 'Thuc_te_1'],
                 columns=['Du_doan_0', 'Du_doan_1']).to_csv('Ma_tran_' + ten.replace(' ', '_') + '.csv')
ket_qua = pd.DataFrame(ket_qua, columns=['mo_hinh', 'accuracy_train', 'accuracy_test', 'precision_1', 'recall_1', 'roc_auc'])
ket_qua.to_csv('Bang09_Ket_qua_mo_hinh.csv', index=False)
du_doan.to_csv('Bang10_Du_doan_test.csv', index=False)
print(ket_qua.to_string(index=False))
print('Mốc luôn dự đoán nhãn 1 trên test:', y_test.mean())


# %% 13 Ma trận nhầm lẫn
# Hiển thị đủ bốn ma trận để thấy đánh đổi giữa bỏ sót và dự đoán nhầm.
fig, axes = plt.subplots(2, 2, figsize=(9, 7))
for ax, (ten, bang) in zip(axes.flat, ma_tran.items()):
    sns.heatmap(bang, annot=True, fmt='d', cmap='Blues', alpha=0.35,
                annot_kws={'color': 'black'}, cbar=False, ax=ax,
                xticklabels=['0', '1'], yticklabels=['0', '1'])
    ax.set_title(ten)
    ax.set_xlabel('Dự đoán')
    ax.set_ylabel('Thực tế')
plt.tight_layout()
plt.savefig('Hinh08_Ma_tran_nham_lan.png', dpi=180)
plt.show()
plt.close()


# %% 14 Đường cong ROC và AUC
# Vẽ ROC trên cùng tập kiểm tra, giữ nguyên mô hình đã huấn luyện.
plt.figure(figsize=(7.5, 5))
for ten, model in models.items():
    proba = model.predict_proba(X_test_scaled)[:, 1]
    fpr, tpr, thresholds = roc_curve(y_test, proba)
    auc = roc_auc_score(y_test, proba)
    plt.plot(fpr, tpr, label=f'{ten}: {auc:.3f}')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('Tỷ lệ dương tính giả')
plt.ylabel('Tỷ lệ dương tính thật')
plt.title('ROC của bốn mô hình trên tập test')
plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('Hinh09_ROC.png', dpi=180)
plt.show()
plt.close()


# %% 15 Tổng hợp phát hiện và kiểm tra đầu ra
# Tổng hợp các phát hiện chính bằng số liệu vừa tính, không dùng số từ phiên bản cũ.
print('Gốc:', len(df_goc), 'Sau bỏ trùng:', len(df))
print('Không có nhãn yêu cầu:', (df['insuranceclaim'] == 0).sum())
print('Có nhãn yêu cầu:', (df['insuranceclaim'] == 1).sum())
print('Tỷ lệ theo hút thuốc:')
print(nhom['smoker'].to_string(index=False))
print('Kết quả mô hình:')
print(ket_qua.to_string(index=False))

# Nêu phạm vi ứng dụng và giới hạn của dữ liệu.
print('Khuyến nghị: chuẩn hóa thông tin hồ sơ, xác minh nhãn và thời điểm quan sát.')
print('Chỉ xem mô hình là thử nghiệm hỗ trợ; chưa dùng để tự động quyết định bồi thường hoặc mức phí.')
print('Các bảng và chín hình đã được lưu trong thư mục làm việc hiện tại.')
