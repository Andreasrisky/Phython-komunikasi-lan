#Nama : Andreas Risky Ardian Kusuma
#Nim  : 195114031
#dasar sockets
#level udp
#bagian pendengar (Penerima)

import socket
pendengar = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #
alamat = ('127.0.0.1',8080)       #alamat paka local address, pengirim dan
                                #penerima dalam satu konputer
pendengar.bind(alamat)
while True:
    print('Menunggu Pesan....')
    pesan = pendengar.recvfrom(1024)
    print('Pesan         : '), pesan
    print('Isi Pesan     : '), pesan[0].decode()
    print('Address,port  : '), pesan[1]
    print('Address       : '), pesan[1][0]
    print('Port          : '), pesan[1][1]
