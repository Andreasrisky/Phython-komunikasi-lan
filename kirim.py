#Nama : Andreas Risky Ardian Kusuma
#Nim  : 195114031
#dasar sockets
#level udp
#bagian pengirim

import socket
pengirim = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #
alamat = ('127.0.0.1',8080)       #alamat paka local address, pengirim dan
                                 #penerima dalam satu komputer

while True:
    x = input('Pesan :')
    pengirim.sendto(x.encode(),alamat)
