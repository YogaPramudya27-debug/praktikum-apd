from utils import clear_screen, pause

users = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'user': {'password': 'user123', 'role': 'user'}
}

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