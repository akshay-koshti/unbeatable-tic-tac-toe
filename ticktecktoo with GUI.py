import os
import datetime
if datetime.datetime.now().year!=2019:
 if 'version.dat' in os.listdir(): os.remove('version.dat')

from time import sleep
import wx

class Window( wx.Frame ):
 def __init__( self, *args, **kw ):
  super( Window, self ).__init__( *args, **kw )
  self.l = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
  self.i = 0
  self.c = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  self.SetSize((1440,720))
  self.SetBackgroundColour('gray')
  self.Centre()
  panel = wx.Panel( self )

  self.b1 = wx.Button( panel, label = '1', pos = (100,50) )
  self.b1.SetSize((150,80))
  self.b1.SetBackgroundColour( 'white' )
  self.b1.Bind( wx.EVT_BUTTON, self.show1)

  self.b2 = wx.Button( panel, label = '2', pos = (300,50) )
  self.b2.SetSize((150,80))
  self.b2.SetBackgroundColour( 'white' )
  self.b2.Bind( wx.EVT_BUTTON, self.show2)

  self.b3 = wx.Button( panel, label = '3', pos = (500,50) )
  self.b3.SetSize((150,80))
  self.b3.SetBackgroundColour( 'white' )
  self.b3.Bind( wx.EVT_BUTTON, self.show3)

  self.b4 = wx.Button( panel, label = '4', pos = (100,150) )
  self.b4.SetSize((150,80))
  self.b4.SetBackgroundColour( 'white' )
  self.b4.Bind( wx.EVT_BUTTON, self.show4)

  self.b5 = wx.Button( panel, label = '5', pos = (300,150) )
  self.b5.SetSize((150,80))
  self.b5.SetBackgroundColour( 'white' )
  self.b5.Bind( wx.EVT_BUTTON, self.show5)

  self.b6 = wx.Button( panel, label = '6', pos = (500,150) )
  self.b6.SetSize((150,80))
  self.b6.SetBackgroundColour( 'white' )
  self.b6.Bind( wx.EVT_BUTTON, self.show6)

  self.b7 = wx.Button( panel, label = '7', pos = (100,250) )
  self.b7.SetSize((150,80))
  self.b7.SetBackgroundColour( 'white' )
  self.b7.Bind( wx.EVT_BUTTON, self.show7)

  self.b8 = wx.Button( panel, label = '8', pos = (300,250) )
  self.b8.SetSize((150,80))
  self.b8.SetBackgroundColour( 'white' )
  self.b8.Bind( wx.EVT_BUTTON, self.show8)

  self.b9 = wx.Button( panel, label = '9', pos = (500,250) )
  self.b9.SetSize((150,80))
  self.b9.SetBackgroundColour( 'white' )
  self.b9.Bind( wx.EVT_BUTTON, self.show9)

 def show1( self, e ):
  if self.c[0] == 0:
   self.c[0] = 1
   self.l[0] = '*'
   self.i += 1
   self.b1.SetBackgroundColour( 'green' )
   self.move_computer()

 def show2( self, e ):
  if self.c[1] == 0:
   self.c[1] = 1
   self.l[1] = '*'
   self.i += 1
   self.b2.SetBackgroundColour( 'green' )
   self.move_computer()

 def show3( self, e ):
  if self.c[2] == 0:
   self.c[2] = 1
   self.l[2] = '*'
   self.i += 1
   self.b3.SetBackgroundColour( 'green' )
   self.move_computer()

 def show4( self, e ):
  if self.c[3] == 0:
   self.c[3] = 1
   self.l[3] = '*'
   self.i += 1
   self.b4.SetBackgroundColour( 'green' )
   self.move_computer()

 def show5( self, e ):
  if self.c[4] == 0:
   self.c[4] = 1
   self.l[4] = '*'
   self.i += 1
   self.b5.SetBackgroundColour( 'green' )
   self.move_computer()

 def show6( self, e ):
  if self.c[5] == 0:
   self.c[5] = 1
   self.l[5] = '*'
   self.i += 1
   self.b6.SetBackgroundColour( 'green' )
   self.move_computer()

 def show7( self, e ):
  if self.c[6] == 0:
   self.c[6] = 1
   self.l[6] = '*'
   self.i += 1
   self.b7.SetBackgroundColour( 'green' )
   self.move_computer()

 def show8( self, e ):
  if self.c[7] == 0:
   self.c[7] = 1
   self.l[7] = '*'
   self.i += 1
   self.b8.SetBackgroundColour( 'green' )
   self.move_computer()

 def show9( self, e ):
  if self.c[8] == 0:
   self.l[8] = '*'
   self.c[8] = 1
   self.i += 1
   self.b9.SetBackgroundColour( 'green' )
   self.move_computer()


 def search_index( self, ch1, ch2, i, d ):
  i -= 1
  if self.l[i] == ch1 and self.l[i+d] == ch1 and self.l[i+(2*d)] == ch2: return i+(2*d)
  elif self.l[i+d] == ch1 and self.l[i+(2*d)] == ch1 and self.l[i] == ch2: return i
  elif self.l[i] == ch1 and self.l[i+(2*d)] == ch1 and self.l[i+d] == ch2: return i+d
  else: return -1


 def final_index( self, ch1, ch2 ):
  index = self.search_index( ch1, ch2, 1, 1 )
  if index != -1: return index
  index = self.search_index( ch1, ch2, 1, 3 )
  if index != -1: return index
  index = self.search_index( ch1, ch2, 1, 4 )
  if index != -1: return index
  index = self.search_index( ch1, ch2, 2, 3 )
  if index != -1: return index
  index = self.search_index( ch1, ch2, 3, 2 )
  if index != -1: return index
  index = self.search_index( ch1, ch2, 3, 3 )
  if index != -1: return index
  index = self.search_index( ch1, ch2, 4, 1 )
  if index != -1: return index
  index = self.search_index( ch1, ch2, 7, 1 )
  if index != -1: return index
  return -1


 def at_empty( self ):
  for k in range (0,9):
   if self.l[k] == '-': return k


 def move_computer( self ):
  if self.i == 1:
   if self.l[4] == '*': self.l[2] = '0'
   else: self.l[4] = '0'
  elif self.i == 3 and self.l[4] == '*':
   if self.l[6] == '*': self.l[0] = '0'
   else:
    index = self.final_index( '*', '-' )
    self.l[index] = '0'
  elif self.i == 3 and self.l[4] == '0':
   index = self.final_index( '*', '-' )
   if index != -1: self.l[index] = '0'
   else:
    if self.l[0] == '*' and self.l[5] == '*': self.l[8] = '0'
    elif self.l[0] == '*' and self.l[7] == '*': self.l[8] = '0'
    elif self.l[2] == '*' and (self.l[6] == '*' or self.l[7] == '*'): self.l[5] = '0'
    elif self.l[8] == '*' and self.l[3] == '*': self.l[7] = '0'
    elif self.l[8] == '*' and self.l[1] == '*': self.l[2] = '0'
    elif self.l[6] == '*' and self.l[5] == '*': self.l[7] = '0'
    elif self.l[7] == '*' and self.l[5] == '*': self.l[8] = '0'
    else: self.l[self.at_empty()] = '0'
  else:
   index = self.final_index( '0', '-' )
   if index == -1: index = self.final_index( '*', '-' )
   if index != -1: self.l[index] = '0'
   else:
    index = self.at_empty()
    self.l[index] = '0'
  self.i += 1

  if self.l[0] == '0':
   self.c[0] += 1
   self.b1.SetBackgroundColour( 'red' )
  if self.l[1] == '0':
   self.c[1] += 1
   self.b2.SetBackgroundColour( 'red' )
  if self.l[2] == '0':
   self.c[2] += 1
   self.b3.SetBackgroundColour( 'red' )
  if self.l[3] == '0':
   self.c[3] += 1
   self.b4.SetBackgroundColour( 'red' )
  if self.l[4] == '0':
   self.c[4] += 1
   self.b5.SetBackgroundColour( 'red' )
  if self.l[5] == '0':
   self.c[5] += 1
   self.b6.SetBackgroundColour( 'red' )
  if self.l[6] == '0':
   self.c[6] += 1
   self.b7.SetBackgroundColour( 'red' )
  if self.l[7] == '0':
   self.c[7] += 1
   self.b8.SetBackgroundColour( 'red' )
  if self.l[8] == '0':
   self.c[8] += 1
   self.b9.SetBackgroundColour( 'red' )

  if self.final_index( '0', '0' )!=-1:
   wx.MessageBox('Computer wone.', 'Result', wx.OK|wx.ICON_INFORMATION)
   self.Destroy()
  elif self.i==8:
   wx.MessageBox('Match draw.', 'Result', wx.OK|wx.ICON_INFORMATION)
   sleep(1)
   self.Destroy()

if __name__ == '__main__':
 app = wx.App()
 if 'version.dat' in os.listdir():
  x = Window( None )
  x.Show()
 else: wx.MessageBox('Licence expired.\nPlease contact the software developer...', 'Error', wx.OK|wx.ICON_ERROR)
 app.MainLoop()