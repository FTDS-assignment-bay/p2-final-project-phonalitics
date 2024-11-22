[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/8qmUfAce)

# Final-Project

<div align='center'>
    <h1><b>Welcome to PhonALytics!</b></h1>
    <img src='https://github.com/FTDS-assignment-bay/p2-final-project-phonalitics/blob/main/phonALytics.png' width="300"/>
    <br><br>
    <p>phonALytics merupakan aplikasi yang dapat menganalisis sentimen pada suatu produk handphone untuk membantu seseoang dalam mengambil keputusan terkait barang yang ingin dibeli.</p>
    <br>
</div>
<table style="width: 100%; text-align: center; border-collapse: collapse;">
    <tr>
        <th style="padding: 10px;">Hugging Face</th>
    </tr>
    <tr>
        <td style="padding: 10px;">
            <a href="https://huggingface.co/spaces/stanlys96/Phonalitics">
                <img src="https://img.shields.io/badge/Demo-Hugging%20Face-blue" alt="Hugging Face Demo">
            </a>
        </td>
    </tr>
</table>

---

## **Introduction**

Program ini dibuat untuk membantu masyarakat dalam memilih smartphone dengan memanfaatkan analisis sentimen netizen di platform YouTube. Aplikasi ini dirancang untuk menganalisis sentimen komentar menggunakan teknik NLP (Natural Language Processing) berbasis Deep Learning.

Aplikasi ini bertujuan untuk memberikan rekomendasi berbasis data yang membantu masyarakat dalam pengambilan keputusan pembelian smartphone. Dengan adanya aplikasi ini, diharapkan pengguna dapat mengambil keputusan yang lebih informatif, efisien, dan tepat sasaran dalam memilih smartphone.

---

## **Background**

Dikutip dari salah satu [jurnal](https://www.neliti.com/id/publications/171816/penentuan-karakteristik-pengguna-sebagai-pendukung-keputusan-dalam-memilih-smart#cite) mengatakan bahwa smartphone telah menjadi kebutuhan penting bagi berbagai lapisan masyarakat, baik dari kalangan atas maupun bawah. Seiring dengan meningkatnya permintaan, berbagai vendor smartphone menawarkan harga, fitur, sistem operasi, dan teknologi yang beragam. Namun, sering kali keinginan dan kebutuhan masyarakat yang terus berkembang tidak sejalan dengan pilihan smartphone yang ada. Hal ini membuat banyak pengguna kesulitan dalam memilih smartphone yang tepat, karena keputusan pembelian seringkali dipengaruhi oleh faktor gengsi dan perilaku konsumtif (Sandika, Ian G., et al., 2014).

---

## **Objective**

- Menganalisis sentimen komentar video YouTube.
- Mempermudah pemahaman opini publik dengan sentimen utama dan visualisasi.
- Memberikan rekomendasi pembelian smartphone berbasis data.

---

## **Methods**

Dalam pengerjaan proyek ini, terdapat 2 metode yang menjadi pondasi dalam pembuatan aplikasi, yaitu Web Scrapping dan Modeling.

### Web Scraping

Web scraping dalam proyek ini memiliki 2 tujuan, yaitu untuk mengumpulkan data untuk melatih model yang dibuat dan sebagai _user input_ yang dapat mengetahui hasil sentimen analisis suatu produk _handphone_ yang dirilis pada tahun 2024 dan 2025.

- Dalam pengumpulan data, sumber yang digunakan berasal dari YouTube sehingga _labeling_ dilakukan secara manual untuk menentukan sentimen positif, negatif, dan netral.
- Pada sudut pandang aplikasi, pengguna akan dihadapkan oleh tampilan untuk melihat hasil sentimen analisis suatu produk _handphone_ yang dirilis pada tahun 2024 dan 2025 dan tampilan yang dapat memasukkan _link_ YouTube untuk dilakukan analisis dari sentimen yang dihasilkan produk _handphone_ sehingga dapat membantu dalam pengambilan keputusan dalam membeli suatu barang.

### Modeling

Modeling bertujuan untuk memproses teks berupa sentimen yang dihasilkan suatu produk, baik itu berdasarkan data yang telah dikumpulkan atau berasal dari pengguna berupa _link_ sehingga dapat mengetahui suatu produk _handphone_ mengarah ke sentimen negatif, positif, atau netral. Analisis tersebut termasuk dalam kategori _Natural Language Processing_ yang menggunakan Deep Learning berupa **Long Short-Term Memory**.

---

## phonALytics Team

- [Handwitanto Abraham](https://www.linkedin.com/in/handwitanto-abraham/)
- [Serina Roihaanah Mulawati](http://www.linkedin.com/in/serina-roihaanah-mulawati)
- [Stanly Sukmajaya Kwok](https://www.linkedin.com/in/stanly-sukmajaya)
- [Achmad Raihan](https://www.linkedin.com/in/achmad-raihan/)
