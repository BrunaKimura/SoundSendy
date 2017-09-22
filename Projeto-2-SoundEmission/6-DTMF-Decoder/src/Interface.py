0##Criado por Leonardo Medeiros
import tkinter as tk
import time
from datetime import datetime
import tkinter.messagebox as tkm
from PIL import ImageTk
from PIL import Image
from tkinter import filedialog
import Encoder
import Decoder 


class Janela_Principal():
    
    def __init__(self):
        
        self.app_config = dict()
        self.app_config['width_button'] = 97
        self.app_config['height_button'] = 125
        self.app_config['window_xpos'] = 100
        self.app_config['window_ypos'] = 100
        
        window_width = 3 * self.app_config['width_button']
        window_height = 4 * self.app_config['height_button']

        self.window = tk.Tk()
        self.window.geometry("{}x{}+{}+{}".format(window_width, 
                                                  window_height, 
                                                  self.app_config['window_xpos'], 
                                                  self.app_config['window_ypos']))
        self.window.title("sOundSendy")
        self.window.resizable(False, False)
    
        # Geometria da pagina
        self.window.rowconfigure(0, minsize = window_height)
        self.window.columnconfigure(0, minsize = window_height)
        
        # Menu Principal
        self.menu_principal = Menu_Principal(self)
    
        #Emissor
        self.emissor_window = Emissor_window(self)
    
        #Receptor
        self.receptor_window = Receptor_window(self)
    
        # Iniciar menu
        self.menu_principal.mostrar()
                
    def mostrar_emissor(self):
        self.emissor_window.mostrar()
        
    def mostrar_receptor(self):
        self.receptor_window.mostrar()
        
    def iniciar(self):
        self.window.mainloop()

class Menu_Principal():
    
    def __init__(self, janela_principal):
        
        self.janela_principal = janela_principal
        self.window1 = tk.Frame(self.janela_principal.window)
        self.window1.grid(row = 0, column = 0, sticky = "nsew")
        self.window1.configure(background = 'white')
        
        # Geometria da pagina        
        self.window1.rowconfigure(0, minsize = 95)
        self.window1.rowconfigure(1, minsize = 50)
        self.window1.rowconfigure(2, minsize = 100)
        self.window1.rowconfigure(3, minsize = 50)
        self.window1.rowconfigure(4, minsize = 100)
        
        self.window1.columnconfigure(0, minsize = 280)
                
        self.Logo = ImageTk.PhotoImage(Image.open("./interface_imgs/Logo.png"))
        self.Logo_label = tk.Label(self.window1,image = self.Logo, height = 4, width = 30)
        self.Logo_label.grid(row = 0, column = 0, sticky = "nsew")
        
        self.button_Emissor = tk.Button(self.window1, text = "Encoder",background = "#90caf9", height = 4, width = 30)        
        self.button_Emissor.grid(row = 2, column = 0)
        self.button_Emissor.configure(command = self.rodaEmissor)

        self.button_Receptor = tk.Button(self.window1, text = "Decoder",background = "#90caf9", height = 4, width = 30)        
        self.button_Receptor.grid(row = 4, column = 0)
        self.button_Receptor.configure(command = self.rodaReceptor)

    def mostrar(self):
        self.window1.tkraise()
    
    def rodaReceptor(self):
        self.janela_principal.mostrar_receptor()
        
    def rodaEmissor(self):
        self.janela_principal.mostrar_emissor() 


