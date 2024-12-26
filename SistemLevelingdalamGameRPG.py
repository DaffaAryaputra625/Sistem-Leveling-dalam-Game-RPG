import time

# Fungsi Sistem RPG (Iteratif)
def rpg_iteratif(n):
    level_pemain = 1
    for stage in range(1, n + 1):
        level_musuh = stage
        if level_pemain >= level_musuh:
            level_pemain = level_musuh + 1
        else:
            break

# Fungsi Sistem RPG (Rekursif)
def rpg_rekursif(level_pemain, stage, max_stage):
    if stage > max_stage:
        return
    level_musuh = stage
    if level_pemain >= level_musuh:
        rpg_rekursif(level_musuh + 1, stage + 1, max_stage)

# Sistem Game RPG untuk Pemain
def rpg_game():
    print("Selamat datang di Sistem RPG!")
    print("Tujuan Anda adalah menyelesaikan 5 stage untuk memenangkan permainan.\n")

    level_pemain = 1
    base_level_musuh = 1
    faktor_scaling = 1
    max_stage = 5

    for stage in range(1, max_stage + 1):
        print(f"\n--- STAGE {stage} ---")
        level_musuh = base_level_musuh + (stage - 1) * faktor_scaling
        print(f"Level Pemain: {level_pemain}")
        print(f"Musuh: Level {level_musuh}")

        konfirmasi = input("Apakah Anda yakin ingin bertarung melawan musuh ini? (ya/tidak): ").strip().lower()
        if konfirmasi != "ya":
            print("Anda memutuskan untuk mundur. Game berakhir.")
            break

        if level_pemain >= level_musuh:
            print("Anda menang melawan musuh!")
            level_pemain = level_musuh + 1
            print(f"Level Anda sekarang: {level_pemain}")
        else:
            print("Anda kalah melawan musuh.")
            print("Game Over.")
            break
    else:
        print("\nSelamat! Anda menyelesaikan semua stage.")
    print("Terima kasih telah bermain!")

# Pengukuran Running Time
def ukur_waktu():
    stages = [1, 2, 3, 4, 5]  # Stage dibatasi hingga 5
    hasil_iteratif = []
    hasil_rekursif = []

    print("\nMengukur waktu eksekusi dalam mikrodetik...\n")
    for n in stages:
        # Iteratif
        start = time.time()
        rpg_iteratif(n)
        end = time.time()
        hasil_iteratif.append((end - start) * 1_000_000)  # Dalam mikrodetik

        # Rekursif
        start = time.time()
        try:
            rpg_rekursif(1, 1, n)
            end = time.time()
            hasil_rekursif.append((end - start) * 1_000_000)  # Dalam mikrodetik
        except RecursionError:
            hasil_rekursif.append("Error")

    # Menampilkan hasil pengukuran
    print("Jumlah Stage | Iteratif (\u00b5s)  | Rekursif (\u00b5s)")
    print("---------------------------------------------")
    for i in range(len(stages)):
        iteratif_time = f"{hasil_iteratif[i]:.2f}" if isinstance(hasil_iteratif[i], float) else hasil_iteratif[i]
        rekursif_time = f"{hasil_rekursif[i]:.2f}" if isinstance(hasil_rekursif[i], float) else hasil_rekursif[i]
        print(f"{stages[i]:<13} | {iteratif_time:<13} | {rekursif_time}")

# Main Program
if __name__ == "__main__":
    # Jalankan game RPG
    rpg_game()

    # Pengukuran dan perbandingan running time
    ukur_waktu()
