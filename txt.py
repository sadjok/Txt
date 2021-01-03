# -*- coding:gbk -*-
import os
import tkinter.messagebox
import time 
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import pyautogui
import ctypes
import wx
import wx.adv
from popo import *

def callback():
    text.edit_undo()


def popup(event):
    popupmenu.post(event.x_root,event.y_root)


def copy():
    global content

    content=text.get(SEL_FIRST,SEL_LAST)
    return content


def cut():
    global content

    content=text.get(SEL_FIRST,SEL_LAST)
    text.delete(SEL_FIRST,SEL_LAST)

    return content


def paste():

        text.insert(INSERT,content)

def select_all():
    pass

def textdelete():
    text.delete(SEL_FIRST,SEL_LAST)

def toggleFullScreen():
	root.attributes("-fullscreen",True)

def quitFullScreen():
	root.attributes("-fullscreen",False)

def load_ttf():
	load = Tk()
	load.title('字体')
	load.iconbitmap('txt.ico')
	
	load.mainloop()

def fast_use_helper():
	
	helper = Tk()
	helper.title('快捷键')
	helper.iconbitmap('txt.ico')
	helper.geometry("300x375") 
	label1 = Label(helper,text = 'ctrl-c' + ' ' + '复制').pack(ipadx = 1)
	label2 = Label(helper,text = 'ctrl-v' + ' ' + '粘贴').pack(ipadx = 2)
	label3 = Label(helper,text = 'ctrl-x' + ' ' + '剪切').pack(ipadx = 3)
	label4 = Label(helper,text = 'ctrl-z' + ' ' + '撤销').pack(ipadx = 4)
	label5 = Label(helper,text = 'ctrl-h' + ' ' + '帮助').pack(ipadx = 5)
	label6 = Label(helper,text = 'ctrl-i' + ' ' + '信息').pack(ipadx = 6)
	label7 = Label(helper,text = 'ctrl-s' + ' ' + '保存').pack(ipadx = 7)
	label8 = Label(helper,text = 'ctrl-o' + ' ' + '打开').pack(ipadx = 8)
	label9 = Label(helper,text = 'ctrl-shift-s' + ' ' + '另存为').pack(ipadx = 9)
	label10 = Label(helper,text = 'ctrl-shift-c' + ' ' + '选取颜色').pack(ipadx = 10)
	label11 = Label(helper,text = 'ctrl-f' + ' ' + '刷新').pack(ipadx = 11)
	label12 = Label(helper,text = 'F11' + ' ' + '全屏').pack(ipadx = 12)
	label13 = Label(helper,text = 'ctrl-q' + ' ' + '退出').pack(ipadx = 13)
	helper.mainloop()

	root.mainloop()
	
def help_all(event = ''):
	tkinter.messagebox.showinfo(title='帮助', message='这是一个文本程序'+'  '+'版本是 V3.0.5'+'   '+'开发者是:admin')
	
def info_all(event = ''):
	tkinter.messagebox.showinfo(title='帮助', message='一个用Python做的记事本')

def open_file(event = ''):

	import easygui
			 
	file_path = easygui.fileopenbox(default='*.*')
				 
	file = open(file_path,'r')
	for line in file:
		file.read(0)
		text.insert(INSERT,line)
				
def autochangeline():
	time.sleep(1)
	pyautogui.press('Enter')	 
						
def save_all_file(event = ''):
	save = Tk()
	width = 650
	height = 450
	screenwidth = save.winfo_screenwidth()
	screenheight = save.winfo_screenheight()	
	save.withdraw()
	Folderpath = filedialog.askdirectory()
	os.chdir(Folderpath)
	f1 = open('未命名.txt','w')
	contents = text.get('0.0','end')
	f1.write(contents)
	f1.close()
	root.title(Folderpath + '  ' + '-记事本')
	
def save_all_file_other_path(event = ''):
	save = Tk()
	width = 650
	height = 450
	screenwidth = save.winfo_screenwidth()
	screenheight = save.winfo_screenheight()
	save.iconbitmap('txt.ico')
	save.withdraw()
	Folderpath = filedialog.askdirectory()
	os.chdir(Folderpath)
	f1 = open('未命名.txt','w')
	contents = text.get('0.0','end')
	f1.write(contents)
	f1.close()
	root.title(Folderpath + '  ' + '-记事本')

def again(event = ''):
	root.update()

def color_set(event = ''):
	from tkinter.commondialog import Dialog

	class Chooser(Dialog):
		"Ask for a color"

		command = "tk_chooseColor"

		def _fixoptions(self):
			try:
				color = self.options["initialcolor"]
				if isinstance(color, tuple):
					self.options["initialcolor"] = "#%02x%02x%02x" % color
			except KeyError:
				pass

	def _fixresult(self, widget, result):

		if not result or not str(result):
			return None, None


		r, g, b = widget.winfo_rgb(result)
		return (r/256, g/256, b/256), str(result)




	def askcolor(color = None, **options):
		"Ask for a color"

		if color:
			options = options.copy()
			options["initialcolor"] = color

		return Chooser(**options).show()



	messagebox.showinfo('颜色是：' + askcolor(),'颜色是：' + askcolor())

