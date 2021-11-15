import shutil
import os
#os.mkdir("C:/Users/user/Desktop/Github/Works/Python/OsModule")
file1="C:/Users/user/Desktop/Github/Works/Python/OsModule/a.txt"
file11=open(file1,"w")
file11.write("Men python yazmaga cehd elirem")
file2="C:/Users/user/Desktop/Github/Works/Python/OsModule/b.txt"
file22=open(file2,"a").close()
location="C:/Users/user/Desktop/Github/Works/Python/OsModule/"
pathold=os.path.join(location,"b.txt")
pathnew=os.path.join(location,"B.txt")
os.renames(pathold,pathnew)

locold="C:/Users/user/Desktop/portfolio/Portfolio/img/"
imgname="bfoto_ru_4762.jpg"
locolnew="C:/Users/user/Desktop/Github/Works/Python/OsModule/"
shutil.move(os.path.join(locold,imgname),locolnew)





