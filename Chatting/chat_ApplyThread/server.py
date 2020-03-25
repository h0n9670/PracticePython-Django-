import socket
import _thread
print('기다리는중...')
HOST = ''
PORT = 8089
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1) 
conn, addr = s.accept()

print(addr,'님이 입장하셨습니다.')

def returningMsg(): 
    while True: 
        recvData,user = conn.recv(1023)  
        conn.sendto(recvData,user) 
    conn.close() 

t1=_thread.start_new_thread(returningMsg,()) #on
t1

while True: 
    pass
