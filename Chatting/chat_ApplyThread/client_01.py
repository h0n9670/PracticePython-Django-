import socket 
import _thread 
HOST = "localhost" 
PORT = 8089 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT)) 

print('접속 완료 했습니다.')
user = input()

def sendingMsg(): 
    global user
    while True: 
        sendData = input() 
        sendData = sendData.encode("utf-8")
        s.sendto(sendData,user) 
    s.close() 
    
def gettingMsg():
    while True: 
        recvData,user = s.recv(1024)
        recvData = recvData.decode('utf-8')
        print(recvData.decode('utf-8'))
    s.close() 

t3=_thread.start_new_thread(sendingMsg,()) 
t4=_thread.start_new_thread(gettingMsg,()) #on
t3
t4

while True: 
    pass