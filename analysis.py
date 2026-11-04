# Project 3 - Mã xuất từ các ô code trong notebook, theo tài liệu được cung cấp.
# Đặt Insurance.csv trong thư mục làm việc trước khi chạy.

# Đọc dữ liệu bằng pandas theo T6-T7; dùng thư viện vẽ theo T12-T15.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cấu hình cỡ chữ biểu đồ theo phần cấu hình Matplotlib trong T12.
plt.rcParams['font.size'] = 14

df_raw = pd.read_csv('Insurance.csv')
print('Số dòng và số cột:', df_raw.shape)
print(df_raw.head())
df_raw.info()
print(df_raw.describe().round(2))

# Kiểm tra kiểu dữ liệu, số lượng và tỷ lệ ô thiếu theo T8-T9.
bang_hien_trang = pd.DataFrame({
    'Kieu_du_lieu': df_raw.dtypes,
    'So_o_thieu': df_raw.isna().sum(),
    'Ty_le_thieu_pct': df_raw.isna().sum() / len(df_raw) * 100
})
print(bang_hien_trang)
print('Tổng số ô thiếu:', df_raw.isna().sum().sum())

# Xem các mã thực tế; chưa tự chuyển mã sang tên giới tính hoặc vùng.
for cot in ['sex', 'smoker', 'region', 'insuranceclaim']:
    print('Số lượng theo mã của', cot)
    print(df_raw[cot].value_counts().sort_index())

# Các điều kiện này chỉ kiểm tra dấu của biến, không phải ngưỡng y tế.
print('Số age <= 0:', (df_raw['age'] <= 0).sum())
print('Số bmi <= 0:', (df_raw['bmi'] <= 0).sum())
print('Số children < 0:', (df_raw['children'] < 0).sum())
print('Số charges < 0:', (df_raw['charges'] < 0).sum())
bang_hien_trang.to_csv('Bang_01_Hien_trang.csv', encoding='utf-8-sig')

# Phát hiện và hiển thị cả hai dòng trong cặp trùng theo T8-T9.
print('Số bản sao cần loại theo quy tắc giữ dòng đầu:', df_raw.duplicated().sum())
print(df_raw[df_raw.duplicated(keep=False)])

# Áp dụng quy tắc khử trùng toàn bộ cột, giữ một bản ghi.
df = df_raw.drop_duplicates().copy()
print('Trước làm sạch:', len(df_raw))
print('Sau làm sạch:', len(df))
print('Tỷ lệ nhãn 1 trước làm sạch (%):', round(df_raw['insuranceclaim'].mean() * 100, 2))
print('Tỷ lệ nhãn 1 sau làm sạch (%):', round(df['insuranceclaim'].mean() * 100, 2))
df.to_csv('Insurance_clean.csv', index=False, encoding='utf-8-sig')

# Xem phân phối và các điểm bất thường bằng boxplot theo ví dụ trong Sources.
print(df[['bmi', 'charges']].describe().round(2))
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
sns.boxplot(y='bmi', data=df, color='#56A79E', ax=axes[0])
axes[0].set_title('Phân phối BMI')
axes[0].set_ylabel('BMI')
sns.boxplot(y='charges', data=df, color='#D6A45A', ax=axes[1])
axes[1].set_title('Phân phối charges')
axes[1].set_ylabel('Charges (đơn vị chưa xác nhận)')
plt.tight_layout()
plt.savefig('Hinh_01_Boxplot.png', dpi=180)
plt.show()

# Bảng so sánh tỷ lệ theo nhóm, dùng groupby và các phép tính cơ bản.
bang_nhom = {}
for cot in ['smoker', 'sex', 'region', 'children']:
    bang = pd.DataFrame({
        'So_ban_ghi': df.groupby(cot)['insuranceclaim'].count(),
        'So_nhan_1': df.groupby(cot)['insuranceclaim'].sum(),
        'Ty_le_nhan_1_pct': df.groupby(cot)['insuranceclaim'].mean() * 100
    })
    bang_nhom[cot] = bang
    print('Phân tích theo', cot)
    print(bang.round(2))
    bang.to_csv('Bang_nhom_' + cot + '.csv', encoding='utf-8-sig')

