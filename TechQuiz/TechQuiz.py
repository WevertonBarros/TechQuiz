#Bibliotecas necessárias para o funcionamento do programa:
from tkinter import *
import random
import pygame

#Declaração de variáveis globais:
imagem = ''
pontoFinal = 0 #Pontuação final do usuário
nome = '' #Nome do usuário
acertos = 0 #Quantas questões o usuário acertou.
tamanho_perguntas = 0 #Variável para saber se o usuário acertou o número máximo de questões
posicao = 0 #Variável que escolhe qual a linha da matriz de perguntas será lida
perguntas = []#Variável que carrega o arquivo de perguntas.

#Definição da janela e suas propriedades.
janela = Tk()
janela.title("TECH QUIZ")
janela.geometry("1280x720")

def menu(): #tela de menu
    
    imagem_menu()    
    
    bt4 = Button(janela,text='Fechar',width=15,bg="blue",command = fecha,font="arial 40").place(x=100,y=510)
    
    bt2 = Button(janela,text='Rank',width=15,bg="blue",command = ranking,font="arial 40").place(x=100,y=440)
    
    bt3 = Button(janela,text='Sobre',width=15,bg="blue",command = sobre,font="arial 40").place(x=100,y=370)
    
    bt1 = Button(janela,text='Jogar',width=15,bg="blue",command = comeca,font="arial 40").place(x=100,y=300)

    pygame.init()
    pygame.mixer_music.load("sounds/msc01.mp3")
    pygame.mixer_music.play(loops=-1)
    
#################################################################################################################################################

#Esta função inicia o quiz.
def comeca(): 
    
    reset_janela()
    
    arquivo = open('questoes.txt', 'r', encoding="utf-8") #carregando o arquivo na matriz perguntas
    
    global perguntas
    
    global tamanho_perguntas
    
    for i in range(20):  #cada é linha um conjunto de perguntas e alternativas
    
        perguntas.append([])
    
        for j in range(5):
    
            perguntas[i].append(arquivo.readline())
    
            perguntas[i][j] = perguntas[i][j].replace('\n','')
    
    arquivo.close() 
    
    random.shuffle(perguntas) #Aleatoriza as questões
    
    tamanho_perguntas = len(perguntas)  #Variável para saber se o usuário acertou o número máximo de questões

    pygame.init()   #musica do menu
    pygame.mixer_music.load("sounds/msc02.mp3")
    pygame.mixer_music.play(loops=10)
    
    random_pergunta()
#########################################################################################################################################################

#Esta função tem a finalidade de "limpar" o conteúdo da janela.
def reset_janela():
    
    global imagem    
    
    imagem = PhotoImage(file="pictures/img03.png")
    
    lbimagem = Label(image = imagem)
    
    lbimagem.place(x=-1,y=-1)
#########################################################################################################################################################


def random_pergunta(): #escolhe pergunta
    
    global perguntas
    
    global posicao
    
    global correta  
    
    correta = perguntas[posicao][4] #A resposta correta sempre será a alternativa 4. este é um padrão para quem for alterar o arquivo.
    
    lb = Label(janela,text='{}'.format(perguntas[posicao][0]),width = 100,font="arial 20",bg="black",fg="blue")
    
    lb.place(x=-5,y=100)

    
    lista = [1,2,3,4]
    
    alterna = random.sample(lista,4) #embaralha alternativas
    
    bt0 = Button(janela,width=40,height=2,text='{}'.format(perguntas[posicao][alterna[0]]),bg="blue", command=lambda:click_bt(bt0['text']))
    bt0.place(x=500,y=300)
    bt1 = Button(janela,width=40,height=2,text='{}'.format(perguntas[posicao][alterna[1]]),bg="blue",command=lambda:click_bt(bt1['text']))
    bt1.place(x=500,y=350)
    bt2 = Button(janela,width=40,height=2,text='{}'.format(perguntas[posicao][alterna[2]]),bg="blue",command=lambda:click_bt(bt2['text']))
    bt2.place(x=500,y=400) 
    bt3 = Button(janela,width=40,height=2,text='{}'.format(perguntas[posicao][alterna[3]]),bg="blue",command=lambda:click_bt(bt3['text']))
    bt3.place(x=500,y=450)
    
    posicao +=1
##############################################################################################################################################################

#Esta função avalia a resposta do usuário
def click_bt(botao):
    
    global resp
    global acertos
    global correta
    global tamanho_perguntas
    global posicao
    global pontoFinal
    resp = botao
    
    if resp == correta:
    
        acertos += 1

        pontoFinal = acertos #Precisamos distinguir pontoFinal de acertos porque precisamos zerar acertos para uma nova rodada.
    
    if resp != correta or acertos == tamanho_perguntas: 
    
        fim_jogo()
    
    else:
    
        reset_janela()
    
        random_pergunta()
###########################################################################################################################################################

#função que encerra a partida e pede o nome do usuário
def fim_jogo():
    
    reset_janela()
    
    global imagem

    global acertos
    
    global tamanho_perguntas
    
    global entrada

    
    if acertos == tamanho_perguntas:
        
        imagem = PhotoImage(file="pictures/img05.png")
        
        lbimagem = Label(image = imagem)
        
        lbimagem.place(x=-1,y=-1)

        pygame.init()
        pygame.mixer_music.load("sounds/msc04.mp3")
        pygame.mixer_music.play()
        
    
    else:
    
        imagem = PhotoImage(file="pictures/img04.gif")
        
        lbimagem = Label(image = imagem)
        
        lbimagem.place(x=-1,y=-1)
        
        lbc =  Label(janela,text="Errooooooou , Como você é burro!",font = 'arial 5',bg="black",fg="red").place(x=270,y=250)

        pygame.init()
        pygame.mixer_music.load("sounds/msc03.mp3")
        pygame.mixer_music.play(loops=10)
    
    
    acertos = 0 #zerando acertos para uma possível nova rodada
    
    entrada = Entry(janela,bg="gray",fg="black")
    
    entrada.place(x=700,y=500) #entrada do nome do usuário
    
    btOk = Button(janela,text='Ok',bg="gray",width=2,command=preencheRank)

    lb = Label(janela,text="Digite seu nome :",bg="black",fg="gray",font="arial 15")
    lb.place(x=500,y=498)
    
    btOk.place(x=870,y=500)
    
    bt_menu()
