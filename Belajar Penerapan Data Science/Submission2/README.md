# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut adalah sebuah institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000. Dengan reputasi yang sangat baik, Jaya Jaya Institut telah mencetak banyak lulusan yang sukses. Namun, salah satu masalah besar yang dihadapi institusi ini adalah tingginya tingkat dropout atau ketidakselesaian pendidikan oleh sejumlah mahasiswa.

Angka dropout yang tinggi ini berdampak negatif terhadap citra institusi dan sumber daya yang telah dikeluarkan. Oleh karena itu, Jaya Jaya Institut ingin mengidentifikasi mahasiswa yang berisiko tinggi untuk drop out sedini mungkin, sehingga mereka dapat diberikan bimbingan atau intervensi yang lebih awal untuk meningkatkan kemungkinan mereka menyelesaikan studi.

### Permasalahan Bisnis

- Tingginya angka dropout yang merugikan reputasi dan stabilitas institusi.
- Tidak adanya sistem yang dapat memprediksi mahasiswa yang berisiko drop out.
- Kurangnya informasi atau pemahaman tentang variabel-variabel yang mempengaruhi keputusan mahasiswa untuk berhenti kuliah.

### Cakupan Proyek

- Melakukan eksplorasi dan analisis data yang diberikan oleh Jaya Jaya Institut mengenai mahasiswa.
- Membangun model machine learning untuk memprediksi status mahasiswa apakah berisiko dropout atau tidak.
- Mengembangkan dashboard bisnis interaktif menggunakan Google Looker Studio untuk memvisualisasikan faktor-faktor yang mempengaruhi kemungkinan mahasiswa dropout.
- Memberikan rekomendasi kepada pihak institusi mengenai tindakan yang bisa diambil berdasarkan hasil analisis dan visualisasi.

