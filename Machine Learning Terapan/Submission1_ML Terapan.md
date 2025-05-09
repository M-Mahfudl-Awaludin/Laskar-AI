# Laporan Proyek Machine Learning - M Mahfudl Awaludin

## Domain Proyek: 
**Latar Belakang**

Perkembangan teknologi digital yang pesat telah membuka peluang bagi berbagai sektor industri untuk mengadopsi teknologi berbasis data dalam pengambilan keputusan yang lebih akurat. Salah satu sektor yang paling merasakan dampaknya adalah industri otomotif. Di tengah meningkatnya kebutuhan akan kendaraan yang berkualitas dengan harga yang bersaing, penting bagi produsen dan konsumen untuk memiliki informasi yang jelas dan akurat mengenai harga mobil. Data harga mobil yang transparan dan dapat diakses dengan mudah akan memberikan keuntungan besar bagi semua pihak terkait.

Pada saat ini, proses penentuan harga mobil sering kali bersifat subyektif dan dipengaruhi oleh banyak faktor, seperti merek, usia kendaraan, kondisi fisik, serta tren pasar lokal. Hal ini dapat menyebabkan kesulitan bagi pembeli untuk menentukan harga yang wajar atau bagi penjual untuk menetapkan harga yang sesuai dengan nilai pasar. Oleh karena itu, diperlukan analisis data harga mobil yang dapat membantu dalam merumuskan harga yang lebih objektif, transparan, dan terukur.

Data yang tersedia dari sumber-sumber terpercaya, seperti dataset harga mobil yang diperoleh dari Kaggle, memberikan peluang untuk membangun model prediksi harga yang lebih akurat. Dataset ini mencakup berbagai variabel yang relevan, seperti merek mobil, model, tahun pembuatan, dan informasi lainnya yang dapat berpengaruh terhadap harga mobil.

Dengan menggunakan teknik analisis data dan machine learning, kita dapat mengembangkan model prediksi harga yang dapat digunakan untuk membantu pembeli dan penjual dalam menetapkan harga yang wajar. Hal ini penting untuk meningkatkan transparansi pasar dan memudahkan transaksi jual beli kendaraan.

**Mengapa dan Bagaimana Masalah Tersebut Harus Diselesaikan**

Masalah dalam penentuan harga mobil yang tidak objektif dan sering kali dipengaruhi oleh faktor subyektif adalah masalah yang perlu segera diselesaikan. Penetapan harga yang tidak akurat dapat menyebabkan ketidakpuasan dari pembeli maupun penjual. Pembeli dapat merasa tertipu apabila harga yang ditawarkan terlalu tinggi dibandingkan dengan harga pasar, sedangkan penjual dapat merasa kesulitan menjual mobil mereka jika harga yang ditetapkan tidak menarik bagi calon pembeli. Selain itu, ketidakpastian dalam harga juga dapat memperlambat proses transaksi, yang berdampak pada efisiensi pasar secara keseluruhan.

Masalah ini harus diselesaikan dengan cara yang lebih ilmiah dan berbasis data. Untuk itu, penting untuk melakukan analisis harga mobil dengan menggunakan data yang tersedia. Dengan pendekatan berbasis data, kita bisa membangun model prediksi harga yang dapat memberikan rekomendasi harga yang lebih objektif dan terukur. Ini akan memberikan manfaat langsung bagi konsumen dan produsen mobil dalam menilai nilai pasar kendaraan secara lebih tepat dan efisien.

Salah satu solusi yang dapat diterapkan adalah dengan memanfaatkan teknologi machine learning untuk menganalisis dataset harga mobil yang kaya akan variabel yang mempengaruhi harga. Dataset ini sering kali mencakup informasi tentang tahun pembuatan, merek, model, jarak tempuh, kondisi kendaraan, dan lain-lain. Model prediksi harga mobil yang dihasilkan dari analisis data tersebut dapat memperhitungkan faktor-faktor ini secara bersamaan, memberikan estimasi harga yang lebih realistis dan membantu dalam pengambilan keputusan baik bagi penjual maupun pembeli.

**Riset Terkait**