def insertimage():
    filename=filedialog.askopenfilename()

    photo=PhotoImage(file=filename)
    text.image_create(INSERT,image=photo)
    
    mainloop()	
	
root = Tk()  
root.title('文本')
root.iconbitmap('txt.ico')
root.resizable(width=False, height=False)

ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor/75)

text=Text(root)
text.pack()

class FolderBookmarkTaskBarIcon(wx.adv.TaskBarIcon):
	ICON = 'txt.ico'
	TITLE = 'txt'

	MENU_ID1, MENU_ID2 , MENU_ID3 = wx.NewIdRef(count=3)

	def __init__(self):
		super().__init__()
		self.SetIcon(wx.Icon(self.ICON), self.TITLE)
		self.Bind(wx.EVT_MENU, self.onOne, id=self.MENU_ID1)
		self.Bind(wx.EVT_MENU, self.onTwo, id=self.MENU_ID2)
		self.Bind(wx.EVT_MENU, self.onExit, id=self.MENU_ID3)

	def CreatePopupMenu(self):

		menu = wx.Menu()
		menu.Append(self.MENU_ID1, '信息')
		menu.Append(self.MENU_ID2, '显示')
		menu.Append(self.MENU_ID3, '退出')
		return menu
	
	def onOne(self,event):
		tkinter.messagebox.showinfo(title='帮助', message='一个用Python做的记事本')

	def onExit(self,event):
		wx.Exit()
		exit(0)
		
	def onTwo(self,event):
		root.attributes('-alpha',1)

class MyFrame(wx.Frame):
	def __init__(self):
		super().__init__()
		FolderBookmarkTaskBarIcon()

class MyApp(wx.App):
	def OnInit(self):
		MyFrame()
		return True

def change_to_little():
	root.attributes('-alpha',0)
	msgTitle = u"txt"
	msgContent = u"系统托盘正在运行。"
	msgTitle = msgTitle
	bubble = MainWindow()
	bubble.startBubble(msgTitle,msgContent)
	app = MyApp()

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="打开", command=open_file)
filemenu.add_command(label="保存", command=save_all_file)
filemenu.add_command(label="另存为", command=save_all_file)
filemenu.add_separator()
filemenu.add_command(label="离开", command=root.quit)
menubar.add_cascade(label="文件", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="插入图片",command=insertimage)
editmenu.add_command(label="刷新", command=again)
editmenu.add_command(label="撤销",command=callback)
editmenu.add("command",label="剪切",command=cut)
editmenu.add_command(label="复制",command=copy)
editmenu.add_command(label="粘贴",command=paste)
editmenu.add_command(label="快键建",command=fast_use_helper)
editmenu.add_command(label="系统托盘",command=change_to_little)
menubar.add_cascade(label="选项", menu=editmenu)

usemenu = Menu(menubar, tearoff=0)
usemenu.add_command(label="颜色选择器", command=color_set)
menubar.add_cascade(label="工具", menu=usemenu)
	
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="查看帮助", command=help_all)
helpmenu.add_command(label="查看更多", command=help_all)
menubar.add_cascade(label="帮助", menu=helpmenu)

settingsmenu = Menu(menubar, tearoff=0)
settingsmenu.add_command(label="全屏", command=toggleFullScreen())
settingsmenu.add_command(label="退出全屏", command=quitFullScreen())
settingsmenu.add_command(label="自动换行", command=autochangeline())
menubar.add_cascade(label="选项", menu=settingsmenu)

popupmenu=Menu(root,tearoff=0)
popupmenu.add_command(label="全选")
popupmenu.add_command(label="插入图片")
popupmenu.add_command(label="撤回")
popupmenu.add_separator()
popupmenu.add("command",label="剪切")
popupmenu.add_command(label="复制")
popupmenu.add_command(label="粘贴")
popupmenu.add("command",label="删除")
text.bind("<Button-3>",popup)

root.bind("<F11>",
	lambda event: root.attributes("-fullscreen",
				not root.attributes("-fullscreen")))
root.bind("<Control-KeyPress-s>",save_all_file)
root.bind("<Control-Shift-KeyPress-S>",save_all_file_other_path)
root.bind("<Control-KeyPress-o>",open_file)
root.bind("<Control-KeyPress-x>",cut)
root.bind("<Control-KeyPress-c>",copy)
root.bind("<Control-KeyPress-v>",paste)
root.bind("<Control-KeyPress-z>",callback)
root.bind("<Control-KeyPress-h>",help_all)
root.bind("<Control-KeyPress-f>",again)
root.bind("<Control-KeyPress-i>",info_all)
root.bind("<Control-Shift-KeyPress-H>",color_set)
root.bind("<Control-q>",quit)

scroll = tkinter.Scrollbar()
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.LEFT, fill=tkinter.Y)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

root.config(menu=menubar)
root.mainloop()


