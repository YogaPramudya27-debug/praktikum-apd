import os

users = { 
    'admin': {'password': 'admin123', 'role': 'admin'}, 
    'user': {'password': 'user123', 'role': 'user'}
}
rental_data = {}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('=== SISTEM PEMINJAMAN PS ANANTA ===')
    print('1. Login')
    print('2. Register')
    print('3. Keluar')

    menu_awal = input('Pilih Menu: ')

    if menu_awal == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('=== LOGIN RENTAL PS ===')
        username = input('Username: ')
        password = input('Password: ')

        if username in users and users[username]['password'] == password:
            print('Berhasil Login!')
            input('Tekan enter buat lanjut...')
            role = users[username]['role']

            if role == 'admin':
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('=== MENU ADMIN ===')
                    print('1. Tambah Sewa')
                    print('2. Lihat Sewa')
                    print('3. Ubah Sewa')
                    print('4. Hapus Sewa')
                    print('5. Logout')

                    pilih = input('Pilih Menu: ')

                    if pilih == '1':
                        nama = input('Nama Penyewa: ')
                        ps = input('Jenis PS: ')
                        durasi = input('Durasi penyewaan (jam): ')
                        harga = input('Harga per jam: ')

                        if durasi.isdigit() and harga.isdigit():
                            total = int(durasi) * int(harga)
                            rental_data.append({
                                'nama': nama,
                                'ps': ps,
                                'durasi': durasi,
                                'harga': harga,
                                'total': total,
                                'petugas': username
                            })
                            print('Data berhasil ditambah!')
                        else:
                            print('Durasi & Harga harus angka!')
                        input('Tekan enter buat lanjut...')

                    elif pilih == '2':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('=== DATA PENYEWA ===')
                        if not rental_data:
                            print('Belum ada data penyewa.')
                        else:
                            for i, data in enumerate(rental_data, start=1):
                                print(f"{i}. {data['nama']} | {data['ps']} | {data['durasi']} jam | Rp{data['harga']}/jam | Total: Rp{data['total']} | petugas: {data['petugas']}")
                        input('Tekan enter buat lanjut...')

                    elif pilih == '3':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('=== UBAH DATA ===')
                        for i, data in enumerate(rental_data, start=1):
                            print(f"{i}. {data['nama']} - {data['ps']} - {data['durasi']} jam, Rp{data['harga']}/jam") 

                        ubah = input('Pilih data penyewa yang mau diubah: ')

                        if ubah.isdigit():
                            ubah = int(ubah)
                            if 1 <= ubah <= len(rental_data):
                                durasi = input('Durasi Baru (jam): ')
                                harga = input('Harga Baru: ')
                                if durasi.isdigit() and harga.isdigit():
                                    total = int(durasi) * int(harga)
                                    rental_data[ubah-1]['durasi'] = durasi
                                    rental_data[ubah-1]['harga'] = harga
                                    rental_data[ubah-1]['total'] = total
                                    print('Data berhasil diubah!')
                                else:
                                    print('Durasi & Harga harus angka!')
                            else:
                                print('Nomor data nggak valid!')
                        else:
                            print('Masukin angka dongg!')
                        input('Tekan enter buat lanjut...')

                    elif pilih == '4':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('=== HAPUS DATA ===')
                        for i, data in enumerate(rental_data, start=1):
                            print(f"{i}. {data['nama']}")
                        hapus = input('Masukin nomor data penyewa yang mau dihapus: ')
                        if hapus.isdigit():
                            hapus = int(hapus)
                            if 1 <= hapus <= len(rental_data):
                                del rental_data[hapus-1]
                                print('Data berhasil dihapus!')
                            else:
                                print('Nomor data nggak valid!')
                        else:
                            print('Masukin angka dongg!')
                        input('Tekan enter buat lanjut...')

                    elif pilih == '5':
                        break

                    else:
                        print('Pilihan menu nggak ada...')
                        input('Tekan enter buat lanjut...')
        else:
            print('Username atau password salah, bro!')
            input('Tekan enter buat balik...')
    elif menu_awal == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('=== REGISTER ===')
        username = input('Username baru: ')
        password = input('Password baru: ')
        if username in users:
            print('Username udah dipake, buat yang lain!')
        else:
            users[username] = {'password': password, 'role': 'user'}
            print('Berhasil daftar! Silahkan login.')
        input('Tekan enter buat lanjut...')
    elif menu_awal == '3':
        print('Keluar... bye!')
        break
    else:
        print('Menu nggak ada nih, bro.')
        input('Tekan enter buat lanjut...')

        

        
                    
    



                     