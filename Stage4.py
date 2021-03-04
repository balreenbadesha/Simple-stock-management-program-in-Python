# Stage 4 -> Balreen Kaur Badesha, 110299719

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
    print('')	

#Printing of menu items
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
          '(L)oad product list\n'+
          '(I)ncrease stock level\n'+
          '(R)eport products and stock\n'+
          '(X)port products and stock\n'+
          '(C)ompare stock levels\n'+
          '(Q)uit\n')
    c = 0
    while (c < 26):
        print('-',end = '')
        c = c + 1

# Adding new products
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

    print(productName, 'was added to the list of products')

#Increasing Stock Levels    
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

        # check index of product and update the stock level
        check = False
        for index in range (0, len(productList),2):
            if productName.lower() == productList[index].lower():
                check = True
                stockLevel = input('Stock Level: ')
                if (stockLevel.isdigit() == True):
                    e = index + 1
                    total = productList[e] + int(stockLevel)
                    productList[e] = total
                    print(productName.capitalize(), 'has been updated to a stock of', total, 'products.\n')
                else:
                    print('*** Error: Incorrect value entered\n')        
        if (check == False):
                 print('*** Error: Product not listed\n')
    else:
        print('\n***No products defined')

# Load Product List
def loadProductList(count):
    a = 0
    while (a < 26):
            print('-',end = '')
            a = a + 1
            
    numRecords = 0 
    productFileName = input('\nFile to Load: ')

    #reading file for its content
    try: 
        fileProducts = open (productFileName , 'r')
        fileContents = fileProducts.readlines()

        for x in fileContents:
            check = False
            x = x.rstrip()
            #check to see if product exist in the product list
            if (len(productList) > 0): 
                for index in range (0, len(productList),2):
                    if x.lower() == productList[index].lower():
                        print('***',x ,'was not loaded as product already exists')
                        check = True
            #If it doesnt exist add it to the product list
            if(check == False):
                productList.append(x)
                productList.append(0)
                count = count + 2
                numRecords = numRecords + 1

        fileProducts.close()
        print(numRecords, 'records loaded\n')
        
    except FileNotFoundError:
        print('***File not found')
        
    return count

# Export Stock Levels
def exportProductStock():
    
    exportFileName = input('Filename: ')
    fileEx = open(exportFileName, 'w')

    # Write to the file
    for index in range (0, (len(productList))- 1,2):
        d = index + 1
        fileEx.write(productList[index] + ','+ str(productList[d]) + '\n')

    fileEx.close()

    print('Data exported as' , exportFileName)
    print('')
    
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

    c = 0
    while (c < 26):
            print('-',end = '')
            c = c + 1

    f = 0
    # Calculating the total stock 
    for index in range (1,(len(productList)),2):
        f = f + int(productList[index])

    print('\n{:15s} {}'.format('Total', f))

    c = 0
    while (c < 26):
            print('-',end = '')
            c = c + 1

    print('\n')       
    

def compareStockLevels():
    import csv
    productFileName = input('Filename: ')

    print('')
    fileList = []
    listCompare = []
    check = False
    #Reading the csv file and putting it in a list
    try: 
        with open (productFileName) as csvfile:
            readCSV = csv.reader(csvfile, delimiter = ',')
            for row in readCSV:
                fileList.append(row[0])
                fileList.append(row[1])
        check = True
                
    except FileNotFoundError:
        print('*** Error: File not found')

    # if the file can be loaded then print the table
    if (check == True):     
        a = 0
        while (a < 39):
                print('-',end = '')
                a = a + 1
                
        print('\n{:15s} {:9s} {:6s} {}'.format('Product', 'Stock', 'Old', 'Change'))

        b = 0
        while (b < 39):
                print('-',end = '')
                b = b + 1
        print('')

        # Combining stock levels and product list in a single list
        for i in range (0, (len(productList))- 1,2):
            j = i + 1
            # Adding identical product records together
            if productList[i] in fileList:
                value = fileList.index(productList[i]) + 1
                listCompare.append(productList[i])
                listCompare.append(productList[j])
                listCompare.append(fileList[value])
                difference = int(productList[j]) - int(fileList[value])
                listCompare.append(difference)
            # Adding different products
            else:
                listCompare.append(productList[i])
                listCompare.append(productList[j])
                listCompare.append('0')
                listCompare.append(productList[j])

        # Adding remaining records from file 
        for i in range (0, (len(fileList))-1,2):
            j = i + 1
            if fileList[i] not in productList:
                listCompare.append(fileList[i])
                listCompare.append('0')
                listCompare.append(fileList[j])
                difference = 0 - int(fileList[j])
                listCompare.append(difference)

        # Printing of summary table
        totalStock = 0
        totalOld = 0
        totalChange = 0
        for index in range (0, (len(listCompare))- 1,4):
            d = index + 1
            e = d + 1
            f = e + 1
            totalStock = totalStock + int(listCompare[d])
            totalOld = totalOld + int(listCompare[e])
            totalChange = totalChange + int(listCompare[f])
            print('{:15s} {:9s} {:6s} {}'.format(listCompare[index], str(listCompare[d]), listCompare[e], listCompare[f] ))

        e = 0
        while (e < 39):
                print('-',end = '')
                e = e + 1

        print('\n{:15s} {:9s} {:6s} {}'.format('Total', str(totalStock), str(totalOld), totalChange))

        g = 0
        while (g < 39):
                print('-',end = '')
                g = g + 1
        print('\n')

heading()

choice = True

productList = []

count = 0

# Loop for user choice

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
            count = loadProductList(count)

        elif(inpChoice == 'R'):
            summary()

        elif(inpChoice == 'X'):
            exportProductStock()

        elif(inpChoice == 'C'):
            compareStockLevels()

        elif(inpChoice == 'Q'):
            print('Goodbye')
            choice = False
    

