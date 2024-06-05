# Submission Akhir: Menyelesaikan Permasalahan Institusi Pendidikan


## Business Understanding
Jaya Jaya Institut merupakan perguruan tinggi yang telah mencetak banyak lulusan yang sangat baik, akan tetapi terdapat siswa yang dropout dengan jumlah yang terbilang tidak sedikit. 

### Permasalahan Bisnis
Membantu untuk mendeteksi penyebab banyaknya siswa yang dropout di Jaya Jaya Institut serta membuat dashboard untuk memonitor peforma siswa.

### Cakupan Proyek
Membuat dashboard untuk menganalisis siswa yang dropout dan membuat machine learning untuk memprediksi kemungkinan siswa yang akan dropout.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md

Setup environment:
```
- conda create --name myenv python=3.xx # create virtual env with your python version
- conda activate myenv # activate virtual env
- pip install -r requirements.txt # install library
- pip install jupyter # to open jupyter notebook
- jupyter-notebook . # open jupyter notebook
```

## Business Dashboard
Business Dashboard menggambarkan penyebab tingginya Dropout yang terjadi di Jaya Jaya Institut, Status terbagi menjadi 2 kategori yaitu Dropout dan Non-Dropout (Graduate & Enrolled) untuk memudahkan analysis. Hasilnya adalah banyak siswa yang menanggung biaya pendidikan sendiri & tidak memiliki beasiswa, lalu terjadi penurunan penilaian dari semester pertama dan semester akhir. 

Link Dashboard:
https://public.tableau.com/app/profile/rizq.ramadhan5793/viz/DicodingJayaJayaInstitutSubmission/Dashboard1?publish=yes

## Menjalankan Sistem Machine Learning
Disarankan menggunaan VSCode atau IDE sejenisnya, dan membuka terminal dengan perintah:

```
- python3 -m venv myenv # create virtual env
- myenv\Scripts\activate # activate virtual env
- pip install -r requirements.txt # installing library
- streamlit run app.py # running streamlit
```
Link Prototype Machine Learning:
https://rizq-ramadhan-final-submission.streamlit.app/

## Conclusion
saya menyimpulkan bahwa kebanyakan siswa yang bersekolah di Jaya Jaya Institut menanggung biayanya sendiri serta tidak menggunakan beasiswa ataupun hutang untuk pendidikannya. 

Kemudian, diketahui status dari siswa di Jaya Jaya Institut masih single dan hanya sedikit yang memiliki pasangan, yang artinya siswa masih tidak memiliki tanggungan, lalu siswa yang berstatus dropout memiliki rata-rata umurnya yaitu 26.1 dan siswa yang sudah lulus/masih belajar mendaftar di usia yang lebih muda yaitu 21.9 tahun.

Siswa yang dropout memiliki nilai yang cenderung menurun, sedangkan siswa yang masih sekolah/sudah lulus cenderung meningkat dalam nilainya, itulah perbedaan yang mendasar antara siswa yang dropout dan siswa yang tidak dropout.

### Rekomendasi Action Items
Rekomendasi Action Items untuk Jaya Jaya Institut, untuk mengurangi dropout siswanya:
- Membuka lebih banyak beasiswa untuk siswanya dalam rangka mengurangi beban biaya pendidikannya pada siswa
- Memantau perkembangan nilai siswa dan mengadakan konseling untuk mengetahui kesulitan dari siswa
- Menghadirkan workshop atau events yang dapat membantu skill dan perkembangan siswa 