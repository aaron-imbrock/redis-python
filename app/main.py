import socket

HOST = "localhost"
PORT = 6379


def main():
    print("Logs from your program will appear here!")

    server_socket = socket.create_server((HOST, PORT), reuse_port=True)
    conn, addr = server_socket.accept()

    with conn:
        conn.recv(1024)
        conn.send("+PONG", end="\r\n".encode())

if __name__ == "__main__":
    main()
