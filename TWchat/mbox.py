# -*- coding: UTF-8
import urwid
import mtxt
import os
class MessageListBox(urwid.ListBox):
    def __init__(self,userName="",msgList=[]):
        self.pos=0
        self.owner =userName
        self.msgList=msgList
        self.currentChat=''
        self.body = urwid.SimpleFocusListWalker([])
        super(MessageListBox,self).__init__(self.body)
    def bindList(self,msgList):
        self.msgList=msgList
        self.refresh()
    def refresh(self):
        del self.body[:]
        for msg in self.msgList:
            self.add_message(msg,False)
    def clear(self):
        del self.body[:]
        del self.msgList[:]
    def add_message(self,msg,addtoList=True):
        if addtoList:
            self.msgList.append(msg)
        box = self.create_text_line(msg)
        self.body.append(box)
        self.focus_position=len(self.body)-1
    def create_text_line(self,msg):
        alig = 'right' if msg['FromUserName']==self.owner else 'left'
        bg= 'mybg' if msg['FromUserName']==self.owner else 'tobg'
        try:
            groupMsgPrefix = msg['ActualNickName'] + ": "
        except:
            groupMsgPrefix = ""
        if not hasattr(msg,'type'):
            newline = urwid.Text(msg['Text'])
            newline.set_align_mode(alig)
            box=urwid.AttrMap(urwid.LineBox(newline),bg)
            return box
        if msg.type is 'Text':
            newline = urwid.Text(groupMsgPrefix + msg['Text'])
        elif msg.type is 'Recording':
            name = self.download(msg)
            newline = mtxt.RecodingText(name)
        elif msg.type is 'Picture':
            name = self.download(msg)
            newline = mtxt.ImageText(name)
        else:
            txt = str(msg.type)+" is not supported yet please check this on your phone"
            newline = urwid.Text(txt)
        newline.set_align_mode(alig)
        box=urwid.AttrMap(urwid.LineBox(newline),bg)
        return box
    def download(self,msg):
        path =os.environ['HOME']+'/.twchat/'+msg.type+'/'
        if os.path.isdir(path):
            pass
        else:
            os.mkdir(path)
        msg.download(path+msg.fileName)
        return path+msg.fileName

