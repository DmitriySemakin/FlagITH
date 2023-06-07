from tkinter import *

root = Tk()
root.title('Флаги')
root.geometry('520x780')
root.resizable(height = False, width = False)
root.iconbitmap('icon.ico') #иконка
root.config(bg = '#87CEFA') #фон

score = 0

def mainmenu():
    labelgame2.place_forget()
    winlabel.place_forget()
    backbotton1.place_forget()
    label10.pack_forget()

    labelgame.place_forget()
    loselabel.place_forget()
    backbotton1.place_forget()

    label4.pack_forget()
    label5.pack_forget()
    label6.pack_forget()
    label7.pack_forget()
    label8.pack_forget()
    label9.pack_forget()

    label3.pack_forget()
    brazillabel.place_forget()
    quest2.place_forget()
    quest4.place_forget()
    quest6.place_forget()
    quest8.place_forget()

    danialabel.place_forget()
    quest10.place_forget()
    quest12.place_forget()
    quest14.place_forget()
    quest16.place_forget()

    egipetlabel.place_forget()
    quest18.place_forget()
    quest20.place_forget()
    quest22.place_forget()
    quest24.place_forget()

    korealabel.place_forget()
    quest26.place_forget()
    quest28.place_forget()
    quest30.place_forget()
    quest32.place_forget()

    serbialabel.place_forget()
    quest34.place_forget()
    quest36.place_forget()
    quest38.place_forget()
    quest40.place_forget()

    vietnamlabel.place_forget()
    quest42.place_forget()
    quest44.place_forget()
    quest46.place_forget()
    quest48.place_forget()

    uzbeklabel.place_forget()
    quest50.place_forget()
    quest52.place_forget()
    quest54.place_forget()
    quest56.place_forget()

    rioiImagelabel.place_forget()
    quest342.place_forget()
    quest344.place_forget()
    quest346.place_forget()
    quest348.place_forget()

    play3.place(x=130, y=150)
    play5.place(x=130, y=300)
    play7.place(x=130, y=450)
    label2.pack()
    labelname.place(x=43, y=670)
    maplabel.place(x=180, y=565)

    label102.pack_forget()
    label103.pack_forget()
    label104.pack_forget()
    label105.pack_forget()
    label106.pack_forget()
    label107.pack_forget()
    label108.pack_forget()

    label202.pack_forget()
    label203.pack_forget()
    label204.pack_forget()
    label205.pack_forget()
    label206.pack_forget()
    label207.pack_forget()

def win1():
    label3.pack_forget()
    uzbeklabel.place_forget()
    quest50.place_forget()
    quest52.place_forget()
    quest54.place_forget()
    quest56.place_forget()

    label108.pack_forget()
    franchImagelabel.place_forget()
    quest152.place_forget()
    quest154.place_forget()
    quest156.place_forget()
    quest158.place_forget()
    label100.pack_forget()
    label101.pack_forget()

    rioiImagelabel.place_forget()
    quest342.place_forget()
    quest344.place_forget()
    quest346.place_forget()
    quest348.place_forget()
    label200.pack_forget()
    label201.pack_forget()
    label207.pack_forget()


    labelgame2.place(y=60, x=140)
    winlabel.place(x=65, y=160)
    backbotton1.place(x=120, y=660)

def gameover():


    label3.pack_forget()
    brazillabel.place_forget()
    quest2.place_forget()
    quest4.place_forget()
    quest6.place_forget()
    quest8.place_forget()


    danialabel.place_forget()
    quest10.place_forget()
    quest12.place_forget()
    quest14.place_forget()
    quest16.place_forget()

    egipetlabel.place_forget()
    quest18.place_forget()
    quest20.place_forget()
    quest22.place_forget()
    quest24.place_forget()

    korealabel.place_forget()
    quest26.place_forget()
    quest28.place_forget()
    quest30.place_forget()
    quest32.place_forget()


    serbialabel.place_forget()
    quest34.place_forget()
    quest36.place_forget()
    quest38.place_forget()
    quest40.place_forget()


    vietnamlabel.place_forget()
    quest42.place_forget()
    quest44.place_forget()
    quest46.place_forget()
    quest48.place_forget()


    uzbeklabel.place_forget()
    quest50.place_forget()
    quest52.place_forget()
    quest54.place_forget()
    quest56.place_forget()

    labelgame.place(y=100, x=14)
    loselabel.place(x=55, y=250)
    backbotton1.place(x=125, y=610)
#Главная страница#########################################################

def play_button():
    label1.pack_forget()
    canvas.pack_forget()
    play1.place_forget()
    play3.place(x=130, y=150)
    play5.place(x=130, y=300)
    play7.place(x=130, y=450)
    labelname.place(x=43, y=670)
    maplabel.place(x=180, y=565)
    mainEarthlabel.place_forget()

