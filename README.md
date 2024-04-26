# UTS-Pemrograman-Jaringan

**Nama : Alvito Uday Alfariz**

**NIM  : 1203220143**



# CONTENT
[HOW CODE WORK](https://github.com/KangFeeder090403/UTS-Pemrograman-Jaringan/blob/main/README.md#how-code-work)
* [Penjelasan Server Side](https://github.com/KangFeeder090403/UTS-Pemrograman-Jaringan/blob/main/README.md#penjelasan)
* [Penjelasan Client Side Side](
https://github.com/KangFeeder090403/UTS-Pemrograman-Jaringan/blob/main/README.md#penjelasan-1)



[CONTOH PENGGUNAAN](https://github.com/KangFeeder090403/UTS-Pemrograman-Jaringan/blob/main/README.md#contoh-penggunaan-)
* [ 1 Server 1 Client](https://github.com/KangFeeder090403/UTS-Pemrograman-Jaringan/blob/main/README.md#1-serverpy-dan-1-clientpy)
*  [ TEST CASE 1 Server 10 Client ](https://github.com/KangFeeder090403/UTS-Pemrograman-Jaringan/blob/main/README.md#1-serverpy-dan-10-clientpy)


[Contoh Output berupa gambar dan vidio](https://github.com/KangFeeder090403/UTS-Pemrograman-Jaringan/tree/main/Gambar%20dan%20Vidio%20Output)






## **Soal**

Buatlah sebuah permainan yang menggunakan soket dan protokol UDP. Permainannya cukup sederhana, dengan 1 server dapat melayani banyak klien (one-to-many). Setiap 10 detik, server akan mengirimkan kata warna acak dalam bahasa Inggris kepada semua klien yang terhubung. Setiap klien harus menerima kata yang berbeda (unik). Selanjutnya, klien memiliki waktu 5 detik untuk merespons dengan kata warna dalam bahasa Indonesia. Setelah itu, server akan memberikan nilai feedback 0 jika jawabannya salah dan 100 jika benar. Program terdiri dari 1 server dan 10 client yang saling terkoneksi


# **How Code Work?**
Kode ini bekerja dengan menggunakan soket dan protokol UDP dalam bahasa _Python_. Server menggunakan konsep **(One to Many)** yang dimana server dapat melayani lebih dari 1 Client, dalam kasus ini server melayani 10 Client sekaligus ketika program server dijalankan. 

# Berikut adalah kode program dari Server.py berserta outputnya :

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

**OUTPUT :**

![image](https://github.com/KangFeeder090403/UTS-Pemrograman-Jaringan/assets/112238835/ad9bdf4c-7c06-4a48-8c86-2dc98763873a)


# Penjelasan

1. Import kode dari libary yaitu `socket` untuk membuat socket jaringan , `random` untuk mendapatkan warna warna random yang akan dikirimkan ke client dan `time` untuk melakukan operasi random.

2. `generate_random_color()` digunakan mendefinisikan warna warna yang ada dan kemudian memilih salah satu warna yang sudah didaftarkan secara acak dari daftar tersebut dengan menggunakan `random.choice()`

3. `server_ip` `server_port` menyimpan alamat ip dan alamat port, dalam kasus ini ditetapkan menjadi `"127.0.0.1" (localhost)`, dan nomor port ditetapkan menjadi `12345`.

4. `socket.socket(socket.AF_INET, socket.SOCK_DGRAM)` Server dibuat dengan menggunakan protkol UDP dan dan nomor port server dengan menggunakan `server_socket.bind((server_ip, server_port))`.

5. `print(f"Server berjalan di {server_ip}:{server_port}")` Menujukan server berjalan di ip mana dan port mana.

6. `connected_clients` digunakan untuk menyimpan daftar alamat klien yang terhubung ke server, setelah itu akan melakukan loop `while True`hingga server menunggu permintaan dari klien. Jika permintaan diterima dan berisi pesan `"request_color"`, server akan memanggil fungsi g`enerate_random_color()` untuk mendapatkan warna secara acak, dan mengirimkan warna tersebut kembali ke klien. Jika klien berhasil terhubung ke server, alamat klien akan ditambahkan ke set `connected_clients`, dan pesan akan dicetak untuk menunjukkan bahwa klien telah terhubung.

Kesimpulan dari penjelasan kode ini adalah, sebuah server UDP yang akan mengirimkan warna secara acak kepada klien - klien  yang berhasil terhubung, setelah itu klien mengirim permintaan `"request_color"`. Maka Server akan langsung berjalan di alamat IP 127.0.0.1 (localhost) dan nomor port 12345.


# Berikut adalah kode program dari salah satu client.py berserta outputnya :

```ruby
import socket # Import sodket untuk membuat jaringan soket
import time # Import modul time digunakan untuk mengirimkan warna baru setiap 10 detik dan 5 detik untuk merespons atau menjawab pertanyaan
import threading # Import modul threading untuk membuat thread baru
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

**OUTPUT :**

![image](https://github.com/KangFeeder090403/UTS-Pemrograman-Jaringan/assets/112238835/74cb2261-d5e5-4283-a234-fb4a13be352b)


# Penjelasan

1. Import kode dari libary yaitu `socket` untuk membuat socket jaringan , `random` untuk mendapatkan warna warna random yang akan dikirimkan ke client dan `time` untuk melakukan operasi random, `threading` untuk membuat thread baru, `keyboard` mendeteksi modul keyboard guna untuk mengheintak program dengan tombol yang ada di keyboard.

2. Mendefinisikan `def english_to_indonesian_color(english_color):` untuk menejermahkan warna warna dari bahasa inggris ke bahasa indonesia, lalu `color_mapping` digunakan untuk memetakan warna warna dalam bahasa inggirs yang sudah diinputkan oleh pengguna serta terjemahannya juga.

3. `server_ip` `server_port` menyimpan alamat ip dan alamat port, dalam kasus ini ditetapkan menjadi `"127.0.0.1" (localhost)`, dan nomor port ditetapkan menjadi `12345`.

4. `socket.socket(socket.AF_INET, socket.SOCK_DGRAM)` Server dibuat dengan menggunakan protkol UDP dan dan nomor port server dengan menggunakan `server_socket.bind((server_ip, server_port))`.

5. Mendefinisikan fungsi `def input_with_timeout(prompt, timeout):` yang berguna untuk membaca input dari pengguna dengan batasan waktu `timeout` detik. Lalu mendefinisikan juga fungsi `def input_thread():` untuk membaca input dari pengguna. Jika pengguna tidak merespons dalam waktu timeout detik, maka akan mencetak pesan dan mengembalikan `None`.

6. Client akan meminta pengiriman `"request_color"` ke server dan menunggu balasan berupa warna dalam bahasa Inggris. Setelah client menerima pengiriman dari server maka fungsi `input_with_timeout()` akan berjalan yang berguna untuk mencetak warna yang sudah dikirimkan dan meminta pengguna untuk menerjemahkan warna tersebut ke dalam bahasa Indonesia menggunakan dengan waktu tunggu 5 detik.

7. Loop Utama: Program memasuki loop utama yang akan berjalan tanpa henti `(while True)`. Di dalam loop ini, klien:
* Mengirim permintaan "request_color" ke server dengan menggunakan client_socket.sendto(). *
* Menerima data dari server (dalam hal ini, warna) dan kemudian menerjemahkannya ke bahasa Indonesia menggunakan fungsi english_to_indonesian_color(). *
* `if random.random() < 0.4:` digunakan untuk membuat perbandinga `40%` salah dan `60%` benar. Jika salah color_mapping yang digunakan tentu berbeda dengan respong benar, color_mapping yang digunakan yang salah memiliki terjemahan yang berbeda contoh nya : `"merah muda": "coklat"` sedangkan color_mapping yang benar adalah `"pink": "merah muda"`. Jika respon benar maka client akan menjalankan fungsi `if response is not None:` lalu mengembalikan dan mencetak dengan  `print("Jawaban benar! Nilai feedback: 100")` sebaliknya jika salah maka akan mencetak `print("Jawaban salah. Nilai feedback: 0")`. *
* Menunggu selama 10 detik sebelum mengirim permintaan kembali ke server.*
8. `if keyboard.is_pressed('esc'):` Pengecekan Keyboard: Program melakukan pengecekan tombol keyboard pada setiap iterasi loop. Jika tombol "esc" ditekan, loop akan dihentikan dan program keluar Inilah kenapa libary `import keyboard` dibutuhkan. *
9. Penutup Soket: Setelah keluar dari loop, program menutup soket klien dengan client_socket.close(). *


# Contoh Penggunaan :

# 1 Server.py dan 1 Client.py.

Untuk menjalankannya cukup dengan `_Run Code_` Sever.py dan `_Run Python File In Dedicated Terminal_`

![image](https://github.com/KangFeeder090403/UTS-Pemrograman-Jaringan/assets/112238835/ad9bdf4c-7c06-4a48-8c86-2dc98763873a)

Server Side

![image](https://github.com/KangFeeder090403/UTS-Pemrograman-Jaringan/assets/112238835/74cb2261-d5e5-4283-a234-fb4a13be352b)

Client Side


Keterangan :

* Jika Menebak warna dengan Benar maka akan mendapatkan nilai feedback 100 *
* Jika menebak warna dengan Salah maka akan mendapatkan nilai feedback 0 *


# TEST CASE 1 Server.py dan 10 Client.py 

Untuk menjalankan 1 server dan 10 Client dengan waktu bersamaan maka diperlukan kode script untuk menangani ini. Kode script nya cukup sederharna yaitu :

```ruby
import subprocess
import platform
import time

def run_command_in_terminal(command):
    if platform.system() == "Windows":
        subprocess.Popen(["start", "cmd", "/k", command], shell=True)
    elif platform.system() == "Linux":
        subprocess.Popen(["x-terminal-emulator", "-e", command])
    elif platform.system() == "Darwin":  # macOS
        subprocess.Popen(["open", "-a", "Terminal", command])
    else:
        print("Unsupported platform")


commands = [
    "python server.py",
    "python client.py",
    "python client2.py",
    "python client3.py",
    "python client4.py",
    "python client5.py",
    "python client6.py",
    "python client7.py",
    "python client8.py",
    "python client9.py",
    "python client10.py",
]

for command in commands:
    run_command_in_terminal(command)
    time.sleep(2)
```

Dengan begini menjalankan 1 Server dan 10 Client cukup menggunakan CMD dengan menjalkan perintah ini :
```
 > python runall.py
```

![image](https://github.com/KangFeeder090403/UTS-Pemrograman-Jaringan/assets/112238835/6ab96f7e-4aff-4e1d-8e5e-c6b63b246b57)


![image](https://github.com/KangFeeder090403/UTS-Pemrograman-Jaringan/assets/112238835/d04e8981-d734-40bd-b7b9-89bc7327f27b)


Keterangan :

* Jika Menebak warna dengan Benar maka akan mendapatkan nilai feedback 100 *
* Jika menebak warna dengan Salah maka akan mendapatkan nilai feedback 0 *









