from cProfile import label
from tkinter import *
from turtle import pos
from PIL import Image, ImageTk
from urllib.request import urlopen

from mahotas import labeled_sum
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
labelUser = Label(janela, text="")
loginUser = Label(janela, text="")
labelPassword = Label(janela, text="")
loginPassword = Label(janela, text="")
loginButton = Button(janela, text="")
errorMsg = Label(janela, text="")
likes = Label(janela, text="")
location = Label(janela, text="")
taggedUsers = Label(janela, text="")
titulo = Label(janela, text="")
hashtags = Label(janela, text="")
mencoes = Label(janela, text="")
photoPost = Label(janela, text="")
dataPost = Label(janela, text="")
voltar = Label(janela, text="")
#moreInfo = Label(janela, text="More info: ")
#função historico
pasta = './'
num = 0
historico = []
for diretorio, subpastas, arquivos in os.walk(pasta):
    if(diretorio.find("\\") == -1):
        if(num > 1):
            historico.append(diretorio)
        #print(diretorio)
        num = num+1

num = num - 3
#print(historico)

def openProfile(profile):
    global accountId, username, name, verified, followees, followers, website, biography, profilePhoto, image, postInterface, pastasPost, labelUser, loginUser, labelPassword, loginPassword, loginButton, errorMsg, likes, location, taggedUsers, titulo, hashtags, mencoes, photoPost, dataPost, voltar
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
    labelUser.destroy()
    loginUser.destroy()
    labelPassword.destroy()
    loginPassword.destroy()
    loginButton.destroy()
    errorMsg.destroy()
    likes.destroy()
    location.destroy()
    taggedUsers.destroy()
    titulo.destroy()
    hashtags.destroy()
    mencoes.destroy()
    photoPost.destroy()
    dataPost.destroy()
    voltar.destroy()
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

def voltarF():
    global pastasPost, postInterface, likes, location, taggedUsers, titulo, hashtags, mencoes, photoPost, dataPost, voltar
    likes.destroy()
    location.destroy()
    taggedUsers.destroy()
    titulo.destroy()
    hashtags.destroy()
    mencoes.destroy()
    photoPost.destroy()
    dataPost.destroy()
    voltar.destroy()
    postInterface = []
    y=0
    column = -1
    row = -23
    while(y < pastasPost.__len__()):
        postInterface.append(Button(janela, text=pastasPost[y], command=lambda m = pastasPost[y]: openPost(m)))
        if(y%23 == 0):
            row = row+23
            column = column+1
        
        postInterface[y].grid(column= 3+column, row=4+y-row)
        y = y + 1

def openPost(path):
    global nomePesquisa, pastasPost, postInterface, likes, location, taggedUsers, titulo, hashtags, mencoes, photoPost, dataPost, voltar
    y=0
    while(y < pastasPost.__len__() and pastasPost != "login"):
        postInterface[y].destroy()
        y = y + 1
    file = open("./"+nomePesquisa.cget("text")+"/"+ path + "/dados.txt", "r")
    content = file.readlines()
    content = [x. rstrip('\n') for x in content]
    voltar = Button(janela, text="Voltar", command=voltarF)
    voltar.grid(column=4, row=3)
    dataPost = Label(janela, text="Data: "+content[7])
    dataPost.grid(column=3, row=4)
    location = Label(janela, text="Localização: "+content[1])
    location.grid(column=3, row=5)
    likes = Label(janela, text="Likes: "+content[0])
    likes.grid(column=3, row=6)
    titulo = Label(janela, text="Titulo: "+content[3])
    titulo.grid(column=3, row=7)
    taggedUsers = Label(janela, text="Tagged Users: "+ content[2])
    taggedUsers.grid(column=3, row=8)
    hashtags = Label(janela, text="Hashtags: "+content[4])
    hashtags.grid(column=3, row=9)
    mencoes = Label(janela, text="Menções: "+content[1])
    mencoes.grid(column=3, row=10)
    u = urlopen(content[6])
    raw_data = u.read()
    u.close()
    photo = ImageTk.PhotoImage(data=raw_data)
    photoPost = Label(janela, image=photo, width=400, height=400)
    photoPost.image = photo
    photoPost.grid(column=3, row=11)
    
    
