n=int(input())
first=1
plus=6
room=1
if n==1:
    print(1)
else:
    while True:
        first=first+plus
        room+=1
        if n<=first:
            print(room)
            break
        else:
            plus+=6