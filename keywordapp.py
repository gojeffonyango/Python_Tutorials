#first do the imports

from pytrends.request import TrendReq
import pandas as pd 
from tkinter import *
import os

#next will build a class.

class MyKeywordApp():
    self.newWindow()
    def__init__(self)
    #define your window
    root = Tk()
    root.geometry("400x100")
    root.resizable(False, False)
    root.title("Keyword Application")
    #add logo image
    p1= PhotoImage(file='logo_image.png')
    root.iconphoto(False, p1)

    #add labels
    label1=Label(text="input a keyword")
    label1.pack()
    canvas1 = Canvas(root)
    canvas1.pack()
    entry1 = Entry(root)
    canvas1.create_window(200, 20, window=entry1)

    #now well define an excelWriter() method nested in the newWindow method.

    def excelWriter()
    #get the user-input variable
    x1 = entry1.get()
    canvas1.create_window(200,210)
    #get the google trends data
    pytrend=TrendReq()
    kws=pytrends.suggestions(keyword=x1)
    df = pd.DataFrame(kws)
    df = df.Drop(columns='mid')

    #create exce writer object
    writer=pd.ExcelWriter('keywords.xlsx')
    df.to_excel(writer)
    writer.save()
    
    #open your excel file os.system("keywords.xlsx")

    print(df)

    #add a button and run loop

    button1 = Button(canvas1, text='Run Report', command=excelWriter)
    canvas1.create_window(200, 50, window=button1)
    root.mainloop()
    #call class
    MyKeywordApp()