def gameover2():
    label100.pack_forget()
    label101.pack_forget()

    argentinaImagelabel.place_forget()
    quest104.place_forget()
    quest106.place_forget()
    quest108.place_forget()
    quest110.place_forget()

    indiaImagelabel.place_forget()
    quest112.place_forget()
    quest114.place_forget()
    quest116.place_forget()
    quest118.place_forget()

    japanImagelabel.place_forget()
    quest120.place_forget()
    quest122.place_forget()
    quest124.place_forget()
    quest126.place_forget()

    liviaImagelabel.place_forget()
    quest128.place_forget()
    quest130.place_forget()
    quest132.place_forget()
    quest134.place_forget()

    chinaImagelabel.place_forget()
    quest136.place_forget()
    quest138.place_forget()
    quest140.place_forget()
    quest142.place_forget()

    canadaImagelabel.place_forget()
    quest144.place_forget()
    quest146.place_forget()
    quest148.place_forget()
    quest150.place_forget()

    franchImagelabel.place_forget()
    quest152.place_forget()
    quest154.place_forget()
    quest156.place_forget()
    quest158.place_forget()

    labelgame.place(y=100, x=14)
    loselabel.place(x=55, y=250)
    backbotton1.place(x=125, y=610)

def gameover3():
    label200.pack_forget()
    label201.pack_forget()

    rusImagelabel.place_forget()
    quest302.place_forget()
    quest304.place_forget()
    quest306.place_forget()
    quest308.place_forget()

    usaImagelabel.place_forget()
    quest310.place_forget()
    quest312.place_forget()
    quest314.place_forget()
    quest316.place_forget()

    japaImagelabel.place_forget()
    quest318.place_forget()
    quest320.place_forget()
    quest322.place_forget()
    quest324.place_forget()

    londonImagelabel.place_forget()
    quest326.place_forget()
    quest328.place_forget()
    quest330.place_forget()
    quest332.place_forget()

    indiImagelabel.place_forget()
    quest334.place_forget()
    quest336.place_forget()
    quest338.place_forget()
    quest340.place_forget()

    rioiImagelabel.place_forget()
    quest342.place_forget()
    quest344.place_forget()
    quest346.place_forget()
    quest348.place_forget()


    labelgame.place(y=100, x=14)
    loselabel.place(x=55, y=250)
    backbotton1.place(x=125, y=610)



label1 = Label(root, text = "Флаги", font = ('Bookman Old Style', 60), bg = '#87CEFA', fg = 'black', pady=15)
label1.pack()

canvas = Canvas(root, width=520, height=780, highlightthickness=0, bg = '#87CEFA')
canvas.pack()

play = PhotoImage(file='play.png')
play = play.subsample(7,7)
play1 = Button(root, image=play, highlightthickness=0, bd=0,activebackground='#87CEFA', command=play_button)
play1.place(x=170, y=510)


mainEarth = PhotoImage(file='main_earth.png')
mainEarth = mainEarth.subsample(2,2)
mainEarthlabel = Label(root, highlightthickness=0, bd=0, activebackground='#87CEFA')
mainEarthlabel.image = mainEarth
mainEarthlabel['image'] = mainEarth
mainEarthlabel.place(x=110,y=160)


#Выбор игры################################################################


def gamechoice1():
    label2.pack_forget()
    canvas2.pack_forget()
    play3.place_forget()
    play5.place_forget()
    play7.place_forget()
    label3.pack()
    label4.pack()
    brazillabel.place(x=110, y=180)
    quest2.place(y=410, x=80)
    quest4.place(y=490, x=80)
    quest6.place(y=570, x=80)
    quest8.place(y=650, x=80)
    labelname.place_forget()
    maplabel.place_forget()

def gamechoice2():
    label2.pack_forget()
    canvas2.pack_forget()
    play3.place_forget()
    play5.place_forget()
    play7.place_forget()
    labelname.place_forget()
    maplabel.place_forget()

    label100.pack()
    label101.pack()
    label102.pack()

    argentinaImagelabel.place(x=50, y=220)
    quest104.place(y=410, x=80)
    quest106.place(y=490, x=80)
    quest108.place(y=570, x=80)
    quest110.place(y=650, x=80)


def gamechoice3():
    label2.pack_forget()
    canvas2.pack_forget()
    play3.place_forget()
    play5.place_forget()
    play7.place_forget()
    labelname.place_forget()
    maplabel.place_forget()

    label200.pack()
    label201.pack()
    label202.pack()

    rusImagelabel.place(x=75, y=220)
    quest302.place(y=410, x=80)
    quest304.place(y=490, x=80)
    quest306.place(y=570, x=80)
    quest308.place(y=650, x=80)

label2 = Label(root, text = "Во что играем?", font = ('Bookman Old Style', 40), bg = '#87CEFA', fg = 'black', pady=15)
label2.pack()
canvas2 = Canvas(root, width=520, height=780, highlightthickness=0, bg = '#87CEFA')
canvas2.pack()