class Emissor_window():
    
    def __init__(self, janela_principal):
        
        self.janela_principal = janela_principal
        self.window2 = tk.Frame(self.janela_principal.window)
        self.window2.grid(row = 0, column = 0, sticky = "nsew")

        self.window2.rowconfigure(0, minsize = self.janela_principal.app_config['height_button'])
        self.window2.rowconfigure(1, minsize = self.janela_principal.app_config['height_button'])
        self.window2.rowconfigure(2, minsize = self.janela_principal.app_config['height_button'])
        self.window2.rowconfigure(3, minsize = self.janela_principal.app_config['height_button'])

        self.window2.columnconfigure(0, minsize = self.janela_principal.app_config['width_button'])
        self.window2.columnconfigure(1, minsize = self.janela_principal.app_config['width_button'])
        self.window2.columnconfigure(2, minsize = self.janela_principal.app_config['width_button'])

        self.image1 = ImageTk.PhotoImage(file="./interface_imgs/blue_1.png")
        self.botao1 = tk.Button(self.window2,image = self.image1, padx=(0), pady = (0))
        self.botao1.grid(row = 0, column = 0, sticky="nsew")
        self.botao1.configure(command = self.botao_clicado1)
        
        self.image2 = ImageTk.PhotoImage(file="./interface_imgs/blue_2.png")
        self.botao2 = tk.Button(self.window2,image = self.image2, padx=(0), pady = (0))
        self.botao2.grid(row = 0, column = 1, sticky="nsew")
        self.botao2.configure(command = self.botao_clicado2)
        
        self.image3 = ImageTk.PhotoImage(file="./interface_imgs/blue_3.png")
        self.botao3 = tk.Button(self.window2,image = self.image3, padx=(0), pady = (0))
        self.botao3.grid(row = 0, column = 2, sticky="nsew")
        self.botao3.configure(command = self.botao_clicado3)
        
        self.image4 = ImageTk.PhotoImage(file="./interface_imgs/blue_4.png")
        self.botao4 = tk.Button(self.window2,image = self.image4, padx=(0), pady = (0))
        self.botao4.grid(row = 1, column = 0, sticky="nsew")
        self.botao4.configure(command = self.botao_clicado4)
        
        self.image5 = ImageTk.PhotoImage(file="./interface_imgs/blue_5.png")
        self.botao5 = tk.Button(self.window2,image = self.image5 ,padx=(0), pady = (0))
        self.botao5.grid(row = 1, column = 1, sticky="nsew")
        self.botao5.configure(command = self.botao_clicado5)
        
        self.image6 = ImageTk.PhotoImage(file="./interface_imgs/blue_6.png")
        self.botao6 = tk.Button(self.window2,image = self.image6, padx=(0), pady = (0))
        self.botao6.grid(row = 1, column = 2, sticky="nsew")
        self.botao6.configure(command = self.botao_clicado6)
        
        self.image7 = ImageTk.PhotoImage(file="./interface_imgs/blue_7.png")
        self.botao7 = tk.Button(self.window2,image = self.image7, padx=(0), pady = (0))
        self.botao7.grid(row = 2, column = 0, sticky="nsew")
        self.botao7.configure(command = self.botao_clicado7)
        
        self.image8 = ImageTk.PhotoImage(file="./interface_imgs/blue_8.png")
        self.botao8 = tk.Button(self.window2,image = self.image8, padx=(0), pady = (0))
        self.botao8.grid(row = 2, column = 1, sticky="nsew")
        self.botao8.configure(command = self.botao_clicado8)

        self.image9 = ImageTk.PhotoImage(file="./interface_imgs/blue_9.png")
        self.botao9 = tk.Button(self.window2,image = self.image9, padx=(0), pady = (0))
        self.botao9.grid(row = 2, column = 2, sticky="nsew")
        self.botao9.configure(command = self.botao_clicado9)

        self.image0 = ImageTk.PhotoImage(file="./interface_imgs/blue_0.png")
        self.botao0 = tk.Button(self.window2,image = self.image0, padx=(0), pady = (0))
        self.botao0.grid(row = 3, column = 1, sticky="nsew")
        self.botao0.configure(command = self.botao_clicado0)

        self.le_imagens()
        
        self.canvas = tk.Canvas(self.window2, width = self.janela_principal.app_config['width_button'], 
                                              height = self.janela_principal.app_config['height_button'])
        self.canvas.configure(bg = "white", highlightthickness = 0)
        self.canvas.grid(row = 3, column = 0)


        self.canvas2 = tk.Canvas(self.window2, width = self.janela_principal.app_config['width_button'],
                                               height = self.janela_principal.app_config['height_button'])
        self.canvas2.configure(bg = "white", highlightthickness = 0)
        self.canvas2.grid(row = 3, column = 2)

        self.window2.after(0, self.animacao)


    def le_imagens(self):
        self.lista_imagens = []
        for i in range(1,18):
            self.lista_imagens.append(tk.PhotoImage(file ='./gifs/image{0}.gif'.format(i)))
        print(self.lista_imagens)
        
    def animacao(self):        
        self.canvas.delete(tk.ALL)

        for j in self.lista_imagens:
            self.canvas.create_image(100//2, 140//2,image = j)
            self.canvas2.create_image(100//2, 140//2,image = j)
            self.canvas.update()
            time.sleep(0.1)
            
        self.window2.after(0, self.animacao)


    def botao_clicado1(self):
        Encoder.main(675,1209)

    def botao_clicado2(self):
        Encoder.main(675,1336)
    
    def botao_clicado3(self):
        Encoder.main(675,1477)
    
    def botao_clicado4(self):
        Encoder.main(770,1209)
    
    def botao_clicado5(self):
        Encoder.main(770,1336)
    
    def botao_clicado6(self):
        Encoder.main(770,1477)
    
    def botao_clicado7(self):
        Encoder.main(852,1209)
    
    def botao_clicado8(self):
        Encoder.main(852,1336)
    
    def botao_clicado9(self):
        Encoder.main(852,1477)
    
    def botao_clicado0(self):
        Encoder.main(941,1336)

    def mostrar(self):
        self.window2.tkraise()
        


class Receptor_window():
    
    def __init__(self, janela_principal):
        
        self.janela_principal = janela_principal
        self.window2 = tk.Frame(self.janela_principal.window)
        self.window2.grid(row = 0, column = 0, sticky = "nsew")
        self.window2.configure(background = 'white')
        
        # Geometria da pagina        
        self.window2.rowconfigure(0, minsize = 95)
        self.window2.rowconfigure(1, minsize = 50)
        self.window2.rowconfigure(2, minsize = 100)
        self.window2.rowconfigure(3, minsize = 50)
        self.window2.rowconfigure(4, minsize = 100)
        
        self.window2.columnconfigure(0, minsize = 280)
                
        self.Logo = ImageTk.PhotoImage(Image.open("./interface_imgs/Logo.png"))
        self.Logo_label = tk.Label(self.window2,image = self.Logo, height = 4, width = 30)
        self.Logo_label.grid(row = 0, column = 0, sticky = "nsew")
        
        self.button_Carregar_arquivo = tk.Button(self.window2, text = "Carregar Arquivo",background = "#90caf9", height = 4, width = 30)        
        self.button_Carregar_arquivo.grid(row = 2, column = 0)
        self.button_Carregar_arquivo.configure(command = self.Carregar)

        self.button_fly = tk.Button(self.window2, text = "On-the-fly",background = "#90caf9", height = 4, width = 30)        
        self.button_fly.grid(row = 4, column = 0)
        self.button_fly.configure(command = self.On_tfly)
    
    def mostrar(self):
        self.window2.tkraise()
    
    def Carregar(self):
        filename = filedialog.askopenfilename()
        Decoder.main(filename)
    
    def On_tfly(self):
        Decoder.main("1")
    
app = Janela_Principal()
app.iniciar()