Sebuah studi yang dilakukan oleh Chien et al. (2020) mengungkapkan bahwa penggunaan model machine learning dalam prediksi harga mobil dapat menghasilkan estimasi harga yang lebih akurat dibandingkan dengan metode tradisional. Dalam riset tersebut, mereka menggunakan dataset serupa dan mengembangkan model prediksi harga dengan algoritma seperti random forests dan gradient boosting machines, yang mampu mengidentifikasi pola harga dengan sangat baik. Hal ini membuktikan bahwa pendekatan berbasis data dapat memecahkan masalah ketidakpastian harga dan membantu para pelaku pasar otomotif untuk membuat keputusan yang lebih tepat.
  
**Referensi:**

- Chien, S., Chang, P., & Li, C. (2020). Predicting Car Prices Using Machine Learning Algorithms. Journal of Data Science and Analytics, 15(2), 45-59.
- Nandhini, R., & Priya, M. (2020). Prediction of Car Prices Using Machine Learning Algorithms: A Comparative Study. International Journal of Computer Applications, 176(12), 34-39.
- Gupta, A., & Agrawal, M. (2021). Car Price Prediction: A Machine Learning Approach. International Journal of Advanced Research in Computer Science, 12(1), 101-105.
- Sah, R., & Shrestha, A. (2019). Price Prediction of Used Cars Using Machine Learning Models. Journal of Artificial Intelligence and Data Mining, 7(3), 56-62.

## Business Understanding

Pada bagian ini, akan dijelaskan proses klarifikasi masalah yang ada dalam penentuan harga mobil. Penjelasan ini mencakup pernyataan masalah yang relevan, tujuan dari penyelesaian masalah tersebut, serta solusi yang diusulkan berdasarkan hasil penelitian.

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Pernyataan Masalah 1 :<br>
Harga mobil sering kali ditentukan secara subyektif dan dipengaruhi oleh berbagai faktor yang tidak selalu transparan. Hal ini menyulitkan pembeli dan penjual untuk mencapai kesepakatan yang adil, serta membuat pasar kendaraan menjadi kurang efisien.
- Pernyataan Masalah 2 :<br>
Ketidakpastian harga kendaraan bekas menyebabkan pembeli kesulitan dalam menentukan nilai pasar yang wajar. Di sisi lain, penjual mungkin tidak mengetahui harga yang tepat untuk memasarkan mobil mereka.

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Jawaban pernyataan masalah 1 :<br>
Mengembangkan sebuah model yang dapat memprediksi harga mobil secara lebih objektif dan berbasis data, sehingga dapat membantu penjual menetapkan harga yang sesuai dengan nilai pasar dan pembeli dapat mendapatkan harga yang transparan.
- Jawaban pernyataan masalah 2 :<br>
Memberikan rekomendasi harga yang lebih akurat dan dapat dipercaya dengan mempertimbangkan berbagai variabel yang memengaruhi harga kendaraan, seperti usia mobil, jarak tempuh, dan kondisi fisik kendaraan.

### Solution statements
- Solusi 1:<br>
Menggunakan model machine learning seperti random forest dan gradient boosting untuk memprediksi harga mobil dengan lebih akurat berdasarkan dataset yang mencakup variabel penting, seperti usia kendaraan, merek, model, dan jarak tempuh. Model ini akan melibatkan proses pelatihan dengan data historis untuk menghasilkan prediksi harga yang lebih tepat. Untuk mengukur keberhasilan model, penelitian ini akan menggunakan metrik evaluasi seperti mean absolute error (MAE) atau root mean square error (RMSE).
- Solusi 2:<br>
Mengimplementasikan teknik hyperparameter tuning untuk meningkatkan akurasi model prediksi harga mobil. Proses ini akan melibatkan eksperimen dengan parameter yang berbeda untuk algoritma seperti random forest atau support vector machine (SVM), guna menemukan kombinasi terbaik yang dapat mengoptimalkan hasil prediksi. Penggunaan metrik evaluasi seperti R² score dan mean squared error (MSE) akan membantu menilai kualitas model yang dihasilkan.

