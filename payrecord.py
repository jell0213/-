# -*- coding: utf-8 -*-
#還沒改分析的時候


from skimage import io
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from Tkinter import *
import time 
import ttk
window = Tk()
window.title('記帳')
window.geometry('1000x1000')
now = 0
cat=[u'食物',u'飲品',u'交通',u'消費',u'娛樂',u'居家',u'3C',u'醫藥',u'其他']
catspend=[0,0,0,0,0,0,0,0,0]
def callback(event):
    f = open("acc_data.txt",'a')  
    y = mcombo.get()
    m = mcombo1.get()
    d = mcombo2.get()
    if y and m and d:
        y = mcombo.get()
        m = mcombo1.get()
        d = mcombo2.get()
        date=y+'/'+m+'/'+d
        text.delete(0,'end')
        text2.delete(0,'end')
        text3.delete(0,'end')
        text4.delete(0,'end')
        text5.delete(0,'end')
        spend['text']=0
        for line in f:
            str=line[:-1]
            if date in str:
                p=str.split(',',5)
                text3.insert(0,p[0])
                text4.insert(0,p[1].decode('utf-8'))
                text.insert(0,p[3].decode('utf-8'))
                text2.insert(0,p[4])
                text5.insert(0,p[2].decode('utf-8'))
                spend['text']+=int(p[4])
    f.close()
mcombolist = ['2018','2019','2020']
mcombo = ttk.Combobox(window, values=mcombolist )
mcombo['width']=4
mcombo.bind('<<ComboboxSelected>>', callback)
mcombo.grid(row=1,column=0)
mcombolist1 = ['1','2','3','4','5','6','7','8','9','10','11','12']
mcombo1 = ttk.Combobox(window, values=mcombolist1 )
mcombo1['width']=4
mcombo1.bind('<<ComboboxSelected>>', callback)
mcombo1.grid(row=2,column=0)
mcombolist2 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
mcombo2 = ttk.Combobox(window, values=mcombolist2 )
mcombo2['width']=4
mcombo2.bind('<<ComboboxSelected>>', callback)
mcombo2.grid(row=3,column=0)
mcombolist3 = ['食物','飲品','交通','消費','娛樂','居家','3C','醫藥','其他']
mcombo3 = ttk.Combobox(window, values=mcombolist3 )
mcombo3['width']=4
mcombo3.grid(row=2,column=1)
######for 分析
mcombolistf = ['2018','2019','2020']
mcombof = ttk.Combobox(window, values=mcombolistf )
mcombof['width']=4
mcombof.grid(row=8,column=0)
mcombolist1f = ['1','2','3','4','5','6','7','8','9','10','11','12']
mcombo1f = ttk.Combobox(window, values=mcombolist1f )
mcombo1f['width']=4
mcombo1f.grid(row=9,column=0)
mcombolist2f = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
mcombo2f = ttk.Combobox(window, values=mcombolist2f )
mcombo2f['width']=4
#mcombo2f.bind('<<ComboboxSelected>>', callback)
mcombo2f.grid(row=10,column=0)
#############
mcombolistt = ['2018','2019','2020']
mcombot = ttk.Combobox(window, values=mcombolistt )
mcombot['width']=4
mcombot.grid(row=8,column=1)
mcombolist1t = ['1','2','3','4','5','6','7','8','9','10','11','12']
mcombo1t = ttk.Combobox(window, values=mcombolist1t )
mcombo1t['width']=4
mcombo1t.grid(row=9,column=1)
mcombolist2t = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
mcombo2t = ttk.Combobox(window, values=mcombolist2t )
mcombo2t['width']=4
#mcombo2t.bind('<<ComboboxSelected>>', callback)
mcombo2t.grid(row=10,column=1)
#############
i=0
l=[]
rec = []
recnum = 0
def input():
    i = e.get()
    j = money.get()
    y = mcombo.get()
    m = mcombo1.get()
    d = mcombo2.get()
    cate=mcombo3.get()
    s = shop.get()
    x = 0
    try:
        f=int(j)        
    except ValueError:
        x = 1
    if i and j and y and m and d and cate and x == 0:
        text.insert(0,i)
        text2.insert(0,j)
        date=y+'/'+m+'/'+d
        text3.insert(0,date)
        text4.insert(0,cate)
        text5.insert(0,s)
        f = open("acc_data.txt", "a")     
        #f.write(date) 
        strr=date+','+cate+','+s+','+i+','+j+'\n'
        strrr=strr.encode('utf-8')
        f.write(strrr)  
        f.close()
        money.delete(0,'end')  
        e.delete(0,'end')
        shop.delete(0,'end')
        result['text'] ='輸入成功'
        spend['text']+=int(j)
    else :          
        result['text'] = '名稱和金錢都要輸入' 
        if x == 1:
            result['text'] = '請輸入數字'            
