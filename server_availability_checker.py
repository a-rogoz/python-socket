import socket
import sys

if len(sys.argv) not in [2, 3]:
    print("Improper number of arguments: at least one is required and not more than two are allowed:")
    exit(code=1)

port = 80

if len(sys.argv) == 3:
    try:
        user_port = int(sys.argv[2])
    except Exception as e:
        print("Incorrect port number")
        exit(code=2)

    if user_port >= 1 and user_port <= 65535:
        port = user_port
    else:
        print("Incorrect port number")
        exit(code=2)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((sys.argv[1], port))
except TimeoutError as e:
    print(e)
    exit(3)
except Exception as e:
    print(e)
    exit(4)

sock.send(b"HEAD / HTTP/1.1\r\nHost: " +
          bytes(sys.argv[1], "utf-8") +
          b"\r\nConnection: close\r\n\r\n")

res = sock.recv(10000)

sock.shutdown(socket.SHUT_RDWR)
sock.close()

print(repr(res))