import socket 
import _thread 
HOST = "localhost" 
PORT = 8089 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT)) 

print('접속 완료')

def sendingMsg(): 
    while True: 
        sendData = input()
        # sendData = str(sendData).split('>>>')[0] 
        sendData = sendData.encode("utf-8")
        s.send(sendData) 
    s.close() 
    
def gettingMsg(): 
    while True: 
        recvData = s.recv(1024)  
        print(recvData.decode('utf-8'))
    s.close() 

t3=_thread.start_new_thread(sendingMsg,()) 
t4=_thread.start_new_thread(gettingMsg,()) #on
t3
t4

while True: 
    pass