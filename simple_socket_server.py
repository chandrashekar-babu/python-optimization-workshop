from socket import socket, AF_INET, SOCK_STREAM

def create_server(host, port, handler):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(100)

    print(f"Server listening on {host}:{port}")

    while True:
        client, addrinfo = sock.accept()
        print(f"Received connection from {addrinfo}")
        handler(client, addrinfo)
        client.close()

def echo_handler(client, addrinfo):
    ins = client.makefile("r")
    outs = client.makefile("w")

    for line in ins:
        if "exit" in line:
            print(f"Client {addrinfo} is exiting...")
            break
        print(line.strip().upper(), file=outs, flush=True)

    print("BYE", file=outs, flush=True)

    ins.close()
    outs.close()

if __name__ == '__main__':

    create_server("127.0.0.1", 6789, echo_handler)


