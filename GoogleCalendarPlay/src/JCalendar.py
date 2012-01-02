'''
Created on 2011. 11. 16.
Last modified 2012. 01. 02

@author: John
'''
try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom
import getopt
import sys
import string
import time
import getpass
import my_calendar_example



class JCalendar():  
  def __init__(self):
    self.cal_client = gdata.calendar.client.CalendarClient(source='Google-Calendar_Python_Sample-1.0')
    
  def Login(self, username='', password=''):
    while not username:
      username = raw_input('Please input google calendar account: ')
      if not username:
        print "User name can not be blank"
    while not password:
      password = getpass.getpass()
      if not password:
        print "Password can not be blank"
        
    self.cal_client.client_login(username, password, self.cal_client.source)
        
  
  def InsertQuickAddEvent(self):
    while 1:
      content = raw_input('please enter content for this event: ')
      if not content:
        print 'content can not be blank'
      else: 
        break
  #    
    event = gdata.calendar.data.CalendarEventEntry()
    event.content = atom.data.Content(text=content)
    event.quick_add = gdata.calendar.data.QuickAddProperty(value='true')
    new_event = self.cal_client.InsertEvent(event)
    return new_event
  
  
def main():
  
  cal = JCalendar()
  cal.Login()
  cal.InsertQuickAddEvent()
  

if __name__ == '__main__':
  main()
