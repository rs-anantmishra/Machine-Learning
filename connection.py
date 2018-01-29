import socket,ssl

# SSL Context
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ipaddr = socket.gethostbyname('imap.gmail.com')
print(ipaddr);

# Connect the socket to the port where the server is listening
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = context.wrap_socket(sock, server_hostname='imap.gmail.com')
ssl_sock.connect(('imap.gmail.com', 993))


#server_address = (ipaddr, 993)
#ssl.wrap_socket(sock)
#sock.connect(server_address)

try:

    # Send data
    message = 'tag login loginID password'
    ssl_sock.send(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = 10

    while amount_received < 10:
        data = ssl_sock.recv(16)
        amount_received += len(data)
        amount_received += 1
        print(data)

finally:
    sock.close()