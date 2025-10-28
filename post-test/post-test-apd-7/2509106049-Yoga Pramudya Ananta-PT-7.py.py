import os

users = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'user': {'password': 'user123', 'role': 'user'}
}
rental_data = []
is_running = True

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input('\nTekan enter untuk lanjut...')

def login():
    clear_screen()
    print('=== LOGIN RENTAL PS ===')
    username = input('Username: ')
    password = input('Password: ')
    if username in users and users[username]['password'] == password:
        print('Login berhasil!')
        pause()
        return username
    print('Username atau password salah!')
    pause()
    return None

def register_user():
    clear_screen()
    print('=== DAFTAR AKUN BARU ===')
    username = input('Masukkan username baru: ')
    password = input('Masukkan password baru: ')
    if username in users:
        print('Username sudah digunakan!')
    else:
        users[username] = {'password': password, 'role': 'user'}
        print('Pendaftaran berhasil! Silakan login.')
    pause()

def tambah_data(petugas, role ='user'):
    clear_screen()
    print('=== TAMBAH DATA PENYEWAAN ===')
    try:
        nama = input('Nama penyewa: ')
        jenis_ps = input('Jenis PS: ')
        durasi = input('Durasi sewa (jam): ')

        if role == 'user':
            harga = 10000
            print(f'Harga sudah tercantum: Rp {harga}/jam')
        else:
            harga = input('Harga per jam: ')
            if not harga.isdigit():
                raise ValueError('Harga harus berupa digit atau angka!')
            harga = int(harga)

        if not durasi.isdigit():
            raise ValueError('Durasi harus berupa angka atau digit!')

        total = int(durasi) * int(harga)
           
        rental_data.append({
            'nama': nama,
            'ps': jenis_ps,
            'durasi': durasi,
            'harga': harga,
            'total': total,
            'petugas': petugas
        })
        print('Data berhasil ditambahkan!')
    except Exception as e:
        print('Terjadi kesalahan:', e)
    finally:
        pause()

def ubah_data(index):
    clear_screen()
    print('=== UBAH DATA PENYEWAAN ===')
    try:
        if 1 <= index <= len(rental_data):
            durasi = input('Durasi baru (jam): ')
            harga = input('Harga baru: ')
            if durasi.isdigit() and harga.isdigit():
                total = int(durasi) * int(harga)
                rental_data[index - 1]['durasi'] = durasi
                rental_data[index - 1]['harga'] = harga
                rental_data[index - 1]['total'] = total
                print('Data berhasil diubah!')
            else:
                print('Durasi dan harga harus angka!')
        else:
            print('Nomor data tidak valid!')
    except Exception as e:
        print('Terjadi kesalahan:', e)
    pause()

def lihat_data():
    clear_screen()
    print('=== DATA PENYEWAAN ===')
    if not rental_data:
        print('Belum ada data penyewaan.')
    else:
        for i, data in enumerate(rental_data, 1):
            print(f"{i}. {data['nama']} | {data['ps']} | {data['durasi']} jam | "
                  f"Rp{data['harga']}/jam | Total: Rp{data['total']} | Petugas: {data['petugas']}")
    pause()

def hapus_data():
    clear_screen()
    print('=== HAPUS DATA PENYEWAAN ===')
    for i, data in enumerate(rental_data, 1):
        print(f"{i}. {data['nama']}")
    try:
        hapus = int(input('Masukkan nomor data yang ingin dihapus: '))
        if 1 <= hapus <= len(rental_data):
            del rental_data[hapus - 1]
            print('Data berhasil dihapus!')
        else:
            print('Nomor data tidak valid!')
    except ValueError:
        print('Masukkan angka yang benar!')
    except Exception as e:
        print('Terjadi kesalahan:', e)
    pause()

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
            tambah_data(username)
        elif pilihan == '2':
            lihat_data()
        elif pilihan == '3':
            lihat_data()
            try:
                index = int(input('Pilih nomor data yang ingin diubah: '))
                ubah_data(index)
            except ValueError:
                print('Masukkan angka yang benar!')
                pause()
        elif pilihan == '4':
            hapus_data()
        elif pilihan == '5':
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
