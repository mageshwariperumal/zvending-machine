print("welcome to ccd")
print("Enjoy your example1")
print("coffee")
print("tea")
print("soup")
print("beversages")
coffee=input("c")#press enter to continue the next one
tea=input("t")
soup=input("s")
beverages=input("b")
w=int(input("enter 1 to continue 0 to exit:")) 
while(w==1): 
    ch=input("Enter the choice:")
    if(ch=="c"):
        print("1.espresso coffee")
        print("2.capuccino coffee")
        print("3.latte coffee")
        p=int(input("enter the value 1 to 3:")) #pres enter to go to next process
        if(p==1):
              espresso_coffee=input("a")
              print(espresso_coffee)
              print("welcome to ccd")
              print("Enjoy your espresso coffee")
        elif(p==2):
            capuccino_coffee=input("b")
            print(capuccino_coffee)
            print("welcome to ccd")
            print("Enjoy your capuccino coffee")
        elif(p==3):
            latte_coffee=input("c")
            print(latte_coffee)
            print("welcome to ccd")
            print("Enjoy your latte coffee")
        else:
            print("invalid")
    elif(ch=="t"):
        print(tea)
        print("1.plain tea")
        print("2.assam tea")
        print("3.ginger tea")
        print("4.cardamom tea")
        print("5.masala tea")
        print("6.lemon tea")
        print("7.masala tea")
        print("8.green tea")
        q=int(input("enter the value 1 to 8:"))#pres enter to go to next process
        if(q==1):
            plain_tea=input("a")
            print(plain_tea)
            print("welcome to ccd")
            print("Enjoy your plain tea")
        elif(q==2):
            assam_tea=input("b")
            print(assam_tea)
            print("welcome to ccd")
            print("Enjoy your assam tea")
        elif(q==3):
            ginger_tea=input("c")
            print(ginger_tea)
            print("welcome to ccd")
            print("Enjoy your ginger tea")
        elif(q==4):
            cardamom_tea=input("d")
            print(cardamom_tea)
            print("welcome to ccd")
            print("Enjoy your cardamom tea")
        elif(q==5):
            masala_tea=input("e")
            print(masala_tea)
            print("welcome to ccd")
            print("Enjoy your masala tea")
        elif(q==6):
            lemon_tea=input("f")
            print(lemon_tea)
            print("welcome to ccd")
            print("Enjoy your lemon tea")
        elif(q==7):
            green_tea=input("g")
            print(green_tea)
            print("welcome to ccd")
            print("Enjoy your green tea")
        elif(q==8):
            organic_darjeeling_tea=input("h")
            print(organic_darjeeling_tea)
            print("welcome to ccd")
            print("Enjoy your organic darjeeling tea")
        else:
            print("invalid")
    elif(ch=="s"):
        print("1.hot and sour soup")#pres enter to go to next process
        print("2.veg corn soup")
        print("3.tomato soup")
        print("4.spicy tomato soup")
        r=int(input("Enter the value 1 to 4:"))
        if(r==1):
            hot_and_sour_soup=input("a")
            print(hot_and_sour_soup)
            print("welcome to ccd")
            print("Enjoy your hot and sour soup")
        elif(r==2):
            veg_corn_soup=input("b")
            print(veg_corn_soup)
            print("welcome to ccd")
            print("Enjoy your veg corn soup")
        elif(r==3):
            tomato_soup=input("c")
            print(tomato_soup)
            print("welcome to ccd")
            print("Enjoy your tomato soup")
        elif(r==4):
            spicy_tomato_soup=input("d")
            print(spicy_tomato_soup)
            print("welcome to ccd")
            print("Enjoy your spicy tomato soup")
        else:
            print("invalid")
    elif(ch=="b"):
        print("1.chocolate drink")
        print("2.badam drink")
        print("3.badam pista drink")
        s=int(input("Enter the value of 1 to 3:"))#pres enter to go to next process
        if(s==1):
            hot_chocolate_drink=input("a")
            print(hot_chocolate_drink)
            print("welcome to ccd")
            print("Enjoy your hot chocolate drink")
        elif(s==2):
            badam_drink=input("b")
            print(badam_drink)
            print("welcome to ccd")
            print("Enjoy your badam drink")
        elif(s==3):
            badam_pista_drink=input("c")
            print(badam_pista_drink)
            print("welcome to ccd")
            print("Enjoy your badam pista drink")
        else:
            print("invalid")
    else:
        print("invalid")
    break;
#program name= vending machine
#developer name=p.mageshwari