# Hình 2: quy mô hai nhãn và tỷ lệ nhãn 1 theo smoker.
so_luong_nhan = df['insuranceclaim'].value_counts().sort_index()
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
so_luong_nhan.plot.bar(ax=axes[0], color=['#56A79E', '#C97C82'], rot=0)
axes[0].set_title('Số lượng bản ghi theo nhãn')
axes[0].set_xlabel('Insuranceclaim')
axes[0].set_ylabel('Số bản ghi')
bang_nhom['smoker']['Ty_le_nhan_1_pct'].plot.bar(ax=axes[1], color='#56A79E', rot=0)
axes[1].set_title('Tỷ lệ nhãn 1 theo smoker')
axes[1].set_xlabel('Mã smoker')
axes[1].set_ylabel('Tỷ lệ nhãn 1 (%)')
axes[1].set_ylim(0, 100)
plt.tight_layout()
plt.savefig('Hinh_02_Nhan_va_smoker.png', dpi=180)
plt.show()

# Hình 3: hình dạng phân phối charges theo histogram trong T12 và T15.
print('Charges trung bình:', round(df['charges'].mean(), 2))
print('Charges trung vị:', round(df['charges'].median(), 2))
print('Charges nhỏ nhất:', round(df['charges'].min(), 2))
print('Charges lớn nhất:', round(df['charges'].max(), 2))
plt.figure(figsize=(10, 4.5))
sns.histplot(df['charges'], bins=30)
plt.title('Phân phối charges sau khi bỏ bản sao')
plt.xlabel('Charges (đơn vị chưa xác nhận)')
plt.ylabel('Số bản ghi')
plt.tight_layout()
plt.savefig('Hinh_03_Phan_phoi_charges.png', dpi=180)
plt.show()

# Tạo nhóm tuổi bằng phép lọc và loc đã dùng trong Sources.
# Các mốc 30 và 45 chỉ để chia nhóm phân tích, không phải ngưỡng rủi ro y tế.
df['nhom_tuoi'] = '18-29'
df.loc[(df['age'] >= 30) & (df['age'] < 45), 'nhom_tuoi'] = '30-44'
df.loc[df['age'] >= 45, 'nhom_tuoi'] = '45-64'
bang_tuoi = pd.DataFrame({
    'So_ban_ghi': df.groupby('nhom_tuoi')['insuranceclaim'].count(),
    'So_nhan_1': df.groupby('nhom_tuoi')['insuranceclaim'].sum(),
    'Ty_le_nhan_1_pct': df.groupby('nhom_tuoi')['insuranceclaim'].mean() * 100
})
print(bang_tuoi.round(2))
bang_tuoi.to_csv('Bang_02_Nhom_tuoi.csv', encoding='utf-8-sig')

# Bảng BMI và tuổi theo nhãn, không dùng thêm ngưỡng phân nhóm BMI.
bang_bmi = pd.DataFrame({
    'So_ban_ghi': df.groupby('insuranceclaim')['bmi'].count(),
    'BMI_trung_binh': df.groupby('insuranceclaim')['bmi'].mean(),
    'BMI_trung_vi': df.groupby('insuranceclaim')['bmi'].median(),
    'Tuoi_trung_binh': df.groupby('insuranceclaim')['age'].mean()
})
print(bang_bmi.round(2))
bang_bmi.to_csv('Bang_03_BMI_theo_nhan.csv', encoding='utf-8-sig')

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
bang_tuoi['Ty_le_nhan_1_pct'].plot.bar(ax=axes[0], color='#56A79E', rot=0)
axes[0].set_title('Tỷ lệ nhãn 1 theo nhóm tuổi')
axes[0].set_xlabel('Nhóm tuổi')
axes[0].set_ylabel('Tỷ lệ nhãn 1 (%)')
axes[0].set_ylim(0, 100)
sns.boxplot(x='insuranceclaim', y='bmi', data=df, color='#D6A45A', ax=axes[1])
axes[1].set_title('BMI theo hai nhãn insuranceclaim')
axes[1].set_xlabel('Insuranceclaim')
axes[1].set_ylabel('BMI')
plt.tight_layout()
plt.savefig('Hinh_04_Tuoi_va_BMI.png', dpi=180)
plt.show()

