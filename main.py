import socket


server_addr = input("Enter the server IP address: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_addr, 80))

sock.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")

reply = sock.recv(10000)
sock.shutdown(socket.SHUT_RDWR)

# socket.SHUT_RD - we aren't going to read the server's messages anymore (we declare ourselves deaf)
# socket.SHUT_WR - we won't say a word (actually, we'll be dumb)
# socket.SHUT_RDWR - specifies the conjunction of the two previous options.

sock.close()

print(repr(reply))

# requests Exceptions
# RequestException
# |___HTTPError
# |___ConnectionError
# |   |___ProxyError	
# |   |___SSLError	
# |___Timeout
# |   |___ConnectTimeout
# |   |___ReadTimeout
# |___URLRequired
# |___TooManyRedirects
# |___MissingSchema
# |___InvalidSchema
# |___InvalidURL
# |   |___InvalidProxyURL
# |___InvalidHeader
# |___ChunkedEncodingError
# |___ContentDecodingError
# |___StreamConsumedError
# |___RetryError
# |___UnrewindableBodyError