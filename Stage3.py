# Stage 3 -> Balreen Kaur Badesha, 110299719

# Heading Printing and Styling
def heading ():

    x = 0
    while (x < 26):
            print('*',end = '')
            x = x + 1
            
    print('\n{: ^26s}'.format('Stock Manager'))

    y = 0
    while (y < 26):
            print('*',end = '')
            y = y + 1
    print('\n')	

# Function for printing of menu items
def menu ():

    a = 0
    while (a < 26):
            print('-',end = '')
            a = a + 1
        
    print('\nMenu')

    b = 0
    while (b < 26):
            print('-',end = '')
            b = b + 1
    print('')
    print('(A)dd a product\n'+
          '(I)ncrease stock level\n'+
          '(L)ist products and stock\n'+
          '(Q)uit')
    c = 0
    while (c < 26):
        print('-',end = '')
        c = c + 1

# Funtion for adding products
def addProduct(count):
    a = 0
    while (a < 26):
            print('-',end = '')
            a = a + 1

    productName = input('\nProduct Name: ')
    check = False
    if (productName != ""):
        # check to see if product exist
        for index in range (0, len(productList),2):
            if productName.lower() == productList[index].lower():
                check = True
                print('*** Error: Product already exists\n')
        # if check is false then add new product to list        
        if(check == False):
            productList.append(productName)
            productList.append(0)
            count = count + 2
            print(productName, 'was added to the list of products.\n')
    else:
        print('*** Error: Invalid Product Name')
    return count
                
def increaseStockLevel():

    a = 0
    while (a < 26):
            print('-',end = '')
            a = a + 1
    if (len(productList) > 0):        
        print('\nEnter a product from the following list:')
        # Printing of existing products
        for index in range (0, len(productList),2):
            print('{:3s}{}'.format(' ', productList[index]))

        productName = input('Product Name: ')

        # check index of product and update stock levels
        check = False
        for index in range (0, len(productList),2):
            if productName.lower() == productList[index].lower():
                check = True
                stockLevel = input('Stock Level: ')
                if (stockLevel.isdigit() == True):
                    e = index + 1
                    total = int(productList[e]) + int(stockLevel)
                    productList[e] = str(total)
                    print(productName.capitalize(), 'has been updated to a stock of', total, 'products.\n')
                else:
                    print('*** Error: Incorrect value entered\n')        
        if (check == False):
                 print('*** Error: Product not listed\n')
    else:
        print('\n***No products defined')
    
# Summary Printing and Styling
def summary ():

    a = 0
    while (a < 26):
            print('-',end = '')
            a = a + 1
            
    print('\n{:15s} {}'.format('Product', 'Stock'))

    b = 0
    while (b < 26):
            print('-',end = '')
            b = b + 1
    print('')

    # Printing of product list with stock levels
    for index in range (0, (len(productList))- 1,2):
        d = index + 1
        print('{:16s}{}'.format(productList[index], productList[d]))

    e = 0
    while (e < 26):
            print('-',end = '')
            e = e + 1
            
    # Calculating stock levels
    totalStock = 0 
    for index in range (1,(len(productList)),2):
        totalStock = totalStock + int(productList[index])

    print('\n{:15s} {}'.format('Total', totalStock))
    g = 0
    while (g < 26):
            print('-',end = '')
            g = g + 1
            
    print('\n\n')
        
heading()

choice = True

productList = []

count = 0

# Loop for users choice
while (choice == True):

    menu()
    inpChoice = input('\nYour Choice: ')

    print('\n')

    if (inpChoice != ""):
        inpChoice = inpChoice.upper()
        
        if(inpChoice == 'A'):
            count = addProduct(count)

        elif(inpChoice == 'I'):
            increaseStockLevel()

        elif(inpChoice == 'L'):
            summary()

        elif(inpChoice == 'Q'):
            print('Goodbye')
            choice = False
    