play2 = PhotoImage(file='game1.png')
play2 = play2.subsample(2,2)                                                               #1 игра
play3 = Button(root, image=play2, highlightthickness=0, bd=0,activebackground='#87CEFA',command=gamechoice1)

play4 = PhotoImage(file='game2.png')
play4 = play4.subsample(2,2)                                                               #2 игра
play5 = Button(root, image=play4, highlightthickness=0, bd=0,activebackground='#87CEFA', command=gamechoice2)

play6 = PhotoImage(file='game3.png')
play6 = play6.subsample(2,2)                                                               #3 игра
play7 = Button(root, image=play6, highlightthickness=0, bd=0,activebackground='#87CEFA', command=gamechoice3)

labelname = Label(root, text='Сделано командой ЕлсуковTeam', font = ('Bookman Old Style', 20), bg = '#87CEFA', fg = '#808080', pady=30)


mapImage = PhotoImage(file='map.png')
mapImage = mapImage.subsample(3,3)
maplabel = Label(root, highlightthickness=0, bd=0)
maplabel.image = mapImage
maplabel['image'] = mapImage



#победа

labelgame2 = Label(root, text = "Победа", font = ('Bookman Old Style', 48), bg = '#87CEFA', fg = 'black', pady=15)

winImage = PhotoImage(file='win.png')
winImage = winImage.subsample(1,1)
winlabel = Label(root, highlightthickness=0, bd=0)
winlabel.image = winImage
winlabel['image'] = winImage

backbotton = PhotoImage(file='mainbutton.png')
backbotton = backbotton.subsample(2,2)
backbotton1 = Button(root, image=backbotton, highlightthickness=0, activebackground='#87CEFA', bd=0, command=mainmenu)



#проигрыш

labelgame = Label(root, text = "Игра окончена", font = ('Bookman Old Style', 48), bg = '#87CEFA', fg = 'black', pady=15)

loseImage = PhotoImage(file='pain.png')
loseImage = loseImage.subsample(1,1)
loselabel = Label(root, highlightthickness=0, bd=0)
loselabel.image = loseImage
loselabel['image'] = loseImage


#Игра 1#############################################################################

label3 = Label(root, text = "Выберите страну по флагу", font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=15)   #Название
label4 = Label(root, text="Счёт: " + str(score), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)                       #Счёт


#1 уровень#########################################################################

def game1level2():
    label4.pack_forget()
    brazillabel.place_forget()
    quest2.place_forget()
    quest4.place_forget()
    quest6.place_forget()
    quest8.place_forget()
    label5.pack()
    danialabel.place(x=110, y=180)
    quest10.place(y=410, x=80)
    quest12.place(y=490, x=80)
    quest14.place(y=570, x=80)
    quest16.place(y=650, x=80)

brailImage = PhotoImage(file="brazil.png")
brailImage = brailImage.subsample(2,2)
brazillabel = Label(root)
brazillabel.image = brailImage
brazillabel['image'] = brailImage

quest1 = PhotoImage(file='nigeria.png')
quest2 = Button(root, image=quest1, highlightthickness=0, bd=0, command=gameover)

quest3 = PhotoImage(file='brazilia.png')
quest4 = Button(root, image=quest3, highlightthickness=0, bd=0, command=game1level2)

quest5 = PhotoImage(file='germany.png')
quest6 = Button(root, image=quest5, highlightthickness=0, bd=0, command=gameover)

quest7 = PhotoImage(file='russia.png')
quest8 = Button(root, image=quest7, highlightthickness=0, bd=0, command=gameover)



#2 уровень#################################################################

def game1level3():
    label5.pack_forget()
    danialabel.place_forget()
    quest10.place_forget()
    quest12.place_forget()
    quest14.place_forget()
    quest16.place_forget()
    label6.pack()
    egipetlabel.place(x=110, y=180)
    quest18.place(y=410, x=80)
    quest20.place(y=490, x=80)
    quest22.place(y=570, x=80)
    quest24.place(y=650, x=80)


label3 = Label(root, text = "Выберите страну по флагу", font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=15)   #Название
label5 = Label(root, text="Счёт: " + str(score+1), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)                       #Счёт

daniaImage = PhotoImage(file='flag_dania.png')
daniaImage = daniaImage.subsample(2,2)
danialabel = Label(root)
danialabel.image = daniaImage
danialabel['image'] = daniaImage


quest9 = PhotoImage(file='chexia.png')
quest10 = Button(root, image=quest9, highlightthickness=0, bd=0, command=gameover)

quest11 = PhotoImage(file='belarussia.png')
quest12 = Button(root, image=quest11, highlightthickness=0, bd=0, command=gameover)

