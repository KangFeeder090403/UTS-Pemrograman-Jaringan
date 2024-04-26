# UTS-Pemrograman-Jaringan

**Nama : Alvito Uday Alfariz**

**NIM  : 1203220143**

# CONTENT
[HOW CODE WORK](https://github.com/KangFeeder090403/UTS-Pemrograman-Jaringan/tree/main?tab=readme-ov-file#how-code-work)



## **Soal**

Buatlah sebuah permainan yang menggunakan soket dan protokol UDP. Permainannya cukup sederhana, dengan 1 server dapat melayani banyak klien (one-to-many). Setiap 10 detik, server akan mengirimkan kata warna acak dalam bahasa Inggris kepada semua klien yang terhubung. Setiap klien harus menerima kata yang berbeda (unik). Selanjutnya, klien memiliki waktu 5 detik untuk merespons dengan kata warna dalam bahasa Indonesia. Setelah itu, server akan memberikan nilai feedback 0 jika jawabannya salah dan 100 jika benar. Program terdiri dari 1 server dan 10 client yang saling terkoneksi


# **How Code Work?**
Kode ini bekerja dengan menggunakan soket dan protokol UDP dalam bahasa _Python_. Server menggunakan konsep **(One to Many)** yang dimana server dapat melayani lebih dari 1 Client, dalam kasus ini server melayani 10 Client sekaligus ketika program server dijalankan. 

Berikut adalah kode program dari Server.py:

```ruby
import socket
import random
import time

def generate_random_color():
    colors = [
        "red", 
        "green", 
        "blue", 
        "yellow", 
        "purple", 
        "orange", 
        "black", 
        "white", 
        "brown", 
        "pink"
        ]
    return random.choice(colors)

server_ip = "127.0.0.1"  
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

print(f"Server berjalan di {server_ip}:{server_port}")

connected_clients = set()

while True:
    try:
        data, client_address = server_socket.recvfrom(1024)
        data = data.decode("utf-8")

        if client_address not in connected_clients:
            connected_clients.add(client_address)
            print(f"Klien terhubung dari {client_address}")

        if data == "request_color":
            color = generate_random_color()
            server_socket.sendto(color.encode("utf-8"), client_address)
            print(f"Kirim warna {color} ke {client_address}")

    except KeyboardInterrupt:
        print("\nServer berhenti.")
        break

server_socket.close()
```

# Penjelasan
## Server.py

```ruby
import socket # Import sodket untuk membuat jaringan soket
import time # Import modul time digunakan untuk mengirimkan warna baru setiap 10 detik dan 5 detik untuk merespons atau menjawab pertanyaan
import threading # Import modul threading untuk membuat thread baru
import random  # Import modul random untuk keperluan randomisasi
import keyboard  # Import modul keyboard untuk deteksi input dari keyboard
```
Menimport libary yang akan digunakan.

```ruby
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
```
Definisikan `def english_to_indonesian_color(english_color):` yang akan menerjemahkan warna dalam bahasa inggris ke bahasa indonesia, Fungsi ini berkesinambungan denga fungsi `color_mapping = {
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
return color_mapping.get(english_color.lower(), "tidak dikenali")` karena jika warna dalam bahasa inggris tidak ditemukan dalam penerjemah maka code akan mengembalikan   `return color_mapping.get(english_color.lower(), "tidak dikenali")`



Berikut adalah kode dari salah satu program client.py:

```ruby
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
```









