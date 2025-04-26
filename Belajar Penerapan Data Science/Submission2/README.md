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

Dashboard yang dibuat menggunakan Google Looker Studio bertujuan untuk menampilkan visualisasi dari faktor-faktor yang memengaruhi attrition karyawan. Beberapa visualisasi utama dalam dashboard antara lain:

- Total karyawan vs karyawan yang keluar
- Attrition rate (%) secara keseluruhan
- Distribusi attrition berdasarkan departemen, usia, gender, status lembur (OverTime), job satisfaction, dll.
- Komparasi attrition berdasarkan faktor-faktor risiko

Visualisasi :

![m_mahfudl_awaludin_ztNf-dashboard](https://github.com/user-attachments/assets/3c8ad559-010d-41da-8845-07ff8905896f)


📊 Link Dashboard : [Dashboard](https://lookerstudio.google.com/reporting/6397db59-743d-444e-8fd5-505799193efd)

## Conclusion

Berdasarkan hasil eksplorasi dan visualisasi data:

- Faktor-faktor seperti lembur, job satisfaction rendah, dan pendapatan bulanan rendah memiliki korelasi kuat dengan tingginya kemungkinan karyawan keluar.
- Model prediksi yang dibuat dengan algoritma Random Forest memberikan performa yang baik dalam mengklasifikasi apakah seorang karyawan berpotensi keluar.
- Dashboard bisnis memungkinkan tim HR untuk memantau kondisi attrition dan faktor risiko secara cepat dan intuitif.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- Tinjau ulang kebijakan lembur dan workload

Karyawan yang bekerja lembur secara rutin menunjukkan kemungkinan attrition yang lebih tinggi. Perusahaan sebaiknya menyeimbangkan beban kerja dan memberikan kompensasi atau kebijakan fleksibel.

- Fokus pada peningkatan kepuasan kerja

Peningkatan job satisfaction melalui program pengembangan karir, pelatihan, dan keterlibatan karyawan dapat secara signifikan mengurangi kemungkinan turnover.

- Kompensasi yang kompetitif

Karyawan dengan pendapatan bulanan rendah cenderung lebih mudah keluar. Perusahaan perlu memastikan skema gaji yang kompetitif dan transparan.

- Gunakan model prediktif untuk monitoring karyawan secara proaktif

Gunakan model machine learning untuk mendeteksi karyawan berisiko tinggi agar tim HR bisa mengambil langkah preventif, seperti dialog langsung atau intervensi pengembangan personal.

