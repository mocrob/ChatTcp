import socket
from tkinter import *

tk=Tk()

s = socket.socket()
host =socket.gethostbyname(socket.gethostname())
print(host)
#host = "0.0.0.0"
port = 11719
s.bind((host, port))

s.listen(5)
c = None

#интерфейс
text=StringVar()
name=StringVar()
name.set('HabrUser')
text.set('')
tk.title('MegaChat')
tk.geometry('400x300')

log = Text(tk)
nick = Entry(tk, textvariable=name)
msg = Entry(tk, textvariable=text)
msg.pack(side='bottom', fill='x', expand='true')
nick.pack(side='bottom', fill='x', expand='true')
log.pack(side='top', fill='both',expand='true')

#while True:
    #Wait for a connection
    #print (sys.stderr, 'waiting for a connection')
    #connection, client_address = s.accept()


def loopproc():
    log.see(END)
    s.setblocking(False)
    try:
        while True:
            if c is None:
                # Halts
                print('[Waiting for connection...]')
                c, addr = s.accept()
                print('Got connection from', addr)
            else:
                # Halts
                print
                '[Waiting for response...]'
                print
                message =c.recv(1024)
                log.insert(END, message.decode("utf-8") + '\n')
                #q = raw_input("Enter something to this client: ")
                #c.send(q)
    except:
        tk.after(1, loopproc)
        return
    tk.after(1, loopproc)
    return

def sendproc(event):
    i=0
    addr=[("127.0.0.2", 11719),("192.168.56.1",11719),("127.0.0.1",11719)]
    addrL = len(addr)
    for i in  range (addrL):
       try:
            s = socket.socket()
            s.settimeout(2)
            s.connect(addr[i])
            s.settimeout(None)
            sData = name.get()+':'+text.get()
            s.send(sData.encode("utf-8"))#тут меняем ip-шники
            log.insert(END, sData + '\n')
            text.set('')
            s.close()
            break
       except:
           print("error %s - is not available" % i)



msg.bind('<Return>',sendproc)

msg.focus_set()

tk.after(1,loopproc)
tk.mainloop()