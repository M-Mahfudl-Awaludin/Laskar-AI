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
1. Pemeriksaan Data Missing (Missing Data Handling)
- Alasan: Data yang hilang dapat mengurangi akurasi model, sehingga perlu ditangani dengan tepat. Jika tidak, bisa menyebabkan bias atau mengurangi kualitas prediksi.
- Proses: Memeriksa setiap kolom dalam dataset untuk melihat apakah ada nilai yang hilang menggunakan metode isnull() dan sum(). Kolom dengan nilai hilang yang signifikan diimputasi dengan nilai yang tepat.

2. Pembersihan Data Duplikat
- Alasan: Data duplikat bisa mengganggu analisis dan memberikan hasil yang bias. Ini dapat menyebabkan rekomendasi yang tidak akurat karena beberapa entri data yang identik diperlakukan seolah-olah mereka adalah data yang berbeda.
- Proses: Memeriksa dan menghapus baris yang memiliki nilai duplikat dengan menggunakan fungsi drop_duplicates().

3. Konversi Tipe Data
- Alasan: Beberapa kolom dalam dataset mungkin memiliki tipe data yang tidak sesuai (misalnya, kolom numerik yang disimpan sebagai string). Konversi tipe data yang tepat diperlukan agar model dapat memproses data dengan benar.
- Proses: Memastikan bahwa kolom seperti rating, harga, dan ID tempat wisata memiliki tipe data numerik yang sesuai.

4. Feature Engineering dan Normalisasi
- Alasan: Beberapa fitur mungkin memerlukan transformasi agar sesuai dengan model rekomendasi. Normalisasi harga atau rating dapat membantu model dalam memahami rentang nilai yang serupa.
- Proses: Menambahkan fitur baru jika diperlukan, seperti menggabungkan kategori tempat wisata atau melakukan normalisasi nilai dengan fungsi MinMaxScaler.

5. Encoding Kategori
- Alasan: Kolom kategori dalam data perlu diubah menjadi format numerik agar dapat digunakan dalam model berbasis algoritma pembelajaran mesin.
- Proses: Menggunakan teknik one-hot encoding untuk kolom kategori tempat wisata dan lokasi.

### Modeling
Pada tahap modeling, dua pendekatan yang berbeda digunakan untuk membangun sistem rekomendasi tempat wisata. Solusi pertama menggunakan Content-Based Filtering, sementara solusi kedua menggunakan Collaborative Filtering.

1. Content-Based Filtering
- Proses:
Menggunakan fitur-fitur tekstual seperti kategori tempat wisata dan deskripsi untuk menentukan kesamaan antar tempat wisata. Model ini memanfaatkan TF-IDF Vectorizer untuk memetakan teks menjadi vektor, kemudian menghitung kemiripan antar tempat wisata menggunakan Cosine Similarity.

- Kelebihan:
    - Tidak memerlukan data interaksi pengguna.
    - Memberikan rekomendasi berdasarkan preferensi pengguna yang sudah diketahui.

- Kekurangan:
    - Terbatas hanya pada item yang sudah diketahui preferensinya. Tidak dapat memberikan rekomendasi item baru (cold start problem).
    - Tidak mempertimbangkan interaksi pengguna dengan item lain yang dapat memberikan perspektif tambahan.

    ***Output***
   ![Capture](https://github.com/user-attachments/assets/da658803-7498-4bd6-9858-098ef6fdcd1f)

2. Collaborative Filtering
- Proses:
Menggunakan pendekatan Neural Collaborative Filtering (NCF) yang dikembangkan menggunakan RecommenderNet. Metode ini mengandalkan embedding untuk memetakan pengguna dan tempat wisata ke dalam ruang vektor laten, dengan pembelajaran dilakukan berdasarkan interaksi pengguna dan tempat wisata.

- Model Arsitektur:
Model dibangun dengan layer embedding untuk pengguna dan tempat wisata, ditambah bias pada masing-masing layer. Hasil embedding dan bias digabungkan menggunakan operasi dot product dan fungsi aktivasi sigmoid.

- Kelebihan:
    - Memberikan rekomendasi berdasarkan pola interaksi antar pengguna dan tempat wisata.
    - Lebih fleksibel dan dapat menangani cold start problem dengan lebih baik, terutama jika ada data pengguna yang cukup.

- Kekurangan:
    - Memerlukan data interaksi pengguna yang banyak untuk memberikan rekomendasi yang akurat.
    - Dapat menjadi kurang efektif jika data interaksi pengguna sangat sedikit atau tidak beragam.

 Output <br>
    ![sss](https://github.com/user-attachments/assets/d1dac8de-08e1-4f5d-b026-77a055a79acf)


## Evaluation

Pada tahap ini, metrik evaluasi yang digunakan untuk menilai kinerja sistem rekomendasi yang telah dibangun dibahas. Metrik evaluasi yang dipilih harus sesuai dengan tujuan dan karakteristik dari sistem rekomendasi.

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

***Evaluasi Berdasarkan Metrik***
Langkah-langkah Evaluasi
Berikut adalah evaluasi yang dapat dilakukan untuk dua model ini berdasarkan rekomendasi yang dihasilkan.

1. Content-Based Filtering Evaluation
Pada Content-Based Filtering, rekomendasi dihitung berdasarkan kesamaan konten dari tempat yang sudah dikunjungi oleh pengguna dengan tempat-tempat lain yang tersedia. Dalam contoh ini, sistem memberikan rekomendasi tempat-tempat berdasarkan kategori dan harga yang relevan dengan preferensi pengguna.

    Contoh output rekomendasi yang dihasilkan: <br>
    ![Capture](https://github.com/user-attachments/assets/6767da50-ae54-4168-8aa9-be550c707f48)
    
    
    Proses evaluasi Content-Based Filtering:
    - Precision@k:
    Mengukur apakah tempat-tempat yang direkomendasikan kepada pengguna relevan dengan preferensi mereka.
    Misalnya, jika tempat yang sudah dikunjungi oleh pengguna memiliki kesamaan kategori dan harga dengan rekomendasi, maka itu dihitung sebagai relevan.
    
    - Recall@k:
    Mengukur apakah rekomendasi berhasil mencakup semua tempat relevan yang mungkin ingin dikunjungi oleh pengguna.
    Jika ada lebih banyak tempat relevan yang tidak tercakup oleh sistem, maka recall akan rendah.
    
    - F1-Score@k:
    Menggunakan Precision dan Recall untuk mendapatkan ukuran keseimbangan antara keduanya.

2. Collaborative Filtering Evaluation
Pada Collaborative Filtering, model ini menggunakan data rating dan preferensi dari pengguna lain untuk memberikan rekomendasi kepada pengguna tertentu.

    Contoh output rekomendasi yang dihasilkan: <br>
    ![sss](https://github.com/user-attachments/assets/e2332d4c-4f24-4a13-b5f9-3b01ece5a33d)
    
    
    
    Proses evaluasi Collaborative Filtering:
    
    - Precision@k:
    Sama seperti pada Content-Based Filtering, kita menghitung seberapa akurat rekomendasi yang diberikan, apakah sesuai dengan rating tinggi yang diberikan oleh pengguna.
    
    - Recall@k:
    Dalam Collaborative Filtering, recall mengukur seberapa banyak tempat yang relevan dari segi rating yang bisa ditemukan dalam rekomendasi yang diberikan oleh sistem.
    
    - F1-Score@k:
    Kombinasi dari Precision dan Recall untuk mengevaluasi keseimbangan antara keduanya.

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

---Ini adalah bagian akhir laporan---
