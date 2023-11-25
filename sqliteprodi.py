# Mengimpor modul yang dibutuhkan
import tkinter as tk
import sqlite3

# Membuat fungsi untuk menyimpan data ke database SQLite
def simpan_data():
    # Membuka koneksi ke database SQLite
    conn = sqlite3.connect("prodidb.db")
    # Membuat objek cursor untuk menjalankan perintah SQL
    cur = conn.cursor()
    # Membuat tabel nilai_siswa jika belum ada
    cur.execute("""CREATE TABLE IF NOT EXISTS nilai_siswa (
        nama_siswa TEXT,
        biologi INTEGER,
        fisika INTEGER,
        inggris INTEGER,
        prediksi_fakultas TEXT
    )""")
    # Mengambil nilai dari entry tkinter
    nama = entry_nama.get()
    biologi = int(entry_biologi.get())
    fisika = int(entry_fisika.get())
    inggris = int(entry_inggris.get())
    # Menentukan prediksi fakultas berdasarkan nilai tertinggi
    if biologi > fisika and biologi > inggris:
        prediksi = "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        prediksi = "Teknik"
    elif inggris > biologi and inggris > fisika:
        prediksi = "Bahasa"
    else:
        prediksi = "Tidak dapat diprediksi"
    # Menyimpan data ke tabel nilai_siswa
    cur.execute("INSERT INTO nilai_siswa VALUES (?, ?, ?, ?, ?)", (nama, biologi, fisika, inggris, prediksi))
    # Menampilkan hasil prediksi di label tkinter
    luaran_label.config(text=f"Hasil Prediksi: {prediksi}")
    # Menutup koneksi ke database SQLite
    conn.commit()
    conn.close()

# Membuat jendela utama
window = tk.Tk()
window.title("Aplikasi Prediksi Prodi Pilihan")

# Membuat label judul
judul_label = tk.Label(window, text="Aplikasi Prediksi Prodi Pilihan", font=("Helvetica", 16))
judul_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Membuat input nama siswa
nama_label = tk.Label(window, text="Masukkan Nama Siswa:")
nama_label.grid(row=1, column=0, padx=10, pady=10)
entry_nama = tk.Entry(window)
entry_nama.grid(row=1, column=1, padx=10, pady=10)

# Membuat input nilai mata pelajaran
mata_pelajaran_label = tk.Label(window, text="Masukkan Nilai Mata Pelajaran:")
mata_pelajaran_label.grid(row=2, column=0, padx=10, pady=10)

# Membuat input nilai biologi
biologi_label = tk.Label(window, text="Biologi:")
biologi_label.grid(row=3, column=0, padx=10, pady=5)
entry_biologi = tk.Entry(window)
entry_biologi.grid(row=3, column=1, padx=10, pady=5)

# Membuat input nilai fisika
fisika_label = tk.Label(window, text="Fisika:")
fisika_label.grid(row=4, column=0, padx=10, pady=5)
entry_fisika = tk.Entry(window)
entry_fisika.grid(row=4, column=1, padx=10, pady=5)

# Membuat input nilai inggris
inggris_label = tk.Label(window, text="Inggris:")
inggris_label.grid(row=5, column=0, padx=10, pady=5)
entry_inggris = tk.Entry(window)
entry_inggris.grid(row=5, column=1, padx=10, pady=5)

# Membuat button simpan data
button_simpan = tk.Button(window, text="Simpan Data", command=simpan_data)
button_simpan.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Membuat label luaran hasil produksi
luaran_label = tk.Label(window, text="Hasil Prediksi: ", font=("Helvetica", 12))
luaran_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Menjalankan jendela aplikasi
window.mainloop()