from auth import login, register_user, users
from menu import menu_admin, menu_user
from utils import clear_screen, pause 

is_running = True

while is_running:
    clear_screen()
    print('=== SISTEM PEMINJAMAN PS ANANTA ===')
    print('1. Login')
    print('2. Daftar Akun Baru')
    print('3. Keluar')
    menu_awal = input('Pilih menu: ')
    if menu_awal == '1':
        username = login()
        if username:
            role = users[username]['role']
            if role == 'admin':
                menu_admin(username)
            elif role == 'user':
                menu_user(username)
            else:
                print('Anda siapa??? Gak kenal ah.')
                pause()
    elif menu_awal == '2':
        register_user()
    elif menu_awal == '3':
        print('Keluar dari program. Sampai jumpa!')
        is_running = False
    else:
        print('Pilihan tidak valid.')
        pause()