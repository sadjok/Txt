# -*- coding:gbk -*-
import os
import tkinter.messagebox
import time 
from tkinter import *
from tkinter.ttk import *
from tkinter.font import *
from tkinter import filedialog
import ctypes
load = Tk()
load.withdraw()
try:
	import txtlog
	import txttaskkill
except:
	txtlog.log.writelog(time.strftime('%H:%M:%S',time.localtime()),'缺少程序库',os.getpid())
	tkinter.messagebox.showerror('错误','缺少程序库')
	exit(0)	

import webbrowser
import base64


def callback(event = ''):
    text.edit_undo()


def popup(event = ''):
    popupmenu.post(event.x_root,event.y_root)


def copy(event = ''):
    global content

    content = text.get(SEL_FIRST,SEL_LAST)
    return content


def cut(event = ''):
    global content

    content = text.get(SEL_FIRST,SEL_LAST)
    text.delete(SEL_FIRST,SEL_LAST)

    return content


def paste(event = ''):

        text.insert(INSERT,content)

def select_all():
    pass

def textdelete():
    text.delete(SEL_FIRST,SEL_LAST)


	
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
	label10 = Label(helper,text = 'ctrl-shift-h' + ' ' + '选取颜色').pack(ipadx = 10)
	label11 = Label(helper,text = 'ctrl-f' + ' ' + '刷新').pack(ipadx = 11)
	label12 = Label(helper,text = 'F11' + ' ' + '全屏').pack(ipadx = 12)
	label13 = Label(helper,text = 'ctrl-q' + ' ' + '退出').pack(ipadx = 13)
	label14 = Label(helper,text = 'ctrl-shift-c' + ' ' + '清空').pack(ipadx = 14)
	helper.mainloop()

	
def help_all(event = ''):
	tkinter.messagebox.showinfo(title='帮助', message='这是一个文本程序'+'  '+'版本是 V3.0.5'+'   '+'开发者是:admin')

def info_all(event = ''):
	tkinter.messagebox.showinfo(title='帮助', message='一个用Python做的记事本')

def open_file(event = ''):

	import easygui
			 
	file_path = easygui.fileopenbox(default='*.*')
	
	text.delete('0.0','end')
	
	try:			 
		file = open(file_path,'r',encoding = 'gbk')
		for line in file:
			file.read(0)
			text.insert(INSERT,line)
			root.title('*' + file_path + ' - 记事本')
	except:
		try:
			file = open(file_path,'r',encoding = 'utf-8')
			for line in file:
				file.read(0)
				text.insert(INSERT,line)
				root.title('*' + file_path + ' - 记事本')
		except:
			tkinter.messagebox.showinfo('记事本','格式不支持')

def search_use_bing():
	webbrowser.open('https://cn.bing.com/search', new=0, autoraise=True)

def get_time():
	get_time_ = time.strftime("%Y-%m-%d", time.localtime())
	text.insert(INSERT,get_time_)

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
	filemenu.entryconfig("保存",state = DISABLED)
		

def clear_text(event = ''):
	text.delete('0.0','end')
	root.title('*未命名 - 记事本')
	filemenu.entryconfig("保存",state = NORMAL)

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

def crash():
	crash = Tk()
	crash.iconbitmap("txt.ico")
	crash.mainloop()
	
def color_set(event = ''):
	from tkinter.commondialog import Dialog

	class Chooser(Dialog):
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

		if color:
			options = options.copy()
			options["initialcolor"] = color

		return Chooser(**options).show()

	color = askcolor()

	messagebox.showinfo('颜色是：' + color,'颜色是：' + color)

def insertimage():
    filename=filedialog.askopenfilename()

    photo=PhotoImage(file=filename)
    text.image_create(INSERT,image=photo)
    
    root.update()
      
root = Tk()  
root.title('记事本')
root.iconbitmap("txt.ico")
root.resizable(width = True, height = True)

try:
	myappid = "txt"
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
	ctypes.windll.shcore.SetProcessDpiAwareness(1)
	ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
	root.tk.call('tk', 'scaling', ScaleFactor/75)
except:
	pass

scrollbarx = Scrollbar(root)
scrollbarx.pack(side = RIGHT, fill = Y)
scrollbary = Scrollbar(root, orient = HORIZONTAL)
scrollbary.pack(side = BOTTOM, fill = X)

text = Text(root, yscrollcommand = scrollbarx.set, xscrollcommand = scrollbary.set, wrap = 'none')
text.pack(fill=BOTH, expand=True)

scrollbarx.config(command = text.yview)
scrollbary.config(command = text.xview)

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=1)
filemenu.add_command(label="新建", command=clear_text)
filemenu.add_command(label="打开", command=open_file)
filemenu.add_command(label="保存", command=save_all_file)
filemenu.add_command(label="另存为", command=save_all_file_other_path)
filemenu.add_command(label="图片",command=insertimage)
filemenu.add_command(label="时间",command=get_time)
filemenu.add_separator()
filemenu.add_command(label="离开", command=root.quit)
menubar.add_cascade(label="文件", menu=filemenu)

editmenu = Menu(menubar, tearoff=1)
editmenu.add_command(label="刷新", command=again)
editmenu.add_command(label="撤销",command=callback)
editmenu.add_command(label="剪切",command=cut)
editmenu.add_command(label="复制",command=copy)
editmenu.add_command(label="粘贴",command=paste)
menubar.add_cascade(label="选项", menu=editmenu)

usemenu = Menu(menubar, tearoff=1)
usemenu.add_command(label="颜色选择器", command=color_set)
usemenu.add_command(label="使用bing搜索", command=search_use_bing)
usemenu.add_command(label="快键建",command=fast_use_helper)
menubar.add_cascade(label="工具", menu=usemenu)
	
helpmenu = Menu(menubar, tearoff=1)
helpmenu.add_command(label="帮助", command=help_all)
helpmenu.add_command(label="更多", command=info_all)
menubar.add_cascade(label="帮助", menu=helpmenu)

popupmenu=Menu(tearoff=0)
popupmenu.add_command(label="撤销",command=callback)
popupmenu.add_command(label="剪切",command=cut)
popupmenu.add_command(label="复制",command=copy)
popupmenu.add_command(label="粘贴",command=paste)
popupmenu.add_separator()
popupmenu.add_command(label="刷新", command=again)
text.bind("<Button-3>",popup)

root.bind("<F11>",
	lambda event: root.attributes("-fullscreen",
				not root.attributes("-fullscreen")))
root.bind("<Control-KeyPress-s>",save_all_file)
root.bind("<Control-Shift-KeyPress-S>",save_all_file_other_path)
root.bind("<Control-KeyPress-o>",open_file)
root.bind("<Control-KeyPress-h>",help_all)
root.bind("<Control-KeyPress-f>",again)
root.bind("<Control-KeyPress-i>",info_all)
root.bind("<Control-Shift-KeyPress-H>",color_set)
root.bind("<Control-Shift-KeyPress-C>",clear_text)
root.bind("<Control-q>",quit)

root.config(menu=menubar)
