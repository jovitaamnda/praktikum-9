# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 15:13:47 2022

@author: jovita amanda putri
"""

def data (a,b,c,d,e):
    file = open('Biodata kalian.txt' ,'w')
    file.write(f'''
Nama kalian { a }
Umur kalian { b }
Alamat kalian { c }
Email kalian { d } 
Dosen wali kalian { e }  ''')
    file.close()

def baca():
    file = open('Biodata kalian.txt' ,'r')
    text=file.read()
    print(text)
    file.close()
    
Nama_kalian=input('siapa nama mu? ')
Umur_kalian=input('berapa umur mu? ')
Alamat_kalian=input('dimana alamat mu? ')
Email_kalian=input('apa email mu? ')
Dosen_Wali=input('siapa dosen wali mu? ')

data(Nama_kalian, Umur_kalian, Alamat_kalian, Email_kalian, Dosen_Wali)
baca()