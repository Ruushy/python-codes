

from tkinter import *
import tkinter.messagebox

class application:
    def __init__(self , master):
        self.master = master
        self.password = Label(master , text = "fadlan gali pinkaga: " , font = 'arial 30 bold ')
        self.password.place(x = 200 , y = 50)
        self.passentry = Entry(master , width= 40 )
        self.passentry.place(x = 260 , y = 110)
        self.passbox = Button(master , text = "OK" ,width=20 , height=2 , fg = 'black' , bg = 'cyan' , command = self.passcheck)
        self.passbox.place(x = 290 , y =165 )
    def passcheck(self):
        self.passwo = '1234'
        if self.passentry.get() == self.passwo:
            
            self.password.destroy()
            self.passentry.destroy()
            self.passentry.destroy()
            self.passbox.destroy()

            self.dooro= Label(self.master , fg = 'steelblue', text = "fadlan dooro" , font='arial 25 bold')
            self.dooro.place(x= 250  , y = 40)
            
            self.haraaga = Label(self.master , text = "1: Haragaaga: " , font= 'arial 15 bold')
            self.haraaga.place(x = 260 , y = 90)

            self.kaarka = Label(self.master , text = "2: kaarka ku hadalka : " , font= 'arial 15 bold')
            self.kaarka.place(x = 260 , y = 120)

            self.bixi = Label(self.master , text = "3: Bixi biil : " , font= 'arial 15 bold')
            self.bixi.place(x = 260 , y = 150)

            self.evc = Label(self.master , text = "4: EVCPlus : " , font= 'arial 15 bold')
            self.evc.place(x = 260 , y = 180)

            self.warbixin = Label(self.master , text = "5: Warbixin kjooban: " , font= 'arial 15 bold')
            self.warbixin.place(x = 260 , y = 210)

            self.salaam = Label(self.master , text = "6: Salaambank " , font= 'arial 15 bold')
            self.salaam.place(x = 260 , y = 240)

            self.maaraynta = Label(self.master , text = "7:maaraynta : " , font= 'arial 15 bold')
            self.maaraynta.place(x = 260 , y = 270)

            self.taaj = Label(self.master , text = "8: Taaj : " , font= 'arial 15 bold')
            self.taaj.place(x = 260 , y = 300)

            self.pay = Label(self.master , text = "9: Bill payment: " , font= 'arial 15 bold')
            self.pay.place(x = 260 , y = 330)

            self.second = Entry(self.master , width = 20 )
            self.second.place(x = 280 , y = 370)

            self.evpox = Button(self.master , text = "submit" , bg = 'cyan' , width = 15 , command = self.adeeg)
            self.evpox.place(x = 290 , y = 400)
            


            
        elif self.passentry.get() == "":
            tkinter.messagebox.showinfo("", "fadlan gali pinka ")
        else :
            tkinter.messagebox.showinfo("ERROR", "pinkaga waa khalad")
    def destroying(self):
            self.dooro.destroy()
            self.haraaga.destroy()
            self.kaarka.destroy()
            self.bixi.destroy()
            self.evc.destroy()
            self.warbixin.destroy()
            self.salaam.destroy()
            self.maaraynta.destroy()
            self.taaj.destroy()
            self.pay.destroy()
            self.second.destroy()
            self.evpox.destroy()

    def adeeg(self):
        self.b = self.second.get()
        self.b = int(self.b)

        if self.b == 1:
            self.destroying()
            Label(self.master , text="haraagagu waa 200" , font = 'arial 40 bold' , fg = 'steelblue').place(x = 250 , y = 100)
        elif self.b == 2:
            self.destroying()
            self.kushubo = Label(self.master , text = "ku shubo" , font = "arial 20 bold " )
            self.kushubo.place(x = 260 , y = 100)
            self.ugushubo = Label(self.master , text = "ugu shubo" , font = "arial 20 bold " )
            self.ugushubo.place(x = 260 , y = 130)
            self.kaar = Entry(self.master , width = 20)
            self.kaar.place(x= 270 , y = 180)
            self.kaarpox = Button(self.master , text = 'submit' , bg = 'cyan' , fg = 'black' , width = 15 , command = self.checkaar)
            self.kaarpox.place(x= 270 , y = 210)
        elif self.b == 4:
            self.destroying()
            self.num4 = Label(self.master , text = "fadlan gali numberka aad u warejineyso"  , font = 'arial 15 bold').place(x = 260 , y = 90)
            self.lacag4 = Entry(self.master , width = 20 )
            self.lacag4.place(x = 270 , y = 130)
            self.num5 = Label(self.master , text = "fadlan gali lacagta "  , font = 'arial 15 bold').place(x = 260 , y = 170)
            self.lacag5= Entry(self.master , width = 20 )
            self.lacag5.place(x = 270 , y = 200)
            self.lacagpox4 = Button(self.master , text = "submit" , bg = 'cyan' , width = 15 , command = self.evcplus)
            self.lacagpox4.place(x = 270 , y = 250)
            






    def checkaar(self):
        self.kaar_hubi = self.kaar.get()
        self.kaar_hubi = int(self.kaar_hubi)

        if self.kaar_hubi == 1:
            self.kushubo.destroy()
            self.ugushubo.destroy()
            self.kaar.destroy()
            self.kaarpox.destroy()
            Label(self.master , text = "fadlan gali lagta aad ku shubaneyso"  , font = 'arial 15 bold').place(x = 260 , y = 90)
            self.lacag = Entry(self.master , width = 20 )
            self.lacag.place(x = 270 , y = 130)
            self.lacagpox = Button(self.master , text = "submit" , bg = 'cyan' , width = 15 , command = self.kushubasho)
            self.lacagpox.place(x = 270 , y = 160)
        
        elif self.kaar_hubi == 2:
            self.kushubo.destroy()
            self.ugushubo.destroy()
            self.kaar.destroy()
            self.kaarpox.destroy()
            self.num1 = Label(self.master , text = "fadlan gali numberka aad u warejineyso"  , font = 'arial 15 bold').place(x = 260 , y = 90)
            self.lacag1 = Entry(self.master , width = 20 )
            self.lacag1.place(x = 270 , y = 130)
            self.num2 = Label(self.master , text = "fadlan gali lacagta "  , font = 'arial 15 bold').place(x = 260 , y = 170)
            self.lacag2 = Entry(self.master , width = 20 )
            self.lacag2.place(x = 270 , y = 200)
            self.lacagpox1 = Button(self.master , text = "submit" , bg = 'cyan' , width = 15 , command = self.tuurid)
            self.lacagpox1.place(x = 270 , y = 250)

            
        elif self.kaar_hubi == "":
            tkinter.messagebox.showinfo(" " , "fadlan dooro number 1")
        else :
            tkinter.messagebox.showinfo(" " , "invalid number")
            root.destroy()
    def tuurid(self):
        self.tuurid = self.lacag1.get()
        self.tuurid1 = self.lacag2.get()

        if self.tuurid == "" :
            tkinter.messagebox.showinfo(" " , "fadlan gali lacagta ama numberka ")
        elif self.tuurid1 == "":
            tkinter.messagebox.showinfo(" " , "fadlan gali lacagta ama numberka ")
        else:
            res = tkinter.messagebox.askquestion(" ma hubtaa" , " in lactan warejiso")
            if res == "yes":
                tkinter.messagebox.showinfo("mahadsanid" , "howshada waa laguu qabtay")
                root.destroy()
            else :
                root.destroy()

    def kushubasho(self):
       self.kush = self.lacag.get()
       self.kush = int(self.kush)

       if self.kush == "":
          tkinter.messagebox.showinfo(" " , "fadlan gali lacagta ")
       elif self.kush > 300:
         tkinter.messagebox.showinfo(" " , "lacagtas badan lama gudbin karo")
         
       else :
          rest = tkinter.messagebox.askquestion(" ma hubtaa" , " in lacgtan ku shubato")
          if rest == "yes":
              tkinter.messagebox.showinfo("mahadsanid" , "howshada waa laguu qabtay")
              root.destroy()
          else :
              root.destroy()
    def evcplus(self):
        self.tuurid4 = self.lacag4.get()
        self.tuurid5 = self.lacag5.get()
        

        if self.tuurid4 == "" :
            tkinter.messagebox.showinfo(" " , "fadlan gali lacagta ama numberka ")
        elif self.tuurid5 == "":
            tkinter.messagebox.showinfo(" " , "fadlan gali lacagta ama numberka ")
        else:
            res = tkinter.messagebox.askquestion(" ma hubtaa" , " in lacagtan warejiso")
            if res == "yes":
                tkinter.messagebox.showinfo("mahadsanid" , "howshada waa laguu qabtay")
                root.destroy()
            else :
                root.destroy()
        
                
        
            
            
    
            




root = Tk()
root.geometry("1350x750")
b = application(root)

root.mainloop()
