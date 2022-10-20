from turtle import pos
from instaloader import instaloader, Profile
import os
import shutil
import re
# Get instance
L = instaloader.Instaloader()

def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)

def posts(nome):
    PROFILE = nome
    profile = Profile.from_username(L.context, PROFILE)
    print(profile.is_private)
    if(profile.is_private == True):
        return "login"
    else:
        posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes, reverse=True)

        num = 1
    
        for post in posts_sorted_by_likes:
            data = str(post.date)
            pasta = './'+nome+"/"+str(data.split(" ")[0])
            num = num+1
            #shutil.rmtree(pasta)
            print(pasta)
            if os.path.isdir(pasta):
                shutil.rmtree(pasta)

            os.mkdir(pasta)
            file = open(pasta+"/dados.txt", "w")
            text = [str(post.likes) + "\n", 
               str(post.location)+ "\n", 
               str(post.tagged_users)+ "\n", 
               remove_emojis(str(post.caption))+ "\n", 
               str(post.caption_hashtags)+ "\n", 
               str(post.caption_mentions)+ "\n", 
               str(post.url)+ "\n", 
               str(post.date_utc)+ "\n"]

            file.writelines(text)  
            file.close()
       

        pasta = './'+ nome
        num = 0
        pastas = []
        for diretorio, subpastas, arquivos in os.walk(pasta):
            if(num > 0):
                print(diretorio.split("\\"))
                pastas.append(diretorio.split("\\")[1])
            #print(diretorio)
            num = num+1
        num = num - 2   

    return pastas

def profile(nome):     
    PROFILE = nome
    profile = Profile.from_username(L.context, PROFILE)
    return {
        "id": profile.userid,
        "followees": profile.followees,
        "followers": profile.followers,
        "username": profile.username,
        "name": profile.full_name,
        "biography": profile.biography,
        "verified": profile.is_verified,
        "profilePic": profile.profile_pic_url,
        "website": profile.external_url
    }

def login(user, passowrd):
    L = instaloader.Instaloader()

    try:
        L.login(user, passowrd) == None
        print("ok")    
        profile = Profile.from_username(L.context, user)
        posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes, reverse=True)

        num = 1
    
        for post in posts_sorted_by_likes:
            data = str(post.date)
            pasta = './'+user+"/"+str(data.split(" ")[0])
            num = num+1
            #shutil.rmtree(pasta)
            print(pasta)
            if os.path.isdir(pasta):
                shutil.rmtree(pasta)

            os.mkdir(pasta)
            file = open(pasta+"/dados.txt", "w")
            text = [str(post.likes) + "\n", 
               str(post.location)+ "\n", 
               str(post.tagged_users)+ "\n", 
               remove_emojis(str(post.caption))+ "\n", 
               str(post.caption_hashtags)+ "\n", 
               str(post.caption_mentions)+ "\n", 
               str(post.url)+ "\n", 
               str(post.date_utc)+ "\n"]

            file.writelines(text)  
            file.close()
       

        pasta = './'+ user
        num = 0
        pastas = []
        for diretorio, subpastas, arquivos in os.walk(pasta):
            if(num > 0):
                print(diretorio.split("\\"))
                pastas.append(diretorio.split("\\")[1])
            #print(diretorio)
            num = num+1
        num = num - 2   
        return pastas
    except:
        return "error"
    

    
                                