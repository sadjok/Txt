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
	load.title('����')
	load.iconbitmap('txt.ico')
	
	load.mainloop()

def fast_use_helper():
	
	helper = Tk()
	helper.title('��ݼ�')
	helper.iconbitmap('txt.ico')
	helper.geometry("300x375") 
	label1 = Label(helper,text = 'ctrl-c' + ' ' + '����').pack(ipadx = 1)
	label2 = Label(helper,text = 'ctrl-v' + ' ' + 'ճ��').pack(ipadx = 2)
	label3 = Label(helper,text = 'ctrl-x' + ' ' + '����').pack(ipadx = 3)
	label4 = Label(helper,text = 'ctrl-z' + ' ' + '����').pack(ipadx = 4)
	label5 = Label(helper,text = 'ctrl-h' + ' ' + '����').pack(ipadx = 5)
	label6 = Label(helper,text = 'ctrl-i' + ' ' + '��Ϣ').pack(ipadx = 6)
	label7 = Label(helper,text = 'ctrl-s' + ' ' + '����').pack(ipadx = 7)
	label8 = Label(helper,text = 'ctrl-o' + ' ' + '��').pack(ipadx = 8)
	label9 = Label(helper,text = 'ctrl-shift-s' + ' ' + '���Ϊ').pack(ipadx = 9)
	label10 = Label(helper,text = 'ctrl-shift-c' + ' ' + 'ѡȡ��ɫ').pack(ipadx = 10)
	label11 = Label(helper,text = 'ctrl-f' + ' ' + 'ˢ��').pack(ipadx = 11)
	label12 = Label(helper,text = 'F11' + ' ' + 'ȫ��').pack(ipadx = 12)
	label13 = Label(helper,text = 'ctrl-q' + ' ' + '�˳�').pack(ipadx = 13)
	helper.mainloop()

	root.mainloop()
	
def help_all(event = ''):
	tkinter.messagebox.showinfo(title='����', message='����һ���ı�����'+'  '+'�汾�� V3.0.5'+'   '+'��������:admin')
	
def info_all(event = ''):
	tkinter.messagebox.showinfo(title='����', message='һ����Python���ļ��±�')

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
	f1 = open('δ����.txt','w')
	contents = text.get('0.0','end')
	f1.write(contents)
	f1.close()
	root.title(Folderpath + '  ' + '-���±�')
	
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
	f1 = open('δ����.txt','w')
	contents = text.get('0.0','end')
	f1.write(contents)
	f1.close()
	root.title(Folderpath + '  ' + '-���±�')

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



	messagebox.showinfo('��ɫ�ǣ�' + askcolor(),'��ɫ�ǣ�' + askcolor())

def insertimage():
    filename=filedialog.askopenfilename()

    photo=PhotoImage(file=filename)
    text.image_create(INSERT,image=photo)
    
    mainloop()	
	
root = Tk()  
root.title('�ı�')
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
		menu.Append(self.MENU_ID1, '��Ϣ')
		menu.Append(self.MENU_ID2, '��ʾ')
		menu.Append(self.MENU_ID3, '�˳�')
		return menu
	
	def onOne(self,event):
		tkinter.messagebox.showinfo(title='����', message='һ����Python���ļ��±�')

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
	msgContent = u"ϵͳ�����������С�"
	msgTitle = msgTitle
	bubble = MainWindow()
	bubble.startBubble(msgTitle,msgContent)
	app = MyApp()

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="��", command=open_file)
filemenu.add_command(label="����", command=save_all_file)
filemenu.add_command(label="���Ϊ", command=save_all_file)
filemenu.add_separator()
filemenu.add_command(label="�뿪", command=root.quit)
menubar.add_cascade(label="�ļ�", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="����ͼƬ",command=insertimage)
editmenu.add_command(label="ˢ��", command=again)
editmenu.add_command(label="����",command=callback)
editmenu.add("command",label="����",command=cut)
editmenu.add_command(label="����",command=copy)
editmenu.add_command(label="ճ��",command=paste)
editmenu.add_command(label="�����",command=fast_use_helper)
editmenu.add_command(label="ϵͳ����",command=change_to_little)
menubar.add_cascade(label="ѡ��", menu=editmenu)

usemenu = Menu(menubar, tearoff=0)
usemenu.add_command(label="��ɫѡ����", command=color_set)
menubar.add_cascade(label="����", menu=usemenu)
	
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="�鿴����", command=help_all)
helpmenu.add_command(label="�鿴����", command=help_all)
menubar.add_cascade(label="����", menu=helpmenu)

settingsmenu = Menu(menubar, tearoff=0)
settingsmenu.add_command(label="ȫ��", command=toggleFullScreen())
settingsmenu.add_command(label="�˳�ȫ��", command=quitFullScreen())
settingsmenu.add_command(label="�Զ�����", command=autochangeline())
menubar.add_cascade(label="ѡ��", menu=settingsmenu)

popupmenu=Menu(root,tearoff=0)
popupmenu.add_command(label="ȫѡ")
popupmenu.add_command(label="����ͼƬ")
popupmenu.add_command(label="����")
popupmenu.add_separator()
popupmenu.add("command",label="����")
popupmenu.add_command(label="����")
popupmenu.add_command(label="ճ��")
popupmenu.add("command",label="ɾ��")
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


