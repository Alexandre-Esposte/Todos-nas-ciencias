from cgitb import text
import tkinter as tk
from tkinter import ttk
from turtle import width
import tk_tools
import serial
import time
import matplotlib.pyplot as plt

ser=0 # variavel global
volume_graf = []
pressao_graf = []

def plotar():
    plt.title("Grafico pressão versus volume")
    plt.scatter(volume_graf,pressao_graf)  
    plt.xlabel("Volume (mL)")
    plt.ylabel("Pressao (HPA)")
    plt.savefig("grafico.png")
    img = tk.PhotoImage(file="/home/uff/Área de Trabalho/todos na ciencia/grafico.png") 
    grafico.configure(image=img)
    grafico.imagem = img
  
    return

def medir():
    global volume_graf,pressao_graf
    time.sleep(1.8)
    ser.write('m'.encode('utf-8'))
    volume = float(volume_entry.get().replace(',','.'))+45.3
    vol_var.set(f"Volume (mL): {volume}")
    time.sleep(1.8)
    temperatura = ser.readline()
    temperatura = temperatura.decode('utf-8')
    temp_var.set(f"Temperatura (°C): {temperatura}")
    time.sleep(1.8)
    pressao = ser.readline()
    pressao = pressao.decode('utf-8')
    pressao_var.set(f"Pressão (HPa): {pressao}")
    
    volume_graf.append(volume)
    pressao_graf.append(float(pressao))

    plotar()
    return

def desconectar():
    global ser

    if(ser != 0):
        time.sleep(1.8)
        ser.write('d'.encode('utf-8'))
        time.sleep(1.8)
        resposta = ser.readline()
        resposta = int(resposta.decode("utf-8"))
        if(resposta):
            texto_arduino.set('Arduino Desconectado')
            led.to_red(on=True)
            ser.write('n'.encode('utf-8'))
            ser.close()
    return

def conectar():

    global ser

    ser = serial.Serial("/dev/ttyACM0",9600,timeout=10)
    time.sleep(1.8)
    ser.write('c'.encode('utf-8'))
    time.sleep(1.8)
    resposta = ser.readline()
    resposta = int(resposta.decode("utf-8"))
    if(resposta):
        texto_arduino.set('Arduino conectado')
        led.to_green(on=True)
        ser.write('n'.encode('utf-8'))
    return


largura = 1000
altura = 600
janela= tk.Tk()

janela.title("Projeto todos nas ciências")
janela.geometry(f'{largura}x{altura}')

frame1 = tk.Frame(janela,height=35)
frame2 = tk.Frame(janela)
frame3 = tk.Frame(janela)
frame1.place(relx=0,rely=0,relwidth=1)
frame2.place(relx=0,y=50,relwidth=0.2,relheight=1)
frame3.place(relx =0.2,relheight=1,y=50,relwidth=1)

#--------- FRAME 1 ---------------
'''Este frame conterá os widgets e as funções para a conexão com o arduino'''

btn_conectar = tk.Button(frame1, text='Conectar arduino', command=conectar)
btn_conectar.place(relx = 0.62)

btn_desconectar = tk.Button(frame1,text='Desconectar arduino',command=desconectar)
btn_desconectar.place(relx=0.80)

led = tk_tools.Led(janela, size=25)
led.place(relx=0)
led.to_red(on=True)

texto_arduino = tk.StringVar()
texto_arduino.set("Arduino desconectado")
ard_label = tk.Label(frame1,textvariable = texto_arduino,pady=7)
ard_label.place(relx=0.05)
ttk.Separator(frame1, orient='horizontal').place(x=0,rely=0.95,relwidth=1)

#--------FRAME 2------------
ttk.Separator(frame2, orient='vertical').place(relheight=1,relx=0.9974)
volume_txt = tk.Label(frame2,text="Volume indicado")
volume_entry_var = tk.StringVar()
volume_entry = tk.Entry(frame2,width=10,textvariable=volume_entry_var)
volume_txt.pack()
volume_entry.pack()

massa_txt = tk.Label(frame2,text='Massa no embolo')
massa_entry_var= tk.StringVar()
massa_entry = tk.Entry(frame2,width=10,textvariable=massa_entry_var)
massa_txt.pack(pady=10)
massa_entry.pack()

tk.Label(frame2,text='\n').pack()
ttk.Separator(frame2, orient='horizontal').pack(fill=tk.X)
tk.Label(frame2,text='Medidas').pack()
ttk.Separator(frame2, orient='horizontal').pack(fill=tk.X)

temp_var = tk.StringVar()
temp_var.set("Temperatura (°C): None")
temp_txt = tk.Label(frame2,textvariable=temp_var,pady=30)
temp_txt.pack()

pressao_var = tk.StringVar()
pressao_var.set("Pressão (HPa): None")
pressao_txt = tk.Label(frame2,textvariable=pressao_var,pady=30)
pressao_txt.pack()

vol_var = tk.StringVar()
vol_var.set("Volume (mL): None")
vol_txt = tk.Label(frame2,textvariable=vol_var,pady=30)
vol_txt.pack()

btn_medir = tk.Button(frame2,text='Medir',command=medir)
btn_medir.place(relx=0.05,rely=0.8,relheight=0.1,relwidth=0.9)

# ----------- Frame 3 ---------------------
grafico = tk.Label(frame3)
grafico.place(relx=0,rely=0)

janela.mainloop()