# Hình 5: tránh chỉ so sánh tổng nhãn 1 khi quy mô các nhóm khác nhau.
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
bang_nhom['children']['Ty_le_nhan_1_pct'].plot.bar(ax=axes[0], color='#56A79E', rot=0)
axes[0].set_title('Tỷ lệ nhãn 1 theo children')
axes[0].set_xlabel('Mã số đếm children')
axes[0].set_ylabel('Tỷ lệ nhãn 1 (%)')
axes[0].set_ylim(0, 100)
bang_nhom['region']['Ty_le_nhan_1_pct'].plot.bar(ax=axes[1], color='#D6A45A', rot=0)
axes[1].set_title('Tỷ lệ nhãn 1 theo region')
axes[1].set_xlabel('Mã region')
axes[1].set_ylabel('Tỷ lệ nhãn 1 (%)')
axes[1].set_ylim(0, 100)
plt.tight_layout()
plt.savefig('Hinh_05_Children_va_region.png', dpi=180)
plt.show()

# So sánh charges theo smoker bằng cả mean và median.
bang_charges = pd.DataFrame({
    'So_ban_ghi': df.groupby('smoker')['charges'].count(),
    'Charges_trung_binh': df.groupby('smoker')['charges'].mean(),
    'Charges_trung_vi': df.groupby('smoker')['charges'].median()
})
print(bang_charges.round(2))
bang_charges.to_csv('Bang_04_Charges_theo_smoker.csv', encoding='utf-8-sig')

# Hình 6: scatter cho hai biến số và boxplot so sánh phân phối nhóm.
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
sns.scatterplot(x='age', y='charges', hue='smoker', data=df, alpha=0.45, ax=axes[0])
axes[0].set_title('Tuổi và charges theo smoker')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Charges (đơn vị chưa xác nhận)')
sns.boxplot(x='smoker', y='charges', data=df, color='#D6A45A', ax=axes[1])
axes[1].set_title('Phân phối charges theo smoker')
axes[1].set_xlabel('Mã smoker')
axes[1].set_ylabel('Charges (đơn vị chưa xác nhận)')
plt.tight_layout()
plt.savefig('Hinh_06_Tuoi_charges_smoker.png', dpi=180)
plt.show()

# In số liệu đối chiếu giả thuyết bằng phép trừ và so sánh cơ bản.
print('H1 - Chênh tỷ lệ smoker=1 trừ smoker=0 (điểm phần trăm):',
      round(bang_nhom['smoker'].loc[1, 'Ty_le_nhan_1_pct'] - bang_nhom['smoker'].loc[0, 'Ty_le_nhan_1_pct'], 2))
print('H2 - Chênh tỷ lệ tuổi 45-64 trừ tuổi 18-29 (điểm phần trăm):',
      round(bang_tuoi.loc['45-64', 'Ty_le_nhan_1_pct'] - bang_tuoi.loc['18-29', 'Ty_le_nhan_1_pct'], 2))
print('H3 - Chênh BMI trung bình nhãn 1 trừ nhãn 0:',
      round(bang_bmi.loc[1, 'BMI_trung_binh'] - bang_bmi.loc[0, 'BMI_trung_binh'], 2))
print('H4 - Chênh charges trung bình smoker=1 trừ smoker=0:',
      round(bang_charges.loc[1, 'Charges_trung_binh'] - bang_charges.loc[0, 'Charges_trung_binh'], 2))
