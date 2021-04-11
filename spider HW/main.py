# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:26:46 2021

@author: Jinye He
"""

import tkinter as tk
import utils

for i in range(10):
    #get new fiction information and package them in to new_fiction
    url = utils.find_newbook(i)
    item = utils.book('','',0,'')
    #initialize
    item.info(url)
    if i==0:
        new_fiction = [item]
    else:
        new_fiction.append(item)
        
for i in range(10):
    #get new fiction information and package them in to new_nonfic
    url = utils.find_newbook(20+i)
    item = utils.book('','',0,'')
    #initialize
    item.info(url)
    if i==0:
        new_nonfic = [item]
    else:
        new_nonfic.append(item)

for i in range(10):
    #get new fiction information and package them in to pop_fiction
    url = utils.find_popularbook(i)
    item = utils.book('','',0,'')
    #initialize
    item.info(url)
    if i==0:
        pop_fiction = [item]
    else:
        pop_fiction.append(item)
        
for i in range(10):
    #get new fiction information and package them in to pop_nonfic    
    url = utils.find_popularbook(i + 10)
    item = utils.book('','',0,'')
    #initialize
    item.info(url)
    if i==0:
        pop_nonfic = [item]
    else:
        pop_nonfic.append(item)



a = 1


def helptxt():
    #set the helpwindow
    helpwin = tk.Tk()
    helpwin.title('HELP')
    helpwin.geometry('1000x400')
    helpwin.wm_resizable(False,False)
    txt = '''
      There are some book news from book.douban.com.
      
      Choose the tpye and book name and Click the button,
      
      There are its author, grade and introduction of the book.
      '''
      #content of help
    content = tk.Label(helpwin, text = txt, fg = 'black', font = ('Arial',14),anchor="w", justify="left")
    content.pack()
    helpwin.mainloop()
    
    
def getindex(listbox):
    #to get index of item selected and return index, if none of them selected, return -1
    for i in range(10):
        if listbox.selection_includes(i) == True:
            return i
    return -1

def showintro():
    #according to the index and type to show the introduction in the Text
    index = getindex(lb[var.get() - 1])
    #get index
    if index == -1:
        tk.messagebox.showwarning(title='Wrong!', message='Please choose right type!!')   
    else:
        text_intro.delete('1.0','end')
        if var.get() == 1:
            txt = '\\'.join(['《'+new_fiction[index].name+'》',new_fiction[index].author,new_fiction[index].grade])+'\n'+new_fiction[index].introduction
        elif var.get() == 2:
            txt = '\\'.join(['《'+new_nonfic[index].name+'》',new_nonfic[index].author,new_nonfic[index].grade])+'\n'+new_nonfic[index].introduction
        elif var.get() == 3:
            txt = '\\'.join(['《'+pop_fiction[index].name+'》',pop_fiction[index].author,pop_fiction[index].grade])+'\n'+pop_fiction[index].introduction
        elif var.get() == 4:
            txt = '\\'.join(['《'+pop_nonfic[index].name+'》',pop_nonfic[index].author,pop_nonfic[index].grade])+'\n'+pop_nonfic[index].introduction
        #choose the right type
        text_intro.insert('end',txt)
      
      

window = tk.Tk()
window.title('BOOK NEWS')
window.geometry('1000x600')
window.wm_resizable(False,False)
#set main window


menubar = tk.Menu(window)
menubar.add_command(label = "Help", command = helptxt)
window.config(menu = menubar)
#set the menubar

headline = tk.Label(window, text = 'BOOK NEWS',bg = 'black', fg = 'white', font = ('Arial',28,'bold'), width = 30, height = 2)
headline.pack()
#set the headline

type_l_1 = tk.Label(window, text = 'New Fiction',bg = 'white', fg = 'black', font = ('Arial',15,'italic'), width = 18, height = 1).place(x=10, y=100, anchor='nw')
type_l_2 = tk.Label(window, text = 'New Non-fiction',bg = 'white', fg = 'black', font = ('Arial',15,'italic'), width = 18, height = 1).place(x=260, y=100, anchor='nw')
type_l_3 = tk.Label(window, text = 'Popular Fiction',bg = 'white', fg = 'black', font = ('Arial',15,'italic'), width = 18, height = 1).place(x=510, y=100, anchor='nw')
type_l_2 = tk.Label(window, text = 'Popular Non-fiction',bg = 'white', fg = 'black', font = ('Arial',15,'italic'), width = 18, height = 1).place(x=760, y=100, anchor='nw')
#set the subhead

list_1 = tk.Listbox(window,height=10,bg='whitesmoke',selectbackground='grey', bd=0,width=24,font=('Arial',13))
for item in new_fiction:
    list_1.insert('end','《'+item.name+'》')
list_1.place(x=10, y=150, anchor='nw')

list_2 = tk.Listbox(window,height=10,bg='white',selectbackground='grey', bd=0,width=24,font=('Arial',13))
for item in new_nonfic:
    list_2.insert('end','《'+item.name+'》')
list_2.place(x=260, y=150, anchor='nw')

list_3 = tk.Listbox(window,height=10,bg='whitesmoke',selectbackground='grey', bd=0,width=24,font=('Arial',13))
for item in pop_fiction:
    list_3.insert('end','《'+item.name+'》')
list_3.place(x=510, y=150, anchor='nw')

list_4 = tk.Listbox(window,height=10,bg='white',selectbackground='grey', bd=0,width=24,font=('Arial',13))
for item in pop_nonfic:
    list_4.insert('end','《'+item.name+'》')
list_4.place(x=760, y=150, anchor='nw')
#set four listbox to show book names

lb = [list_1,list_2,list_3,list_4]

var = tk.IntVar() 
op_1 = tk.Radiobutton(window, text='New Fiction', variable=var, value='1').place(x=760, y=390, anchor='nw')
op_2 = tk.Radiobutton(window, text='New Non-fiction', variable=var, value='2').place(x=760, y=420, anchor='nw')
op_3 = tk.Radiobutton(window, text='Popular Fiction', variable=var, value='3').place(x=760, y=450, anchor='nw')
op_4 = tk.Radiobutton(window, text='Popular Non-fiction', variable=var, value='4').place(x=760, y=480, anchor='nw')
#set the type option

button_intro = tk.Button(window,text = 'get introduction',bg = 'white', fg = 'black', font = ('Arial',15,'italic'), width = 18, height = 1, command = showintro).place(x=730,y=520)
#set the button, click it to show the introduction

text_intro = tk.Text(window,bg='white',selectbackground='grey',font = ('Arial',12),bd=0,width = 63,height = 10)
text_intro.insert('end','There are introductions...')
text_intro.place(x=130,y=390,anchor='nw')
#set the text used to show introdution

window.mainloop()
