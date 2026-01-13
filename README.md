# SHTKA – Organisir File Sertifikat TKA

Script Python sederhana untuk memindahkan file PDF SHATKA siswa ke folder per rombel (kelas) berdasarkan data NISN di Excel. File PDF SHTKA dihasilkan dengan mendownload dari web portal TKA.

Format nama file:
NISN - NAMA_SISWA.pdf

```
Contoh:
0088237814 - ALESHA_RAIA_DWIPAYANA.pdf
```
```
Data referensi diambil dari file Excel dengan header:
No | NISN | Nama PD | Rombel
```

## Fitur

- Otomatis membuat folder rombel (contoh: XII-1, XII-2, dst)
- Memindahkan / menyalin file PDF sesuai rombel
- Menangani NISN dengan leading zero (contoh: 00xxxx)
- Aman digunakan untuk data besar


## Environment

### Sistem Operasi
- Windows 10 / 11
- Linux (Ubuntu, Debian, dll)

### Versi Python
- Python 3.9+ (disarankan 3.10 atau 3.11)

### Package Manager
- pip 21+


## Struktur Folder
```
shtka/
├── pindah.py
├── data_siswa.xlsx
├── files/          (taruh semua PDF di sini)
│   └── .gitkeep
├── output/         (hasil akan muncul di sini)
├── requirements.txt
└── README.md
```

## Setup Awal (Sebelum Run)

Pastikan Python dan pip sudah terinstall.

### 1. Clone Repository

```
git clone https://github.com/andripriyanto/shtka.git
cd shtka
```

### 2. (Disarankan) Buat Virtual Environment

Linux / macOS:
```
python3 -m venv venv
source venv/bin/activate
```

Windows (PowerShell):
```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependency

```
pip install -r requirements.txt
```

### 4. Siapkan Data

1. Taruh semua file PDF ke folder: files/

2. Pastikan format nama file: NISN - NAMA.pdf

3. Pastikan data_siswa.xlsx ada di root project dan memiliki kolom: NISN | Rombel


## Cara Menjalankan

```
python pindah.py
```

Setelah selesai:
- Folder output/ akan berisi subfolder sesuai rombel
- File PDF akan berada di folder rombel masing-masing


## Catatan Penting

- Kolom NISN di Excel harus bertipe Text, bukan Number (agar leading zero tidak hilang)
- Folder files/ tidak ikut di-push ke repository (hanya placeholder)
- Folder output/ di-generate otomatis oleh script


## Versi

1.0.0 – Versi awal, sortir PDF berdasarkan NISN & rombel


## Author

Andri Priyanto  
IT Support – SMA Taruna Bakti


## Lisensi

Bebas digunakan untuk keperluan internal sekolah / pendidikan.
