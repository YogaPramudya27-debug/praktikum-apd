from utils import clear_screen, pause 
from rental import tambah_data, lihat_data, ubah_data, hapus_data

def menu_admin(username):
    while True:
        clear_screen()
        print('=== MENU ADMIN ===')
        print('1. Tambah Data Sewa')
        print('2. Lihat Data Sewa')
        print('3. Ubah Data Sewa')
        print('4. Hapus Data Sewa')
        print('5. Logout')
        pilihan = input('Pilih menu: ')
        if pilihan == '1':
            tambah_data(username, role='admin')
        elif pilihan == '2':
            lihat_data()
        elif pilihan == '3':
            ubah_data()
        elif pilihan == '4':
            hapus_data()
        elif pilihan == '5':
            print('Logout berhasil! Kembali ke menu login...')
            pause()
            break
        else:
            print('Pilihan tidak valid.')
            pause()

def menu_user(username):
    while True:
        clear_screen()
        print('=== MENU USER ===')
        print('1. Tambah data')
        print('2. Lihat data')
        print('3. Logout')

        pilihan = input('Pilih menu: ')
        if pilihan == '1':
            tambah_data(username, role ='user')
        elif pilihan == '2':
            lihat_data()
        elif pilihan == '3':
            break
        else:
            print('Pilihan mu gak valid bro.')
            pause()