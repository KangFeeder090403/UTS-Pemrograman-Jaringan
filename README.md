# UTS-Pemrograman-Jaringan

**Nama : Alvito Uday Alfariz**

**NIM  : 1203220143**




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

**OUTPUT**

![image](https://github.com/KangFeeder090403/UTS-Pemrograman-Jaringan/assets/112238835/ad9bdf4c-7c06-4a48-8c86-2dc98763873a)








