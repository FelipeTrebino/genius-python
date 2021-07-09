from tkinter import *
from random import *
from tkinter import messagebox
import winsound 

class Jogo(Frame):
    def __init__(self,janela,d):
        self.contador = 0
        Frame.__init__(self,janela)
        self.janela = janela
        janela.title("Genius")
        janela.geometry("600x480")
        janela.resizable(width=False,height=False)
        self.listajogada = []
        self.listaatual = []

#Adicionar as fotos
       
        self.grid(row=0, column=0)
        self.verde = PhotoImage(file="PART_VERDE.gif")
        self.amarelo = PhotoImage(file="PART_AMARELA.gif")
        self.vermelho = PhotoImage(file="PART_VERMELHA.gif")
        self.azul =  PhotoImage(file="PART_AZUL.gif")
        self.verde2 = PhotoImage(file="PART_VERDE_2.gif")
        self.amarelo2 = PhotoImage(file="PART_AMARELA_2.gif")
        self.vermelho2 = PhotoImage(file="PART_VERMELHA_2.gif")
        self.azul2 =  PhotoImage(file="PART_AZUL_2.gif")
        self.dificuldade = d
        self.botoes = []
        self.contadorbotoes = 0
        if(self.dificuldade == 1):
            dif ="Fácil"
        if(self.dificuldade == 2):
            dif ="Médio"
        if(self.dificuldade == 3):
            dif ="Difícíl"
                        
        
#Colocar os botões na janela
        
        for i in range(2):
            linha = []
            for j in range(2):
                botao = Button(self,image=self.verde,command=lambda x=i,y=j:self.botaoadd(x,y))
                botao.grid(row=i,column=j)
                linha.append(botao)
            self.botoes.append(linha)
        self.botoes[0][1]["image"] = self.vermelho     
        self.botoes[1][0]["image"] = self.amarelo
        self.botoes[1][1]["image"] = self.azul
#Criar botão start
        botao = Button(self,text="Start",width=15,height=5,command=self.start)
        botao.grid(row=0,column=2)
        botao['background'] = "red"
        linha.append(botao)
        
#Botão que indica que rodada o jogador está
        
        botao = Label(self,text="Rodada\n"+str(self.contador+1),width=15,height=5)
        botao.place(x=495,y=400)
        linha.append(botao)
        self.rodada = botao

#Botão que indica que dificuldade o jogador está

        botao = Label(self,text="Dificuldade:\n"+str(dif),width=15,height=5)
        botao.place(x=495,y=0)
        linha.append(botao)
        self.dificuldader = botao

#Sorteador da lista de botões que vão piscar de acordo com o nível        

        if(self.dificuldade == 1):
            x = sample(range(1,1000),10)
            self.listafacil = []
            for n in x:
                self.listafacil.append(n%4+1)                
            for x in self.listafacil:
                self.listaatual=self.listafacil[:]
                
        if(self.dificuldade == 2):
            x = sample(range(1,1000),20)
            self.listamedio = []
            for n in x:
                self.listamedio.append(n%4+1)                
            for x in self.listamedio:
                self.listaatual=self.listamedio[:]
                
        if(self.dificuldade == 3):
            x = sample(range(1,1000),30)
            self.listadificil = []
            for n in x:
                self.listadificil.append(n%4+1)                
            for x in self.listadificil:
                self.listaatual=self.listadificil[:]
            

#Função que adiciona os botoes clicados pelo jogador, e os adicionam em uma lista

    def botaoadd(self,i,j):
        if (i==0 and j==0):
            self.listajogada.append(1)
            self.comparar()
        elif (i==0 and j==1):
            self.listajogada.append(2)
            self.comparar()
        elif (i==1 and j==0):
            self.listajogada.append(3)
            self.comparar()
        else:
            self.listajogada.append(4)
            self.comparar()
            
#Função que faz os botões apagarem
            
    def piscar2(self,args):
        if(args==1):           
            self.botoes[0][0]["image"] = self.verde
        if(args==2):
            self.botoes[0][1]["image"] = self.vermelho
        if(args==3):
            self.botoes[1][0]["image"] = self.amarelo
        if(args==4):
            self.botoes[1][1]["image"] = self.azul
            
#Função que faz os botões piscarem

    def piscar3(self,args):
        if(args==1):           
            self.botoes[0][0]["image"] = self.verde2
          #  self.beep = winsound.Beep(500,900)
        if(args==2):
            self.botoes[0][1]["image"] = self.vermelho2
        if(args==3):
            self.botoes[1][0]["image"] = self.amarelo2
        if(args==4):
            self.botoes[1][1]["image"] = self.azul2

#Função piscar
            
    def piscar(self,args):
        i=0
        
        self.rodada["text"] ="Rodada\n"+str(self.contador+1)
        
        for x in self.listaatual[0:self.contador+1]:

            i+=1000

         
            self.janela.after(i,lambda j=x:self.piscar3(j))
            self.janela.after(i+900,lambda j=x:self.piscar2(j))
            
        self.contador+=1
        
#Função que inicia com botão de start, que inicia o jogo
            
    def start(self):
        self.listajogada = []  
        self.piscar(self.listaatual)

#Comparar se as a lista de jogadas é igual ou não à predefinida

    def comparar(self):

        self.contadorbotoes+=1


        if(self.contadorbotoes == len(self.listaatual)):
            if(self.listajogada == self.listaatual[0:self.contador]):
                messagebox.showinfo("Parabéns!","Você ganhou\n\nJogo por:\nFelipe Trebino\nJúlia Caminha\nSâmek Novaes\nAna Caroline Gassi")
            else:
                messagebox.showinfo("Fim de Jogo","Você perdeu\n\nJogo por:\nFelipe Trebino\nJúlia Caminha\nSâmek Novaes\nAna Caroline Gassi")
                
        elif(self.contadorbotoes == self.contador):
            if(self.listajogada == self.listaatual[0:self.contador]):
                self.contadorbotoes = 0
                self.listajogada = []              
                self.piscar(self.listaatual)
            else:                
                messagebox.showinfo("Fim de Jogo","Você perdeu\n\nJogo por:\nFelipe Trebino\nJúlia Caminha\nSâmek Novaes\nAna Caroline Gassi")

        else:
             if(self.listajogada != self.listaatual[0:self.contadorbotoes]):
                 messagebox.showinfo(messagebox.showinfo("Fim de Jogo","Você perdeu\nJogo por:\n\nFelipe Trebino\nJúlia Caminha\nSâmek Novaes\nAna Caroline Gassi"))

#Escolher a dificuldade
           
class Aplicacao(Frame):
    def __init__(self,janela):
        Frame.__init__(self,janela)
        janela.title("Dificuldade")
        self.pack()
        botaoFacil = Button(text="Fácil",width=30,height=2,command=self.facil)
        botaoMedio = Button(text="Médio",width=30,height=2,command=self.medio)
        botaoDificil = Button(text="Difícil",width=30,height=2,command=self.dificil)
        botaoFacil.pack()
        botaoFacil['background'] = "green"
        botaoMedio.pack()
        botaoMedio['background'] = "yellow"
        botaoDificil.pack()
        botaoDificil['background'] = "red"

    def facil(self):
        j = Toplevel()
        d = 1
        app = Jogo(j,1)
        app.mainloop()
    def medio(self):
        j = Toplevel()
        d = 2
        app = Jogo(j,2)
        app.mainloop()
    def dificil(self):
        j = Toplevel()
        d = 3
        app = Jogo(j,3)
        app.mainloop()
       
g = Tk()
app = Aplicacao(g)
app.mainloop()