quest13= PhotoImage(file='belgia.png')
quest14 = Button(root, image=quest13, highlightthickness=0, bd=0, command=gameover)

quest15= PhotoImage(file='dania.png')
quest16 = Button(root, image=quest15, highlightthickness=0, bd=0, command=game1level3)



#3 уровень#####################################################################################

def game1level3():
    egipetlabel.place_forget()
    label6.pack_forget()
    quest18.place_forget()
    quest20.place_forget()
    quest22.place_forget()
    quest24.place_forget()
    label7.pack()
    korealabel.place(x=110, y=180)
    quest26.place(y=410, x=80)
    quest28.place(y=490, x=80)
    quest30.place(y=570, x=80)
    quest32.place(y=650, x=80)



label6 = Label(root, text="Счёт: " + str(score+2), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)
egipetImage = PhotoImage(file='flag_egipet.png')
egipetImage = egipetImage.subsample(3,3)
egipetlabel = Label(root)
egipetlabel.image = egipetImage
egipetlabel['image'] = egipetImage


quest17 = PhotoImage(file='egipet.png')
quest18 = Button(root, image=quest17, highlightthickness=0, bd=0, command=game1level3)

quest19 = PhotoImage(file='irak.png')
quest20 = Button(root, image=quest19, highlightthickness=0, bd=0, command=gameover)

quest21= PhotoImage(file='franch.png')
quest22 = Button(root, image=quest21, highlightthickness=0, bd=0, command=gameover)

quest23= PhotoImage(file='greek.png')
quest24 = Button(root, image=quest23, highlightthickness=0, bd=0, command=gameover)



#4 уровень#######################################################################################

def game1level4():
    label3.pack()
    label7.pack_forget()
    korealabel.place_forget()
    quest26.place_forget()
    quest28.place_forget()
    quest30.place_forget()
    quest32.place_forget()

    label8.pack()
    serbialabel.place(x=110, y=180)
    quest34.place(y=410, x=80)
    quest36.place(y=490, x=80)
    quest38.place(y=570, x=80)
    quest40.place(y=650, x=80)




label7 = Label(root, text="Счёт: " + str(score+3), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)
koreaImage = PhotoImage(file='flag_korea.png')
koreaImage = koreaImage.subsample(2,2)
korealabel = Label(root)
korealabel.image = koreaImage
korealabel['image'] = koreaImage


quest25 = PhotoImage(file='japan.png')
quest26 = Button(root, image=quest25, highlightthickness=0, bd=0, command=gameover)

quest27 = PhotoImage(file='kuba.png')
quest28 = Button(root, image=quest27, highlightthickness=0, bd=0, command=gameover)

quest29= PhotoImage(file='korea.png')
quest30 = Button(root, image=quest29, highlightthickness=0, bd=0, command=game1level4)

quest31= PhotoImage(file='spain.png')
quest32 = Button(root, image=quest31, highlightthickness=0, bd=0, command=gameover)




#5 уровень#######################################################################################

def game1level5():
    label8.pack_forget()
    serbialabel.place_forget()
    quest34.place_forget()
    quest36.place_forget()
    quest38.place_forget()
    quest40.place_forget()

    label9.pack()

    vietnamlabel.place(x=110, y=180)
    quest42.place(y=410, x=80)
    quest44.place(y=490, x=80)
    quest46.place(y=570, x=80)
    quest48.place(y=650, x=80)




label8 = Label(root, text="Счёт: " + str(score+4), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)

serbiaImage = PhotoImage(file='flag_serbia.png')
serbiaImage = serbiaImage.subsample(3,3)
serbialabel = Label(root)
serbialabel.image = serbiaImage
serbialabel['image'] = serbiaImage


quest33 = PhotoImage(file='serbia.png')
quest34 = Button(root, image=quest33, highlightthickness=0, bd=0, command=game1level5)

quest35 = PhotoImage(file='turkey.png')
quest36 = Button(root, image=quest35, highlightthickness=0, bd=0, command=gameover)

quest37= PhotoImage(file='slovakia.png')
quest38 = Button(root, image=quest37, highlightthickness=0, bd=0, command=gameover)

quest39= PhotoImage(file='vengria.png')
quest40 = Button(root, image=quest39, highlightthickness=0, bd=0, command=gameover)


#6 уровень#########################################################################################

def game1level6():
    label9.pack_forget()
    vietnamlabel.place_forget()
    quest42.place_forget()
    quest44.place_forget()
    quest46.place_forget()
    quest48.place_forget()

    label10.pack()
    uzbeklabel.place(x=110, y=180)
    quest50.place(y=410, x=80)
    quest52.place(y=490, x=80)
    quest54.place(y=570, x=80)
    quest56.place(y=650, x=80)

label9 = Label(root, text="Счёт: " + str(score+5), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)

