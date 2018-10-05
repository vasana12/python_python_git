#-*-coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
hostPort = 8999

class MyServer(BaseHTTPRequestHandler):
#기본 GET 방식을 구현 했을때 리턴하는 값을 지정하는 핸들러를 BaseHTTPRequestHandler로 상속받는다.
    def do_GET(self):
        self.send_response(200) #-> 접속이 OK 값을 리턴하고
            #html 로 응답 마인을 지정한다.
        self.send_header("Content-type","text/html")
        self.end_headers()
        #창 제목을 html 로 지정하고
        self.wfile.write(bytes("<html><head><title>Test.</title></head>","utf-8"))
        #body 부분의 코드를 지정한다
        self.wfile.write(bytes("<body><p>Hello Python!</p>", "utf-8"))
        #디렉토리를 출력하는데 url 패스가 출력된다
        self.wfile.write(bytes("<p>U accessed kjy.path: %s</p>"% self.path, "utf-8"))
        self.wfile.write(bytes("</body></html>","utf-8"))

#HTTPServer 클래스를 통해 서버를 실행하고 접속이 되면 MyServer로 액세스 하도록 지정한다.
myServer = HTTPServer((hostName, hostPort), MyServer) #MyServer 핸들러 지정
#콘솔에 호스트 이름과 포트명을 출력해본다.
print("Server Starts- %s:%s"%(hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

