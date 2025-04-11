# Laporan Proyek Machine Learning - M Mahfudl Awaludin

## Project Overview

Pariwisata merupakan salah satu sektor utama pendorong perekonomian Indonesia, menyumbang devisa negara yang signifikan dan menciptakan lapangan kerja bagi masyarakat. Seiring berkembangnya teknologi informasi, digitalisasi dalam industri pariwisata semakin menjadi kebutuhan, terutama dalam hal personalisasi layanan bagi wisatawan. Salah satu pendekatan yang semakin banyak digunakan dalam sektor ini adalah penerapan sistem rekomendasi (recommendation system) untuk mempermudah wisatawan dalam menemukan destinasi wisata yang sesuai dengan preferensi mereka.

Dalam konteks Indonesia yang memiliki ribuan destinasi wisata dengan karakteristik dan daya tarik yang sangat beragam, sistem rekomendasi menjadi alat yang sangat penting untuk meningkatkan pengalaman pengguna, mempercepat proses perencanaan perjalanan, dan mendorong pemerataan kunjungan ke berbagai daerah, termasuk destinasi yang kurang populer.

Proyek ini bertujuan untuk mengembangkan dua jenis sistem rekomendasi:
1. Content-Based Filtering, yaitu sistem yang merekomendasikan destinasi wisata berdasarkan kemiripan fitur destinasi dengan destinasi yang sebelumnya disukai oleh pengguna.<br>
2. Collaborative Filtering, yaitu sistem yang memanfaatkan preferensi pengguna lain yang memiliki kesamaan selera untuk memberikan rekomendasi yang relevan.

Kedua pendekatan ini dipilih untuk saling melengkapi, sehingga sistem yang dikembangkan dapat memberikan hasil rekomendasi yang lebih akurat dan bervariasi.

**Mengapa Proyek Ini Penting untuk Diselesaikan**<br>
Pengembangan sistem rekomendasi dalam sektor pariwisata sangat penting karena dapat membantu wisatawan menemukan destinasi yang sesuai dengan preferensi mereka secara lebih cepat dan efisien, sekaligus meningkatkan pengalaman perjalanan yang lebih personal dan memuaskan. Di era digital saat ini, wisatawan cenderung mencari informasi melalui platform daring, dan mereka semakin mengandalkan teknologi untuk mendukung pengambilan keputusan, termasuk saat memilih tujuan wisata.

Studi oleh Gretzel et al. (2015) menunjukkan bahwa personalized recommendation systems dapat meningkatkan kepuasan wisatawan dan membantu mereka mengeksplorasi destinasi yang belum populer namun memiliki potensi tinggi. Sistem semacam ini juga berkontribusi pada distribusi arus kunjungan yang lebih merata ke berbagai daerah, mengurangi overtourism di destinasi yang sudah jenuh, dan membantu mendorong pertumbuhan ekonomi daerah lain yang kurang terekspos.

Selain itu, menurut Ricci, Rokach, & Shapira (2011), sistem rekomendasi telah menjadi komponen penting dalam aplikasi pariwisata modern karena mampu memproses preferensi individu dan memberikan rekomendasi yang lebih relevan dibandingkan pencarian manual atau umum.

Proyek ini juga menjadi signifikan dalam konteks Indonesia, yang memiliki karakteristik geografis dan budaya yang sangat beragam. Dengan banyaknya pilihan destinasi, wisatawan lokal maupun mancanegara sering kali mengalami kesulitan dalam memilih destinasi yang sesuai dengan minat mereka. Sistem rekomendasi berbasis konten dan kolaboratif dapat mengatasi tantangan ini, dengan memberikan rekomendasi yang disesuaikan dan berbasis data, sehingga berdampak pada peningkatan jumlah kunjungan serta memperkuat citra pariwisata Indonesia di mata dunia.

**Referensi**<br>
- Prabowo, A. (2021). Indonesia Tourism Destination Dataset. Kaggle. Diakses dari: https://www.kaggle.com/datasets/aprabowo/indonesia-tourism-destination
- Gretzel, U., Werthner, H., Koo, C., & Lamsfus, C. (2015). Conceptual foundations for understanding smart tourism ecosystems. Computers in Human Behavior, 50, 558–563.
- Ricci, F., Rokach, L., & Shapira, B. (2011). Introduction to Recommender Systems Handbook. Springer.

