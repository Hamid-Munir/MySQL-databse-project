import pyinputplus as pyip

products = ['apple', 'orange']
productmenu = """

Slecet a Number for your Chosen Option 

[0]  Return to Main Menu
[1]  Print the products 
[2]  Create a new Products 
[3]  Update a Product 
[4]  Delete a Product 

"""
def new_product(products_data):
    newproduct = str(input('write name of new product: '))            
    products_data.append(newproduct)

    return products_data

def update_product(products_data):
    selectedproduct = pyip.inputMenu(products_data)
    updateproduct = str(input('Wrtite the new product: '))
            
    for n, i in enumerate(products_data):
        if i == selectedproduct:
            products_data[n]= updateproduct
            return products_data
        
def remove_product(products_data):
    remove_product = pyip.inputMenu(products_data)
    print('the product is removed')
    products_data.remove(remove_product)
    return products_data


def product_menu(products):
    
    while True:
        
        option2 = pyip.inputNum(productmenu, min = 0, max = 4)

        if option2 == 0:
            
            break

        elif option2 == 1:
            print(products)

        elif option2 == 2:
            new_product(products)
            
        elif option2 == 3:
            update_product(products)
            
        elif  option2 == 4:
            remove_product(products)


        