def analysis():
    catspend=[0,0,0,0,0,0,0,0,0]
    f = open("acc_data.txt",'r')  
    for line in f:
        str=line[:-1]
        p=str.split(',',5)
        for i in range(9):
            if p[1].decode('utf-8')==cat[i]:
                catspend[i]+=int(p[4])
                print catspend
                break
    #print catspend
    plt.figure(figsize=(6,6)) #大小
    colors = ['red','yellowgreen','lightskyblue','yellow','orange','blue','#33ffbb','#008fb3','#ff66ff'] 
    explode = (0,0,0,0,0,0,0,0,0) 
    patches,text1,text2 = plt.pie(catspend,
                          explode=explode,
                          labels=cat,
                          colors=colors,
                          autopct = '%3.2f%%', #保留固定位
                          shadow = False, 
                          startangle =90, 
                          #pctdistance = 0.6
                          ) 
    
    plt.axis('equal')
    plt.legend()
    
    plt.savefig('pie.png') #一定放在plt.show()之前
    '''
    bm=io.imread('pie.png')
    labelima = Label(window,
                         image='pie.png',
                         text='diu',        
                         font=('Arial', 8),
                         bd = 2,
                         relief=GROOVE,
                         width=50,height=50
                         )
    labelima.grid(row = 12 , column = 0)
    
    
    img_gif = io.imread('pie.png')  
    label_img = Label(window, image = img_gif)  
    label_img.grid(row = 6 , column = 3,columnspan=4,rowspan=15)
    window.mainloop()
    '''
    
    '''
    root = Tk()  
    root.title('程序窗口')       
    root.geometry('600x600')
    bm=io.imread('pie.gif')  
    label_img = Label(root, image = bm)  
    label_img.grid(row=0,column=0)
    root.mainloop()  
    '''
    plt.show()
    f.close()
i = 0
result = Label(window, 
text='',        
font=('Arial', 8),
bd = 2,
relief=GROOVE,
width=18, height=1 
)
result.grid(row = 2 , column = 6)

today = Label(window, 
text='今日已花費 : ',        
font=('Arial', 8),
bd = 2,
relief=GROOVE,
width=15, height=1 
)
today.grid(row = 5 , column = 0)


optionLabel1 = Label(window, 
text='日期',        
font=('Arial', 8),
bd = 2,
relief=GROOVE,
width=15, height=1 
)
optionLabel1.grid(row = 0 , column = 0)

optionLabel2 = Label(window, 
text='類別',        
font=('Arial', 8),
bd = 2,
relief=GROOVE,
width=15, height=1 
)
optionLabel2.grid(row = 0 , column = 1)

optionLabel3 = Label(window, 
text='項目',        
font=('Arial', 8),
bd = 2,
relief=GROOVE,
width=15, height=1 
)
optionLabel3.grid(row = 0 , column = 3)

optionLabel4 = Label(window, 
text='價錢',        
font=('Arial', 8),
bd = 2,
relief=GROOVE,
width=15, height=1 
)
optionLabel4.grid(row = 0 , column = 4)

optionLabel5 = Label(window, 
text='店家',        
font=('Arial', 8),
bd = 2,
relief=GROOVE,
width=15, height=1 
)
optionLabel5.grid(row = 0 , column = 2)

anal = Label(window, 
text='花費分析',        
font=('Arial', 16),
bd = 2,
relief=GROOVE,
width=8, height=2
)
anal.grid(row = 6 , column = 0)

fromdate = Label(window,
text='起始日期',        
font=('Arial', 8),
bd = 2,
relief=GROOVE,
width=15, height=1 
)
fromdate.grid(row = 7 , column = 0)

tilldate = Label(window,
text='結束日期',        
font=('Arial', 8),
bd = 2,
relief=GROOVE,
width=15, height=1 
)
tilldate.grid(row = 7 , column = 1)

spend = Label(window, 
text=0,        
font=('Arial', 8),
bd = 2,
relief=GROOVE,
width=10, height=1 
)
spend.grid(row = 5 , column = 1)

lb=Button(window,                              #按鈕
    text='輸入',        
    font=('Arial', 12),      
    bd = 2,
    command=input,
    relief=RAISED,
    width=4, height=1  
    )
lb.grid(row=2,column=5)

def clean():
    f = open("acc_data.txt", "w")        
    f.close()
    text.delete(0,'end')
    text2.delete(0,'end')
    text3.delete(0,'end')
    text4.delete(0,'end')
    text5.delete(0,'end')
    
ob=Button(window,                              #按鈕
    text='清除資料',        
    font=('Arial', 12),      
    bd = 2,
    command=clean,
    relief=RAISED,
    width=8, height=1  
    )
ob.grid(row=9,column=5)

ana=Button(window,                              #按鈕
    text='開始分析',        
    font=('Arial', 12),      
    bd = 2,
    command=analysis,
    relief=RAISED,
    width=8, height=1  
    )
ana.grid(row=9,column=2)

shop=Entry(window,       #店家(可不填)
    font=('Arial', 12),      
    bd = 2,
    relief=RAISED,
    width=8
    )
shop.grid(row=2,column=2)

e=Entry(window,             #品項  
    font=('Arial', 12),      
    bd = 2,
    relief=RAISED,
    width=8
    )
e.grid(row=2,column=3)

money=Entry(window,       #價錢
    font=('Arial', 12),      
    bd = 2,
    relief=RAISED,
    width=8
    )
money.grid(row=2,column=4)

text = Listbox(window)
text.grid(row=4,column=3)
text2 = Listbox(window)
text2.grid(row=4,column=4)
text3 = Listbox(window)
text3['width']=12
text3.grid(row=4,column=0)
text4 = Listbox(window)
text4['width']=7
text4.grid(row=4,column=1)
text5 = Listbox(window)
text5['width']=12
text5.grid(row=4,column=2)

window.resizable(0,0)
window.mainloop()