print('H5 - Đọc lần lượt các tỷ lệ dưới đây để đối chiếu nhận định tăng liên tục:')
print(bang_nhom['children'].round(2))

# Chọn đặc trưng, chia train/test trước khi chuẩn hóa theo T15.
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X = df[['age', 'sex', 'bmi', 'children', 'smoker', 'region']]
y = df['insuranceclaim']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# One-hot để mã region không bị hiểu thành số có thứ tự.
X_train_encoded = pd.get_dummies(X_train, columns=['sex', 'region'], drop_first=True)
X_test_encoded = pd.get_dummies(X_test, columns=['sex', 'region'], drop_first=True)
X_train_encoded, X_test_encoded = X_train_encoded.align(
    X_test_encoded, join='left', axis=1, fill_value=0)

# Chỉ fit trên train; test dùng đúng các tham số học từ train.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_encoded)
X_test_scaled = scaler.transform(X_test_encoded)
print('Kích thước train:', X_train_encoded.shape)
print('Kích thước test:', X_test_encoded.shape)
print('Các cột sau one-hot:', list(X_train_encoded.columns))
print('Số lượng nhãn trong train:')
print(y_train.value_counts().sort_index())
print('Số lượng nhãn trong test:')
print(y_test.value_counts().sort_index())

# Khởi tạo đúng bốn mô hình và bộ tham số minh họa phân loại trong T15.
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

models = {
    'Logistic Regression': LogisticRegression(random_state=42),
    'KNeighbors Classifier': KNeighborsClassifier(n_neighbors=5),
    'Decision Tree': DecisionTreeClassifier(max_depth=3, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=10, random_state=42)
}
ket_qua = []
ma_tran = {}
for ten, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    ket_qua.append({
        'Mo_hinh': ten,
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred, pos_label=1),
        'Recall': recall_score(y_test, y_pred, pos_label=1)
    })
    ma_tran[ten] = confusion_matrix(y_test, y_pred)

bang_mo_hinh = pd.DataFrame(ket_qua)
print(bang_mo_hinh.round(4))
bang_mo_hinh.to_csv('Bang_05_Ket_qua_mo_hinh.csv', index=False, encoding='utf-8-sig')

# Hình 7: so sánh ba chỉ số có trong phần phân loại T15.
bang_mo_hinh.set_index('Mo_hinh')[['Accuracy', 'Precision', 'Recall']].plot.bar(
    figsize=(11, 5), rot=15)
plt.title('Kết quả bốn mô hình trên cùng tập test')
plt.xlabel('Mô hình')
plt.ylabel('Giá trị chỉ số (0-1)')
plt.ylim(0, 1)
plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('Hinh_07_So_sanh_mo_hinh.png', dpi=180)
plt.show()

# Hình 8: ma trận nhầm lẫn theo T15, bố trí 2x2 để dễ đọc.
fig, axes = plt.subplots(2, 2, figsize=(11, 8))
for i, (ten, model) in enumerate(models.items()):
    hang = i // 2
    cot = i % 2
    sns.heatmap(ma_tran[ten], annot=True, fmt='d', cmap='Blues',
                xticklabels=['0', '1'], yticklabels=['0', '1'], ax=axes[hang, cot])
    axes[hang, cot].set_title(ten)
    axes[hang, cot].set_xlabel('Dự đoán')
    axes[hang, cot].set_ylabel('Thực tế')
    pd.DataFrame(ma_tran[ten], index=['Thuc_te_0', 'Thuc_te_1'],
                 columns=['Du_doan_0', 'Du_doan_1']).to_csv(
                     'Ma_tran_' + str(i + 1) + '.csv', encoding='utf-8-sig')
plt.tight_layout()
plt.savefig('Hinh_08_Ma_tran_nham_lan.png', dpi=180)
plt.show()
