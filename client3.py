import socket
import time
import threading
import random  # Import modul random untuk keperluan randomisasi
import keyboard  # Import modul keyboard untuk deteksi input dari keyboard


def english_to_indonesian_color(english_color):
    # Color mapping untuk terjemahan warna dari bahasa Inggris ke Indonesia
    color_mapping = {
        "red": "merah",
        "green": "hijau",
        "blue": "biru",
        "yellow": "kuning",
        "purple": "ungu",
        "orange": "oranye",
        "black": "hitam",
        "white": "putih",
        "brown": "coklat",
        "pink": "merah muda",
    }
    return color_mapping.get(english_color.lower(), "tidak dikenali")

server_ip = "127.0.0.1"  # Ganti dengan alamat IP server
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def input_with_timeout(prompt, timeout):
    print(prompt, flush=True)
    response = [None]  # Response will be stored here

    def input_thread():
        try:
            response[0] = input()
        except:
            pass

    thread = threading.Thread(target=input_thread)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        print(f"\nAnda tidak menjawab selama {timeout} detik\n")
        print("Tekan Enter untuk melanjutkan\n")
        thread.join()
        return None
    else:
        return response[0]

try:
    while True:
        client_socket.sendto("request_color".encode("utf-8"), (server_ip, server_port))
        color, server_address = client_socket.recvfrom(1024)
        color = color.decode("utf-8")
        print(f"Warna yang diterima: {color}")

        indonesian_color = english_to_indonesian_color(color)
        print(f"Jawaban yang benar: {indonesian_color}")

        # Tentukan respons klien
        if random.random() < 0.4:  # 40% kemungkinan jawaban salah
            # Color mapping untuk jawaban yang salah
            wrong_color_mapping = {
                "merah muda": "coklat",
                "biru": "hijau",
                "hijau": "biru",
                "ungu": "kuning",
                "kuning": "ungu",
                "hitam": "orange",
                "oranye": "hitam",
                "coklat": "putih",
                "putih": "brown",
                "merah": "pink",
            }
            response = wrong_color_mapping.get(indonesian_color.lower(), "tidak dikenali")
        else:
            response = indonesian_color  # Jawaban yang benar

        print(f"Jawaban klien: {response}")

        if response is not None:
            if response.lower() == indonesian_color.lower():
                print("Jawaban benar! Nilai feedback: 100")
            else:
                print("Jawaban salah. Nilai feedback: 0")
        else:
            print("Waktu habis. Nilai feedback: 0")

        print("-" * 40)  # Garis pembatas antar respon
        time.sleep(10)  # Tunggu 10 detik sebelum mengirim permintaan lagi

        if keyboard.is_pressed('esc'):
            print("\nKlient Berhenti.")
            break

except KeyboardInterrupt:
    print("\nKlien berhenti.")
finally:
    client_socket.close()
