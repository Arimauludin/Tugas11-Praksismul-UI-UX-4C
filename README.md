# AriMA-crunch - Web Penjualan Berbasis Flask & Bootstrap

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Flask](https://img.shields.io/badge/Framework-Flask-green.svg)
![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap-purple.svg)
![Deployment](https://img.shields.io/badge/Deploy-Render%20%2F%20Heroku-brightgreen.svg)

Proyek ini merupakan **Tugas 11 Praktikum Sistem Multimedia (Praksismul)** yang bertujuan untuk membangun dan mendeploy aplikasi web penjualan produk dari brand **AriMA-crunch** berbasis *Point of View* (POV) User.

---

## 📌 Fitur Utama

- **Home (`/`)**: Halaman utama yang menampilkan banner promosi, keunggulan produk, dan pengenalan brand **AriMA-crunch**.
- **Daftar Produk (`/products`)**: Menampilkan katalog varian produk (seperti Makroni Pedas Level 1, Level 2, Level 3) lengkap dengan gambar, harga, dan deskripsi.
- **Form Checkout (`/checkout`)**: Halaman transaksi pemesanan produk yang dilengkapi dengan **validasi form**.
- **Riwayat Transaksi (`/history`)**: Halaman untuk melihat riwayat pesanan yang telah dikirimkan oleh pengguna.

---

## 📁 Struktur Direktori Project

```text
AriMA-crunch/
│
├── static/                  # File Statis (CSS & Gambar)
│   ├── css/
│   │   └── style.css
│   └── images/
│       ├── logo.png
│       ├── makroni-level1.jpeg
│       ├── makroni-level2.jpeg
│       └── makroni-level3.jpeg
│
├── templates/               # Template HTML (Jinja2)
│   ├── base.html            # Layout utama (Navbar & Footer)
│   ├── index.html           # Halaman Home
│   ├── products.html        # Halaman Daftar Produk
│   ├── checkout.html        # Halaman Form Checkout
│   └── history.html         # Halaman Riwayat Pesanan
│
├── .gitignore               # Mengabaikan file yang tidak perlu di-push ke Git
├── app.py                   # File utama aplikasi Flask (Backend)
├── Procfile                 # Konfigurasi deployment (Gunicorn)
└── requirements.txt         # Daftar dependensi library Python