vietnamImage = PhotoImage(file='flag_vietnam.png')
vietnamImage = vietnamImage.subsample(2,2)
vietnamlabel = Label(root)
vietnamlabel.image = vietnamImage
vietnamlabel['image'] = vietnamImage

quest41 = PhotoImage(file='china.png')
quest42 = Button(root, image=quest41, highlightthickness=0, bd=0, command=gameover)

quest43 = PhotoImage(file='korea.png')
quest44 = Button(root, image=quest43, highlightthickness=0, bd=0, command=gameover)

quest45= PhotoImage(file='japan.png')
quest46 = Button(root, image=quest45, highlightthickness=0, bd=0, command=gameover)

quest47= PhotoImage(file='vietnam.png')
quest48 = Button(root, image=quest47, highlightthickness=0, bd=0, command=game1level6)


#7 уровень#########################################################################################

label10 = Label(root, text="Счёт: " + str(score+6), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)

uzbekImage = PhotoImage(file='flag_uzbekistan.png')
uzbekImage = uzbekImage.subsample(2,2)
uzbeklabel = Label(root)
uzbeklabel.image = vietnamImage
uzbeklabel['image'] = uzbekImage

quest49 = PhotoImage(file='kazahstan.png')
quest50 = Button(root, image=quest49, highlightthickness=0, bd=0, command=gameover)

quest51 = PhotoImage(file='uzbek.png')
quest52 = Button(root, image=quest51, highlightthickness=0, bd=0, command=win1)

quest53= PhotoImage(file='sydan.png')
quest54 = Button(root, image=quest53, highlightthickness=0, bd=0, command=gameover)

quest55= PhotoImage(file='irak.png')
quest56 = Button(root, image=quest55, highlightthickness=0, bd=0, command=gameover)






#Игра 2############################################################################################33

label100 = Label(root, text = "Выберите страну", font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=15)   #Название
label101 = Label(root, text = "по известному факту", font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=15)
label102 = Label(root, text="Счёт: " + str(score), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)                       #Счёт

#1 уровень############################################################################################

def game2level2():
    argentinaImagelabel.place_forget()
    quest104.place_forget()
    quest106.place_forget()
    quest108.place_forget()
    quest110.place_forget()
    label102.pack_forget()

    label103.pack()
    indiaImagelabel.place(x=50, y=220)
    quest112.place(y=410, x=80)
    quest114.place(y=490, x=80)
    quest116.place(y=570, x=80)
    quest118.place(y=650, x=80)

argentinaImage = PhotoImage(file='question_argentina.png')
argentinaImage = argentinaImage.subsample(1,1)
argentinaImagelabel = Label(root, highlightthickness=0, bd=0)
argentinaImagelabel.image = argentinaImage
argentinaImagelabel['image'] = argentinaImage

quest103 = PhotoImage(file='argentina.png')
quest104 = Button(root, image=quest103, highlightthickness=0, bd=0, command=game2level2)

quest105 = PhotoImage(file='brazilia.png')
quest106 = Button(root, image=quest105, highlightthickness=0, bd=0, command=gameover2)

quest107 = PhotoImage(file='korea.png')
quest108 = Button(root, image=quest107, highlightthickness=0, bd=0, command=gameover2)

quest109 = PhotoImage(file='china.png')
quest110 = Button(root, image=quest109, highlightthickness=0, bd=0, command=gameover2)


#2 уровень############################################################################################

def game2level3():
    indiaImagelabel.place_forget()
    quest112.place_forget()
    quest114.place_forget()
    quest116.place_forget()
    quest118.place_forget()
    label103.pack_forget()

    label104.pack()
    japanImagelabel.place(x=50, y=220)
    quest120.place(y=410, x=80)
    quest122.place(y=490, x=80)
    quest124.place(y=570, x=80)
    quest126.place(y=650, x=80)


label103 = Label(root, text="Счёт: " + str(score+1), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)

indiaImage = PhotoImage(file='question_india.png')
indiaImage = indiaImage.subsample(1,1)
indiaImagelabel = Label(root, highlightthickness=0, bd=0)
indiaImagelabel.image = indiaImage
indiaImagelabel['image'] = indiaImage

quest111 = PhotoImage(file='china.png')
quest112 = Button(root, image=quest111, highlightthickness=0, bd=0, command=gameover2)

quest113 = PhotoImage(file='vietnam.png')
quest114 = Button(root, image=quest113, highlightthickness=0, bd=0, command=gameover2)

quest115 = PhotoImage(file='india.png')
quest116 = Button(root, image=quest115, highlightthickness=0, bd=0, command=game2level3)

quest117 = PhotoImage(file='japan.png')
quest118 = Button(root, image=quest117, highlightthickness=0, bd=0, command=gameover2)



#3 уровень###########################################################################################

