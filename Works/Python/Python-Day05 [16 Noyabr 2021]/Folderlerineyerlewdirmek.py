import os
import shutil
ad=input("Hansi folderi yaratmaq ve fayillari dahil etmek?")
def organizeFolder(folderPath) :
    locate="C:/Users/user/Desktop/Github/Works/Python/Python-Day05 [16 Noyabr 2021]/project/"
    path1=os.path.join(locate,folderPath)
    if folderPath=="Css":
       os.mkdir(path1)
       shutil.move(os.path.join(locate,"style.css"),path1)
    elif folderPath=="Html":
        os.mkdir(path1)
        shutil.move(os.path.join(locate,"home.html"),path1)
        shutil.move(os.path.join(locate,"second.html"),path1)
    elif folderPath=="Js":
        os.mkdir(path1)
        shutil.move(os.path.join(locate,"app.js"),path1)
        shutil.move(os.path.join(locate,"javascriptwork.js"),path1)
    elif folderPath=="image":
        os.mkdir(path1)
        shutil.move(os.path.join(locate,"pro.png"),path1)
        shutil.move(os.path.join(locate,"python.png"),path1)
        shutil.move(os.path.join(locate,"pngwing.com.png"),path1)
organizeFolder(ad)
        



