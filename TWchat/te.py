# -*- coding: UTF-8
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(unicode(text), unicode(title)))

notify(u'👌',u'asd'+'😄')