def game2level4():
    japanImagelabel.place_forget()
    quest120.place_forget()
    quest122.place_forget()
    quest124.place_forget()
    quest126.place_forget()
    label104.pack_forget()

    label105.pack()
    liviaImagelabel.place(x=50, y=220)
    quest128.place(y=410, x=80)
    quest130.place(y=490, x=80)
    quest132.place(y=570, x=80)
    quest134.place(y=650, x=80)


label104 = Label(root, text="Счёт: " + str(score+2), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)

japanImage = PhotoImage(file='question_japan.png')
japanImage = japanImage.subsample(1,1)
japanImagelabel = Label(root, highlightthickness=0, bd=0)
japanImagelabel.image = japanImage
japanImagelabel['image'] = japanImage

quest119 = PhotoImage(file='dania.png')
quest120 = Button(root, image=quest119, highlightthickness=0, bd=0, command=gameover2)

quest121 = PhotoImage(file='usa.png')
quest122 = Button(root, image=quest121, highlightthickness=0, bd=0, command=gameover2)

quest123 = PhotoImage(file='britan.png')
quest124 = Button(root, image=quest123, highlightthickness=0, bd=0, command=gameover2)

quest125 = PhotoImage(file='japan.png')
quest126 = Button(root, image=quest125, highlightthickness=0, bd=0, command=game2level4)


#4 уровень############################################################################################

def game2level5():
    liviaImagelabel.place_forget()
    quest128.place_forget()
    quest130.place_forget()
    quest132.place_forget()
    quest134.place_forget()
    label105.pack_forget()

    label106.pack()
    chinaImagelabel.place(x=50, y=220)
    quest136.place(y=410, x=80)
    quest138.place(y=490, x=80)
    quest140.place(y=570, x=80)
    quest142.place(y=650, x=80)

label105 = Label(root, text="Счёт: " + str(score+3), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)

liviaImage = PhotoImage(file='question_livia.png')
liviaImage = liviaImage.subsample(1,1)
liviaImagelabel = Label(root, highlightthickness=0, bd=0)
liviaImagelabel.image = liviaImage
liviaImagelabel['image'] = liviaImage

quest127 = PhotoImage(file='egipet.png')
quest128 = Button(root, image=quest127, highlightthickness=0, bd=0, command=gameover2)

quest129 = PhotoImage(file='livia.png')
quest130 = Button(root, image=quest129, highlightthickness=0, bd=0, command=game2level5)

quest131 = PhotoImage(file='sydan.png')
quest132 = Button(root, image=quest131, highlightthickness=0, bd=0, command=gameover2)

quest133 = PhotoImage(file='pery.png')
quest134 = Button(root, image=quest133, highlightthickness=0, bd=0, command=gameover2)





#5 уровень##########################################################################################

def game2level6():
    chinaImagelabel.place_forget()
    quest136.place_forget()
    quest138.place_forget()
    quest140.place_forget()
    quest142.place_forget()
    label106.pack_forget()

    label107.pack()
    canadaImagelabel.place(x=50, y=220)
    quest144.place(y=410, x=80)
    quest146.place(y=490, x=80)
    quest148.place(y=570, x=80)
    quest150.place(y=650, x=80)

label106 = Label(root, text="Счёт: " + str(score+4), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)

chinaImage = PhotoImage(file='question_china.png')
chinaImage = chinaImage.subsample(1,1)
chinaImagelabel = Label(root, highlightthickness=0, bd=0)
chinaImagelabel.image = chinaImage
chinaImagelabel['image'] = chinaImage

quest135 = PhotoImage(file='germany.png')
quest136 = Button(root, image=quest135, highlightthickness=0, bd=0, command=gameover2)

quest137 = PhotoImage(file='india.png')
quest138 = Button(root, image=quest137, highlightthickness=0, bd=0, command=gameover2)

quest139 = PhotoImage(file='turkey.png')
quest140 = Button(root, image=quest139, highlightthickness=0, bd=0, command=gameover2)

quest141 = PhotoImage(file='china.png')
quest142 = Button(root, image=quest141, highlightthickness=0, bd=0, command=game2level6)


#6 уровень##########################################################################################

def game2level7():
    canadaImagelabel.place_forget()
    quest144.place_forget()
    quest146.place_forget()
    quest148.place_forget()
    quest150.place_forget()
    label107.pack_forget()

    label108.pack()
    franchImagelabel.place(x=50, y=220)
    quest152.place(y=410, x=80)
    quest154.place(y=490, x=80)
    quest156.place(y=570, x=80)
    quest158.place(y=650, x=80)

label107 = Label(root, text="Счёт: " + str(score+5), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)

canadaImage = PhotoImage(file='question_canada.png')
canadaImage = canadaImage.subsample(1,1)
canadaImagelabel = Label(root, highlightthickness=0, bd=0)
canadaImagelabel.image = canadaImage
canadaImagelabel['image'] = canadaImage

