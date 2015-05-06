__author__ = 'admin'
from os.path import join
from array import array
import operator
from numpy.core.multiarray import where
import numpy as np
from tkinter import *
class App(Frame):
    def __init__(self, master):
        super(App,self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        self.lbl = Label(self, text = "enter pass: ")
        self.lbl.grid(row = 0,column = 0, columns = 2, sticky = W)

        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 0, column = 1, sticky = W)

        self.buttn = Button(self, text = "ok", command = self.reveal)
        self.buttn.grid(row = 2, column = 0, sticky = W)

        self.buttn2 = Button(self, text = "clear", command = self.clear)
        self.buttn2.grid(row = 2, column = 1, sticky = W)

        self.secret_txt = Text(self, width = 100, height = 100, wrap = WORD)
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def clear(self):
        self.secret_txt.delete(0.0,END)
    def reveal(self):

        word_need = self.pw_ent.get()
        word_need = word_need.lower()
        ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
        word_need = word_need.replace(' ', '')
        word_need_len = len(word_need)

        c = np.array([
            ['a', 'b', 'c', 'd', 'e', 'f'],
            ['g', 'h', 'i', 'j', 'k', 'l'],
            ['m', 'n', 'o', 'p', 'q', 'r'],
            ['s', 't', 'u', 'v', 'w', 'x'],
            ['y', 'z', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-']
        ])

        for i in word_need:
           if word_need_len != 0:
                #поиск по индексу
                index_old = ALPHABET.find(i) + 1
                #формирование нового индекса -  атбаш
                index_new = len(ALPHABET) - index_old
                new_word_atbash = ALPHABET[index_new]
                #print(new_word_atbash,end="|")
                #формирование цезаря
                index_old = ALPHABET.find(new_word_atbash) + 1
                new_word = ALPHABET[index_old - 2]

                print(new_word,end="")

                #создание полибия
                a = where(c == new_word)
                first = a[0]+1
                two = a[1]+1

                result_pol="буква - " + new_word + " её координаты - " + str(first)+str(two)+"\n"

                self.secret_txt.insert(0.0, result_pol,"\n")

                word_need_len -= 1



root = Tk()
root.title("lol")
root.geometry("800x800")

App = App(root)
root.mainloop()
