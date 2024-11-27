import fbchat
from fbchat import Client
from getpass import getpass

client=Client("9639463969","x214Bha8")

num=int(input("enter the num of friends"))

for i in range(num):
    name=str(input("name:"))
    friends=client.searchForUsers(name)
    friend=friends[0]
    print(friend.uid)

    if sent:
        print("msg send")
