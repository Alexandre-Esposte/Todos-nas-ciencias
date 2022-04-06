from tkinter import *
import tk_tools
import serial
import time



def clique():
		
		ser = serial.Serial("/dev/ttyACM0",9600)
		arq= open("data", 'a')
		time.sleep(1.8)
		ser.write(b'a')
		temp = ser.readline()
		temp = temp.decode("utf-8")
		time.sleep(2)
		pres = ser.readline()
		pres = pres.decode("utf-8")
		volume=txt.get()
		txt.delete(0,5)
		vol.configure(text=f"Volume: {float(volume)} ml")
		volume=float(volume)
		volume=((volume+45.3))
		volume=str(volume)
		arq.write(temp+"		"+pres+"	"+volume+"\n")
		tempa.configure(text=f"Temperatura: {float(temp)} °C")
		pressao.configure(text=f"Pressão: {float(pres)} hPa")
		#plot(float(temp),float(volume))
		arq.close()
		ser.close()

	
	
largura = 600
altura = 400
janela= Tk()
janela.title("Projeto todos nas ciências")
janela.geometry('600x400')

frame_medidas = Frame(janela,bg = 'pink',height = altura, width = 0.35*largura)
frame_medidas.grid(columns = 1, row = 1)


lbl1=Label(frame_medidas,text='Informe o volume indicado na seringa:')
#lbl1.grid(column=0,row=0)


txt=Entry(frame_medidas,width=5)
#txt.grid(column=0,row=1)
txt.place(relx = 0.1,rely = 0.05)
txt.focus()

lbl=Label(frame_medidas,text='Aperte o botão para medir')
lbl.place(relx = 0.1,rely = 0.15)
#lbl.grid(column=0,row=2)


botao= Button(frame_medidas, text="Medir",command=clique)
botao.place(relx = 0.1,rely = 0.25)
#botao.grid(column=0,row=3)

vol=Label(frame_medidas,text="Volume: ")
vol.place(relx = 0.1,rely = 0.35)
#vol.grid(column=0,row=4)

tempa=Label(frame_medidas,text="Temperatura: ")
tempa.place(relx = 0.1,rely = 0.45)
#tempa.grid(column=0,row=5)

pressao=Label(frame_medidas,text="Pressão: ")
pressao.place(relx = 0.1,rely = 0.55)
#pressao.grid(column=0,row=6)



janela.mainloop()

