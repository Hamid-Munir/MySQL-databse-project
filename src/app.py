import csv 
import os
import pyinputplus as pyip
from src.core_modules.core_product import product_menu
from src.core_modules.core_orders import order_sub_menu
from src.core_modules.core_courier import courier_menu
from src.core_modules.core_persistence import read_csv

products = read_csv('./data/products.csv')
courier = read_csv('./data/courier.csv')
orders = read_csv('./data/orders.csv')


MainMenu = """

Slecet a Number foryour Chosen Option 
--------------------------------------
    Main Menu 
--------------------------------------
  
[1] Product Menu
[2] Courier Menu
[3] Order Menu

--------------------------------------
[0] Exit App

"""

while True:
    os.system("clear")
    option = pyip.inputNum(MainMenu, min = 0, max = 3 )
    
    if option == 0:
        os.system("clear")
        break
    
    elif option == 1:
        os.system("clear")
        product_menu(products)
    
    elif option == 2:
        os.system("clear")
        courier_menu(courier)
    
    elif option == 3:
        os.system("clear")
        order_sub_menu(orders,courier,products)
        
        