import socket


print('''

8888888b.   .d88888b.  8888888b. 88888888888                                    
888   Y88b d88P" "Y88b 888   Y88b    888                                        
888    888 888     888 888    888    888                                        
888   d88P 888     888 888   d88P    888                                        
8888888P"  888     888 8888888P"     888                                        
888        888     888 888 T88b      888                                        
888        Y88b. .d88P 888  T88b     888                                        
888         "Y88888P"  888   T88b    888                                        
                                                                                
                                                                                
                                                                                
 .d8888b.   .d8888b.        d8888 888b    888 888b    888 8888888888 8888888b.  
d88P  Y88b d88P  Y88b      d88888 8888b   888 8888b   888 888        888   Y88b 
Y88b.      888    888     d88P888 88888b  888 88888b  888 888        888    888 
 "Y888b.   888           d88P 888 888Y88b 888 888Y88b 888 8888888    888   d88P 
    "Y88b. 888          d88P  888 888 Y88b888 888 Y88b888 888        8888888P"  
      "888 888    888  d88P   888 888  Y88888 888  Y88888 888        888 T88b   
Y88b  d88P Y88b  d88P d8888888888 888   Y8888 888   Y8888 888        888  T88b  
 "Y8888P"   "Y8888P" d88P     888 888    Y888 888    Y888 8888888888 888   T88b 
                                                                                
                                                                                
                                                                                

      ''')

ip = ''

print("please enter the ip address")
ip = input()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3)
open_ports = []

for port in range(1,65535):
    location = (ip,port)
    try:
       print("trying port : ",port)
       res = s.connect_ex((ip,port))
       if(res==0):
           open_ports.append(port)

    except Exception as e:
        print(e)

print("port scan complete, closing socket")
s.close()
if(len(open_ports)>0):
    print("List of open ports:")
    for i in open_ports:
        print(i)
else:
    print("No open ports found")
