#ip is 192.168.35.205

s=""

with open("./hoge.txt","r", encoding="utf-8") as file:
    for sline in file:
        s+=sline.strip()

with open("./hoge2.txt","w", encoding="utf-8") as file:
    file.write(s)
        