#############################################################################################################################################################

#Função que cria um botão para voltar ao menu principal
def bt_menu():
    
    bt_menu = Button(janela,width=20,command = click_menu,bg="blue",text = "Menu").place(x=1200,y=1)
    
    acertos = 0
    
    qualquer = 0
###################################################################################################################################################################################

#Função que retorna ao menu inicial
def click_menu():
    
    global janela
    
    global perguntas
    
    global posicao
    
    posicao = 0
    
    perguntas.clear()
    
    menu()
###################################################################################################################################################################################


#Esta função é chamada para adicionar ao arquivo do ranking, os novos nome e pontuação do usuário assim que este encerra a partida
def preencheRank():
    
    global nome
    
    global pontoFinal
    
    nome = entrada.get() #nome recebe a entrada escrita pelo usuário
    
    arquivo = open('ranking.txt','a',encoding="utf-8") #Preenchimento do arquivo no modo append
    
    arquivo.write(nome)
    
    arquivo.write('\n')
    
    arquivo.write(str(pontoFinal))
    
    arquivo.write('\n')
    
    arquivo.close()
    
    menu()
###################################################################################################################################################################################

#Função que exibe informações ao usuário quanto à finalidade do jogo.
def sobre():
    
    reset_janela()
    
    global imagem    
    
    imagem = PhotoImage(file="pictures/img02.png")
    
    lbimagem = Label(image = imagem)
    
    lbimagem.place(x=-1,y=-1)
    
    lb = Label(janela,text='Programa escrito em python\npara a disciplina introdução à programação.\n\nProfessor: Francisco Simões\n\nAlunos: J. Weverton Barros e Alysson P. Assunção\n\nSoundtracks: Tetris Theme,Mario Bros.(Gameover)\nZelda ALTTP (prologue theme),gonna fly now(8 bit cover)',bg = "black",fg = "blue",font="arial 20")
    lb.place(x=370,y=250)
    lb1 = Label(janela,text="Sobre :",font = "arial 30",bg="black",fg="blue")
    lb1.place(x=340,y=25)

    bt_menu()
#########################################################################################################################################################

#Ao escolher o botão rank do menu, o usuário vê a partir desta função, os 5 melhores jogadores.
def ranking():
    
    reset_janela()
    
    global imagem    
    
    imagem = PhotoImage(file="pictures/img02.png")
    
    lbimagem = Label(image = imagem)
    lbimagem.place(x=-1,y=-1)
    
    primeiros = '' #Variável que carrega o texto com os melhores jogadores
    
    
    lista = []
    
    x = [] #Variável que recebe o conteúdo do arquivo linha por linha para saber o número de linhas do arquivo
    with open ('ranking.txt','r') as arquivo:
        x = arquivo.readlines()
    
    arquivo = open('ranking.txt','r', encoding="utf-8")
    
    for i in range(len(x)//2): #x//2 pois supondo que o arquivo tem 10 linhas, 5 são para nome e 5 para pontuação.
    
        lista.append([])
    
        for j in range(2):
    
            lista[i].append(arquivo.readline())
    
            lista[i][j] = lista[i][j].replace('\n','')
            
    
    arquivo.close()
    
    lista = sorted(lista, key=lambda a_entry: a_entry[1], reverse=True) #Função que sorteia em ordem decrescente, a lista com os dados do arquivo de ranking
                                                              #a_entry define o índice que será comparado de cada linha da matriz. reverse para por em ordem decrescente
    
    arquivo = open ('ranking.txt','w',encoding='utf-8') #aqui, reeescrevemos o arquivo de ranking, pois não nos interessa guardar abaixo da quinta colocação.
    
    for i in range(len(x)//2):
    
        for j in range(2):
    
            arquivo.write(lista[i][j])
    
            arquivo.write('\n')
            
            if i == 4 and j == 1: #se já estamos no quinto colocado (i==4) e em sua pontuação (j==1), não é necessário guardar mais nada. 
                break
    
    arquivo.close()
    
    arquivo = open('ranking.txt','r',encoding='utf-8') #aqui, finalmente lemos o ranking atualizado para exibir ao usuário
    
    for i in range (1,6):
    
        primeiros += str(i)+'º lugar: '+arquivo.readline()+' Pontuação: '+arquivo.readline()+'\n'
    
    arquivo.close()
    
    lb1 = Label(janela,text="Ranking :",font = "arial 30",bg="black",fg="blue")
    
    lb1.place(x=340,y=25)
    
    lab = Label(janela,text=primeiros,bg="black",fg="blue",font = "arial 13")
    
    lab.place(x=370,y=210)
    
    bt_menu()
#########################################################################################################################################################


def fecha():
    janela.destroy() #comando para fechar o programa
########################################################################################################################################################

#função que define a imagem do menu
def imagem_menu():
    
    global imagem
    
    imagem = PhotoImage(file="pictures/img01.png")
    
    lbimagem = Label(image = imagem)
    
    lbimagem.place(x=-1,y=-1)
    

#########################################################################################################################################################


#início do programa chanando o menu e iniciando a janela.
menu()

janela.mainloop()