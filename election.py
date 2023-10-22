import mysql.connector
from tkinter import *
from PIL import Image,ImageTk
mydata=mysql.connector.connect(host='localhost',user='root',password='1234')
curs=mydata.cursor()
curs.execute('use election')
root=Tk()
root.geometry('1920x1080')


def check():
    #Gets values from Entry Box
    c=e1.get()
    c2=e2.get()
    for widget in f2.winfo_children():
        widget.destroy()

    #Fetching Voter names from Database
    curs.execute('select voters from blue_house')
    d=curs.fetchall()
    d2=''
    for  i in range(len(d)):
        for j  in range(len(d[i])): 
            d2=d2+d[i][j]

    #Checks the Validity of Code and Name Entered       
    if c2==''or c=='':
        if c=='':
            l2=Label(f2,text='Enter your code',bg='#00b8e6',font=('Calibri',15)).pack()
        else:
            l2=Label(f2,text='Enter your name',bg='#00b8e6',font=('Calibri',15)).pack()
    elif c.isalpha():
        l2=Label(f2,text='Invalid Input',bg='#00b8e6',font=('Calibri',15)).pack()
    elif c in d2:
        l2=Label(f2,text='You Cannot vote twice',bg='#00b8e6',font=('Calibri',15)).pack()
    elif not c[1:].isdigit():
        l2=Label(f2,text='Invalid Input',bg='#00b8e6',font=('Calibri',15)).pack()

    elif int(c[1:])>300 or int(c[1:]) <100:
        l2=Label(f2,text='Invalid Input',bg='#00b8e6',font=('Calibri',15)).pack()
    elif c[0]=='s' or c[0]=='S' and  (int(c[1:])>100 or int(c[1:])<300):                                                                                                                                                                                                                                                                                                                                                      
        vote()
    else:
        l2=Label(f2,text='Invalid Input',bg='#00b8e6',font=('Calibri',15)).pack()


