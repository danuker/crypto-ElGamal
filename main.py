# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 18:11:59 2014

@author: dan
"""

import Tkinter as tk
import tkMessageBox
from algorithm import *



class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.lettersLabel = tk.Label(self, text="Alphabet:")
        self.lettersLabel.grid()
        self.lettersTxt = tk.Entry(self) # Allowed letters
        self.lettersTxt.grid(column=1, row=0, sticky=tk.W )
        self.lettersTxt.insert(0, alphabet)
        self.lettersTxt.config(width=50)
        
                
        self.pubpLabel = tk.Label(self, text="Public key p:")
        self.pubpLabel.grid()
        self.pubpTxt = tk.Entry(self)
        self.pubpTxt.grid(column=1, row=1)
        self.pubpTxt.config(width=150)
        
        self.pubgLabel = tk.Label(self, text="Public key g:")
        self.pubgLabel.grid()
        self.pubgTxt = tk.Entry(self)
        self.pubgTxt.grid(column=1, row=2)
        self.pubgTxt.config(width=150)        
        
        self.pubgaLabel = tk.Label(self, text="Public key g^a:")
        self.pubgaLabel.grid()
        self.pubgaTxt = tk.Entry(self)
        self.pubgaTxt.grid(column=1, row=3)
        self.pubgaTxt.config(width=150)        
        
        self.privLabel = tk.Label(self, text="Private key:")
        self.privLabel.grid()
        self.privTxt = tk.Entry(self)
        self.privTxt.grid(column=1, row=4)
        self.privTxt.config(width=150)        
        
        self.plainLabel = tk.Label(self, text="Plaintext:")
        self.plainLabel.grid()
        self.plainTxt = tk.Entry(self)
        self.plainTxt.grid(column=1, row=5)
        self.plainTxt.insert(0, 'testing')
        self.plainTxt.config(width=150)

        self.cipherLabel = tk.Label(self, text="Ciphertext:")
        self.cipherLabel.grid()
        self.cipherTxt = tk.Entry(self)
        self.cipherTxt.grid(column=1, row=6)
        self.cipherTxt.config(width=150)
        
        self.encButton = tk.Button(self, text='Encrypt', command=self.encrypt)
        self.encButton.grid(column=0, sticky=tk.E)
        self.decButton = tk.Button(self, text='Decrypt', command=self.decrypt)
        self.decButton.grid(column=1, row=7, sticky=tk.W )
        self.genButton = tk.Button(self, text='Generate', command=self.gen_keys)
        self.genButton.grid(column=0, row=8, sticky=tk.E )
        self.bitTxt = tk.Entry(self)
        self.bitTxt.grid(column=1, row=8, sticky=tk.W )
        self.bitTxt.insert(0, '128')
        
    def gen_keys(self):
        try:
            if self.bitTxt.get() == '':
                return tkMessageBox.showerror('Keygen', 'Enter number of bits.')
            self.crypto_keys = get_keys(int(self.bitTxt.get()))
            self.pubpTxt.insert(0, str(self.crypto_keys['public'][0]))
            self.pubgTxt.insert(0, str(self.crypto_keys['public'][1]))
            self.pubgaTxt.insert(0, str(self.crypto_keys['public'][2]))
            self.privTxt.insert(0, str(self.crypto_keys['private']))

            self.crypto_keys['public'] = (int(self.pubpTxt.get()),
                                          int(self.pubgTxt.get()), 
                                          int(self.pubgaTxt.get()))
            self.crypto_keys['private'] = (int(self.privTxt.get()))
        except ValueError:
            tkMessageBox.showerror('Keygen', 'Enter number of bits.')
    def encrypt(self):
        if any((self.pubpTxt.get()=='',
               self.pubgTxt.get()=='', 
               self.pubgaTxt.get()=='')):
                   return tkMessageBox.showerror('Encryption error', 'Missing key. Please generate.')
               
        try:
            # alphabet = self.lettersTxt.get()
            self.crypto_keys['public'] = (int(self.pubpTxt.get()),
                                          int(self.pubgTxt.get()), 
                                          int(self.pubgaTxt.get()))

            cipher = encrypt(self.crypto_keys['public'] , self.plainTxt.get())
            formatted_cipher = ', '.join([str(a) + ' '+str(b) for a,b in cipher])
            self.cipherTxt.delete(0, len(self.cipherTxt.get()))
            self.cipherTxt.insert(0, formatted_cipher)
        except ValueError as e:
            tkMessageBox.showerror('Encryption error', e.message)
    def decrypt(self):
        if self.privTxt.get()=='':
            return tkMessageBox.showerror('Encryption error', 'Missing key. Please generate.')
        
        try:
            # Read the keys
            self.crypto_keys['private'] = (int(self.privTxt.get()))
            # Read the ciphertext
            parsed_cipher = []
            formatted_cipher = self.cipherTxt.get().split(',')
            for cipher in formatted_cipher:
                alpha, beta = cipher.strip().split(' ')
                parsed_cipher.append((long(alpha), long(beta)))
            
            plaintext = decrypt(self.crypto_keys,
                                parsed_cipher)
            self.plainTxt.delete(0, len(self.plainTxt.get()))
            self.plainTxt.insert(0, plaintext)
        except ValueError as e:
            tkMessageBox.showerror('Encryption error', e.message)
    
app = Application()
app.master.title('El Gamal - Dan Haiduc & Brent Nibbe')
app.mainloop()
