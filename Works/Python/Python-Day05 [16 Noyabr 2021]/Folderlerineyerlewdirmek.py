import os
import shutil

def organizeFolder(folderPath) :
    locate="C:/Users/user/Desktop/Github/Works/Python/Python-Day05 [16 Noyabr 2021]/project/"
    path1=os.path.join(locate,folderPath)
    if folderPath=="Css":
       os.mkdir(path1)
       shutil.move(os.path.join(locate,"style.css"),path1)
       shutil.move(os.path.join(locate,"layout.css"),path1)
       shutil.move(os.path.join(locate,"common.css"),path1)
    elif folderPath=="Html":
        os.mkdir(path1)
        shutil.move(os.path.join(locate,"about.html"),path1)
        shutil.move(os.path.join(locate,"contact.html"),path1)
        shutil.move(os.path.join(locate,"index.html"),path1)
        shutil.move(os.path.join(locate,"work.html"),path1)
    elif folderPath=="Js":
        os.mkdir(path1)
        shutil.move(os.path.join(locate,"app.js"),path1)
        shutil.move(os.path.join(locate,"gallery.js"),path1)
        shutil.move(os.path.join(locate,"script.js"),path1)
    elif folderPath=="image":
        os.mkdir(path1)
        shutil.move(os.path.join(locate,"1.jpg"),path1)
        shutil.move(os.path.join(locate,"2.jpg"),path1)
        shutil.move(os.path.join(locate,"3.jpg"),path1)
        shutil.move(os.path.join(locate,"7.jpg"),path1)
        shutil.move(os.path.join(locate,"14.jpg"),path1)
        shutil.move(os.path.join(locate,"22.jpg"),path1)


add=input("Bawlayaq?(yes/no)")
while add=="yes":
    ad=input("Hansi folderi yaratmaq ve fayillari dahil etmek?")
    organizeFolder(ad)
    add=input("Davam edek?(yes/no)")
        



