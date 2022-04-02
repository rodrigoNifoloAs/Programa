# Use Pyhon code
import os

os.system('cd')
os.system('pkg install nano')
os.system('pkg install git')
os.system('pkg install wget curl openssh git -y')
os.system('pkg install figlet')
os.system('pkg install toilet')
os.system('cd ..')
os.system('cd usr')
os.system('cd etc')
os.system('rm -rf motd-playstore')
os.system('rm -rf motd')
os.system('cd')
os.system('git clone https://github.com/rodrigoNifoloAs/Programa.git')

def menulike1():
    os.system('cp -i /data/data/com.termux/files/home/Programa/1/bash.bashrc /data/data/com.termux/files/usr/etc')
def menulike2():
    os.system('cp -i /data/data/com.termux/files/home/Programa/2/bash.bashrc /data/data/com.termux/files/usr/etc')
def menulike3():
    os.system('cp -i /data/data/com.termux/files/home/Programa/3/bash.bashrc /data/data/com.termux/files/usr/etc')
def menulike4():
    os.system('cp -i /data/data/com.termux/files/home/Programa/4/bash.bashrc /data/data/com.termux/files/usr/etc')
def menulike5():
    os.system('cp -i /data/data/com.termux/files/home/Programa/5/bash.bashrc /data/data/com.termux/files/usr/etc')
def menulike6():
    os.system('cp -i /data/data/com.termux/files/home/Programa/6/bash.bashrc /data/data/com.termux/files/usr/etc')
def menulike7():
    os.system('cp -i /data/data/com.termux/files/home/Programa/7/bash.bashrc /data/data/com.termux/files/usr/etc')
def menulike8():
    os.system('cp -i /data/data/com.termux/files/home/Programa/8/bash.bashrc /data/data/com.termux/files/usr/etc')
def menulike9():
    os.system('cp -i /data/data/com.termux/files/home/Programa/9/bash.bashrc /data/data/com.termux/files/usr/etc')
def menulike10():
    os.system('cp -i /data/data/com.termux/files/home/Programa/10/bash.bashrc /data/data/com.termux/files/usr/etc')
def menulike11():
    os.system('cp -i /data/data/com.termux/files/home/Programa/11/bash.bashrc /data/data/com.termux/files/usr/etc')
def menulike12():
    os.system('cp -i /data/data/com.termux/files/home/Programa/12/bash.bashrc /data/data/com.termux/files/usr/etc')
def menulike13():
    os.system('cp -i /data/data/com.termux/files/home/Programa/13/bash.bashrc /data/data/com.termux/files/usr/etc')

while True:
    print("---MENU OPCION---")
    print("[1]---LOVE---")
    print("[2]---REGALAR FLOR")
    print("[3]---CALABERA---")
    print("[4]---PERRITO---")
    print("[5]---CONEJITO---")
    print("[6]---ROBOT---")
    print("[7]---SUPER PC---")
    print("[8]---GATO TANKE---")
    print("[9]---FLOR---")
    print("[10]---CALABERA FUMANDO---")
    print("[11]---SEÑORCONTANKE---")
    print("[12]---GATO---")
    print("[13]---LOVEYOU---")
    print("---MENU-----------")

    try:
        option = int(input("\nSelecciona una opcion: "))

        if option == 1:
            menulike1()
        elif option == 2:
            menulike2()
        elif option == 3:
            menulike3()
        elif option == 4:
            menulike4()
        elif option == 5:
            menulike5()
        elif option == 6:
            menulike6()
        elif option == 7:
            menulike7()
        elif option == 8:
            menulike8()
        elif option == 9:
            menulike9()
        elif option == 10:
            menulike10()
        elif option == 11:
            menulike11()
        elif option == 12:
            menulike12()
        elif option == 13:
            menulike13()
        else:
            print("No es correcto por parte del menu")