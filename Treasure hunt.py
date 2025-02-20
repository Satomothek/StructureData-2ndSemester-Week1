import random

while True:
    try:
        size = int(input("Masukkan ukuran peta: "))
        if size > 0:
            break
        else:
            print("Masukikan angka positif!")
    except ValueError:
        print("Masukkan angka yang valid!")

treasure_map = ["_" for _ in range(size)]

treasure_index = random.randint(0, size - 1)
treasure_map[treasure_index] = "X"

print(f"Selamat datang di Treasure Hunt! Peta memiliki {size} lokasi (0 hingga {size-1}).")

def play_treasure_hunt():
    visible_map = ["_" for _ in range(size)]
    print("\nHarta karun telah disembunyikan! Sekarang giliran pemain menebak.")
    print("Cobalah untuk menemukan harta karun dengan menebak indeks yang benar.")

    while True:
        print("\nPeta saat ini:", visible_map)
        try:
            guess = int(input(f"Masukkan indeks tebakanmu (0-{size-1}): "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if guess < 0 or guess >= size:
            print("Indeks tidak valid, pilih antara 0 hingga", size - 1)
            continue

        if treasure_map[guess] == "X":
            visible_map[guess] = "X"
            print("\nPeta saat ini:", visible_map)
            print("✓ Selamat! Kamu menemukan harta karun di lokasi:", guess)
            break
        else:
            visible_map[guess] = "O"
            print("✖ Tidak ada harta di lokasi ini. Coba lagi!")

    print("Terima kasih sudah bermain!")

play_treasure_hunt()