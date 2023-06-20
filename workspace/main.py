import socket


def main():
    """
    ini hanyalah contoh untuk mendengarkan koneksi dari redis client
    selebihnya silahkan kerjakan sendiri
    bisa menggunakan bahasa pemograman lain
    tidak ada pembatasan menggunakan stack teknologi yang lain
    ini hanyalah contoh
    namun tcp harus me listen pada port 6379 dan host 127.0.0.1
    """
    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 6379  # Port to listen on (non-privileged ports are > 1023)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                print(data)
                if not data:
                    break
                conn.sendall(data)


if __name__ == '__main__':
    main()
