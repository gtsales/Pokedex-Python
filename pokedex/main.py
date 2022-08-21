from tkinter import *
from tkinter import ttk
from dados import *
from PIL import Image, ImageTk
#CORES USADAS NO PROJETO


co0 = "#010A09" #Preto
co1 = "#feffff" #Branco
co2 = "#6f9fbd" #Azul
co3 = "#38576b" #Valor
co4 = "#403d3d" #Letra
co5 = "#ef5350" #Vermelha
co6 = '#B1FEF3' #Azul bebê

#Criando a janela

janela = Tk()
janela.title('Pokedex')
janela.geometry('550x510')
janela.configure(bg=co6)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

#Criando frame

frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

def trocar_pokemon(i):#Trocar as informações dos pokemons

    global imagem_pokemon, pok_imagem

    #Trocando a cor de fundo
    frame_pokemon['bg'] = pokemon[i]['tipo'][3]

    #Trocando as informações do pokemon
    pok_nome['text'] = i
    pok_nome['bg'] = pokemon[i]['tipo'][3]
    pok_tipo['text'] = pokemon[i]['tipo'][1]
    pok_tipo['bg'] = pokemon[i]['tipo'][3]
    pok_id['text'] = pokemon[i]['tipo'][0]
    pok_id['bg'] = pokemon[i]['tipo'][3]

    imagem_pokemon = pokemon[i]['tipo'][2]

    #Imagem do pokemon

    imagem_pokemon = Image.open(imagem_pokemon)
    imagem_pokemon = imagem_pokemon.resize((238, 238))
    imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

    pok_imagem = Label(frame_pokemon, image=imagem_pokemon, relief='flat', bg=pokemon[i]['tipo'][3], fg=co0)
    pok_imagem.place(x=80, y=50)

    #Status
    pok_hp['text'] = pokemon[i]['status'][0]
    pok_ataque['text'] = pokemon[i]['status'][1]
    pok_defesa['text'] = pokemon[i]['status'][2]
    pok_velo['text'] = pokemon[i]['status'][3]
    pok_total['text'] = pokemon[i]['status'][4]

    #Habilidades
    pok_habi1['text'] = pokemon[i]['habilidades'][0]
    pok_habi2['text'] = pokemon[i]['habilidades'][1]

#Label nome

pok_nome = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 20'), bg=co1, fg=co0)
pok_nome.place(x=12, y=15)

#Label tipo

pok_tipo = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Yvi 10 bold'), bg=co1, fg=co0)
pok_tipo.place(x=12, y=50)

#Label id pokedex

pok_id = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Yvi 10 bold'), bg=co1, fg=co0)
pok_id.place(x=12, y=90)

#Label status

pok_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20 bold'), bg=co6, fg=co0)
pok_status.place(x=15, y=310)

#Hp
pok_hp = Label(janela, text='HP: 300', relief='flat', anchor=CENTER, font=('Verdana 10 italic'), bg=co6, fg=co0)
pok_hp.place(x=15, y=360)

#Ataque
pok_ataque = Label(janela, text='Ataque: 600', relief='flat', anchor=CENTER, font=('Verdana 10 italic'), bg=co6, fg=co0)
pok_ataque.place(x=15, y=385)

#Defesa
pok_defesa = Label(janela, text='Defesa: 500', relief='flat', anchor=CENTER, font=('Verdana 10 italic'), bg=co6, fg=co0)
pok_defesa.place(x=15, y=410)

#Velocidade
pok_velo = Label(janela, text='Velociade: 300', relief='flat', anchor=CENTER, font=('Verdana 10 italic'), bg=co6, fg=co0)
pok_velo.place(x=15, y=435)

#Total
pok_total = Label(janela, text='Total: 1700', relief='flat', anchor=CENTER, font=('Verdana 10 italic'), bg=co6, fg=co0)
pok_total.place(x=15, y=460)

#Label habilidades

pok_status = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20 bold'), bg=co6, fg=co0)
pok_status.place(x=160, y=310)

#Habilidade 1
pok_habi1 = Label(janela, text='Choque do trovão', relief='flat', anchor=CENTER, font=('Verdana 10 italic'), bg=co6, fg=co0)
pok_habi1.place(x=160, y=360)

#Habilidade 2
pok_habi2 = Label(janela, text='Cabeçada', relief='flat', anchor=CENTER, font=('Verdana 10 italic'), bg=co6, fg=co0)
pok_habi2.place(x=160, y=385)

#Criando botões para escolher o pokemon #Pikachu
imagem_pokemon1 = Image.open('images/cabeca-pikachu.png')
imagem_pokemon1 = imagem_pokemon1.resize((40, 40))
imagem_pokemon1 = ImageTk.PhotoImage(imagem_pokemon1)

bupok1 = Button(janela, command=lambda: trocar_pokemon('Pikachu'), image=imagem_pokemon1, text='Pikachu', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
bupok1.place(x=375, y=10)

#Bulbasaur
imagem_pokemon2 = Image.open('images/cabeca-bulbasaur.png')
imagem_pokemon2 = imagem_pokemon2.resize((40, 40))
imagem_pokemon2 = ImageTk.PhotoImage(imagem_pokemon2)

bupok2 = Button(janela, command=lambda: trocar_pokemon('Bulbasaur'), image=imagem_pokemon2, text='Bulbasaur', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
bupok2.place(x=375, y=65)

#Charmander
imagem_pokemon3 = Image.open('images/cabeca-charmander.png')
imagem_pokemon3 = imagem_pokemon3.resize((40, 40))
imagem_pokemon3 = ImageTk.PhotoImage(imagem_pokemon3)

bupok3 = Button(janela, command=lambda: trocar_pokemon('Charmander'), image=imagem_pokemon3, text='Charmander', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
bupok3.place(x=375, y=120)

#Gyarados
imagem_pokemon4 = Image.open('images/cabeca-gyarados.png')
imagem_pokemon4 = imagem_pokemon4.resize((40, 40))
imagem_pokemon4 = ImageTk.PhotoImage(imagem_pokemon4)

bupok4 = Button(janela, command=lambda: trocar_pokemon('Gyarados'), image=imagem_pokemon4, text='Gyarados', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
bupok4.place(x=375, y=175)

#Gengar
imagem_pokemon5 = Image.open('images/cabeca-gengar.png')
imagem_pokemon5 = imagem_pokemon5.resize((40, 40))
imagem_pokemon5 = ImageTk.PhotoImage(imagem_pokemon5)

bupok5 = Button(janela, command=lambda: trocar_pokemon('Gengar'), image=imagem_pokemon5, text='Gengar', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
bupok5.place(x=375, y=230)

#Dragonite
imagem_pokemon6 = Image.open('images/cabeca-dragonite.png')
imagem_pokemon6 = imagem_pokemon6.resize((40, 40))
imagem_pokemon6 = ImageTk.PhotoImage(imagem_pokemon6)

bupok6 = Button(janela, command=lambda: trocar_pokemon('Dragonite'), image=imagem_pokemon6, text='Dragonite', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
bupok6.place(x=375, y=285)

#Iniciando a janela/programa

janela.mainloop()
