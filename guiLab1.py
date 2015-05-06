__author__ = 'dima'
from tkinter import *
root = Tk()


#----------------laba



ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def initLvl(one,two,three):
    one_resu = OneLvl(one)
    two_resu = TwoLvl(two)
    three_resu = ThreeLvl(three)
    four_resu = FourLvl(one,two)
    return one_resu, two_resu,three_resu,four_resu

def OneLvl(one):
    firsSymbol = one[len(one)-2]
    firsSymbol = ALPHABET.find(firsSymbol)
    firsSymbol = ALPHABET[firsSymbol-1]
    return firsSymbol

def TwoLvl(two):
    twoSymbol = two[len(two)-1]
    twoSymbol = ALPHABET.find(twoSymbol)
    twoSymbol = ALPHABET[twoSymbol+1]
    return twoSymbol

def ThreeLvl(three):
    threeSymbol = len(three) % 2 #1 - íå÷åòíîå
    if threeSymbol == 1:


        krat = three[len(three)//2]
        threeSymbol = ALPHABET.find(krat)
        threeSymbol = ALPHABET[threeSymbol+2]

    if threeSymbol == 0:
        noKrat = three[3]
        threeSymbol = ALPHABET.find(noKrat)
        threeSymbol = ALPHABET[threeSymbol-1]

    return threeSymbol

def FourLvl(one,two):
    one = len(one)
    two = len(two)
    summ = one + two + 2
    fourSymbol = ALPHABET[summ]

    return fourSymbol




#---------------GUI



def output(event):
     s = ent.get()

     what = initLvl("Sony", "Hewlett", "Packard")
     corrPass = []
     for i in range(len(what)):
         check = what[i]
         if ALPHABET.find(check):
             corrPass.append(check)
         i+=1

     sep = ''

     corrPass = sep.join(corrPass)

     if s == corrPass:
          tex.delete(1.0,END)
          tex.insert(END,"пароль верен!")
     else:
          tex.delete(1.0,END)
          tex.insert(END,"пароль не верен или поле пусто")



ent = Entry(root, show="*", width=15)
but = Button(root,text="сравнить")
tex = Text(root,width=20,height=3,font="12",wrap=WORD)

ent.grid(row=0,column=0,padx=20)
but.grid(row=0,column=1)
tex.grid(row=0,column=2,padx=20,pady=10)
but.bind("<Button-1>",output)

root.mainloop()