quest143 = PhotoImage(file='canada.png')
quest144 = Button(root, image=quest143, highlightthickness=0, bd=0, command=game2level7)

quest145 = PhotoImage(file='russia.png')
quest146 = Button(root, image=quest145, highlightthickness=0, bd=0, command=gameover2)

quest147 = PhotoImage(file='sweeden.png')
quest148 = Button(root, image=quest147, highlightthickness=0, bd=0, command=gameover2)

quest149 = PhotoImage(file='kuba.png')
quest150 = Button(root, image=quest149, highlightthickness=0, bd=0, command=gameover2)


#7 уровень###########################################################################################

label108 = Label(root, text="Счёт: " + str(score+6), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)

franchImage = PhotoImage(file='question_franch.png')
franchImage = franchImage.subsample(1,1)
franchImagelabel = Label(root, highlightthickness=0, bd=0)
franchImagelabel.image = franchImage
franchImagelabel['image'] = franchImage

quest151 = PhotoImage(file='usa.png')
quest152 = Button(root, image=quest151, highlightthickness=0, bd=0, command=gameover2)

quest153 = PhotoImage(file='kazahstan.png')
quest154 = Button(root, image=quest153, highlightthickness=0, bd=0, command=gameover2)

quest155 = PhotoImage(file='serbia.png')
quest156 = Button(root, image=quest155, highlightthickness=0, bd=0, command=gameover2)

quest157 = PhotoImage(file='franch.png')
quest158 = Button(root, image=quest157, highlightthickness=0, bd=0, command=win1)






#Игра 3########################################################################################################3

label200 = Label(root, text = "Выберите страну", font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=15)   #Название
label201 = Label(root, text = "по фотографии", font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=15)
label202 = Label(root, text="Счёт: " + str(score), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)


#1 уровень#######################################################################################################

def game3level2():
    rusImagelabel.place_forget()
    quest302.place_forget()
    quest304.place_forget()
    quest306.place_forget()
    quest308.place_forget()
    label202.pack_forget()

    label203.pack()
    usaImagelabel.place(x=75, y=220)
    quest310.place(y=410, x=80)
    quest312.place(y=490, x=80)
    quest314.place(y=570, x=80)
    quest316.place(y=650, x=80)


rusImage = PhotoImage(file='game3perm.png')
rusImage = rusImage.subsample(4,4)
rusImagelabel = Label(root, highlightthickness=0, bd=0)
rusImagelabel.image = rusImage
rusImagelabel['image'] = rusImage

quest301 = PhotoImage(file='kazahstan.png')
quest302 = Button(root, image=quest301, highlightthickness=0, bd=0, command=gameover3)

quest303 = PhotoImage(file='brazilia.png')
quest304 = Button(root, image=quest303, highlightthickness=0, bd=0, command=gameover3)

quest305 = PhotoImage(file='franch.png')
quest306 = Button(root, image=quest305, highlightthickness=0, bd=0, command=gameover3)

quest307 = PhotoImage(file='russia.png')
quest308 = Button(root, image=quest307, highlightthickness=0, bd=0, command=game3level2)


#2 уровень###############################################################################################

def game3level3():
    usaImagelabel.place_forget()
    quest310.place_forget()
    quest312.place_forget()
    quest314.place_forget()
    quest316.place_forget()
    label203.pack_forget()

    label204.pack()
    japaImagelabel.place(x=75, y=220)
    quest318.place(y=410, x=80)
    quest320.place(y=490, x=80)
    quest322.place(y=570, x=80)
    quest324.place(y=650, x=80)

label203 = Label(root, text="Счёт: " + str(score+1), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)

usaImage = PhotoImage(file='game3newyork.png')
usaImage = usaImage.subsample(4,4)
usaImagelabel = Label(root, highlightthickness=0, bd=0)
usaImagelabel.image = usaImage
usaImagelabel['image'] = usaImage

quest309 = PhotoImage(file='germany.png')
quest310 = Button(root, image=quest309, highlightthickness=0, bd=0, command=gameover3)

quest311 = PhotoImage(file='usa.png')
quest312 = Button(root, image=quest311, highlightthickness=0, bd=0, command=game3level3)

quest313 = PhotoImage(file='greek.png')
quest314 = Button(root, image=quest313, highlightthickness=0, bd=0, command=gameover3)

quest315 = PhotoImage(file='pery.png')
quest316 = Button(root, image=quest315, highlightthickness=0, bd=0, command=gameover3)


#3 уровень#################################################################################################

def game3level4():
    japaImagelabel.place_forget()
    quest318.place_forget()
    quest320.place_forget()
    quest322.place_forget()
    quest324.place_forget()
    label204.pack_forget()

    label205.pack()
    londonImagelabel.place(x=75, y=220)
    quest326.place(y=410, x=80)
    quest328.place(y=490, x=80)
    quest330.place(y=570, x=80)
    quest332.place(y=650, x=80)

