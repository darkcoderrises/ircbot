import socket,sys

server="irc.freenode.net"
channel="#osdg-iiith"
botnick="iiithbot"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server,6667))
irc.send("USER "+botnick+" "+botnick+" "+botnick+" :TestBot\n")
irc.send("NICK "+botnick+"\n")
irc.send("PRIVMSG nickserv :iNOOPE\r\n") #I don't know what this line does....
irc.send("JOIN "+channel+"\n")

logfile = open("log.txt","a+",0)

ONLINE=[]
NOTNEWCHECK=[]

def sendmsg(msg):
    irc.send("PRIVMSG "+ channel +" :"+ msg +"\n") 

def new(user):
    NOTNEWCHECK.append(user)
    sendmsg("hello "+user+",Here are some links that may be useful to you")

while 1:
        text=irc.recv(2040)
        print text
        logfile.write(text)
        if text.find("PING")!=-1:
            irc.send("PONG "+text.split(" ")[1]+"\r\n")

        if text:
            if "JOIN" in text:
                ONLINE.append(text.split("!")[0][1:])
            
            if "QUIT" in text:
                if text.split("!")[0][1:] in ONLINE:
                    ONLINE.remove(text.split("!")[0][1:])

            if "PRIVMSG" in text:
                pinger=text.split("!")[0][1:]
                msg=text.split(":")[-1]
                

                if "i am new" in msg.lower() and pinger not in NOTNEWCHECK:
                    new(pinger)

                

        
