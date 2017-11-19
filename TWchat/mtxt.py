import urwid
import os
from PIL import Image
class ImageText(urwid.Text):
    def __init__(self,image_name,markup='Img Message Click to see the Image', align='left', wrap='space', layout=None):
        urwid.Text.__init__(self,markup,align,wrap,layout)
        self.image_name=image_name
        self.ishowen=False
        try:
            self.img = Image.open(self.image_name) 
        except:
            self.set_text("Image dowload failed , please check on your phone")
    def keypress(self,size, key):
        if key =='enter':
            self.show_img()
    def mouse_event(self,size, event, button, col, row, focus):
        if event == 'mouse release':
            self.show_img()
    def selectable(self):
        return True
    def show_img(self):
        if hasattr(self, 'img') :
            self.img.show()

class RecodingText(urwid.Text):
    def __init__(self,voice_name,markup='Voice Message Click to listen', align='left', wrap='space', layout=None):
        urwid.Text.__init__(self,markup,align,wrap,layout)
        self.voice_name=voice_name
        self.mpg123=0
        for cmdpath in os.environ['PATH'].split(':'):
            if os.path.isdir(cmdpath) and 'mpg123' in os.listdir(cmdpath):
                self.mpg123=1
    def keypress(self,size, key):
        if key =='enter':
            self.play_voide()
    def mouse_event(self,size, event, button, col, row, focus):
        self.play_voide()
    def selectable(self):
        return True
    def play_voide(self):
        if self.mpg123:
            os.popen('mpg123 '+self.voice_name+" 1>/dev/null 2>&1")
        else:
            self.set_text("please install mpg123")
 
