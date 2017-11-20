# -*- coding: UTF-8
import urwid
from urwid import raw_display
import leftBox 
import mbox

screenCols, screenRows = raw_display.Screen().get_cols_rows()
class WechatMain(object):
    def __init__(self,palette):
        self.chatButton = urwid.Button("chat")
        self.contactButton = urwid.Button("contact")
        self.sendButton = urwid.Button("send")
        self.inputBox = urwid.Edit(multiline=True)
        self.current_chat_from="" 
        self.owner_id=""
        self.palette=palette
        self.loop=None
    def initUserInfo(self,owner_id,owner_name,on_contact_item_click,on_chat_item_click,contactlist=[],chatlist=[]):
        self.owner_id=owner_id
        self.owner_name = owner_name
        self.messageListBox = mbox.MessageListBox(self.owner_id)
        self.chatListBox = leftBox.ChatListBox(owner_id,on_contact_item_click,on_chat_item_click,contactlist,True)
    def bind_itchat(self,itchat):
        self.itchat=itchat
    def createLoop(self):
        placeholder = urwid.SolidFill()
        urwid.set_encoding("UTF-8")
        self.loop = urwid.MainLoop(placeholder,self.palette,unhandled_input=exit_on_alt_q)
        self.loop.screen.set_terminal_properties(colors=256)
        self.loop.widget = urwid.AttrMap(placeholder, 'bg')
        self.loop.widget.original_widget = urwid.Filler(self.createLayout())
        self.loop.run()
    def createLayout(self):
        left = self.createLeft()
        right = self.createRight()
        return urwid.Columns([('weight',2,left),('weight',5,right)],dividechars=1)
    def createLeft(self):
        wrapedChatButton = wrapButton(self.chatButton)
        wrapedContactButton= wrapButton(self.contactButton)
        urwid.connect_signal(self.chatButton,'click',self.on_chat_button_click)
        urwid.connect_signal(self.contactButton,'click',self.on_contact_button_click)
        topLeft = urwid.Columns([wrapedChatButton,wrapedContactButton],dividechars=1)
        bottomLeft = urwid.BoxAdapter(self.chatListBox,screenRows-3) 
        return urwid.Pile([topLeft,bottomLeft])
    def createRight(self):
        wrapedInputEdit = wrapEdit(self.inputBox)
        urwid.connect_signal(self.sendButton,'click',self.on_send_button_click)
        self.chat_name = urwid.Text("TWchat",align='center')
        title = urwid.AttrMap(urwid.LineBox(self.chat_name),'button')
        wrapedSendButton = wrapButton(self.sendButton)
        bottomRight = urwid.Columns([('weight',5,wrapedInputEdit),('weight',1,wrapedSendButton)],dividechars=1)
        topRight= urwid.BoxAdapter(self.messageListBox,screenRows-6)
        return urwid.Pile([title,topRight,bottomRight])
    def on_chat_button_click(self,button):
        self.chatListBox.show_chat()
    def on_contact_button_click(self,button):
        self.chatListBox.show_contact()
    def on_send_button_click(self,button):
        text = self.inputBox.edit_text
        self.send_message_to(text,self.owner_id,self.current_chat_from) 
    def send_message_to(self,text,fromUserName,toUserName):
        if text=="":
            return 
        if self.current_chat_from in [None,""]:
            return
        self.recive_message(create_msg(fromUserName,toUserName,text),self.currentchat_name)
        self.itchat.send(text,toUserName)
        self.inputBox.set_edit_text("")
    def set_current_chat(self,chat_id,chat_name):
        self.current_chat_from =chat_id 
        self.currentchat_name = chat_name
        self.chat_name.set_text(chat_name)
        msgList = self.chatListBox.get_chat_message(chat_id)
        self.messageListBox.bindList(msgList)
        self.loop.draw_screen()
    def recive_message(self,msg,chat_name,is_group=False):
        if msg['User']['UserName']==self.owner_id:
            self.chatListBox.add_chat_by_msg(msg['User']['UserName'],self.currentchat_name,msg)
            self.set_current_chat(self.current_chat_from,self.currentchat_name)
            return
        self.chatListBox.add_chat_by_msg(msg['User']['UserName'],chat_name,msg)
        if not self.current_chat_from or self.current_chat_from==msg['User']['UserName']:
#            self.chatListBox.show_chat()
            self.set_current_chat(msg['User']['UserName'],chat_name)
        self.loop.draw_screen()
def create_msg(fromUserName,toUserName,text):
    newMsg={}
    newMsg['FromUserName']=fromUserName
    newMsg['User']={}
    newMsg['User']['UserName']=toUserName
    newMsg['Text']=text
    newMsg['type']='Text'
    return newMsg
def wrapButton(button):
    button = urwid.LineBox(button)
    return urwid.AttrMap(button,'button')
def wrapEdit(edit):
    return urwid.AttrMap(urwid.LineBox(edit),'edit')
def exit_on_alt_q(key):
    if key in (u'œ',u'Œ'):
        raise urwid.ExitMainLoop()
