# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:27:57 2020

@author: Shane Vandewinckel
@University: Norwich University
"""

#Category Begin

c1 = input("Category 1: ")
itemcat1 = input("Enter Item1 in Cat1: ")
pricecat1 = input("Enter Price of Item1 in Cat1: ")
qitemcat1 = input("Enter Quantity of Item1 in Cat1: ")
item2cat1 = input("Enter Item2 in Cat 2: ")
price2cat1 = input("Enter Price of Item2 in Cat1: ")
qitem2cat1 = input("Enter Quantity of Item2 in Cat1: ")

c2 = input("Category 2: ")
itemcat2 = input("Enter Item1 in Cat2: ")
pricecat2 = input("Enter Price of Item1 in Cat2: ")
qitemcat2 = input("Enter Quantity of Item1 in Cat2: ")
item2cat2 = input("Enter Item2 in Cat 2: ")
price2cat2 = input("Enter Price of Item2 in Cat2: ")
qitem2cat2 = input("Enter Quantity of Item2 in Cat2: ")

c3 = input("Category 3: ")
itemcat3 = input("Enter Item1 in Cat3: ")
pricecat3 = input("Enter Price of Item1 in Cat3: ")
qitemcat3 = input("Enter Quantity of Item1 in Cat3: ")
item2cat3 = input("Enter Item2 in Cat3: ")
price2cat3 = input("Enter Price of Item2 in Cat3: ")
qitem2cat3 = input("Enter Quantity of Item2 in Cat3: ")

c4 = input("Category 4: ")
itemcat4 = input("Enter Item1 in Cat4: ")
pricecat4 = input("Enter Price of Item1 in Cat4: ")
qitemcat4 = input("Enter Quantity of Item1 in Cat4: ")
item2cat4 = input("Enter Item2 in Cat4: ")
price2cat4 = input("Enter Price of Item2 in Cat4: ")
qitem2cat4 = input("Enter Quantity of Item2 in Cat4: ")

c5 = input("Category 5: ")
itemcat5 = input("Enter Item1 in Cat5: ")
pricecat5 = input("Enter Price of Item1 in Cat5: ")
qitemcat5 = input("Enter Quantity of Item1 in Cat5: ")
item2cat5 = input("Enter Item2 in Cat5: ")
price2cat5 = input("Enter Price of Item2 in Cat5: ")
qitem2cat5 = input("Enter Quantity of Item2 in Cat5: ")

#Category End
#Calculations Begin

_tax = input("Enter Percent Tax: ")

_total_itemCount = (int(qitemcat1) + int(qitem2cat1)) + (int(qitemcat2) + int(qitem2cat2)) + (int(qitemcat3) + int(qitem2cat3)) + (int(qitemcat4) + int(qitem2cat4)) + (int(qitemcat5) + int(qitem2cat5))

_total_sub = int(qitemcat1) * float(pricecat1) + int(qitemcat2) * float(pricecat2) + int(qitemcat3) * float(pricecat3) + int(qitemcat4) * float(pricecat4) + int(qitemcat5) * float(pricecat5)
_total_tax = ((float(_tax)/100) + 1) * _total_sub

_Ftotal_sub = _total_sub
_pointsE = int(_Ftotal_sub)*5
_tpoints = int(_pointsE)

#print("Tax: ", _tax, "\nTotal Items: ", _total_itemCount, "\nSub Total", format(_total_sub, '.2f'), "\nTotal Due: ", format(_total_tax, '.2f'))
#Calculations End
#Reciept Gen Begin
print("")
print("               ....                                                                             ")   
print("         ,/((((((((((,                                                                          ")   
print("      .((((((((((((((.    ,*//(//*.       .,//////,.*////////////.   ,*/////*     .*//////,     ")   
print("     /((((((((*,.,/(/ ./(((((((((((((,  /((((((((((*((((((((((((*./(((((((((/  *(((((((((((((*  ")   
print("    /((((((/.       ./((((((///(((((((*((((((,  .*.*/*((((((/*//(((((((/**/(**(((((((//(((((((/ ")   
print("   .(((((((*        ((((((,     *((((((((((((((((/.  .((((((.  /(((((*      *(((((/     ,(((((/ ")   
print("   .(((((((((*,,*/(/((((((.    ,((((((. ,*/((((((((. /(((((*  .((((((,     ./(((((*    ./(((((* ")   
print("    .((((((((((((((./(((((((((((((((/./((***/(((((* ,(((((/    /(((((((((((,*((((((((((((((((,  ")   
print("      ,/((((((((((*  ,((((((((((((*..(((((((((((/.  /(((((.     ,((((((((((  ./(((((((((((/,,,. ")   
print("            ..           ..,,..         ..,,.       ......          .,,...       ..,,..         ")   
print("    /##########################/(#( *#( *####( *#(,*(###/./#(. ,####/,(###, /##(  (#/  *####*   ")   
print("    *///////////////////////////*#(/##(/#(,(#((#####/ .(####/  /##(/*(#((*.(#((#,,##*  (#(//    ")   
print("    ,***************************,(##*/##( *#(,,(#/(#(((#(/##((/(#(///(*(########((##((*(#(/*    ")   
print("    ............................. ..  ..   ..  ..   ...   .... ....  ...  ..   ....... ....     ")   
print("")
print("")
print("                                      Rochester #891                                            ")
print("                                     335 Westfall Rd                                            ")
print("                                    Rochester, NY 14620                                         ")
print("")
print("")
print("                                  Member Number 1121494328                                      ")
print("                                        ", c1)
print("                          ", "E     ", "QTY", qitemcat1, "          ", itemcat1, "     ", pricecat1)
print("                          ", "E     ", "QTY", qitem2cat1, "          ", item2cat1, "     ", price2cat1)
print("                                        ", c2)
print("                          ", "E     ", "QTY", qitemcat2, "          ", itemcat2, "     ", pricecat2)
print("                          ", "E     ", "QTY", qitem2cat2, "          ", item2cat2, "     ", price2cat2)
print("                                        ", c3)
print("                          ", "E     ", "QTY", qitemcat3, "          ", itemcat3, "     ", pricecat3)
print("                          ", "E     ", "QTY", qitem2cat3, "          ", item2cat3, "     ", price2cat3)
print("                                        ", c4)
print("                          ", "E     ", "QTY", qitemcat4, "          ", itemcat4, "     ", pricecat4)
print("                          ", "E     ", "QTY", qitem2cat4, "          ", item2cat4, "     ", price2cat4)
print("                                        ", c5)
print("                          ", "E     ", "QTY", qitemcat5, "          ", itemcat5, "     ", pricecat5)
print("                          ", "E     ", "QTY", qitem2cat5, "          ", item2cat5, "     ", price2cat5)
print("")
print("                          ","Tax: ", _tax, "\n                          Total Items: ", _total_itemCount, "\n                          Sub Total: $", format(_total_sub, '.2f'), "\n                          Total Due: $", format(_total_tax, '.2f'))
print("")
print("")
print("                          ","Points Earned: ", _pointsE)
print("")
print("")
print("                                       Thank You!                                               ")
print("                                   Please Come Again                                            ")