def getLogin():
    global errorMsg, postInterface, labelUser, loginUser, labelPassword, loginPassword, loginButton, pastasPost
    pastasPost = main.login(loginUser.get(), loginPassword.get())
    if(pastasPost == 'error'):
        errorMsg.destroy()
        errorMsg = Label(janela, text="Erro ao realizar login tente novamente.")
        errorMsg.grid(column=4, row=6)
    else:
        labelUser.destroy()
        loginUser.destroy()
        labelPassword.destroy()
        loginPassword.destroy()
        loginButton.destroy()
        errorMsg.destroy()
        postInterface = []
        y=0
        column = -1
        row = -23
        while(y < pastasPost.__len__()):
            postInterface.append(Button(janela, text=pastasPost[y], command=lambda m = pastasPost[y]: openPost(m)))
            if(y%23 == 0):
                row = row+23
                column = column+1
            
            postInterface[y].grid(column= 3+column, row=4+y-row)
            y = y + 1
        print(x)

postInterface = []
pastasPost = []
def openPosts(x):
    global postInterface, pastasPost, accountId, username, name, verified, followees, followers, website, biography, profilePhoto, image, labelUser, loginUser, labelPassword, loginPassword, loginButton, errorMsg
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
    labelUser.destroy()
    loginUser.destroy()
    labelPassword.destroy()
    loginPassword.destroy()
    loginButton.destroy()
    errorMsg.destroy()
    
    if(postInterface.__len__() != 0):
        y=0
        while(y < pastasPost.__len__()):
            postInterface[y].destroy()
            y = y + 1
    print(x)
    pastasPost = main.posts(x)
    print(pastasPost)
    if(pastasPost == "login"):
        labelUser = Label(janela, text="Username or Email:")
        labelUser.grid(column=3, row=4)
        loginUser = Entry(janela)
        loginUser.grid(column=4, row=4)
        labelPassword = Label(janela, text="Password:")
        labelPassword.grid(column=3, row=5)
        loginPassword = Entry(janela)
        loginPassword.grid(column=4, row=5)
        loginButton = Button(janela, text="Login", command = getLogin)
        loginButton.grid(column=3, row=6)
    else:
        postInterface = []
        y=0
        column = -1
        row = -23
        while(y < pastasPost.__len__()):
            postInterface.append(Button(janela, text=pastasPost[y], command=lambda m = pastasPost[y]: openPost(m)))
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
    global accountId, username, name, verified, followees, followers, website, biography, profilePhoto, image, nomePesquisa, profile, posts, historicoInterface, delete, num, postInterface, pastasPost, labelUser, loginUser, labelPassword, loginPassword, loginButton, errorMsg, likes, location, taggedUsers, titulo, hashtags, mencoes, photoPost, dataPost, voltar
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
    labelUser.destroy()
    loginUser.destroy()
    labelPassword.destroy()
    loginPassword.destroy()
    loginButton.destroy()
    errorMsg.destroy()
    likes.destroy()
    location.destroy()
    taggedUsers.destroy()
    titulo.destroy()
    hashtags.destroy()
    mencoes.destroy()
    photoPost.destroy()
    dataPost.destroy()
    voltar.destroy()
    pasta = './'
    num = 0
    historico = []
    for diretorio, subpastas, arquivos in os.walk(pasta):
        if(diretorio.find("\\") == -1):
            if(num > 1):
                historico.append(diretorio)
            #print(diretorio)
            num = num+1

    num = num - 3
    x = 0
    while(x < num):
        historicoInterface[x].destroy()
        historicoInterface[x] = Button(janela, text=historico[x], command=lambda m = historico[x]: openUser(m))
        historicoInterface[x].grid(column= 0, row=4+x)
        x = x + 1

    y=0
    while(y < pastasPost.__len__() and pastasPost != "login"):
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