***Referensi***
- Laporan: "Rekomendasi Tempat Wisata dengan Algoritma Content-Based Filtering" (Jurnal Informatika, 2022).
- Dataset: Tourism Dataset (UCI Repository).

## Business Understanding

***Problem Statements:***
1. Bagaimana cara memberikan rekomendasi tempat wisata yang relevan berdasarkan preferensi pengguna, kategori wisata, dan anggaran?
2. Bagaimana mengidentifikasi pola perilaku pengguna yang dapat membantu memberikan rekomendasi yang lebih personal?

***Goals:***
1. Mengembangkan sistem rekomendasi yang memanfaatkan data wisata dan rating untuk menyarankan destinasi yang sesuai dengan preferensi pengguna.
2. Menyediakan rekomendasi berdasarkan kategori wisata dan lokasi yang relevan dengan pengguna serta anggaran mereka.

***Solusi***
1. Content-Based Filtering: Sistem ini menggunakan informasi terkait kategori dan lokasi wisata, dengan menggunakan teknik vectorisasi seperti TF-IDF dan cosine similarity untuk menghitung kesamaan antar tempat wisata.
2. Collaborative Filtering: Model ini menggunakan data rating pengguna untuk memprediksi rating yang belum diberikan oleh pengguna terhadap tempat wisata, menggunakan pendekatan neural network berbasis embeddings.

### Data Understanding
***Deskripsi Dataset***<br>
Dataset yang digunakan dalam proyek ini berisi informasi tentang tempat wisata di lima kota besar di Indonesia: Jakarta, Yogyakarta, Semarang, Bandung, dan Surabaya. Dataset ini dibuat untuk Capstone Project Bangkit Academy 2021 dan digunakan dalam pengembangan aplikasi GetLoc. Aplikasi ini berfungsi untuk memberikan rekomendasi tempat wisata berdasarkan preferensi pengguna, seperti kota, harga, kategori, dan waktu. Selain itu, GetLoc juga memberikan rekomendasi mengenai rute tercepat dan termurah untuk mengunjungi tempat-tempat tersebut.