### Persiapan
Sumber Data:
Data Asli : [students' performance]([https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)).

Dataset yang telah dibersihkan: [data_clean.csv](https://github.com/M-Mahfudl-Awaludin/Laskar-AI/blob/a57ab5fe6f4eb7e33f1821e3532ed4a9128c0ab4/Belajar%20Penerapan%20Data%20Science/Submission2/data/data_clean.xlsx)

### Setup Environment:
1. Persyaratan Sistem
- Python 3.7+
- PIP (Python Package Manager)
- Jupyter Notebook / JupyterLab / Google Colab
- IDE seperti VSCode (opsional)
2. 2. Installasi Dependensi
Pastikan sudah berada di direktori project.
- Buat Virtual Environment (Opsional tapi direkomendasikan)
```
python -m venv venv
source venv/bin/activate        # Linux / Mac
venv\Scripts\activate           # Windows
```
- Install Dependensi
```
pip install -r requirements.txt
```

Jika belum ada file requirements.txt, kamu bisa install manual:
```
pip install pandas matplotlib seaborn numpy jupyter
```
3. Struktur Direktori
```
├── notebook.ipynb         <- File utama berisi analisis
├── dataset.csv            <- Dataset (jika terpisah)
├── requirements.txt       <- Daftar dependensi
└── README.md              <- Petunjuk ini
```

4. Menjalankan Notebook
```
jupyter notebook
```
Setelah itu, buka file notebook.ipynb dari Jupyter interface.

**Alternatif: Jalankan di Google Colab**
1. Buka Google Colab
2. Upload file notebook.ipynb
3. Jalankan seluruh cell

Untuk mengakses Dashboard Business : [Dashboard](https://lookerstudio.google.com/reporting/8be8c7b8-501d-4148-936b-396f2c27bc7a)

Untuk mengakses Solusi Machine Learning : [Status Mahasiswa App](https://laskar-ai-quzymd6tgksk5jincbdd8w.streamlit.app/)

## Business Dashboard

Dashboard Bisnis: Faktor-Faktor yang Mempengaruhi Status Mahasiswa
Dashboard yang dibuat menggunakan Google Looker Studio bertujuan untuk memberikan visualisasi yang komprehensif mengenai faktor-faktor yang memengaruhi status mahasiswa di Jaya Jaya Institut, dengan fokus pada analisis mahasiswa yang mengalami dropout dan mereka yang berhasil lulus. Beberapa visualisasi yang akan ditampilkan adalah sebagai berikut:

1. Jumlah Mahasiswa yang Dropout vs Jumlah Mahasiswa yang Lulus
Pada visualisasi ini, Anda akan melihat perbandingan antara jumlah mahasiswa yang berhasil menyelesaikan studinya (lulus) dan jumlah mahasiswa yang tidak berhasil menyelesaikan pendidikannya (dropout). Grafik ini memungkinkan kita untuk memahami seberapa besar dampak dropout terhadap keseluruhan jumlah mahasiswa dan memberikan gambaran awal tentang tingkat keberhasilan institusi dalam mendukung mahasiswa menyelesaikan pendidikan mereka.

2. Korelasi Antara Nilai Kualifikasi dan Status Mahasiswa
Di dalam dashboard, terdapat visualisasi yang menunjukkan hubungan antara nilai kualifikasi sebelumnya (sebelum masuk ke Jaya Jaya Institut) dengan status mahasiswa (apakah dropout atau lulus). Hal ini bertujuan untuk menganalisis apakah mahasiswa dengan nilai kualifikasi rendah memiliki kecenderungan lebih besar untuk dropout dibandingkan mereka yang memiliki kualifikasi lebih tinggi.

Insight:

Mahasiswa dengan nilai kualifikasi rendah cenderung berisiko lebih tinggi untuk tidak menyelesaikan studi mereka.

3. Distribusi Mahasiswa Berdasarkan Program Studi dan Usia
Visualisasi ini memperlihatkan distribusi mahasiswa berdasarkan program studi mereka dan usia saat pendaftaran. Analisis ini memberikan gambaran apakah faktor program studi atau usia mahasiswa memiliki pengaruh terhadap kemungkinan mereka untuk dropout. Misalnya, program studi yang lebih menantang atau memerlukan keterampilan khusus mungkin memiliki angka dropout yang lebih tinggi.

4. Visualisasi Faktor-Faktor Risiko yang Mempengaruhi Keputusan Mahasiswa untuk Dropout
Pada visualisasi terakhir, dashboard ini menampilkan faktor-faktor risiko yang mungkin mempengaruhi keputusan mahasiswa untuk dropout. Faktor-faktor ini mencakup nilai akademik, evaluasi unit kurikuler, status penerima beasiswa, dan kebutuhan pendidikan khusus. Dengan memahami faktor-faktor ini, pihak institusi dapat merancang intervensi dini untuk membantu mahasiswa yang berisiko tinggi dropout, seperti memberikan bimbingan akademik atau bantuan lebih lanjut di semester awal.

Visualisasi :

Hali.1 

![dashboard_1](https://github.com/user-attachments/assets/4dfbd902-0897-4edc-9826-484969252598)

Hal.2

![dashboard_2](https://github.com/user-attachments/assets/ebeeeab4-0eb1-47aa-9dcd-cacf114df6e6)


📊 Link Dashboard : [Dashboard](https://lookerstudio.google.com/reporting/6397db59-743d-444e-8fd5-505799193efd)


## Menjalankan Sistem Machine Learning
1. Akses Prototype
Akses prototype sistem Machine Learning yang telah dikembangkan menggunakan Streamlit melalui tautan berikut: [Status Mahasiswa App](https://laskar-ai-quzymd6tgksk5jincbdd8w.streamlit.app/).

Setelah membuka tautan, halaman utama prototype akan muncul.

![Solusi ML](https://github.com/user-attachments/assets/69e2f604-2d82-49f3-9edf-5e6d68203758)

2. Input Data Mahasiswa
Pada halaman utama, data mahasiswa yang diperlukan untuk memprediksi status mereka (Lulus, Putus Studi, atau Terdaftar) harus dimasukkan. Berikut adalah data yang perlu diinputkan:

- 📝 Data Pendaftaran Mahasiswa
  - Mode Pendaftaran: Pilih cara pendaftaran mahasiswa (misalnya: online, langsung).
  - Fakultas: Pilih fakultas yang diikuti (misalnya: Fakultas Ekonomi).
  - Urutan Pendaftaran: Pilih urutan pendaftaran mahasiswa pada periode tertentu.
  - Pendaftar Kedua: Menunjukkan apakah mahasiswa adalah pendaftar kedua (Ya/Tidak).
  - Program Studi: Pilih program studi yang diambil oleh mahasiswa (misalnya: Akuntansi).
- 📅 Jadwal & Kualifikasi
  - Waktu Kuliah: Pilih waktu kuliah yang diambil (Pagi/Siang/Malam).
  - Kualifikasi Sebelumnya: Pilih kualifikasi pendidikan yang dimiliki mahasiswa sebelum mendaftar di institut (misalnya: Diploma 3).
  - Nilai Kualifikasi Sebelumnya: Masukkan nilai kualifikasi sebelumnya (misalnya: 0.00).
- 📊 Data Personal & Beasiswa
  - Nilai Penerimaan: Masukkan nilai penerimaan mahasiswa (misalnya: 0.00).
  - Kebutuhan P.Khusus: Pilih apakah mahasiswa memerlukan kebutuhan khusus (Memerlukan/Tidak Memerlukan).
  - Jenis Kelamin: Pilih jenis kelamin mahasiswa (Laki-laki/Perempuan).
  - Penerima Beasiswa: Pilih apakah mahasiswa merupakan penerima beasiswa (Ya/Tidak).
- 📈 Data Akademik Semester 1
  - Usia Daftar: Masukkan usia mahasiswa pada saat pendaftaran (misalnya: 18).
  - Unit K. Smt 1 Dikreditkan: Masukkan jumlah unit yang dikreditkan pada semester pertama (misalnya: 0).
  - Unit K. Smt 1 Daftar: Masukkan jumlah unit yang didaftar pada semester pertama (misalnya: 0).
  - Evaluasi K. Smt 1: Masukkan nilai evaluasi untuk semester pertama (misalnya: 0).
  - Unit K. Smt 1 Disetujui: Masukkan jumlah unit yang disetujui pada semester pertama (misalnya: 0).
  - Nilai Unit K. Smt 1: Masukkan nilai unit yang didapat pada semester pertama (misalnya: 0).
  - Unit K. Smt 1 Tanpa Eval: Masukkan jumlah unit tanpa evaluasi pada semester pertama (misalnya: 0).
- 📈 Data Akademik Semester 2
  - Unit K. Smt 2 Dikreditkan: Masukkan jumlah unit yang dikreditkan pada semester kedua (misalnya: 2).
  - Unit K. Smt 2 Daftar: Masukkan jumlah unit yang didaftar pada semester kedua (misalnya: 3).
  - Evaluasi Unit K. Smt 2: Masukkan nilai evaluasi unit pada semester kedua (misalnya: 2).
  - Nilai Unit K. Smt 2: Masukkan nilai unit yang didapat pada semester kedua (misalnya: 2).
  - Unit K. Smt 1 Tanpa Eval: Masukkan jumlah unit pada semester pertama yang tidak dievaluasi (misalnya: 2).
  - Unit K. Smt 2 Disetujui: Masukkan jumlah unit yang disetujui pada semester kedua (misalnya: 0).

3. Proses Prediksi
Setelah data mahasiswa dimasukkan, sistem akan secara otomatis melakukan proses prediksi menggunakan model XGBoost yang telah dilatih.

Model ini akan memproses data yang diinputkan dan memberikan prediksi status mahasiswa apakah Lulus, Putus Studi (Dropout), atau Terdaftar.

4. Lihat Hasil Prediksi
Setelah proses prediksi selesai, hasilnya akan ditampilkan secara langsung pada dashboard.

Status mahasiswa dapat dilihat apakah berisiko tinggi untuk dropout atau tidak, berdasarkan data yang dimasukkan. Hasil ini akan memberikan insight tentang status akademik mahasiswa dan seberapa besar kemungkinan mereka untuk lulus atau putus studi.


```
https://laskar-ai-quzymd6tgksk5jincbdd8w.streamlit.app/
```


## Conclusion

Dari hasil analisis dan model prediksi yang menggunakan XGBoost, dapat disimpulkan sebagai berikut:

1. Hubungan Antara Evaluasi dan Kualifikasi dengan Dropout:

Nilai kualifikasi sebelumnya dan evaluasi unit kurikuler semester 1 menunjukkan hubungan yang signifikan dengan keputusan mahasiswa untuk berhenti kuliah (dropout). Mahasiswa dengan evaluasi rendah atau kualifikasi sebelumnya yang kurang memadai lebih berisiko untuk tidak menyelesaikan studi mereka. Evaluasi yang buruk pada awal masa perkuliahan menjadi indikator penting dalam prediksi risiko mahasiswa untuk dropout.

2. Keunggulan Model XGBoost:

Model XGBoost memberikan hasil yang sangat baik dalam mengidentifikasi mahasiswa yang berisiko tinggi untuk dropout. Dengan precision, recall, dan f1-score yang memadai pada kategori lulus dan dropout, model ini lebih unggul dalam menangani imbalanced class, di mana jumlah mahasiswa yang dropout relatif lebih sedikit dibandingkan dengan yang lulus. Hal ini memungkinkan model untuk memberikan prediksi yang lebih akurat dibandingkan dengan model lain.

3. Pemantauan Kinerja Mahasiswa dengan Google Looker Studio dan Streamlit:

Dengan menggunakan Google Looker Studio, pihak Jaya Jaya Institut dapat memantau performa mahasiswa secara real-time. Hal ini memungkinkan mereka untuk mengambil tindakan preventif lebih cepat terhadap mahasiswa yang berisiko tinggi untuk dropout, serta memastikan tindakan yang lebih tepat sasaran. Selain itu, platform Streamlit yang terintegrasi dengan solusi ML memungkinkan interaksi yang lebih mudah dan visualisasi prediksi yang lebih efisien.

### Rekomendasi Action Items (Optional)

Berdasarkan hasil prediksi dan analisis menggunakan XGBoost, berikut adalah beberapa rekomendasi yang dapat diambil oleh Jaya Jaya Institut untuk mengurangi angka dropout dan meningkatkan tingkat kelulusan mahasiswa:

1. **Peningkatan Dukungan Akademik untuk Mahasiswa dengan Evaluasi Rendah pada Semester Pertama:** Mahasiswa dengan evaluasi unit kurikuler semester pertama yang rendah perlu diberikan bimbingan intensif agar dapat meningkatkan kinerja akademik mereka. Ini dapat mencakup pendampingan akademik serta intervensi psikososial untuk membantu mereka mengatasi hambatan yang ada.

2. **Program Bimbingan Intensif bagi Mahasiswa yang Berisiko Tinggi untuk Dropout:** Mahasiswa yang terdeteksi berisiko tinggi untuk dropout harus segera menerima program bimbingan intensif yang dirancang untuk meningkatkan motivasi, prestasi akademik, dan kesejahteraan mereka secara menyeluruh. Menggunakan prediksi model, pihak institusi dapat merancang program bimbingan yang lebih terfokus dan tepat sasaran.

3. **Pemantauan Terus-Menerus Menggunakan Dashboard untuk Memantau Kinerja Mahasiswa Secara Real-Time:** Dengan Google Looker Studio dan Streamlit, pihak institut dapat memantau kinerja mahasiswa secara real-time dan dengan mudah mengidentifikasi mahasiswa yang berisiko tinggi. Dashboard ini menyediakan visualisasi yang jelas terkait status mahasiswa berdasarkan data input yang diberikan oleh mahasiswa, sehingga langkah-langkah pencegahan bisa dilakukan lebih cepat dan lebih terarah.

