# Stage 1 -> Balreen Kaur Badesha, 110299719

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

# Summary Printing and Styling
def summary ():

    print('')
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
    for c in range (0, (len(productList))- 1,2):
        d = c + 1
        print('{:16s}{}'.format(productList[c], productList[d]))

    e = 0
    while (e < 26):
            print('-',end = '')
            e = e + 1
            
heading()

keepAskingForProducts = True

productList = []

#Loop to keep asking for products

while (keepAskingForProducts == True):
    productName = input('\nProduct Name: ')
    stockLevel = int(input('Stock Level: '))
    productList.append(productName)
    productList.append(stockLevel)

    print(productName, 'has been entered with a stock of', stockLevel, 'products.\n')
    askIfTheyWantToContinue = True

    # Loop to check if user wants to continue
    while (askIfTheyWantToContinue == True):

        continueAnswer = input('Do you wish to enter another record? (Y/N) ')

        # Change it to lowercase
        continueAnswer = continueAnswer.upper()

        # Check to see if they said yes
        if (continueAnswer == 'Y'):
            
            askIfTheyWantToContinue = False

        # Check to see if they said no
        if (continueAnswer == 'N'):
            
            askIfTheyWantToContinue = False
            
            keepAskingForProducts = False

summary()