label204 = Label(root, text="Счёт: " + str(score+2), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)

japaImage = PhotoImage(file='game3tokio.png')
japaImage = japaImage.subsample(4,4)
japaImagelabel = Label(root, highlightthickness=0, bd=0)
japaImagelabel.image = japaImage
japaImagelabel['image'] = japaImage

quest317 = PhotoImage(file='korea.png')
quest318 = Button(root, image=quest317, highlightthickness=0, bd=0, command=gameover3)

quest319 = PhotoImage(file='china.png')
quest320 = Button(root, image=quest319, highlightthickness=0, bd=0, command=gameover3)

quest321 = PhotoImage(file='japan.png')
quest322 = Button(root, image=quest321, highlightthickness=0, bd=0,command=game3level4)

quest323 = PhotoImage(file='dania.png')
quest324 = Button(root, image=quest323, highlightthickness=0, bd=0, command=gameover3)



#4 уровень#############################################################################################

def game3level5():
    londonImagelabel.place_forget()
    quest326.place_forget()
    quest328.place_forget()
    quest330.place_forget()
    quest332.place_forget()
    label205.pack_forget()

    label206.pack()
    indiImagelabel.place(x=75, y=220)
    quest334.place(y=410, x=80)
    quest336.place(y=490, x=80)
    quest338.place(y=570, x=80)
    quest340.place(y=650, x=80)

label205 = Label(root, text="Счёт: " + str(score+3), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)

londonImage = PhotoImage(file='game3london.png')
londonImage = londonImage.subsample(4,4)
londonImagelabel = Label(root, highlightthickness=0, bd=0)
londonImagelabel.image = londonImage
londonImagelabel['image'] = londonImage

quest325 = PhotoImage(file='britan.png')
quest326 = Button(root, image=quest325, highlightthickness=0, bd=0, command=game3level5)

quest327 = PhotoImage(file='chexia.png')
quest328 = Button(root, image=quest327, highlightthickness=0, bd=0, command=gameover3)

quest329 = PhotoImage(file='irak.png')
quest330 = Button(root, image=quest329, highlightthickness=0, bd=0, command=gameover3)

quest331 = PhotoImage(file='slovakia.png')
quest332 = Button(root, image=quest331, highlightthickness=0, bd=0, command=gameover3)



#5 уровень##########################################################################################33

def game3level6():
    indiImagelabel.place_forget()
    quest334.place_forget()
    quest336.place_forget()
    quest338.place_forget()
    quest340.place_forget()
    label206.pack_forget()

    label207.pack()
    rioiImagelabel.place(x=75, y=220)
    quest342.place(y=410, x=80)
    quest344.place(y=490, x=80)
    quest346.place(y=570, x=80)
    quest348.place(y=650, x=80)

label206 = Label(root, text="Счёт: " + str(score+4), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)

indiImage = PhotoImage(file='game3india.png')
indiImage = indiImage.subsample(4,4)
indiImagelabel = Label(root, highlightthickness=0, bd=0)
indiImagelabel.image = indiImage
indiImagelabel['image'] = indiImage

quest333 = PhotoImage(file='egipet.png')
quest334 = Button(root, image=quest333, highlightthickness=0, bd=0, command=gameover3)

quest335 = PhotoImage(file='vengria.png')
quest336 = Button(root, image=quest335, highlightthickness=0, bd=0, command=gameover3)

quest337 = PhotoImage(file='spain.png')
quest338 = Button(root, image=quest337, highlightthickness=0, bd=0, command=gameover3)

quest339 = PhotoImage(file='india.png')
quest340 = Button(root, image=quest339, highlightthickness=0, bd=0, command=game3level6)


#6 уровень########################################################################################

label207 = Label(root, text="Счёт: " + str(score+5), font = ('Bookman Old Style', 27), bg = '#87CEFA', fg = 'black', pady=10)

rioiImage = PhotoImage(file='game3rio_de_janeyro.png')
rioiImage = rioiImage.subsample(4,4)
rioiImagelabel = Label(root, highlightthickness=0, bd=0)
rioiImagelabel.image = rioiImage
rioiImagelabel['image'] = rioiImage

quest341 = PhotoImage(file='brazilia.png')
quest342 = Button(root, image=quest341, highlightthickness=0, bd=0, command=win1)

quest343 = PhotoImage(file='livia.png')
quest344 = Button(root, image=quest343, highlightthickness=0, bd=0, command=gameover3)

quest345 = PhotoImage(file='vietnam.png')
quest346 = Button(root, image=quest345, highlightthickness=0, bd=0, command=gameover3)

quest347 = PhotoImage(file='uzbek.png')
quest348 = Button(root, image=quest347, highlightthickness=0, bd=0, command=gameover3)




root.mainloop()