### Sumber Dataset:<br>
Tautan ke Kaggle: [Indonesia Tourism Destination](https://www.kaggle.com/datasets/aprabowo/indonesia-tourism-destination/data)

***Deskripsi Dataset***<br>
Dataset terdiri dari empat file utama dengan rincian sebagai berikut:
1. tourism_with_id.csv
File ini berisi informasi lengkap mengenai destinasi wisata yang tersedia di Indonesia. Terdapat total 437 baris data, masing-masing merepresentasikan satu tempat wisata, dengan 13 kolom/fitur. Berikut adalah penjelasan masing-masing variabel:

| Kolom       | Deskripsi       | Tipe Data       |
|--------------|---------------|---------------|
| Place_Id | ID unik tempat wisata  |  int64  |
| Place_Name  | Nama tempat wisata  |  object (string)  |
| Description  |  Uraian/deskripsi destinasi  |  object (string)  |
| Category  |  Kategori wisata (misal: Nature, Culture)  |  object (string)  |
| City  |  Kota lokasi wisata  | object (string)   |
| Price  |  Estimasi harga (kemungkinan dalam Rupiah)  |  float64  |
| Rating  |  Nilai rating (skala 1–5)  |  float64  |
| Time_Minutes  |  Estimasi waktu kunjungan (dalam menit)  |  float64  |
|  Coordinate |  Koordinat (gabungan lat-long dalam string)  |  object (string)  |
| Lat  |  Latitude destinasi wisata  | float64   |
| Long  |  Longitude destinasi wisata  |  float64  |
| Unnamed: 11  |  Kolom kosong (semua nilai NaN)  |  float64 (null)  |
|  Unnamed: 12 |  Kolom tidak terdokumentasi, berisi angka 0/1  | float64 (biner?) |
  
2. user.csv
File ini berisi interaksi pengguna dengan destinasi wisata berupa rating, yang digunakan dalam Collaborative Filtering. Jumlah data sebanyak 10.000 baris, dengan 3 kolom utama:

| Kolom       | Deskripsi       | Tipe Data       |
|--------------|---------------|---------------|
| User_Id | ID unik pengguna  |  int64  |
| Place_Id  | Lokasi asal pengguna (kota/daerah)  |  int64  |
| Place_Ratings  |  Nilai rating dari pengguna (diduga skala 1–5)  |  float64  |

3. tourism_rating.csv
File ini menyimpan profil pengguna sistem, terdiri dari 300 entri dengan 3 fitur berikut:

| Kolom       | Deskripsi       | Tipe Data       |
|--------------|---------------|---------------|
| User_Id | ID unik pengguna  |  int64  |
| Location  | ID tempat wisata (relasi ke Tourism_Info.csv)  |  object (string)  |
| Age  |  Usia pengguna  |  int64  |

### Eksplorasi Data Analysis
1. Cek Missing Values (Nilai Kosong)
```python
info_tourism.isnull().sum()
tourism_rating.isnull().sum()
users.isnull().sum()
   ```
Deskripsi: Langkah ini digunakan untuk memeriksa apakah terdapat data yang hilang (missing values) di masing-masing dataframe (info_tourism, tourism_rating, dan users). Hasilnya:
- info_tourism memiliki 232 nilai kosong pada kolom Time_Minutes dan 437 nilai kosong (semua) pada Unnamed: 11.
- tourism_rating dan users bersih dari missing values.
2. Drop Kolom Tidak Relevan
```python
info_tourism = info_tourism.drop(columns=['Unnamed: 11'], errors='ignore')
   ```
Deskripsi: Menghapus kolom Unnamed: 11 karena tidak mengandung informasi apapun (semua nilai NaN).
3. Eksplorasi Kategori Tempat Wisata
```python
info_tourism.Category.unique()
   ```
- Deskripsi: Melihat seluruh jenis kategori wisata yang tersedia dalam dataset.
- Output:  array(['Budaya', 'Taman Hiburan', 'Cagar Alam', 'Bahari',
       'Pusat Perbelanjaan', 'Tempat Ibadah'], dtype=object)
4. Statistik Deskriptif Data Rating
```python
tourism_rating.describe()
   ```
Deskripsi: Menganalisis statistik ringkasan dari data rating: jumlah data, rata-rata, standar deviasi, nilai minimum dan maksimum, serta kuartil.

| Statistik       | Place_Ratings      | 
|--------------|---------------|
| count | 10.000  | 
| mean  | 3.066  | 
| std  |  1.38  |
| min  |  1  |
| max  |  5  |
| 25%	  |  2  |
| 50% (median)  |  3  |
| 75%  |  4  |

**Visualisasi Data Tempat Wisata :**<br>
1. Visualisasi Distribusi Kategori Tempat Wisata
Tujuan: Untuk melihat jumlah tempat wisata berdasarkan kategorinya.
![1](https://github.com/user-attachments/assets/99bd717b-3bdc-4270-8128-2b4884ef4b20)

3. Distribusi Harga Tempat Wisata
Tujuan: Memahami rentang harga dan distribusinya di seluruh tempat wisata.
![2](https://github.com/user-attachments/assets/e632d9d1-5eb8-4fee-9d4d-11e8092c495e)

3. Distribusi Rating Tempat Wisata
Tujuan: Mengetahui bagaimana rating tersebar di seluruh tempat wisata.
![3](https://github.com/user-attachments/assets/fa4e3d56-1722-4b55-9f97-cde55e6934df)

4. Korelasi Antar Fitur Numerik
Tujuan: Melihat hubungan antara variabel numerik, yaitu Price, Rating, dan Time_Minutes.
![4](https://github.com/user-attachments/assets/e542aa00-4d63-478a-b760-73f2f40e0504)

**Visualisasi Data Rating Wisata :**<br>
1. Tempat Wisata dengan Jumlah Rating Terbanyak
Tujuan: Mengetahui tempat wisata yang paling sering diberi rating oleh pengguna.
![5](https://github.com/user-attachments/assets/bc1d8729-48aa-4092-a279-ef68b01e8476)

2. Distribusi Rating yang Diberikan Pengguna
Tujuan: Melihat pola penilaian dari pengguna.
![6](https://github.com/user-attachments/assets/671b7905-23cb-448b-97ff-5c351b0c363b)

**Visualisasi Data User :**<br>
1. Distribusi Umur Pengguna
Tujuan: Mengetahui kelompok usia yang paling aktif menggunakan platform.
![7](https://github.com/user-attachments/assets/e8a4a86d-2d6c-4c57-8903-6c53efa8a8f0)

**Visualisasi Hubungan Antar Data :**<br>
1. Rata-rata Rating per Kategori Tempat Wisata
Tujuan: Melihat kategori mana yang paling disukai pengguna berdasarkan rata-rata rating.
![8](https://github.com/user-attachments/assets/c8aa563c-2c43-466f-bf4e-31c1f002795a)

2. Rata-rata Rating Berdasarkan Umur Pengguna
Tujuan: Menganalisis perbedaan preferensi pengguna dari sisi usia.
![9](https://github.com/user-attachments/assets/79212740-2384-4377-8e0d-cb119344c887)


## Data Preparation
ada bagian ini, langkah-langkah yang diambil untuk mempersiapkan data sebelum dilakukan modeling dalam sistem rekomendasi dijelaskan. Persiapan data yang matang sangat penting untuk memastikan bahwa model yang dibangun memiliki data yang berkualitas dan dapat menghasilkan rekomendasi yang akurat.

***Langkah-langkah Data Preparation:***
1. Menggabungkan Tempat Wisata dari Dua Dataset
- Tujuan: Menggabungkan semua ID tempat wisata dari dataset informasi dan dataset rating.
- Alasan: Untuk memastikan cakupan data lengkap, karena bisa saja ada tempat wisata yang hanya muncul di satu dataset.
2. Melihat Jumlah Tempat Wisata Unik
- Tujuan: Mengecek berapa banyak total tempat wisata unik yang dimiliki sistem.
- Alasan: Untuk validasi awal dan memahami ruang rekomendasi yang akan dibangun.
3. Menggabungkan Data Rating dengan Data Tempat Wisata
- Tujuan: Menggabungkan detail tempat wisata dengan data ratingnya.
- Alasan: Dibutuhkan untuk model content-based karena memerlukan fitur seperti kota, kategori, dan deskripsi.
4. Membuat Fitur Gabungan city_category
- Tujuan: Membuat fitur teks gabungan antara kota dan kategori wisata.
- Alasan: Memberi konteks lokasi & tipe wisata secara bersamaan untuk filtering berbasis konten.
5. Pengecekan Nilai Hilang
- Tujuan: Mengecek apakah ada nilai kosong/missing.
- Alasan: Nilai kosong bisa mengganggu proses pemodelan dan perlu ditangani jika ditemukan.
6. Menghapus Duplikat Tempat Wisata
- Tujuan: Menghapus duplikat data tempat wisata.
- Alasan: Duplikasi bisa menyebabkan bias dalam perhitungan similarity atau rekomendasi yang berulang.

**Content-Based Filtering**
7. Membuat Fitur Teks dengan CountVectorizer
- Tujuan: Mengubah fitur teks city_category menjadi format numerik (bag-of-words).
- Alasan: Diperlukan agar bisa menghitung kemiripan antar item secara matematis.
8. Melihat Nama Fitur
- Tujuan: Memeriksa fitur yang dihasilkan oleh vectorizer.
- Alasan: Untuk validasi dan pemahaman fitur mana yang digunakan dalam analisis.
9. Melihat Representasi Matrix
- Tujuan: Menampilkan matriks numerik dari fitur teks.
- Alasan: Untuk memverifikasi bentuk akhir data yang akan dihitung kesamaannya.
- Output : <br>
![10](https://github.com/user-attachments/assets/32ea765b-4f9f-4911-a7be-a72f19dc9232)

![11](https://github.com/user-attachments/assets/1e863e51-b818-4c5a-a0b6-a76d301ee23f)

10. Menghitung Cosine Similarity
- Tujuan: Mengukur seberapa mirip dua tempat wisata berdasarkan fitur teksnya.
- Alasan: Digunakan sebagai dasar sistem rekomendasi berdasarkan konten.
- Output :

![12](https://github.com/user-attachments/assets/05f5e2a2-f672-4e98-b063-d83b85c73246)

11. Membuat DataFrame Kesamaan
- Tujuan: Menyimpan hasil cosine similarity dalam bentuk DataFrame yang mudah dibaca.
- Alasan: Untuk memudahkan pencarian tempat wisata yang mirip. 
- output :

![13](https://github.com/user-attachments/assets/7688edf0-9775-45a2-97e6-595369cc9f15)

**Collaborative Filtering**
12. Menyiapkan Data Rating
- Tujuan: Menyiapkan dataset utama untuk collaborative filtering.
- Alasan: Ini adalah data interaksi user dengan tempat wisata yang akan digunakan oleh model.
13. Encoding User & Place
- Tujuan: Mengubah ID ke format numerik.
- Alasan: Model pembelajaran mesin tidak bisa membaca string, perlu representasi angka.  
14. Menambahkan Kolom user & place
- Tujuan: Membuat kolom user dan place dalam bentuk encoded.
- Alasan: Digunakan sebagai input (X) dalam model.
15. Normalisasi Rating
- Tujuan: Mengubah rating ke rentang 0–1.
- Alasan: Model bisa lebih stabil dan cepat belajar jika data sudah dinormalisasi.
16. Membuat Input dan Target
- Tujuan: Menyiapkan X (fitur) dan y (label).
- Alasan: Format ini digunakan saat training model machine learning.
17. Split Data Train dan Validation
- Tujuan: Membagi data menjadi data latih dan validasi.
- Alasan: Untuk mengevaluasi model dengan data yang belum pernah dilihat sebelumnya, menghindari overfitting.

Output :

![14](https://github.com/user-attachments/assets/c1f98aa1-025b-4076-990b-2887791a726c)

![15](https://github.com/user-attachments/assets/eadbcb67-93d6-4ff2-b9a4-710799acb15a)
  
### Modeling
Pada tahap modeling, dua pendekatan yang berbeda digunakan untuk membangun sistem rekomendasi tempat wisata. Solusi pertama menggunakan Content-Based Filtering, sementara solusi kedua menggunakan Collaborative Filtering.

1. Content-Based Filtering
- Proses:
Menggunakan fitur-fitur tekstual seperti kategori tempat wisata dan deskripsi untuk menentukan kesamaan antar tempat wisata. Model ini memanfaatkan TF-IDF Vectorizer untuk memetakan teks menjadi vektor, kemudian menghitung kemiripan antar tempat wisata menggunakan Cosine Similarity.
Fungsi yang digunakan adalah:
```python
def generate_candidates(city=None, max_price=None, items=data[['Place_Id', 'Place_Name', 'Category', 'Description', 'City', 'Price']]):
    filtered_items = items
    if city:
        filtered_items = filtered_items[filtered_items['City'] == city]
    if max_price:
        filtered_items = filtered_items[filtered_items['Price'] <= max_price]
    return filtered_items
   ```
- Cara Kerja
  - Pengguna memasukkan filter seperti lokasi (kota) dan/atau harga maksimum.
  - Sistem akan menyaring tempat wisata berdasarkan dua parameter tersebut.
  - Output-nya berupa daftar tempat wisata sesuai filter, yang bisa ditampilkan sebagai Top-N (misalnya Top-5 tempat teratas).
- Kelebihan:
  - Mudah diimplementasikan
  - Tidak membutuhkan data pengguna
  - Bisa digunakan langsung meskipun pengguna baru (cold start friendly)
- Kekurangan:
  - Rekomendasi kurang bervariasi
  - Hanya menyarankan yang "mirip", tanpa kejutan atau eksplorasi baru
  - Tidak belajar dari pola pengguna lain

2. Collaborative Filtering
- Proses:
Menggunakan pendekatan Neural Collaborative Filtering (NCF) yang dikembangkan menggunakan RecommenderNet. Metode ini mengandalkan embedding untuk memetakan pengguna dan tempat wisata ke dalam ruang vektor laten, dengan pembelajaran dilakukan berdasarkan interaksi pengguna dan tempat wisata.

- Struktur Model:
```python
class RecommenderNet(tf.keras.Model):

    def __init__(self, num_users, num_place, embedding_size, **kwargs):
        ...
   ```
- Komponen utama:
1. user_embedding – memetakan user ID ke vektor embedding berdimensi tertentu
2. place_embedding – memetakan place ID ke vektor embedding
3. user_bias dan place_bias – untuk mengatasi bias pengguna dan tempat
4. dot_user_place – menghitung kemiripan antara user dan place melalui dot product
5. Activation: Fungsi sigmoid digunakan untuk mengubah output menjadi nilai probabilistik antara 0 dan 1.
   
- Training Model
Model dilatih dengan parameter berikut:
```python
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 8,
    epochs = 100,
    validation_data = (x_val, y_val),
)
   ```
Penjelasan Data
- x_train berisi pasangan [user_id, place_id]
- y_train berisi rating atau interaksi (misalnya 1 jika dikunjungi atau disukai, 0 jika tidak)
- Model belajar untuk memprediksi kemungkinan pengguna akan menyukai suatu tempat wisata

Hasil Training : <br>
![16](https://github.com/user-attachments/assets/a35b517c-61c4-484d-a996-ae1859dfed44)

- Kelebihan:
  - Menyediakan rekomendasi yang personal
  - Dapat menemukan hubungan yang tidak terlihat antar tempat wisata
  - Rekomendasi lebih akurat seiring bertambahnya data

- Kekurangan:
  - Membutuhkan banyak data historis
  - Cold Start Problem: sulit merekomendasikan untuk user baru atau tempat baru
  - Lebih kompleks dan butuh waktu pelatihan


## Evaluation

Pada tahap ini, metrik evaluasi yang digunakan untuk menilai kinerja sistem rekomendasi yang telah dibangun dibahas. Metrik evaluasi yang dipilih harus sesuai dengan tujuan dan karakteristik dari sistem rekomendasi.

1. Visualisasi Training dan Validation RMSE
Root Mean Squared Error (RMSE) : Untuk mengevaluasi model Collaborative Filtering berbasis neural network, digunakan metrik Root Mean Squared Error (RMSE). RMSE mengukur seberapa besar kesalahan prediksi model terhadap data aktual. Nilai RMSE yang lebih kecil menandakan bahwa prediksi model mendekati nilai aktual.

Formula RMSE:<br>
![21](https://github.com/user-attachments/assets/a69d0234-0e2d-4b87-b911-afa58480ee1a)

- $\hat{y}_i$ = prediksi model  
- $y_i$ = nilai aktual  
- $n$ = jumlah data  

Hasil :

![17](https://github.com/user-attachments/assets/2bbdee91-a4f6-4cf1-84bd-5901f490c098)


***Metrik Evaluasi yang Digunakan***
Untuk sistem rekomendasi, terdapat beberapa metrik evaluasi yang sering digunakan. Dalam proyek ini, kita akan fokus pada dua metrik utama yang sesuai dengan konteks Collaborative Filtering (SVD) dan Content-Based Filtering, yaitu Precision@k dan Recall@k.

1. Precision@k
Precision@k mengukur seberapa banyak item yang direkomendasikan di posisi k yang relevan bagi pengguna.
Formula dari Precision@k adalah sebagai berikut: <br>
![1](https://github.com/user-attachments/assets/d254d310-2a89-47e3-8867-917aa45762e2)

Penjelasan:
Metrik ini digunakan untuk menilai akurasi dari rekomendasi yang diberikan. Sebagai contoh, jika kita memberikan 10 rekomendasi tempat wisata kepada pengguna, maka Precision@k akan mengukur berapa banyak dari 10 tempat wisata tersebut yang relevan dengan preferensi pengguna.
3. Recall@k
Recall@k mengukur seberapa banyak item relevan yang berhasil ditemukan dari seluruh item relevan yang ada. 
Formula dari Recall@k adalah sebagai berikut: <br>
![2](https://github.com/user-attachments/assets/4174d897-a245-45f6-8439-03b3bf291ef3)

Penjelasan : 
Metrik ini digunakan untuk menilai sejauh mana rekomendasi kita dapat mencakup seluruh item relevan yang mungkin diinginkan oleh pengguna. Dalam konteks ini, recall mengukur kemampuan model untuk menyarankan tempat wisata yang relevan dari seluruh tempat wisata yang sesuai dengan preferensi pengguna.
4. F1-Score@k
F1-Score adalah metrik gabungan yang menggabungkan Precision dan Recall. 
Formula untuk F1-Score adalah: <br>
![3](https://github.com/user-attachments/assets/0bda7818-bfb3-4cb8-b143-7289cca627f4)

Penjelasan:
Metrik ini memberikan gambaran yang lebih menyeluruh mengenai kinerja model. F1-Score menjadi penting ketika kita ingin menyeimbangkan Precision dan Recall dalam memberikan rekomendasi. F1-Score digunakan untuk mengevaluasi kualitas rekomendasi yang diberikan dengan memperhatikan baik seberapa relevan rekomendasi tersebut (Precision) serta seberapa banyak item relevan yang bisa ditemukan (Recall).

**Perbandingan Evaluasi antara Content-Based Filtering dan Collaborative Filtering**

Output <br>
![sasa](https://github.com/user-attachments/assets/d443dd61-e04b-4e2d-a08a-aba2ef9ab14f)


Berikut adalah penjelasan mengenai hasil evaluasi dari dua model rekomendasi: Content-Based Filtering dan Collaborative Filtering:

1. Content-Based Filtering:
- Precision@5: 0.4000
    - Precision mengukur seberapa banyak rekomendasi yang relevan dibandingkan dengan jumlah total rekomendasi yang diberikan. Dalam hal ini, nilai precision sebesar 0.4000 menunjukkan bahwa dari 5 rekomendasi yang diberikan, hanya 40% yang relevan atau sesuai dengan preferensi pengguna.
    - Interpretasi: Ini menunjukkan bahwa hanya 2 dari 5 tempat yang direkomendasikan oleh model Content-Based Filtering dianggap relevan oleh pengguna.
- Recall@5: 0.4000
    - Recall mengukur seberapa banyak item relevan yang berhasil ditemukan dalam rekomendasi yang diberikan. Nilai 0.4000 menunjukkan bahwa hanya 40% dari tempat-tempat yang relevan (berdasarkan data relevansi pengguna) yang berhasil direkomendasikan oleh model.
    - Interpretasi: Ini berarti bahwa hanya 40% dari tempat yang seharusnya relevan menurut data pengguna berhasil dicakup oleh sistem rekomendasi. Jika ada 10 tempat yang relevan, model hanya mampu menemukan 4 dari tempat tersebut.
- F1-Score@5: 0.4000
    - F1-Score adalah metrik yang menggabungkan Precision dan Recall untuk memberikan gambaran yang lebih seimbang antara keduanya. Nilai 0.4000 menunjukkan bahwa meskipun sistem mampu memberikan beberapa rekomendasi relevan (precision), ia tidak sepenuhnya berhasil menemukan seluruh item yang relevan (recall).
    - Interpretasi: Nilai F1-Score yang sama dengan Precision dan Recall menunjukkan bahwa model tidak terlalu efektif dalam memberikan rekomendasi yang relevan, karena meskipun ada beberapa item relevan, sistem gagal menemukan banyak item yang seharusnya relevan.

Kesimpulan untuk Content-Based Filtering: Model Content-Based Filtering tampaknya memberikan rekomendasi yang kurang relevan untuk pengguna, dengan hanya 40% rekomendasi yang relevan, dan hanya dapat menemukan 40% dari item relevan yang seharusnya direkomendasikan. Ini mungkin disebabkan oleh keterbatasan model dalam memahami preferensi pengguna dengan tepat, misalnya karena kurangnya variasi dalam fitur konten yang digunakan (seperti kategori atau harga).

2. Collaborative Filtering:
- Precision@5: 1.0000
    - Precision 1.0000 menunjukkan bahwa semua dari 5 rekomendasi yang diberikan adalah relevan dengan preferensi pengguna. Dalam hal ini, 100% rekomendasi yang diberikan oleh model Collaborative Filtering dianggap tepat atau relevan.
    - Interpretasi: Ini adalah hasil yang sangat baik, yang berarti semua tempat yang direkomendasikan sesuai dengan keinginan pengguna, berdasarkan data rating atau preferensi pengguna lain yang memiliki kesamaan.
- Recall@5: 1.0000
    - Recall 1.0000 menunjukkan bahwa semua tempat yang relevan berhasil ditemukan dalam 5 rekomendasi yang diberikan. Model Collaborative Filtering berhasil menangkap semua item yang relevan dari total tempat yang relevan yang ada dalam data.
    - Interpretasi: Ini berarti bahwa jika ada 5 tempat relevan yang harus direkomendasikan, model ini berhasil menemukan dan menyarankan semuanya.
- F1-Score@5: 1.0000
    - F1-Score 1.0000 menunjukkan bahwa model berhasil menemukan keseimbangan yang sangat baik antara Precision dan Recall. Dengan Precision dan Recall keduanya sempurna (1.0000), F1-Score juga sempurna.
    - Interpretasi: Ini menandakan bahwa model Collaborative Filtering tidak hanya memberikan rekomendasi yang sangat relevan tetapi juga berhasil menemukan semua item yang relevan tanpa kehilangan item yang penting.

Kesimpulan untuk Collaborative Filtering: Model Collaborative Filtering bekerja sangat baik, memberikan rekomendasi yang sempurna dengan 100% Precision dan 100% Recall, serta mencapai F1-Score yang sangat tinggi. Ini menunjukkan bahwa model ini mampu memanfaatkan data rating dari pengguna lain untuk memberikan rekomendasi yang sangat sesuai dengan preferensi pengguna. Biasanya, Collaborative Filtering sangat efektif jika ada cukup banyak data interaksi atau rating dari pengguna lain untuk membuat prediksi.

***Perbandingan:***

- Content-Based Filtering memiliki hasil yang lebih rendah karena model ini hanya bergantung pada konten dan fitur yang ada pada tempat-tempat wisata. Dengan demikian, model ini mungkin gagal menangkap keinginan pengguna yang lebih spesifik atau tidak dapat menemukan tempat yang cukup relevan untuk direkomendasikan.
- Collaborative Filtering, di sisi lain, berfungsi lebih baik karena memanfaatkan interaksi pengguna lain (misalnya, rating atau preferensi dari pengguna serupa), yang sering kali menghasilkan rekomendasi yang lebih akurat. Ini bisa sangat efektif dalam kasus di mana preferensi pengguna tidak sepenuhnya dapat dipahami hanya dari konten.

### Testing Model
1. Content-Based Filtering
Untuk menguji sistem rekomendasi berbasis Content-Based Filtering, digunakan fungsi generate_candidates() yang menerima parameter seperti kota dan harga maksimum. Fungsi ini bertujuan menghasilkan daftar tempat wisata yang relevan berdasarkan atribut kesukaan pengguna sebelumnya, seperti lokasi dan kisaran harga.
```python
# Generate kandidat rekomendasi wisata di Bandung dengan harga maksimal Rp100.000
generate_candidates(city="Bandung", max_price=100000).head(5)

# Generate kandidat rekomendasi wisata di Surabaya dengan harga maksimal Rp110.000
generate_candidates("Surabaya", 110000).head(5)
   ```
Deskripsi: Fungsi ini mengeliminasi tempat-tempat wisata yang tidak memenuhi kriteria pengguna, lalu mengurutkan dan menampilkan 5 tempat teratas berdasarkan kesamaan fitur. Hal ini membantu pengguna menemukan wisata serupa dari preferensi sebelumnya, meski belum pernah dikunjungi.

Output : <br>

![22](https://github.com/user-attachments/assets/f9b38246-7d2c-4f6a-96fb-1337f3857463)<br>

![23](https://github.com/user-attachments/assets/d8c267e0-47b1-4ec9-bf60-11496877cdf2)

2. Collaborative Filtering
Untuk pengujian Collaborative Filtering, pendekatan yang digunakan melibatkan model prediktif berdasarkan interaksi pengguna dengan tempat wisata. Model ini memprediksi rating untuk tempat yang belum dikunjungi berdasarkan pola rating pengguna lain yang mirip.

Langkah-Langkah:
1. Mengambil Data Acak Pengguna:
```python
user_id = df.User_Id.sample(1).iloc[0]
place_visited_by_user = df[df.User_Id == user_id]
   ```
2. Menentukan Tempat yang Belum Dikunjungi: Tempat wisata yang belum dikunjungi oleh pengguna dipilih dari dataframe place_df dengan menyaring berdasarkan Place_Id.
3. Encoding dan Prediksi Rating: Tempat-tempat tersebut diencoding lalu dikombinasikan dengan ID pengguna, kemudian diprediksi ratingnya oleh model:
```python
top_ratings_indices = ratings.argsort()[-10:][::-1]
recommended_place_ids = [
    place_encoded_to_place.get(place_not_visited[x][0]) for x in top_ratings_indices
]
   ```   
4. Menampilkan Rekomendasi Terbaik:
```python
ratings = model.predict(user_place_array).flatten()
   ```
Rekomendasi ditentukan berdasarkan top 10 tempat dengan prediksi rating tertinggi.
5. Visualisasi dan Verifikasi: Ditampilkan juga tempat-tempat yang sudah pernah dikunjungi dengan rating tertinggi untuk memverifikasi kesesuaian rekomendasi:
```python
top_place_user = (
    place_visited_by_user.sort_values(
        by = 'Place_Ratings',
        ascending=False
    )
    .head(5)
    .Place_Id.values
)

place_df_rows = place_df[place_df['Place_Id'].isin(top_place_user)]
pd.DataFrame(place_df_rows)
   ```

Output : 

![24](https://github.com/user-attachments/assets/b3b381d1-499c-40c8-ac9c-618569da0b1c)


---Ini adalah bagian akhir laporan---
