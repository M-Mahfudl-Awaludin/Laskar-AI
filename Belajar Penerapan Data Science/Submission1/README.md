# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju adalah sebuah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan mempekerjakan lebih dari 1000 karyawan yang tersebar di seluruh Indonesia. Walaupun telah menjadi perusahaan besar, Jaya Jaya Maju menghadapi tantangan dalam mengelola karyawannya secara efisien. Hal ini terlihat dari tingginya tingkat attrition (turnover) karyawan, yang telah mencapai lebih dari 10% dari total keseluruhan tenaga kerja.

Tingginya angka attrition ini dapat menyebabkan kerugian besar bagi perusahaan, seperti meningkatnya biaya rekrutmen, pelatihan, penurunan produktivitas, serta kehilangan pengetahuan dan pengalaman yang berharga. Oleh karena itu, perusahaan ingin memahami penyebab utama dari tingginya attrition rate dan memantau faktor-faktor risiko tersebut secara real-time melalui dashboard bisnis.

### Permasalahan Bisnis

- Tingginya attrition rate yang berdampak negatif terhadap kinerja dan stabilitas perusahaan.
- Tidak adanya sistem monitoring yang terintegrasi untuk mengidentifikasi potensi penyebab attrition.
- Kurangnya pemahaman terhadap pola atau variabel-variabel penting yang memicu karyawan keluar dari perusahaan.
- Belum adanya model prediksi yang bisa digunakan HR untuk mengidentifikasi risiko turnover.

### Cakupan Proyek

- Melakukan eksplorasi dan analisis data karyawan yang telah disediakan perusahaan.
- Membuat model machine learning sederhana untuk memprediksi kemungkinan seorang karyawan akan keluar dari perusahaan.
- Mengembangkan business dashboard interaktif menggunakan Google Looker Studio untuk memantau metrik-metrik penting terkait attrition.
- Memberikan rekomendasi kebijakan strategis berdasarkan hasil analisis dan visualisasi.

### Persiapan
Sumber Data:
Data Asli : [Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee).

Dataset yang telah dibersihkan: [employee_cleaned_data.csv](https://github.com/M-Mahfudl-Awaludin/Laskar-AI/blob/a61ead7411dc4cfbab560964e231b40e10257303/Belajar%20Penerapan%20Data%20Science/Submission1/dataset/employee_cleaned_data.csv)

Setup Environment:

- Bahasa pemrograman: Python

- Library: pandas, sklearn, matplotlib, seaborn, joblib

- Alat visualisasi: Google Looker Studio

- Tools pendukung: Google Colab untuk eksplorasi data dan pembuatan model


## Business Dashboard

Dashboard yang dibuat menggunakan Google Looker Studio bertujuan untuk menampilkan visualisasi dari faktor-faktor yang memengaruhi attrition karyawan. Beberapa visualisasi utama dalam dashboard antara lain:

- Total karyawan vs karyawan yang keluar
- Attrition rate (%) secara keseluruhan
- Distribusi attrition berdasarkan departemen, usia, gender, status lembur (OverTime), job satisfaction, dll.
- Komparasi attrition berdasarkan faktor-faktor risiko

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

