import random
from tkinter import *

MysticNumber = random.randint(100,1000)
Guess =5 
#为神秘数字去重
def check():
	global MysticNumber
	MysticNumber = random.randint(100,1000)
	while len(set(str(MysticNumber)))!= len(list(str(MysticNumber))):
		MysticNumber = random.randint(100,1000)
	
def Clue(num):
	global MysticNumber
	list1 = list(str(MysticNumber))
	list2 = list(str(num))
	result = []
	for i in range(len(list2)):
		if list2[i] == list1[i]:
			result.append('fermi')
		elif list2[i] in list1:
			result.append('pico')
		else:
			pass
	if len(result)==0:
		return 'Begals'
	else:
		return " ".join(sorted(result))
		
def Begals(num):
	global Guess,MysticNumber
	if int(num) == MysticNumber:
		return 'You Win!'
	else:
		Guess = Guess - 1
		if Guess ==0:
			return f"I'm sorry you're lose,the MysticNumber is {MysticNumber}"
		else:
			return Clue(num)
#进行判断
def on_hit1():
	Num = Entry.get()
	content = Begals(Num)
	text.insert(INSERT,content+'\n')
	
	
#重置	
def on_hit2():
	global MysticNumber,Guess
	check()
	Guess = 5
	#删除输入框的数
	Entry.delete(0,END)
	#删除提示框的数
	text.delete(0.0,END)
#建立一个窗口对象
check()
tk = Tk()


tk.title('Begals')
#设置窗口大小
tk.geometry('500x300')

#设置标签
label = Label(tk,text = 'Welcome to play Begals.',bg = 'yellow',font = ('Arial',12),width = 30,height =2)

#放置标签
label.pack()


#设置输入框
Entry = Entry(tk,show = None,font=('Arial',14)) #显示为明文形式

#放置输入框
Entry.pack()

#设置按钮
Button1 = Button(tk,text='Guess',font=('Arial',12),width = 10,height = 1,command = on_hit1 )
Button1.pack()
Button2 = Button(tk,text='Reset',font=('Arial',12),width = 10,height =1,command = on_hit2 )
Button2.pack()

#设置显示
text = Text(tk,width = 30,height =20)
text.pack()

tk.mainloop()



