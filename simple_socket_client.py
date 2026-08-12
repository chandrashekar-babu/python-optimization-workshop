from socket import socket, AF_INET, SOCK_STREAM

def create_client(host, port, handler):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    handler(sock, (host, port))
    sock.close()

def echo_client_handler(sock, addrinfo):
    print(f"Connected to {addrinfo}")
    ins = sock.makefile("r")
    outs = sock.makefile("w")

    while True:
        line = input("Enter string: ")
        print(line, file=outs, flush=True)

        response = ins.readline().strip()
        print("Server reponded with:", response)
        if "BYE" in response:
            break
    ins.close()
    outs.close()

if __name__ == '__main__':
    create_client("127.0.0.1", 6789, echo_client_handler)

       
