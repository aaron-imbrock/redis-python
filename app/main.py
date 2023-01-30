# Uncomment this to pass the first stage
import socket

HOST = "localhost"
PORT = 6379


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server((HOST, PORT), reuse_port=True)
    server_socket.accept() # wait for client


if __name__ == "__main__":
    main()
