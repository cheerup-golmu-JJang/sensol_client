# 댐 관리 프로젝트(?)의 클라이언트용 


import socket
import os
from dotenv import load_dotenv
import time
import datetime

#변화 없는 값들 STX=시작
STX=b'\x02' # Start of Text
ETX=b'\x03'# End of Text


load_dotenv() #환경변수 불러오기(호스트 주소를 불러오기 위함... 호스트주소IP:효택's LG노트북)


host=os.environ.get('host')
port=int(os.environ.get('port'))

# 현재 사용중인 PC(여기선 라즈베리파이)의 IP가져오기
ip=[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
ip=[i for i in (ip.split('.'))]


# Dam id 구하기 리턴 값: 댐 번호
def get_id():
    '''
    Return: Dam ID & returntype = int
    '''
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(STX+chr(10).encode()+b'\x03')
        recv=sock.recv(1024)
        print("id====",int(recv[2]),int(recv[3]))
        sock.close()
        return recv[2]*100+recv[3]


def send_data(Type,id,Data):
    
    """
    Type: 1의 자리: 데이터 종류 
    1:수위 2:조도 3:들어오는 스위치 4:나가는 스위치
    """

    if(type(Data)!=int):return

    #측정 시간
    now=datetime.datetime.now()
    year=str(now.year).rjust(4,'0')
    month=str(now.month).rjust(2,'0')
    day=str(now.day).rjust(2,'0')
    hour=str(now.hour).rjust(2,'0')
    minute=str(now.minute).rjust(2,'0')
    second=str(now.second).rjust(2,'0')
    
    #서버와 소켓통신
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.connect((host, port))


        message=STX+chr(Type).encode()+chr(int(id/100)).encode()+chr(id%100).encode()
        print(chr(Type).encode())
        length=None
        ipEncode= None
        for i in ip:
            if length==None:
                length=str(len(str(i))).encode()
                ipEncode=str(i).encode()
            else :    
                length= length+str(len(str(i))).encode()
                ipEncode= ipEncode+str(i).encode()
        timemessage=year.encode()+month.encode()+day.encode()+hour.encode()+minute.encode()+second.encode()
        datamessage=str(len(str(Data))).encode()+str(Data).encode()
        print(year.encode())
        message=message=message+timemessage+datamessage+ETX+'\n'.encode()   


        print("보낸 메시지"+message.decode())


        #메시지를 서버에 보냄.
        sock.sendall(message)
            
        #아직 리시브 메시지를 구현안함... 구현하면 주석제거    
        # recive=sock.recv(1024)
                

        # print(recive.decode(),"recive")
        
        sock.close()
if __name__ == "__main__":
    id=get_id()
    send_data(1,id,123)