def vote():
    #Values from Entry box
    x=e1.get()
    x2=e2.get()
    e1.delete(0,END)
    e2.delete(0,END)
    def cad1():
        #Using MySql to store voter id and votes count
        curs.execute('select names from blue_house where sl_no=1')
        a=curs.fetchall()
        a1=a[0][0]
        a2=a1+','+x2
        print('a2 ,',a2)
        curs.execute('select voters from blue_house where sl_no=1')
        y=curs.fetchall()
        y1=y[0][0]
        y1=y1+','+x
        print('y1 ',y1)
        
        #Updating the Database with voter's name and id
        curs.execute('update blue_house set voters=%s where sl_no=1',(y1,))
        curs.execute('commit')
        curs.execute('update blue_house set names=%s where sl_no=1',(a2,))
        curs.execute('commit')
        curs.execute('update blue_house set votes=votes+1 where sl_no=1')
        curs.execute('commit')
        top.destroy()
        
    def cad2():
        curs.execute('select names from blue_house where sl_no=2')
        a=curs.fetchall()
        a1=a[0][0]
        a2=a1+','+x2
        curs.execute('update blue_house set names=%s where sl_no=2',(a2,))
        curs.execute('commit')
        curs.execute('select voters from blue_house where sl_no=2')
        y=curs.fetchall()
        y1=y[0][0]
        y1=y1+','+x
        
        curs.execute('update blue_house set voters=%s where sl_no=2',(y1,))
        curs.execute('update blue_house set votes=votes+1 where sl_no=2')
        curs.execute('commit')
        top.destroy()
        
    
    def cad3():
        curs.execute('select names from blue_house where sl_no=3')
        a=curs.fetchall()
        a1=a[0][0]
        a2=a1+','+x2
        curs.execute('update blue_house set names=%s where sl_no=3',(a2,))
        curs.execute('commit')
        curs.execute('select voters from blue_house where sl_no=3')
        y=curs.fetchall()
        y1=y[0][0]
        y1=y1+','+x
        
        curs.execute('update blue_house set voters=%s where sl_no=3',(y1,))
        curs.execute('update blue_house set votes=votes+1 where sl_no=3')
        curs.execute('commit')
        top.destroy()
        
        
    def cad4():
        curs.execute('select names from blue_house where sl_no=4')
        a=curs.fetchall()
        a1=a[0][0]
        a2=a1+','+x2
        curs.execute('update blue_house set names=%s where sl_no=4',(a2,))
        curs.execute('commit')
        curs.execute('select voters from blue_house where sl_no=4')
        y=curs.fetchall()
        y1=y[0][0]
        y1=y1+','+x

        
        curs.execute('update blue_house set voters=%s where sl_no=4',(y1,))
        curs.execute('update blue_house set votes=votes+1 where sl_no=4')
        curs.execute('commit')
        top.destroy()

    
    #New Window (Window 2)
    #Voting Window
    top=Toplevel()
    top.geometry('1920x1080')
    labe1=Label(top,image=img2)
    labe1.place(x=0,y=0)
    x1=Label(top,text='Choose Your Candidate',bg='#00b8e6',font=('Calibri',18,'bold')).pack(pady=10)
    
    #Window 2 LabelFrame 1 
    f1=LabelFrame(top,text='Candidate 1',height=300,width=450,bg='#00b8e6',font=('Calibri',13))
    f11=LabelFrame(f1,text='',height=200,width=200)    #Label Frame for Image
    f11.place(x=40,y=10)
    
    i1=Image.open(r'C://Images  Floder//Blue//Bhuvan_Aradhya S.png')
    r1=i1.resize((200,200))
    i2=ImageTk.PhotoImage(r1)
    z1=Label(f11,image=i2)
    z1.place(x=0,y=0)
    
    l2=Label(f1,text='Bhuvan Aradhya S\nVII A',height=3,bg='#00b8e6',font=('Calibri',15,'bold'))
    b1=Button(f1,text='Vote',command=cad1,borderwidth=0.5,font=('Calibri',13),width=10)
    
    l2.place(x=260,y=40)
    b1.place(x=200,y=230)
    f1.place(x=200,y=100)

    #Window 2 LabelFrame 2
    f2=LabelFrame(top,text='Candidate 2',bg='#00b8e6',font=('Calibri',13),height=300,width=450)
    f22=LabelFrame(f2,text='',height=200,width=200)     #Label Frame for Image
    f22.place(x=40,y=10)
    
    i3=Image.open(r'C://Images  Floder//Blue//Yashas M Kashyap.jpg')
    r2=i3.resize((200,200))
    i4=ImageTk.PhotoImage(r2)
    z2=Label(f22,image=i4)
    z2.place(x=0,y=0)
    
    l3=Label(f2,text='Yashas M Kashyap\nVIII B',height=5,bg='#00b8e6',font=('Calibri',15,'bold'))
    b2=Button(f2,text='Vote',command=cad2,borderwidth=0.5,font=('Calibri',13),width=10)
    
    l3.place(x=260,y=40)
    b2.place(x=200,y=230)
    f2.place(x=640,y=100)
    
    #Window 2 LabelFrame 3
    f3=LabelFrame(top,text='Candidate 3',bg='#00b8e6',font=('Calibri',13),height=300,width=450)
    f33=LabelFrame(f3,text='',height=200,width=200)
    f33.place(x=30,y=10)
    
    i5=Image.open(r'C://Images  Floder//Blue//Maurya Vardhan M.png')
    r3=i5.resize((200,200))
    i6=ImageTk.PhotoImage(r3)
    z3=Label(f33,image=i6)
    z3.place(x=0,y=0)
    
    l4=Label(f3,text='Mauryavardhan M\n Aradhya\nVIII',height=5,bg='#00b8e6',font=('Calibri',15,'bold'))
    b3=Button(f3,text='Vote',command=cad3,borderwidth=0.5,font=('Calibri',13),width=10)
    
    l4.place(x=250,y=40)
    b3.place(x=200,y=230)
    f3.place(x=200,y=420)

    #Window 2 LabelFrame 4
    f4=LabelFrame(top,text='Candidate 4',height=300,width=450,bg='#00b8e6',font=('Calibri',13))
    f44=LabelFrame(f4,text='',height=200,width=200)
    f44.place(x=40,y=10)
    
    i7=Image.open(r'C://Images  Floder//Blue//Nakul S.png')
    r4=i7.resize((200,200))
    i8=ImageTk.PhotoImage(r4)
    z4=Label(f44,image=i8)
    z4.place(x=0,y=0)
    
    l5=Label(f4,text='Nakul S\nIX C',height=5,bg='#00b8e6',font=('Calibri',15,'bold'))
    b4=Button(f4,text='Vote',command=cad4,borderwidth=0.5,width=10,font=('Calibri',13))
    
    l5.place(x=260,y=40)
    b4.place(x=200,y=230)
    f4.place(x=640,y=420)
    
    top.mainloop()


