print("********************************************************************* NIKKI FASHION MALL **************************************************************************")
print()
print()
print("************************************************************************** WELCOME ***************************************************************************************")
import pickle
import sys
import os

print("PRESS 1 TO START OR 2 TO END")
c=int(input("enter your choise"))

if c==1:
    dict={}
    def write():
        file =open("preeti.dat","ab")
        print("ENTER YOUR DETAILS")
        dict["name"]=input("ENTER YOUR NAME")
        dict["adress"]=input("ENTER YOUR ADDRESS")
        dict["phone"]=int(input("ENTER YOUR CONTACT NUMBER"))
        print("** THANK YOU FOR GIVING YOUR DATA **")
        pickle.dump(dict,file)
        file.close()
    def display():
        file=open("preeti.dat","rb")
        try:
            while True:
                disc=pickle.load(file)
                print(disc)
        except EOFError:
            pass
        file.close()
    def search():
        while True:
            print("* WHAT YOU WANT TO BUY *")
            print("menu \n 1=CLOTH \n 2=TOYS \n 3=MAKEUP EQUIPMENT \n 4=FOOD \n 6=exit")
            ch=int(input("** ENTER YOUR CHOICE **"))
            if ch==1:
                while True:
                    print("MENU \n 1=FOR MEN \n 2=FOR WOMEN \n 3=EXIT")
                    a=int(input("enter your choice"))
                    if a==1:
                        print("menu \n 1=age between 1-10 \n 2= age between 10-25 \n 3=above 25")
                        b=int(input("enter the age of those who want to buy the cloth"))
                        if b==1:
                            print("floor no=3")
                            print("2nd last shop from the right corner")
                            print("colour of the shop=**blue**")
                        elif b==2:
                            print("floor no=3")
                            print("corner shop from left")
                            print("colour of the shop=**red**")
                        else:
                            print("floor no=4")
                            print("first right shop from stairs")
                            print("colour=**white**")
                    elif a==2:
                        print("MENU \n 1=AGE BETWEEN 1-10 \n 2=AGE BETWEEN 10-25 \n 3=ABOVE 25 ")
                        k=int(input("enter the age of person for which you are buying the cloth"))
                        if k==1:
                            print("floor no=5")
                            print("2nd last shop from the right corner")
                            print("colour of the shop=**blue**")
                        elif k==2:
                            print("floor no=5")
                            print("corner shop from left")
                            print("colour of the shop=**red**")
                        elif k==3:
                            print("floor no=5")
                            print("last right shop")
                            print("colour=**white**")
                        else:
                            print("thankyou")
                            break
                    else:
                        print("THANK YOU ")
                        break
            elif ch==2:
                while True:
                    print("MENU \n 1=AGE BETWEEN 1-10 \n 2=ABOVE 10 \n 3=EXIT")
                    d=int(input("enter the age so we can give you toys accrding to thier ages:"))
                    if d==1:
                        print("floor no=1")
                        print("right side from the entry gate")
                        print("colour=**pink**")
                    elif d==2:
                        print("floor no=1")
                        print("left side from the entry gate:")
                        print("colour=**green**")
                    else:
                        print("** THANK YOU **")
                        break
            elif ch==3:
                while True:
                    print("floor no=1")
                    print("right side from the exit gate")
                    print("colour=** light pink**")
                    break
            elif ch==4:
                while True:
                    print("MENU CARD \n 1=VEGETRAINS \n 2=NON VEGETRAINS \n 3=DESERTS \n 4=EXIT")
                    p=int(input("enter your choise:"))
                    if p==1:
                        print("floor no=2")
                        print("right side from the stairs")
                        print("colour=brown")
                    elif p==2:
                        print("floor no=2")
                        print("left side from the stairs")
                        print("colour=black")
                    elif p==3:
                        print("floor no=2")
                        print("first right shop from the stairs")
                        print("colour=purple")
                    else:
                        print("**THANK YOU**")
                        break
            else:
                print("THANK YOU .. MAY YOU LIKE OUR SHOP..")
                break
    def update():
        f1=open("preeti.dat","rb")
        f2=open("temp.dat","ab")
        n=input("enter your name") 
        try:
            while True:
                data=pickle.load(f1)
                if data["name"]==n:
                    print("WHAT DO YOU WANT TO UPDATE")
                    print(" 1= NAME \n 2= ADDRESS \n 3= PHONE NUMBER")
                    ch=int(input("ENTER YOUR CHOISE"))
                    if ch==1:
                        data["name"]=input("ENTER YOU NAME")
                        pickle.dump(data,f2)
                    if ch==2:
                        data["adress"]=input("ENTER YOUR ADDRESS")
                        pickle.dump(data,f2)
                    if ch==3:
                        data["phone"]=int(input("ENTER YOUR PHONE NUMBER"))
                        pickle.dump(data,f2)
                else:
                    pickle.dump(data,f2)
        except EOFError:
            pass
        f1.close()
        f2.close()
        os.remove("preeti.dat")
        os.rename("temp.dat","preeti.dat")
        file=open("preeti.dat","rb")
        try:
            while True:
                std=pickle.load(file)
                print(std)
        except EOFError:
           pass
        file.close()
    def delete():
        f1=open("preeti.dat","rb")
        f2=open("temp.dat","ab")
        d=input("enter the name u want to delete")
        try:
            while True:
                data=pickle.load(f1)
                if data["name"]==d:
                    pass
                else:
                    pickle.dump(data,f2)
        except EOFError:
            pass
        f1.close()
        f2.close()
        os.remove("preeti.dat")
        os.rename("temp.dat","preeti.dat")
        file=open("preeti.dat","rb")
        print("record after deletion")
        try:
            while True:
                stud=pickle.load(file)                    #read from file
                print(stud)
        except EOFError:
            pass
        file.close()
    def end():
        print("THANK YOU")
        sys.exit

#main programming
    while True:
        print("\n1=WRITE MY DETAILS \n2=DISPLAY MY DETALS \n3=SEARCH ITEMS \n4=UPDATE MY DETAILS \n5=DELETE MY DETAILS  \n6=END ")
        ch=int(input("ENTER YOUR CHOICE"))
        if ch==1:
            write()
        if ch==2:
            display()
        if ch==3:
            search()
        if ch==4:
            update()
        if ch==5:
            delete()
        if ch==6:
            print("** THANK YOU **")

            sys.exit()


if c==2:
    print("** THANK YOU **")

    sys.exit()
