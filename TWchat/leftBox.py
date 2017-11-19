# -*- coding: UTF-8
import urwid
class ChatListBox(urwid.ListBox):
    def __init__(self,userName,contact_click_fn,chat_click_fn,contactList,is_contact_list=False):
        self.contactList=contactList 
        self.chatList={}
        self.chat_name_dic={}
        self.owner=userName
        self.contact_click_fn = contact_click_fn
        self.chat_click_fn = chat_click_fn
        self.is_contact_list=is_contact_list
        self.body = urwid.SimpleFocusListWalker([])
        if self.is_contact_list:
            self.show_contact()
        else:
            self.show_chat()
        super(ChatListBox,self).__init__(self.body)
    def show_chat(self):
        del self.body[:]
        self.is_contact_list=False
        for key in self.chat_name_dic:
            self.insert_new_line(key,self.chat_name_dic[key],False)
    def show_contact(self):
        del self.body[:]
        self.is_contact_list=True
        for contact in self.contactList:
            self.addcontacts(contact,self.contact_click_fn)
    def addNewChat(self,chat_id,chat_name,unread=False):
        self.chat_name_dic[chat_id]=chat_name
        if not chat_id in self.chatList:
            self.chatList[chat_id]=[]
            self.insert_new_line(chat_id,chat_name,unread)
    def add_chat_by_msg(self,chat_id,chat_name,msg,unread=False):
        self.chat_name_dic[chat_id]=chat_name
        if chat_id in self.chatList :
            self.chatList[chat_id].append(msg)
            return
        else:
            self.chatList[chat_id]=[msg]
            self.insert_new_line(chat_id,chat_name,unread)
    def insert_new_line(self,chat_id,chat_name,unread):
        if self.is_contact_list:
            return
        button = urwid.Button(chat_name)
        urwid.connect_signal(button,'click',self.chat_click_fn,[chat_id,chat_name])
        text=""
        if unread:
            text=u'◆'
        else:
            text=""
        unread_sig = urwid.Text(text)
        line = urwid.Columns([('weight',1,unread_sig),('weight',8,button)])
        self.body.append(urwid.LineBox(line))
    def get_chat_message(self,chat_id):
        if chat_id in self.chatList:
            return self.chatList[chat_id]
        else:
            return []

    def addcontacts(self,contact,clickFun):
        name = ''
        if contact['UserName']==self.owner:
            return
        if not contact['RemarkName']:
            name = contact['NickName']
        else:
            name = contact['RemarkName']
        newline = urwid.Button(name)
        nickname = contact['RemarkName'] if contact['RemarkName'] else contact['NickName']
        urwid.connect_signal(newline,'click',clickFun,[contact['UserName'],nickname])
        self.body.append(urwid.LineBox(newline))