def admin():
    def result():
        def view():
            c1=clicked.get()
            
            f=LabelFrame(top5,text='',font=('calibri',10),bg='#00b8e6')
            f.place(y=355,x=40)

            curs.execute('select name from blue_house')
            t1=curs.fetchall()
            i=0;h1=[]
            #Creates a list of names
            for i in range(len(t1)):
                h1.append(t1[i][0])

            #Displays Voter ids and names
            #Checks Candidate's name and name selected from dropdown menu
            if c1==h1[0]:
                l1=Label(f,text='Voter Id',font=('calibri',10),bg='#00b8e6')
                l1.pack()

                #Fetches all the voter ids and names
                curs.execute('select voters from blue_house where sl_no=1')
                t=curs.fetchall()
                l2=Label(f,text=t,font=('calibri',10),bg='#00b8e6')
                l2.pack()
                
                curs.execute('select names from blue_house where sl_no=1')
                r=curs.fetchall()
                l3=Label(f,text=r,font=('calibri',10),bg='#00b8e6')
                l3.pack()
                

            elif c1==h1[1]:
                l1=Label(f,text='Voter Id',font=('calibri',10),bg='#00b8e6')
                l1.pack()
                
                curs.execute('select voters from blue_house where sl_no=2')
                t=curs.fetchall()
                l2=Label(f,text=t,font=('calibri',10),bg='#00b8e6')
                l2.pack()
                
                curs.execute('select names from blue_house where sl_no=2')
                r=curs.fetchall()
                l3=Label(f,text=r,font=('calibri',10),bg='#00b8e6')
                l3.pack()

            elif c1==h1[2]:
                l1=Label(f,text='Voter Id',font=('calibri',10),bg='#00b8e6')
                l1.pack()
                
                curs.execute('select voters from blue_house where sl_no=3')
                t=curs.fetchall()
                l2=Label(f,text=t,font=('calibri',10),bg='#00b8e6')
                l2.pack()
                
                curs.execute('select names from blue_house where sl_no=3')
                r=curs.fetchall()
                l3=Label(f,text=r,font=('calibri',10),bg='#00b8e6')
                l3.pack()

            else:
                l1=Label(f,text='Voter Id',font=('calibri',10),bg='#00b8e6')
                l1.pack()
                
                curs.execute('select voters from blue_house where sl_no=4')
                t=curs.fetchall()
                l2=Label(f,text=t,font=('calibri',10),bg='#00b8e6')
                l2.pack()
                
                curs.execute('select names from blue_house where sl_no=4')
                r=curs.fetchall()
                l3=Label(f,text=r,font=('calibri',10),bg='#00b8e6')
                l3.pack()
                
        # result funtion 
       
        x1=Label(top5,text='Results',font=('calibri',15),bg='#00b8e6')
        x1.pack()

        #Fetching the candidate names and id
        curs.execute('select name,votes from blue_house ')
        d1=curs.fetchall()
        n=[];v=[]
        
        for i in range(len(d1)):
            n.append(d1[i][0])
            v.append(d1[i][1])

        #Loop to create a table
        for i in range(len(n)):
            h1=Entry(top5,width=30)
            h1.insert(END,n[i])
            h2=Entry(top5,width=30)
            h2.insert(END,v[i])
            h1.place(x=500,y=150+(i*20))
            h2.place(x=680,y=150+(i*20))

        #Displays Winner's name   
        curs.execute('select name,votes from  blue_house  order by votes desc')
        d1=curs.fetchone()
        x1=Label(top5,text='The Winner Is '+d1[0],font=('calibri',14),bg='#00b8e6')
        x1.place(x=580,y=250)
        
        d1=curs.fetchall()
        curs.execute('select name from blue_house')
        t1=curs.fetchall()
        i=0;h1=[]
        for i in range(len(t1)):
            h1.append(t1[i][0])
            
        #Code for a Dropdown Menu
        clicked=StringVar()
        clicked.set('Select a Candidate')
        drop=OptionMenu(top5,clicked,*h1)
        drop.place(x=600,y=300)
        b=Button(top5,text='Enter',command=view,borderwidth=0.5)
        b.place(x=660,y=330)

            
    def pswd():
        z1=e5.get()
        if z1=='2345':
            x=Label(top5,text='Access  granted',font=('calibri',15),bg='#00b8e6')
            x.pack()
            result()
        else:
            top5.destroy()

        
    top5=Toplevel()
    top5.geometry('1920x1080')
    p1=Label(top5,image=img2,bg='#00b8e6')  #Background image
    p1.place(x=0,y=0)
    
    p2=Label(top5,text='Enter The Password',font=('calibri',15),bg='#00b8e6')
    p2.pack(pady=10)
    e5=Entry(top5)
    e5.pack()
    b5=Button(top5,text='Enter',command=pswd,borderwidth=0.5)
    b5.pack()
    
    top5.mainloop()