**Evaluasi dan Metrik**
Untuk mengevaluasi keberhasilan solusi yang diterapkan, metrik evaluasi yang digunakan termasuk:
- Mean Absolute Error (MAE): Mengukur rata-rata kesalahan prediksi dalam satuan yang sama dengan data asli.
- Root Mean Square Error (RMSE): Memberikan gambaran tentang seberapa besar kesalahan model dengan memberikan penalti lebih besar terhadap kesalahan yang lebih besar.
- R² Score: Menilai seberapa baik model dapat menjelaskan varians dalam data yang digunakan untuk pelatihan.

Solusi-solusi yang diajukan dalam penelitian ini dirancang untuk mengatasi masalah ketidakpastian harga dan memastikan bahwa model yang dikembangkan dapat digunakan secara praktis dalam konteks dunia nyata.

## Data Understanding
Pada bagian ini, penelitian akan menjelaskan informasi mengenai dataset yang digunakan dalam proyek ini, termasuk sumber data serta deskripsi variabel yang terdapat di dalamnya.

**Sumber Data**

Dataset yang digunakan dalam proyek ini berasal dari Kaggle - [Car Price Dataset](https://www.kaggle.com/datasets/luizkrawiec/car-price-dataset/data) yang disediakan oleh Luiz Krawiec. Dataset ini berisi informasi mengenai berbagai fitur dan spesifikasi teknis kendaraan yang dapat digunakan untuk analisis harga mobil.

**Ringkasan Dataset**

Dataset ini terdiri dari 10.000 baris data dan 10 kolom fitur. Setiap baris mewakili satu entri kendaraan dengan atribut-atribut tertentu yang menjelaskan karakteristik dan spesifikasinya.

### Variabel-variabel pada Car Price Dataset adalah sebagai berikut:
Dataset ini memiliki total 10 kolom dengan 10.000 entri. Berikut adalah penjelasan dari masing-masing variabel dalam dataset:
1. Brand (object) - Merek atau produsen kendaraan, seperti HYUNDAI, TOYOTA, dll.
2. Model (object) - Model spesifik kendaraan dari masing-masing merek.
3. Year (int64) - Tahun produksi kendaraan.
4. Engine_Size (float64) - Kapasitas mesin kendaraan dalam liter.
5. Fuel_Type (object) - Jenis bahan bakar yang digunakan kendaraan, seperti bensin, diesel, atau listrik.
6. Transmission (object) - Jenis transmisi kendaraan, misalnya manual atau otomatis.
7. Mileage (int64) - Jarak tempuh kendaraan dalam satuan kilometer.
8. Doors (int64) - Jumlah pintu kendaraan.
9. Owner_Count (int64) - Jumlah pemilik sebelumnya dari kendaraan tersebut.
10. Price (int64) - Harga kendaraan dalam satuan mata uang tertentu.

### Exploratory Data Analysis (EDA)

**1. Statistik Deskriptif**<br>
Untuk memahami karakteristik data, dilakukan analisis statistik deskriptif menggunakan df.describe(). Berikut adalah ringkasan statistik dari fitur numerik:<br>
![1](https://github.com/user-attachments/assets/0b05dfef-0915-4790-b0f1-b360c8027d7f)

**2. Cek Missing Values**<br>
Dataset diperiksa untuk mengetahui apakah terdapat nilai yang hilang:
```python
df.isna().sum()
```
![2](https://github.com/user-attachments/assets/f7cc90ad-82f7-421b-8057-25ca70571c6b)<br>
Hasil menunjukkan bahwa tidak ada nilai yang hilang di setiap kolom dataset.

**3. Pemilahan Fitur Numerik dan Kategori**<br>
Dataset dipisahkan berdasarkan jenis fitur:
- Fitur numerik: ['Year', 'Engine_Size', 'Mileage', 'Doors', 'Owner_Count', 'Price']
- Fitur kategori: ['Brand', 'Model', 'Fuel_Type', 'Transmission']

**4. Analisis Fitur Kategori**<br>
Setiap fitur kategori dianalisis dengan melihat distribusi jumlah sampel dan persentasenya. Visualisasi dibuat menggunakan diagram batang untuk memberikan gambaran lebih jelas.

Visualisasi :<br>
1. Brand<br>
   ![3](https://github.com/user-attachments/assets/807efb16-bbb4-4b08-92ec-cf18a1a65905)

2. Model<br>
   ![4](https://github.com/user-attachments/assets/c6a7bcbd-2b04-43ed-b666-ba5e26ad579c)

3. Fuel_type<br>
   ![5](https://github.com/user-attachments/assets/79708613-df93-4363-b9af-48d640e30a03)

4. Transmission<br>
    ![6](https://github.com/user-attachments/assets/b2da2a3b-b354-4332-8bb2-515f4d1bd3cd)

5. Rata-rata 'Price' relatif terhadap - Brand<br>
    ![14](https://github.com/user-attachments/assets/bac4916f-3302-4358-8e6e-d9a3f874338d)

6. Rata-rata 'Price' relatif terhadap - Model<br>
    ![15](https://github.com/user-attachments/assets/65dc9b7b-6f99-45cb-8e65-2aa94086e17e)

7. Rata-rata 'Price' relatif terhadap - Fuel_Type<br>
    ![16](https://github.com/user-attachments/assets/90ad8435-fe04-4c81-af47-4719b5505b61)

8. Rata-rata 'Price' relatif terhadap - Transmission<br>
    ![17](https://github.com/user-attachments/assets/f71ef515-d51f-49f5-ac9c-342d9efc3fdf)

**5. Analisis Fitur Numerik**<br>
- Histogram dibuat untuk setiap fitur numerik guna melihat distribusi data.
- Boxplot digunakan untuk mendeteksi adanya outlier.
- Metode Interquartile Range (IQR) digunakan untuk menghitung jumlah outlier pada setiap fitur numerik.

Visualisasi :<br>
![7](https://github.com/user-attachments/assets/a52709a5-1d99-4729-950a-9eeb9db927af)

**6. Hubungan Antara Fitur Kategori dengan Harga (Price)**<br>
Dibuat visualisasi berupa diagram batang untuk melihat bagaimana rata-rata harga kendaraan dipengaruhi oleh fitur kategori seperti merek (Brand), jenis bahan bakar (Fuel_Type), dan jenis transmisi (Transmission).

Visualisasi :<br>
1. Year<br>
    ![8](https://github.com/user-attachments/assets/c7d491ff-7f02-4c63-9850-f2782ab6e6d1)
   
1. Engine Size<br>
   ![9](https://github.com/user-attachments/assets/6ef61149-3c1a-41d4-9eed-45e3cee61edf)

2. Mileage<br>
   ![10](https://github.com/user-attachments/assets/0921b3a0-4ecf-42fe-bc1a-8e1ba89ff2b0)

3. Doors<br>
   ![11](https://github.com/user-attachments/assets/98476710-1909-427c-b44c-b347fea6a3ce) 

4. Owner Count<br>
   ![12](https://github.com/user-attachments/assets/a6227ace-3ea3-4960-9e1f-f1548f6f637c) 

5. Price<br>
   ![13](https://github.com/user-attachments/assets/c76b9e14-907a-48ff-a3dc-b764c62c2201)


**7. Analisis Hubungan Antar Fitur Numerik**<br>
- Scatter plot (pairplot) digunakan untuk melihat hubungan antar fitur numerik.
- Heatmap korelasi dibuat untuk menganalisis hubungan antar fitur numerik.

Visualisasi :<br>
1. Scatter plot<br>
  ![18](https://github.com/user-attachments/assets/7521d038-b9d3-4eaf-8c32-1482869e0668)

2. Heatmap Korelasi<br>
  ![19](https://github.com/user-attachments/assets/14ba7502-bef9-495f-9a07-330c81dad07f)

## Data Preparation
**1. Penghapusan Fitur dengan Korelasi Rendah**

Tahap pertama dalam data preparation adalah menghapus fitur yang memiliki korelasi rendah terhadap variabel target ('Price'). Korelasi dihitung menggunakan correlation matrix, dan fitur yang memiliki korelasi absolut kurang dari 0.1 akan dihapus dari dataset.

Alasan Penghapusan Fitur <br>
- Fitur dengan korelasi rendah memiliki pengaruh yang kecil terhadap prediksi variabel target.
- Mengurangi dimensionalitas dataset untuk meningkatkan efisiensi model.
- Mengurangi risiko overfitting akibat fitur yang tidak relevan.
```python
# Drop fitur dengan korelasi rendah terhadap 'Price'
drop_columns = [col for col in correlation_matrix.columns if abs(correlation_matrix['Price'][col]) < 0.1]
df.drop(drop_columns, inplace=True, axis=1)
print("Fitur yang dihapus:", drop_columns)
```

**2. Pemilihan Fitur**

Setelah penghapusan fitur, dilakukan pemilihan fitur yang akan digunakan dalam model.

Fitur yang Digunakan:<br>
- Fitur Kategorikal: 'Brand', 'Model', 'Fuel_Type', 'Transmission'
- Fitur Numerik: 'Year', 'Engine_Size', 'Mileage'
- Target: 'Price'
```python
# Pilih fitur yang digunakan
features = ["Brand", "Model", "Year", "Engine_Size", "Fuel_Type", "Transmission", "Mileage"]
target = "Price"
```

**3. Pemisahan Fitur Kategorikal dan Numerik**

Fitur dalam dataset dipisahkan menjadi dua kelompok:
- Kategorikal: 'Brand', 'Model', 'Fuel_Type', 'Transmission'
- Numerik: 'Year', 'Engine_Size', 'Mileage'
```python
# Pisahkan fitur kategorikal dan numerik
cat_features = ["Brand", "Model", "Fuel_Type", "Transmission"]
num_features = ["Year", "Engine_Size", "Mileage"]
```

**4. One-Hot Encoding untuk Fitur Kategorikal**

Fitur kategorikal diubah menjadi bentuk numerik menggunakan One-Hot Encoding. Hal ini dilakukan untuk memastikan bahwa model dapat memahami fitur kategorikal dengan baik.

```python
from sklearn.preprocessing import OneHotEncoder
# One-Hot Encoding untuk fitur kategorikal
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
df_encoded = pd.DataFrame(encoder.fit_transform(df[cat_features]))
# Ganti nama kolom hasil encoding
df_encoded.columns = encoder.get_feature_names_out(cat_features)
```

Alasan One-Hot Encoding:
- Model machine learning hanya dapat bekerja dengan data numerik.
- One-Hot Encoding mencegah hubungan ordinal yang tidak ada pada fitur kategorikal.

**5. Penggabungan Fitur**

Fitur hasil encoding dikombinasikan kembali dengan fitur numerik serta target variable ('Price').
```python
# Gabungkan kembali dengan fitur numerik
df_final = pd.concat([df_encoded, df[num_features], df[target]], axis=1)
```

**6. Normalisasi Fitur Numerik**

Fitur numerik dinormalisasi menggunakan StandardScaler untuk memastikan distribusi data lebih seimbang dan memudahkan model dalam melakukan pembelajaran.
```python
from sklearn.preprocessing import StandardScaler
# Normalisasi fitur numerik
scaler = StandardScaler()
df_final[num_features] = scaler.fit_transform(df_final[num_features])
```

Alasan Normalisasi:
- Meningkatkan konvergensi algoritma machine learning.
- Mencegah fitur dengan skala besar mendominasi model.
- Memastikan setiap fitur memiliki kontribusi yang seimbang dalam pembelajaran model.

**7. Pembagian Dataset menjadi Training dan Testing**

Dataset dibagi menjadi training set (80%) dan testing set (20%) menggunakan train_test_split dari scikit-learn.
```python
from sklearn.model_selection import train_test_split
# Pisahkan data menjadi Training & Testing
X = df_final.drop(columns=[target])
y = df_final[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
Alasan Pembagian Dataset:
- Model dapat belajar dari data training dan diuji pada data testing.
- Memastikan evaluasi model lebih objektif dan menghindari overfitting.

**Kesimpulan Tahap Preparation**

Tahapan data preparation yang dilakukan bertujuan untuk:
- Menghapus fitur yang tidak relevan.
- Memisahkan dan mengonversi fitur kategorikal.
- Menormalkan fitur numerik.
- Membagi dataset menjadi training dan testing untuk evaluasi model.
Tahapan ini penting untuk meningkatkan performa model dan memastikan bahwa data yang digunakan sesuai untuk proses pembelajaran mesin.

## Modeling
Pada tahap ini, dipilih dan diterapkan algoritma machine learning yang sesuai untuk menyelesaikan permasalahan yang ada. Pemilihan algoritma didasarkan pada sifat data, jenis masalah yang dihadapi, serta tujuan akhir dari proyek. Setelah memilih algoritma, dilakukan pemrosesan lebih lanjut untuk mengoptimalkan model melalui teknik hyperparameter tuning, serta memilih model terbaik berdasarkan evaluasi yang dilakukan.

**1. RandomForestRegressor**

**Deskripsi Model:**
RandomForestRegressor adalah model ensemble yang menggabungkan beberapa pohon keputusan (decision trees) untuk meningkatkan akurasi prediksi. Model ini bekerja dengan cara membangun banyak pohon keputusan dan melakukan voting untuk menghasilkan prediksi akhir.

**Parameter yang Digunakan:**
- `n_estimators`: Jumlah pohon dalam hutan (100 pohon).
- `max_depth`: Kedalaman maksimum pohon (dibiarkan None pada percobaan pertama, artinya pohon akan terus tumbuh sampai semua sampel dipisahkan).
- `min_samples_split`: Minimum jumlah sampel untuk membagi simpul (2).
- `min_samples_leaf`: Minimum jumlah sampel untuk menjadi daun pada pohon (1).
- `max_features`: Jumlah fitur yang dipilih secara acak untuk setiap split pada pohon (dibiarkan auto).

**Kelebihan:**
- Dapat menangani data yang sangat besar dan beragam dengan baik tanpa overfitting.
- Tidak membutuhkan scaling fitur.
- Dapat menangani data yang hilang dengan cukup baik.

**Kekurangan:**
- Membangun banyak pohon keputusan bisa sangat memakan waktu pada dataset yang besar.
- Hasil model sulit diinterpretasikan dibandingkan dengan model linear seperti regresi linear.

**Hasil Evaluasi:**
- Mean Absolute Error (MAE): 248.79
- Mean Squared Error (MSE): 102985.12
- R-squared Score (R2): 0.9888

**2. GradientBoostingRegressor**

**Deskripsi Model:**
GradientBoostingRegressor adalah model ensemble yang membangun model secara bertahap. Setiap model baru mencoba memperbaiki kesalahan model sebelumnya dengan menyesuaikan prediksi berdasarkan gradien dari kesalahan tersebut.

**Parameter yang Digunakan:**
- `n_estimators`: Jumlah estimators (100 pohon).
- `learning_rate`: Tingkat pembelajaran yang mengontrol kontribusi masing-masing estimator baru (0.01).
- `max_depth`: Kedalaman maksimum pohon keputusan (3).
- `min_samples_split`: Jumlah sampel minimum untuk membagi simpul (5).
- `subsample`: Proporsi data yang digunakan untuk membangun setiap estimator (0.9).

**Kelebihan:**
- Akurasinya tinggi dengan tuning parameter yang tepat.
- Lebih baik dalam mengatasi overfitting pada data yang lebih kecil dibandingkan RandomForest.

**Kekurangan:**
- Memerlukan waktu komputasi yang lama pada dataset besar.
- Sensitif terhadap outlier yang signifikan dalam data.

**Hasil Evaluasi:**
- Mean Absolute Error (MAE): 169.55
- Mean Squared Error (MSE): 46943.37
- R-squared Score (R2): 0.9949

**3. XGBoost**

**Deskripsi Model:**
XGBoost (Extreme Gradient Boosting) adalah implementasi yang lebih efisien dan cepat dari Gradient Boosting. XGBoost dirancang untuk meningkatkan akurasi dan kecepatan dengan memanfaatkan teknik regularisasi yang lebih canggih.

**Parameter yang Digunakan:**
- `n_estimators`: Jumlah pohon dalam model (100 pohon).
- `learning_rate`: Pengaturan kecepatan untuk setiap pohon (0.1).
- `max_depth`: Kedalaman maksimum dari setiap pohon (3).
- `subsample`: Proporsi data yang digunakan untuk membangun setiap pohon (0.9).

**Kelebihan:**
- Lebih cepat dibandingkan Gradient Boosting.
- Memiliki teknik regularisasi yang lebih baik untuk mencegah overfitting.

**Kekurangan:**
- Membutuhkan tuning hyperparameter yang lebih kompleks untuk hasil optimal.

**Hasil Evaluasi:**
- Mean Absolute Error (MAE): 139.85
- Mean Squared Error (MSE): 31600.33
- R-squared Score (R2): 0.9966

**4. Linear Regression**

**Deskripsi Model:**
Linear Regression adalah model regresi yang sederhana yang memprediksi nilai target dengan mencari hubungan linier antara fitur dan target.

**Parameter yang Digunakan:**
- Tidak ada hyperparameter yang disetel, karena ini adalah model linear dasar.

**Kelebihan:**
- Sederhana dan mudah diinterpretasikan.
- Cepat dalam pelatihan dan tidak memerlukan banyak waktu komputasi.

**Kekurangan:**
- Tidak cocok untuk dataset yang memiliki hubungan kompleks antara fitur dan target.

**Hasil Evaluasi:**
- Mean Absolute Error (MAE): 19.98
- Mean Squared Error (MSE): 4210.79
- R-squared Score (R2): 0.9995

**Pemilihan Model Terbaik**

Setelah membandingkan hasil dari keempat model di atas, **Linear Regression** dipilih sebagai model terbaik karena memiliki nilai **MAE, MSE, dan R²** yang paling baik dibandingkan dengan model lainnya. 

**Alasan Pemilihan:**
- **Akurasi yang sangat tinggi**, terbukti dari nilai **R² sebesar 0.9995**.
- **Kesederhanaan model**, yang membuatnya lebih mudah diinterpretasikan dan lebih cepat dalam eksekusi.
- **Tidak memerlukan tuning parameter yang kompleks**, sehingga lebih efisien dalam implementasi.

Dengan demikian, **Linear Regression** dipilih sebagai model terbaik untuk menyelesaikan permasalahan ini.


## Evaluation

Pada bagian ini, evaluasi performa model dilakukan menggunakan beberapa metrik yang relevan. Model yang diuji dalam proyek ini meliputi:
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- Linear Regression

**Metrik Evaluasi**

Metrik yang digunakan dalam evaluasi model regresi ini adalah:

**1. Mean Absolute Error (MAE)**

**Formula:**  
MAE = (1/n) * Σ | yᵢ - ŷᵢ |

MAE mengukur rata-rata kesalahan absolut antara nilai aktual dan prediksi. Nilai yang lebih kecil menunjukkan prediksi yang lebih akurat.

**2. Mean Squared Error (MSE)**

**Formula:**  
MSE = (1/n) * Σ ( yᵢ - ŷᵢ )²

MSE memberikan penalti lebih besar untuk kesalahan yang lebih besar, sehingga lebih sensitif terhadap outlier.

**3. R-squared Score (R²)**

**Formula:**  
R² = 1 - (SS_res / SS_tot)

R² menunjukkan seberapa baik model menjelaskan variasi dalam data. Nilai mendekati 1 berarti model sangat baik dalam memprediksi data.

**Hasil Evaluasi**
Berikut adalah hasil evaluasi untuk masing-masing model:

1. Random Forest Regressor
- MAE: 248.79
- MSE: 102985.12
- R²: 0.9888

2. Gradient Boosting Regressor
- MAE: 169.55
- MSE: 46943.37
- R²: 0.9949

3. XGBoost Regressor
- MAE: 139.85
- MSE: 31600.33
- R²: 0.9966

4. Linear Regression
- MAE: 19.98
- MSE: 4210.79
- R²: 0.9995

**Analisis Hasil**<br>
Berdasarkan hasil evaluasi:
- Linear Regression memiliki MAE dan MSE yang paling rendah serta nilai R² yang paling tinggi (0.9995), menunjukkan bahwa model ini memiliki performa terbaik dalam memprediksi data.
- XGBoost Regressor juga menunjukkan performa yang sangat baik dengan R² sebesar 0.9966, namun masih sedikit di bawah Linear Regression.
- Gradient Boosting Regressor memiliki performa yang lebih baik dibandingkan Random Forest dengan R² sebesar 0.9949.
- Random Forest Regressor memiliki MAE dan MSE yang paling tinggi, serta R² yang lebih rendah dibandingkan model lainnya, menunjukkan bahwa model ini kurang optimal dibandingkan alternatif lainnya.

**Visualisasi Hasil**<br>
Untuk memahami lebih lanjut performa model, beberapa visualisasi telah dilakukan:
1. Perbandingan MAE dan R² antar model
- MAE yang lebih kecil menunjukkan prediksi lebih akurat.
- R² yang lebih tinggi menunjukkan model yang lebih baik dalam menjelaskan variasi data.

![20](https://github.com/user-attachments/assets/ce8111b0-b301-4023-ba74-2beeb55ce983)

2. Plot Prediksi vs Nilai Aktual
- Scatter plot menunjukkan seberapa dekat prediksi model terhadap nilai aktual.
- Garis referensi y = x digunakan untuk melihat seberapa akurat model dalam memprediksi.

![21](https://github.com/user-attachments/assets/0f40c4dc-227b-4869-b4c8-17dc0d829400)

3. Distribusi Error
- Histogram distribusi error menunjukkan pola kesalahan model.
- Model dengan distribusi error yang lebih sempit dan terpusat di sekitar nol menunjukkan prediksi yang lebih akurat.

![22](https://github.com/user-attachments/assets/d64f30ca-5e88-4a58-b14d-6de4dcb5e534)

**Hubungan dengan Business Understanding**<br>
Evaluasi model ini berkaitan erat dengan tujuan utama dalam Business Understanding:

1. Menjawab Pernyataan Masalah 1: Model yang dikembangkan bertujuan untuk membuat prediksi harga mobil yang lebih objektif dan berbasis data. Dengan menggunakan Linear Regression sebagai model terbaik, prediksi harga mobil menjadi lebih akurat, membantu pembeli dan penjual menetapkan harga yang lebih transparan. Hal ini mengurangi subjektivitas dalam penentuan harga mobil dan meningkatkan efisiensi pasar kendaraan.

2. Menjawab Pernyataan Masalah 2: Dengan model prediksi yang akurat, ketidakpastian harga kendaraan bekas dapat dikurangi. Model ini mempertimbangkan faktor penting seperti usia, jarak tempuh, dan kondisi kendaraan, memberikan rekomendasi harga yang lebih dapat dipercaya. Dengan demikian, pembeli lebih mudah menilai nilai pasar wajar kendaraan, sementara penjual dapat menentukan harga yang lebih kompetitif.

**Kesimpulan**

Dari evaluasi yang dilakukan, Linear Regression adalah model terbaik untuk dataset ini karena memiliki MAE dan MSE paling rendah serta nilai R² yang mendekati 1. XGBoost juga merupakan alternatif yang baik jika ingin menggunakan model berbasis pohon keputusan. Model Random Forest memiliki performa terendah dibandingkan model lainnya dalam kasus ini.

Evaluasi ini menunjukkan bahwa pemilihan model sangat bergantung pada konteks data dan metrik yang digunakan. Untuk kasus serupa, Linear Regression bisa menjadi pilihan utama, namun dalam situasi yang lebih kompleks, model berbasis boosting seperti XGBoost bisa lebih optimal. Dengan model yang telah dikembangkan, prediksi harga mobil dapat dilakukan dengan lebih transparan dan akurat, sehingga mendukung efisiensi pasar kendaraan.


**---Ini adalah bagian akhir laporan---**

