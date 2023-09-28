#Nama : Andreas Risky Ardian Kusuma
#Nim  : 195114031
#dasar sockets
#level udp
#bagian pendengar (Penerima)

from tkinter import*
import socket
import threading

root = Tk()
root.title("Aplikasi Chat, User = AAAA")
root.geometry("580x400")
l1 = Label(root, text = 'IP Tujuan : ')
l2 = Label(root, text = 'Port Tujuan: ')
l1.grid(column=0, row=0, padx=5, pady=3)
l2.grid(column=0, row=1, padx=5, pady=3)
e1 = Entry(root,width = 16)
e2 = Entry(root,width = 16)
e1.grid(column=1, row=0, padx=5, pady=3)
e2.grid(column=1, row=1, padx=5, pady=3)

l1b = Label (root, text = 'IP Asal :')
l2b = Label(root, text = 'Port Asal:')
l1b.grid(column=0, row=2, padx=5, pady=3)
l2b.grid(column=0, row=3, padx=5, pady=3)
e1b = Entry(root,width = 16)
e2b = Entry(root,width = 16)
e1b.grid(column=1, row=2, padx=5, pady=3)
e2b.grid(column=1, row=3, padx=5, pady=3)

tchat = Text (root, bg= 'lime' , width= 70, height=12)
tchat.grid(column=0, row=4, padx=5, pady=5, sticky=N+E+W+S, columnspan=4)

epesan = Entry(root, bg= 'lime' )
epesan.grid(row=5, column=0, padx=5, pady=5, columnspan=2, sticky=E+W)

def bersih():
    epesan.delete(0, END)

bok = Button(root, text='ok')
bok.grid(row=5, column=2, padx=5, pady=5,sticky = E+W)
bclr = Button(root, text='clear', command=bersih)
bclr.grid(row=5, column=3, padx=5, pady=5,sticky = E+W)

pendengar = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #
alamat1 = ('127.0.0.1',8008)   #alamat pakai local address, Pengirim dan
                                #penerima dalam satu komputer

pendengar.bind(alamat1)
pengirim = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #
alamat2 = ('127.0.0.1',8080)  #alamat pakai local address, pengirim dan
                              #penerima dalam satu komputer
e1.insert(0,alamat2[0])
e2.insert(0,alamat2[1])
e1b.insert(0,alamat1[0])
e2b.insert(0,alamat1[1])

def dengar():
    while True:
        print ('menunggu pesan...')
        pesan = pendengar.recvfrom(1024)
        print (pesan)
        tchat.insert(1.0,pesan[0].decode() + '\n')
def kirim(event):
    alamat_tujuan= (e1.get(), int(e2.get()))
    print(alamat_tujuan)
    pesan = epesan.get()
    print(pesan)
    pengirim.sendto(pesan.encode(),alamat_tujuan)

bok.bind('<Button-1>', kirim)
th= threading.Thread(target=dengar)
th.setDaemon(True)
th.start()
root.mainloop()