#Code For Images
from PIL import Image,ImageTk
img=Image.open(r'C:\Images  Floder\image7.jpg')
img3=Image.open(r'C:\Images  Floder\SCS3.jpg')
resized=img.resize((1920,1080))
resized2=img3.resize((90,90))
img2=ImageTk.PhotoImage(resized)
img4=ImageTk.PhotoImage(resized2)
Label1=Label(root,image=img2,bg='#00b8e6')
Label1.place(x=0,y=0)

#Window 1 LabelFrame 2 (Images)
f1=LabelFrame(root,text='',width=100,height=200,bg='#00b8e6',font=('Calibri',15))
label2=Label(f1,image=img4,bg='#00b8e6')
label2.pack(padx=0,pady=5)

#Window 1 LabelFrame 1
image1=Image.open(r'C:\Images  Floder\blue_house3e.jpg')
image2=image1.resize((342,350))
image3=ImageTk.PhotoImage(image2)
f5=LabelFrame(root,text='',width=350,height=541,bg='#00b8e6',font=('Calibri',15))
label3=Label(f5,text='Blue House\n Vikram Sarabhai',bg='#00b8e6',font=('Calibri',16),fg='white')
label3.place(x=95,y=40)
label4=Label(f5,image=image3)
label4.place(x=0,y=105)
f5.place(x=390,y=120)

#Window 1 LabelFrame 1 (Buttons and text)
l1=Label(f1,text='Soundarya Central School\nHouse Election 2022-2023\n',bg='#00b8e6',font=('Calibri',16),fg='white')
l1.pack(pady=20)

l2=Label(f1,text='Enter your code',justify='left',bg='#00b8e6',font=('Calibri',15),fg='white')
l2.place(x=18,y=228)
e1=Entry(f1,width=45)
e1.pack(padx=20,pady=25)

l3=Label(f1,text='Enter your name',justify='left',bg='#00b8e6',font=('Calibri',15),fg='white')
l3.place(x=18,y=283)
e2=Entry(f1,width=45)
e2.pack(padx=20,pady=10)

b1=Button(f1,text='Enter',command=check,borderwidth=0.5,font=('Calibri'),width=10,activebackground='#ccccb3')
b1.pack(pady=10)

f2=LabelFrame(f1,text='',bg='#00b8e6',font=('Calibri',15),borderwidth=0)
l4=Label(f2,text='',bg='#00b8e6',font=('Calibri',15)).pack()
y=Button(root,text='',command=admin,borderwidth=0.5)
y.place(x=1240,y=670)
lab=Label(root,text='Developed by\nMonisha.J\nXII Science',bg='#46ddf5')

lab.place(x=1250,y=730)
f2.pack(pady=60)
f1.place(x=740,y=120)

root.mainloop()
