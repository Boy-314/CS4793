import socket;
import sys;

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
sock.bind(('',8080));
sock.listen();
counter = 0;
while True:
    (conn,(ip,port)) = sock.accept();
    request = conn.recv(1024).decode('utf-8');
    string_list = request.split(' ');
    if string_list[0] == 'GET' and string_list[1] == '/':
        counter = counter + 1;
        page1 = '<HTML><HEAD><TITLE>HTTP Homework</TITLE></HEAD><BODY><H3><CENTER>HTTP Homework</CENTER></H3>This is the main page<P>You can click on <A HREF="/page2">page 2</A> or <A HREF="/page3">or Page 3</A><P><CENTER>This server has been used ' + str(counter) + ' times</CENTER></BODY></HTML>';
        conn.sendall(b'HTTP/1.0 200 OK');
        conn.sendall(b'Server: wy667');
        contentLength1 = 'Content-Length: ' + str(sys.getsizeof(page1));
        conn.sendall(contentLength1.encode('utf-8'));
        conn.sendall(b'Content-Type: text/html');
        conn.sendall(b'Connection: Closed\r\n\r\n');
        conn.sendall(page1.encode('utf-8'));
    elif string_list[0] == 'GET' and string_list[1] == '/page2':
        counter = counter + 1;
        page2 = '<HTML><HEAD><TITLE>HTTP Homework</TITLE></HEAD><BODY><H3><CENTER>HTTP Homework</CENTER></H3>This is page 2<P>You can go <A HREF="/">back</A><P><CENTER>This server has been used ' + str(counter) + ' times</CENTER></BODY></HTML>';
        conn.sendall(b'HTTP/1.0 200 OK');
        conn.sendall(b'Server: wy667');
        contentLength2 = 'Content-Length: ' + str(sys.getsizeof(page2));
        conn.sendall(contentLength2.encode('utf-8'));
        conn.sendall(b'Content-Type: text/html');
        conn.sendall(b'Connection: Closed\r\n\r\n');
        conn.sendall(page2.encode('utf-8'));
    elif string_list[0] == 'GET' and string_list[1] == '/page3':
        counter = counter + 1;
        page3 = '<HTML><HEAD><TITLE>HTTP Homework</TITLE></HEAD><BODY><H3><CENTER>HTTP Homework</CENTER></H3>This is page 3<P>You can go <A HREF="/">back</A> <P><CENTER>This server has been used ' + str(counter) + ' times</CENTER></BODY></HTML>';
        conn.sendall(b'HTTP/1.0 200 OK');
        conn.sendall(b'Server: wy667');
        contentLength3 = 'Content-Length: ' + str(sys.getsizeof(page3));
        conn.sendall(contentLength3.encode('utf-8'));
        conn.sendall(b'Content-Type: text/html');
        conn.sendall(b'Connection: Closed\r\n\r\n');
        conn.sendall(page3.encode('utf-8'));
    elif string_list[0] == 'GET':
        counter = counter + 1;
        errorNotFound = '404 Error: Request for ' + string_list[1] + ' not found';
        conn.sendall(b'HTTP/1.0404 Not Found');
        conn.sendall(b'Server: wy667');
        contentLength404 = 'Content-Length: ' + str(sys.getsizeof(errorNotFound));
        conn.sendall(b'Content-Type: text/plain');
        conn.sendall(b'Connection: Closed\r\n\r\n');
        conn.sendall(errorNotFound.encode('utf-8'));
    else:
        counter = counter + 1;
        conn.sendall(b'HTTY/1.0 400 OK');
        conn.sendall(b'Server: wy667');
        conn.sendall(b'Content-Length: 0');
        conn.sendall(b'Content-Type: text/html');
        conn.sendall(b'Connection: Closed\r\n\r\n');
    conn.close();
