import socket
import _thread
print('기다리는중...')
HOST = ''
PORT = 8089
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1) 
conn, addr = s.accept()

print('Connected by', addr)

def sendingMsg(): 
    while True: 
        sendData = input()
        # sendData = str(sendData).split('>>>')[0] 
        sendData = sendData.encode("utf-8") 
        conn.send(sendData) 
    conn.close() 

def gettingMsg(): 
    while True: 
        recvData = conn.recv(1023)  
        print(recvData.decode('utf-8')) 
    conn.close() 

t1=_thread.start_new_thread(sendingMsg,()) #on
t2=_thread.start_new_thread(gettingMsg,()) 
t1
t2

while True: 
    pass
