from cProfile import label
from tkinter import *
from turtle import pos
from PIL import Image, ImageTk
from urllib.request import urlopen
import main 
import os
import shutil

#inicia a janela
janela = Tk()
janela.title("Search Case")
#variveis que precisam de refresh
accountId = Label(janela, text='')
username = Label(janela, text='')
name = Label(janela, text='')
verified = Label(janela, text='')
followers = Label(janela, text='')
followees = Label(janela, text='')
website = Label(janela, text='')
biography = Label(janela, text='')
profilePhoto = Label(janela, text='')
image = Label(janela, image='')
nomePesquisa = Label(janela, text="")
profile = Button(janela, text='')
posts = Button(janela, text='')
delete = Button(janela, text='')
#moreInfo = Label(janela, text="More info: ")
#função historico
pasta = './'
num = 0
historico = []
for diretorio, subpastas, arquivos in os.walk(pasta):
    if(diretorio.find("\\") == -1):
        if(num > 0):
            historico.append(diretorio)
        #print(diretorio)
        num = num+1

num = num - 2
#print(historico)

def openProfile(profile):
    global accountId, username, name, verified, followees, followers, website, biography, profilePhoto, image, postInterface, pastasPost
    accountId.destroy()
    username.destroy()
    name.destroy()
    verified.destroy()
    followees.destroy()
    followers.destroy()
    website.destroy()
    biography.destroy()
    profilePhoto.destroy()
    image.destroy()
    if(postInterface.__len__() != 0):
        y=0
        while(y < pastasPost.__len__()):
            postInterface[y].destroy()
            y = y + 1
    variables = main.profile(profile)
    accountId = Label(janela, text="Account ID: "+ str(variables["id"]))
    accountId.grid(column=1, row=4)
    username = Label(janela, text="Username: "+ variables["username"])
    username.grid(column=1, row=5)
    name = Label(janela, text="Name: "+ variables["name"])
    name.grid(column=1, row=6)
    verified = Label(janela, text="Verified Badge: "+ str(variables["verified"]))
    verified.grid(column=1, row=7)
    followers = Label(janela, text="Followers: "+ str(variables["followers"]))
    followers.grid(column=1, row=8)
    followees = Label(janela, text="Followees: "+ str(variables["followees"]))
    followees.grid(column=1, row=9)
    website = Label(janela, text="Website: "+ str(variables['website']))
    website.grid(column=1, row=10)
    biography = Label(janela, text="Biography: "+ variables["biography"])
    biography.grid(column=1, row=11)
    #moreInfo = Label(janela, text="More info: ")
    #moreInfo.grid(column=1, row=12)
    profilePhoto = Label(janela, text="Profile Photo")
    profilePhoto.grid(column=1, row=12)
    u = urlopen(variables["profilePic"])
    raw_data = u.read()
    u.close()
    photo = ImageTk.PhotoImage(data=raw_data)
    image = Label(janela, image=photo)
    image.image = photo
    image.grid(column=1, row=13)

def openPhoto(path):
    global nomePesquisa
    file = open("./"+nomePesquisa+"/"+ path + "/dados.txt", "r")
    print(file.readlines())
    
postInterface = []
pastasPost = []
def openPosts(x):
    global postInterface, pastasPost, accountId, username, name, verified, followees, followers, website, biography, profilePhoto, image
    accountId.destroy()
    username.destroy()
    name.destroy()
    verified.destroy()
    followees.destroy()
    followers.destroy()
    website.destroy()
    biography.destroy()
    profilePhoto.destroy()
    image.destroy()
    if(postInterface.__len__() != 0):
        y=0
        while(y < pastasPost.__len__()):
            postInterface[y].destroy()
            y = y + 1
        
    pastasPost = main.posts(x)
    postInterface = []
    y=0
    column = -1
    row = -23
    while(y < pastasPost.__len__()):
        postInterface.append(Button(janela, text=pastasPost[y], command=lambda m = pastasPost[y]: openPhoto(m)))
        if(y%23 == 0):
            row = row+23
            column = column+1
        
        postInterface[y].grid(column= 3+column, row=4+y-row)
        y = y + 1
    print(x)

def leE1():
    global historicoInterface
    os.mkdir(e1.get())
    historicoInterface.append(Button(janela, text=''))
    e1.delete(0, END)
    refresh()

def deleteUser(x):
    global historicoInterface, num
    shutil.rmtree(x)
    historicoInterface[num-1].destroy()
    refresh()

click = 0
def openUser(x):
    refresh()
    x = x[2:len(x)]  
    global nomePesquisa, profile, posts, delete 
    nomePesquisa.destroy()
    profile.destroy()
    posts.destroy()
    delete.destroy()
    nomePesquisa = Label(janela, text=x)
    nomePesquisa.grid(column=2,row=2)
    delete = Button(janela, text="Delete", command = lambda m = x: deleteUser(x))
    delete.grid(column=2, row=0)
    profile = Button(janela, text="Profile", command=lambda m = x: openProfile(x))
    profile.grid(column=1, row=3)
    posts = Button(janela, text="Posts", command=lambda m = x: openPosts(x))
    posts.grid(column=3, row=3)

def refresh():
    global accountId, username, name, verified, followees, followers, website, biography, profilePhoto, image, nomePesquisa, profile, posts, historicoInterface, delete, num, postInterface, pastasPost
    delete.destroy()
    profile.destroy()
    posts.destroy()
    nomePesquisa.destroy()
    accountId.destroy()
    username.destroy()
    name.destroy()
    verified.destroy()
    followees.destroy()
    followers.destroy()
    website.destroy()
    biography.destroy()
    profilePhoto.destroy()
    image.destroy()

    pasta = './'
    num = 0
    historico = []
    for diretorio, subpastas, arquivos in os.walk(pasta):
        if(diretorio.find("\\") == -1):
            if(num > 0):
                historico.append(diretorio)
            #print(diretorio)
            num = num+1

    num = num - 2
    x = 0
    while(x < num):
        historicoInterface[x].destroy()
        historicoInterface[x] = Button(janela, text=historico[x], command=lambda m = historico[x]: openUser(m))
        historicoInterface[x].grid(column= 0, row=4+x)
        x = x + 1

    y=0
    while(y < pastasPost.__len__()):
        postInterface[y].destroy()
        y = y + 1

#janela.geometry("600x600")
texto_principal = Label(janela, text="Seja bem vindo ao Search Case, escreva abaixo o @ do usuário que deseja investigar!")
texto_principal.grid(column=0, row=0)

e1 = Entry(janela)
e1.grid(column=0, row=1)

botao = Button(janela, text="Search", command = leE1)
botao.grid(column=0, row=2)

quit = Label(janela, text='Historico')
quit.grid(row=3, column=0)

historicoInterface = []
x = 0
while(x < num):
    historicoInterface.append(Button(janela, text=historico[x], command=lambda m = historico[x]: openUser(m)))
    historicoInterface[x].grid(column= 0, row=4+x)
    x = x + 1

refreshButton = Button(janela, text='Refresh', command=refresh)
refreshButton.grid(row=x+5, column=0, sticky=W, pady=4)
quit = Button(janela, text='Quit', command=janela.quit)
quit.grid(row=x+6, column=0, sticky=W, pady=4)
janela.mainloop()