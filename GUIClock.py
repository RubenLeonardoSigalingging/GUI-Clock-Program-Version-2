#!/usr/bin/env python3


# IMPORT MODULE.
import os
from os import system
system("clear")
system("pip install tk")
system("pip install pyfiglet")
system("chmod 777 GUIClock.py")
system("clear")
import tkinter
from tkinter import *
import time
from time import asctime


# Use Your Imagination To Create Programs
def GUI_Clock_Program(Created_By="Ruben Leonardo Sigalingging"):
	from pyfiglet import figlet_format
	tampilan=figlet_format("GUIC",font="3-d")
	print(tampilan)
	print("[!] Dibuat Oleh: Ruben Leonardo Sigalingging.")
	print("[!] Dibuat Pada: Senin, 4 Juli, 2022, Pukul 21:51 PM.")
	print("[!] Menggunakan: Bahasa Pemrogramman Python Versi 3.8.10")
	print("[!] Pesan: Use Your Imagination To Create Programs.\n")


	# BUAT METODE TKINTER TERLEBIH DAHULU.
	tampilan_program=Tk()


	# BUAT TITLE ATAU JUDUL PROGRAM, MENGGUNAKAN METODE .TITLE()
	tampilan_program.title("GUI CLOCK PROGRAM")


	# UBAH WARNA LATAR BELAKANG PROGRAM, MENGGUNAKAN METODE .CONFIGURE(BG="")
	tampilan_program.configure(background="#000000",cursor="pirate")


	# UBAH UKURAN JENDELA ROOT TKINTER, DENGAN METODE .RESIZABLE(5,5)
	tampilan_program.resizable(width=True,height=True)


	# UBAH UKURAN GUI NYA, MENGGUNAKAN METODE .GEOMETRY()
	tampilan_program.geometry("500x500")


	# BUAT LABEL PROGRAM, MENGGUNAKAN METODE LABEL()
	# Label_Program=Label(tampilan_program,text="GUI CLOCK PROGRAM",font=("Ubuntu",25,"bold","italic"),background="#000000",foreground="#ff0000",cursor="crosshair",bd=25)
	# Label_Program.pack()


	# LABEL PROGRAM KE-2
	label=Label(tampilan_program,cursor="clock",font=("Ubuntu",25,"italic"),bg="#808080",fg="#00ffff",width=50,height=3)
	label.grid(row=3,column=3)
	label.pack()


	# BUAT FUNGSI LAGI.
	def GUI_Code(Created_By="Ruben Leonardo Sigalingging"):
		# string_waktu=strftime("%H:%M:%S")
		string_waktu=asctime()
		label.config(text=string_waktu)
		label.after(500,GUI_Code)
	if __name__ == '__main__':
		GUI_Code()


	# EXIT PROGRAM
	def Exit_Program(Created_By="Ruben Leonardo Sigalingging"):
		tampilan_program.quit()


	# KELUAR PROGRAM
	Exit=Button(tampilan_program,text="Exit",font=("Times",25,"italic"),background="darkcyan",fg="darkred",command=Exit_Program)
	if __name__ == '__main__':
		Exit.pack()


	# BUAT FUNGSI LAGI, UNTUK MENAMPUNG STRING TIME.

	# BUAT PROGRAM BERJALAN ATAU AKTIF TERUS, MENGGUNAKAN METODE .MAINLOOP()
	if __name__ == '__main__':
		tampilan_program.mainloop()


GUI_Clock_Program()