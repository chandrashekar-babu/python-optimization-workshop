from socket import socket, AF_INET, SOCK_STREAM
from concurrent.futures import ThreadPoolExecutor as Executor



def create_server(host, port, handler):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(100)

    print(f"Server listening on {host}:{port}")

    with Executor(max_workers=3) as workers:
        while True:
            client, addrinfo = sock.accept()
            print(f"Received connection from {addrinfo}")
            #handler(client, addrinfo)
            #Thread(target=handler, args=(client, addrinfo)).start()
            workers.submit(handler, args=(client, addrinfo))


def echo_handler(client, addrinfo):
    ins = client.makefile("r")
    outs = client.makefile("w")

    tname = current().name

    for line in ins:
        if "exit" in line:
            print(f"Client {addrinfo} is exiting...")
            break
        print(line.strip().upper(), file=outs, flush=True)
        print(f"Client: {addrinfo}, Thread: {tname}, Line: {line}")

    print("BYE", file=outs, flush=True)

    ins.close()
    outs.close()
    client.close()

if __name__ == '__main__':

    create_server("127.0.0.1", 6789, echo_handler)


