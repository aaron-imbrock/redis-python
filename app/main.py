import socket

HOST = "localhost"
PORT = 6379


def main():
    print("Logs from your program will appear here!")

    pong = "+PONG\r\n"

    server_socket = socket.create_server((HOST, PORT), reuse_port=True)
    conn, addr = server_socket.accept()

    with conn:
        conn.recv(1024)
        conn.send(pong.encode())

if __name__ == "__main__":
    main()
