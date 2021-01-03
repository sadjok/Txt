# -*- encoding:utf-8 -*-  
import sys  
import os  
import struct  
import time  
import win32con  
  
from win32api import *  

try:  
  from winxpgui import *  
except ImportError:  
  from win32gui import *  
  
  
class PyNOTIFYICONDATA:  
  _struct_format = (  
    "I" 
    "I"  
    "I" 
    "I"  
    "I"  
    "I"  
    "128s"   
    "I" 
    "I" 
    "256s" 
    "I" 
    "64s"  
    "I"   
  )  
  _struct = struct.Struct(_struct_format)  
  
  hWnd = 0  
  uID = 0  
  uFlags = 0  
  uCallbackMessage = 0  
  hIcon = 0  
  szTip = ''  
  dwState = 0  
  dwStateMask = 0  
  szInfo = ''  
  uTimeoutOrVersion = 0  
  szInfoTitle = ''  
  dwInfoFlags = 0  
  
  def pack(self):  
    return self._struct.pack(  
     self._struct.size,  
      self.hWnd,  
      self.uID,  
      self.uFlags,  
      self.uCallbackMessage,  
      self.hIcon,  
      self.szTip.encode("gbk"),  
      self.dwState,  
      self.dwStateMask,  
      self.szInfo.encode("gbk"),  
      self.uTimeoutOrVersion,  
      self.szInfoTitle.encode("gbk"),  
      self.dwInfoFlags
    )
  
  def __setattr__(self, name, value):  
     
    if not hasattr(self, name):  
      raise (NameError, name)  
    self.__dict__[name] = value  
  
class MainWindow():  
  def __init__(self):
   
    self.title =""
    self.msg =""
    self.duration=5
    self.hwnd =None
    self.hinst =None
    self.regOk = False
 
 
  
  def creWind(self):
   
    wc = WNDCLASS()  
    self.hinst = wc.hInstance = GetModuleHandle(None)  
    wc.lpszClassName = "PythonTaskbarDemo"
    wc.lpfnWndProc = { win32con.WM_DESTROY: self.OnDestroy }
    classAtom = RegisterClass(wc)
 
    style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU  
    self.hwnd = CreateWindow(classAtom, "Taskbar Demo", style,  
      0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,  
      0, 0, self.hinst, None  
    )
    UpdateWindow(self.hwnd)
  
  def startBubble(self,title, msg, duration=3):
    
    if(self.hwnd==None):
      self.creWind()
    self.title =title
    self.msg=msg
    self.duration=duration
    
    iconPathName = "txt.ico"  
    icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE  
    try:  
      hicon = LoadImage(self.hinst, iconPathName, win32con.IMAGE_ICON, 0, 0, icon_flags)  
    except:  
      hicon = LoadIcon(0, win32con.IDI_APPLICATION)  
    flags = NIF_ICON | NIF_MESSAGE | NIF_TIP  
    nid = (self.hwnd, 0, flags, win32con.WM_USER + 20, hicon, "Balloon  tooltip demo")  
    try:
      Shell_NotifyIcon(NIM_ADD, nid)
    except:
      self.hwnd==None
    self.show_balloon(self.title, self.msg)
    
    time.sleep(self.duration)

    try:
      DestroyWindow(self.hwnd)
      self.hwnd==None
    except:
      return None
    
  
  def show_balloon(self, title, msg):  

  
    nid = PyNOTIFYICONDATA()  
    nid.hWnd = self.hwnd  
    nid.uFlags = NIF_INFO  
  
  
    nid.szInfo = msg[:64]
    nid.szInfoTitle = title[:256]  

    from ctypes import windll  
    Shell_NotifyIcon = windll.shell32.Shell_NotifyIconA  
    Shell_NotifyIcon(NIM_MODIFY, nid.pack())  
  
  def OnDestroy(self, hwnd, msg, wparam, lparam):  
    nid = (self.hwnd, 0)  
    Shell_NotifyIcon(NIM_DELETE, nid)  
    PostQuitMessage(0)



