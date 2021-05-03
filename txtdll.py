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
	txtlog.log.writelog(time.strftime('%H:%M:%S',time.localtime()),'ȱ�ٳ����',os.getpid())
	tkinter.messagebox.showerror('����','ȱ�ٳ����')
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
	label10 = Label(helper,text = 'ctrl-shift-h' + ' ' + 'ѡȡ��ɫ').pack(ipadx = 10)
	label11 = Label(helper,text = 'ctrl-f' + ' ' + 'ˢ��').pack(ipadx = 11)
	label12 = Label(helper,text = 'F11' + ' ' + 'ȫ��').pack(ipadx = 12)
	label13 = Label(helper,text = 'ctrl-q' + ' ' + '�˳�').pack(ipadx = 13)
	label14 = Label(helper,text = 'ctrl-shift-c' + ' ' + '���').pack(ipadx = 14)
	helper.mainloop()

	
def help_all(event = ''):
	tkinter.messagebox.showinfo(title='����', message='����һ���ı�����'+'  '+'�汾�� V3.0.5'+'   '+'��������:admin')

def info_all(event = ''):
	tkinter.messagebox.showinfo(title='����', message='һ����Python���ļ��±�')

def open_file(event = ''):

	import easygui
			 
	file_path = easygui.fileopenbox(default='*.*')
	
	text.delete('0.0','end')
	
	try:			 
		file = open(file_path,'r',encoding = 'gbk')
		for line in file:
			file.read(0)
			text.insert(INSERT,line)
			root.title('*' + file_path + ' - ���±�')
	except:
		try:
			file = open(file_path,'r',encoding = 'utf-8')
			for line in file:
				file.read(0)
				text.insert(INSERT,line)
				root.title('*' + file_path + ' - ���±�')
		except:
			tkinter.messagebox.showinfo('���±�','��ʽ��֧��')

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
	f1 = open('δ����.txt','w')
	contents = text.get('0.0','end')
	f1.write(contents)
	f1.close()
	root.title(Folderpath + '  ' + '-���±�')
	filemenu.entryconfig("����",state = DISABLED)
		

def clear_text(event = ''):
	text.delete('0.0','end')
	root.title('*δ���� - ���±�')
	filemenu.entryconfig("����",state = NORMAL)

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

	messagebox.showinfo('��ɫ�ǣ�' + color,'��ɫ�ǣ�' + color)

def insertimage():
    filename=filedialog.askopenfilename()

    photo=PhotoImage(file=filename)
    text.image_create(INSERT,image=photo)
    
    root.update()
      
root = Tk()  
root.title('���±�')
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
filemenu.add_command(label="�½�", command=clear_text)
filemenu.add_command(label="��", command=open_file)
filemenu.add_command(label="����", command=save_all_file)
filemenu.add_command(label="���Ϊ", command=save_all_file_other_path)
filemenu.add_command(label="ͼƬ",command=insertimage)
filemenu.add_command(label="ʱ��",command=get_time)
filemenu.add_separator()
filemenu.add_command(label="�뿪", command=root.quit)
menubar.add_cascade(label="�ļ�", menu=filemenu)

editmenu = Menu(menubar, tearoff=1)
editmenu.add_command(label="ˢ��", command=again)
editmenu.add_command(label="����",command=callback)
editmenu.add_command(label="����",command=cut)
editmenu.add_command(label="����",command=copy)
editmenu.add_command(label="ճ��",command=paste)
menubar.add_cascade(label="ѡ��", menu=editmenu)

usemenu = Menu(menubar, tearoff=1)
usemenu.add_command(label="��ɫѡ����", command=color_set)
usemenu.add_command(label="ʹ��bing����", command=search_use_bing)
usemenu.add_command(label="�����",command=fast_use_helper)
menubar.add_cascade(label="����", menu=usemenu)
	
helpmenu = Menu(menubar, tearoff=1)
helpmenu.add_command(label="����", command=help_all)
helpmenu.add_command(label="����", command=info_all)
menubar.add_cascade(label="����", menu=helpmenu)

popupmenu=Menu(tearoff=0)
popupmenu.add_command(label="����",command=callback)
popupmenu.add_command(label="����",command=cut)
popupmenu.add_command(label="����",command=copy)
popupmenu.add_command(label="ճ��",command=paste)
popupmenu.add_separator()
popupmenu.add_command(label="ˢ��", command=again)
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
