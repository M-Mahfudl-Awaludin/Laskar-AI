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
Paragraf awal bagian ini menjelaskan informasi mengenai data yang Anda gunakan dalam proyek. Sertakan juga sumber atau tautan untuk mengunduh dataset. Contoh: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data).

Selanjutnya uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

### Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
- accepts : merupakan jenis pembayaran yang diterima pada restoran tertentu.
- cuisine : merupakan jenis masakan yang disajikan pada restoran.
- dst

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data atau exploratory data analysis.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.
