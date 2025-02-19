# Ukuran Peta
size = 10

# Membuat peta dengan harta karun tersembunyi
treasure_map = ["_" for _ in range(size)]

# Tentukan lokasi harta karun secara manual
print(f"Selamat Datang di Treasure Hunt! Peta memiliki {size} lokasi (0 hingga {size-1}).")
treasure_index = int(input(f"Masukkan lokasi harta karun (0-{size-1}) : "))
while treasure_index < 0 or treasure_index >= size:
  print("Lokasi tidak valid. Masukkan angka dalam rentang yang benar.")
  treasure_index = int(input(f"Masukkan lokasi harta karun (0-{size-1}) : "))

treasure_map[treasure_index] = "X" # Menyembunyikan harta karun dilokasi yang dipilih

# Fungsi untuk memulai permainan
def play_treasure_hunt():
  print("\nHarta karun telah disembunyikan! Sekarang giliran pemain menebak.")
  print("Cobalah untuk menemukan harta karun dengan menebak indeks yang benar.")

  # Loop Permainan
  while True:
    # Menampilkan peta tersembunyi kepada pemain
    print("\nPeta saat ini : ", ["_" for _ in range (size)]) # Peta Tersembunyi

    # Input Pemain
    try:
      guess = int(input(f"Masukkan indeks tebakanmu (0-{size-1}) : "))
    except ValueError:
      print("Masukkan angka yang valid!")
      continue

    # Validasi Input
    if guess < 0 or guess >= size:
      print("Indeks tidak valid, pilih antara 0 hingga", size-1)
      continue

    # Mengecek apakah tebakan benar
    if treasure_map[guess] == "X":
      print("✓ Selamat! Kamu menemukan harta karun di lokasi : ", guess)
      break
    else:
      print("✖ Tidak ada harta dilokasi ini. Coba lagi!")
  print("Terimakasih Sudah bermain!")

# Jalankan Permainan
play_treasure_hunt()