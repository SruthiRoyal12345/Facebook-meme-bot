import fbchat
from fbchat import  Client, log
from fbchat.models import *
import fileinput

class punkjj(Client):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        friends=["100011047361109","100009222423465","100012745653392"] #add your friends uid here
        #if you dont have yours friends uid then try to find it from the facebook website or the find_uid.py program
        if author_id != self.uid and author_id not in friends:
            sent=client.sendLocalImage("./images.jpg",message=Message(text="This is a local image"),thread_id=author_id,thread_type=ThreadType.USER,)

client = punkjj("username", "password")
client.listen()
