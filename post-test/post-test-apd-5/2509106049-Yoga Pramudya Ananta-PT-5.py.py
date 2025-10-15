import os

users = [['Yoga', '900', 'admin'], ['pelanggan', '123', 'user']]
rental_data = []  

while True:
    print('=== SISTEM PEMINJAMAN PS ANANTA ===')
    print('1. Login')
    print('2. Register')
    print('3. Keluar')

    menu_awal = input('Pilih Menu: ')

    if menu_awal == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('=== LOGIN RENTAL PS ===')
        user = input('Username: ')
        pw = input('Password: ')

        login_berhasil = False
        role = 'user'

        for u in users:
            if u[0] == user and u[1] == pw:
                login_berhasil = True
                role = u[2]
                break

        if login_berhasil:
            print('Berhasil Login!')
            input('Tekan enter untuk lanjut...')

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
                            rental_data.append([nama, ps, durasi, harga, total, user])
                            print('Data berhasil ditambah!')
                        else:
                            print('Durasi & Harga harus angka!')
                        input('Tekan enter untuk lanjut...')

                    elif pilih == '2':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('=== DATA PENYEWA ===')
                        if len(rental_data) == 0:
                            print('Belum ada data penyewa.')
                        else:
                            for i in range(len(rental_data)):
                                data = rental_data[i]
                                print(f"{i+1}. {data[0]} | {data[1]} | {data[2]} jam | Rp{data[3]}/jam | Total: Rp{data[4]} | Petugas: {data[5]}")
                        input('Tekan enter untuk lanjut...')

                    elif pilih == '3':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('=== UBAH DATA ===')
                        for i in range(len(rental_data)):
                            data = rental_data[i]
                            print(f"{i+1}. {data[0]} - {data[1]} ({data[2]} jam, Rp{data[3]}/jam)")

                        ubah = input('Masukkan nomor data yang ingin diubah: ')

                        if ubah.isdigit():
                            ubah = int(ubah)
                            if 1 <= ubah <= len(rental_data):
                                durasi = input('Durasi Baru: ')
                                harga = input('Harga Baru: ')

                                if durasi.isdigit() and harga.isdigit():
                                    total = int(durasi) * int(harga)
                                    rental_data[ubah-1][2] = durasi
                                    rental_data[ubah-1][3] = harga
                                    rental_data[ubah-1][4] = total
                                    print('Data berhasil diubah!')
                                else:
                                    print('Durasi & Harga harus angka!')
                            else:
                                print('Nomor data tidak valid!')
                        else:
                            print('Masukkan angka!')
                        input('Tekan enter untuk lanjut...')

                    elif pilih == '4':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('=== HAPUS DATA ===')
                        for i in range(len(rental_data)):
                            print(f"{i+1}. {rental_data[i][0]}")

                        hapus = input('Masukkan nomor data yang ingin dihapus: ')
                        if hapus.isdigit():
                            hapus = int(hapus)
                            if 1 <= hapus <= len(rental_data):
                                del rental_data[hapus-1]
                                print('Data berhasil dihapus!')
                            else:
                                print('Nomor data tidak ditemukan!')
                        else:
                            print('Masukkan angka!')
                        input('Tekan enter untuk lanjut...')

                    elif pilih == '5':
                        print('Logout berhasil!\n')
                        break
                    else:
                        print('Pilihan tidak valid!')
                        input('Tekan enter untuk lanjut...')

            elif role == 'user':
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'=== MENU USER ({user}) ===')
                    print('1. Sewa PS')
                    print('2. Lihat Riwayat Sewa')
                    print('3. Logout')

                    pilih = input('Pilih Menu: ')

                    if pilih == '1':
                        ps = input('Jenis PS yang disewa: ')
                        durasi = input('Durasi penyewaan (jam): ')
                        harga = input('Harga per jam: ')

                        if durasi.isdigit() and harga.isdigit():
                            total = int(durasi) * int(harga)
                            rental_data.append([user, ps, durasi, harga, total, user])
                            print(f'Sewa berhasil! Total yang harus dibayar: Rp{total}')
                        else:
                            print('Durasi & Harga harus angka!')
                        input('Tekan enter untuk lanjut...')

                    elif pilih == '2':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'=== RIWAYAT SEWA {user.upper()} ===')
                        ditemukan = False
                        for data in rental_data:
                            if data[5] == user:
                                print(f"- {data[1]} | {data[2]} jam | Rp{data[3]}/jam | Total: Rp{data[4]}")
                                ditemukan = True
                        if not ditemukan:
                            print('Belum ada riwayat sewa.')
                        input('Tekan enter untuk lanjut...')

                    elif pilih == '3':
                        print('Logout berhasil!')
                        break

                    else:
                        print('Pilihan tidak valid!')
                        input('Tekan enter untuk lanjut...')

        else:
            print('Username atau password salah!')
            input('Tekan enter untuk kembali...')

    elif menu_awal == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('=== REGISTRASI ===')
        user_baru = input('Masukkan username baru: ')
        pw_baru = input('Masukkan password baru: ')
        users.append([user_baru, pw_baru, 'user'])
        print('Registrasi berhasil! Anda sekarang bisa login.')
        input('Tekan enter untuk lanjut...')

    elif menu_awal == '3':
        print('Terima kasih telah menggunakan program ini!')
        break

    else:
        print('Pilihan tidak valid!')
        input('Tekan enter untuk lanjut...')
        

        
                    
    



                     