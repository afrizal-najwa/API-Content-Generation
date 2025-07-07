# API Generator Konten Otomatis

Sebuah API performa tinggi berbasis **FastAPI** yang terintegrasi dengan model **OpenAI (GPT-4o)** untuk menghasilkan berbagai jenis konten teks secara dinamis.

---

## 🚀 Tentang Proyek Ini

Proyek ini dibangun untuk menunjukkan implementasi praktis dari Large Language Models (LLM) dalam sebuah aplikasi nyata. API ini berfungsi sebagai backend yang dapat menerima permintaan terstruktur (topik, gaya bahasa, dll.) dan mengembalikan konten teks yang relevan dan berkualitas, cocok untuk mengotomatisasi tugas-tugas kreatif.

###  ✨ Fitur Utama

* **Generasi Konten Dinamis:** Mampu membuat artikel blog, caption media sosial, teks iklan, dan lainnya.
* **Kustomisasi Fleksibel:** Pengguna dapat menentukan topik, gaya bahasa, platform target, dan panjang konten.
* **Backend Cepat:** Dibangun di atas FastAPI dan Uvicorn untuk performa tinggi dan respons latensi rendah.
* **Dokumentasi Otomatis:** Dokumentasi API interaktif langsung tersedia di endpoint `/docs` (Swagger UI) dan `/redoc`.
* **Keamanan:** Pengelolaan API key yang aman menggunakan environment variables (`.env`).

---

## 🛠️ Teknologi yang Digunakan

* **Python 3.9+**
* **FastAPI:** Untuk membangun API.
* **Uvicorn:** Sebagai ASGI server.
* **OpenAI API:** Untuk mengakses model GPT.
* **Pydantic:** Untuk validasi data.
* **python-dotenv:** Untuk manajemen environment variables.

---

## ⚙️ Panduan Instalasi & Penggunaan

Berikut adalah cara untuk menjalankan proyek ini di lingkungan lokal Anda.

### 1. Prasyarat

* Python 3.9 atau yang lebih baru
* Git
* OpenAI API Key

### 2. Instalasi

1.  **Clone repository ini:**
    ```bash
    git clone [Link ke Repository GitHub Anda]
    cd [nama-folder-repo]
    ```

2.  **Buat dan aktifkan virtual environment:**
    ```bash
    # Untuk Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Untuk macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Buat file `requirements.txt`**
    *Jika Anda belum membuatnya, jalankan perintah ini di terminal PyCharm Anda untuk membuat file yang berisi semua library yang dibutuhkan:*
    ```bash
    pip freeze > requirements.txt
    ```

4.  **Install semua dependensi:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Konfigurasi Environment Variable:**
    * Buat file baru bernama `.env` di direktori utama proyek.
    * Tambahkan API Key OpenAI Anda ke dalam file `.env` seperti ini:
        ```
        OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxx"
        ```

### 3. Menjalankan Server

Jalankan server API menggunakan Uvicorn dari terminal:
```bash
uvicorn main:app --reload