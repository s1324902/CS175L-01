#CS175L-01
#Ryan Basile
#Stocks

COMMISSION_RATE=float(input('What was the Comission Rate?: '))
NUM_SHARES=float(input('How many shares did you purchase?: '))
PURCHASE_PRICE=float(input('What was the purchase price?: ' ))
SELLING_PRICE=float(input('What was the selling price?: '))
amountPaidForStock = NUM_SHARES*PURCHASE_PRICE
purchaseCommission=COMMISSION_RATE*amountPaidForStock
totalPaid=amountPaidForStock+purchaseCommission
stockSoldFor=NUM_SHARES*SELLING_PRICE
sellingCommission=COMMISSION_RATE*stockSoldFor
totalRecieved=stockSoldFor-sellingCommission
profitOrLoss=totalRecieved-totalPaid
print('Amount Paid for stock: $',amountPaidForStock)
print('Commission paid on the purchase: $',purchaseCommission)
print('Amount the stock sold for: $',stockSoldFor)
print('Commission paid om the sale: $',sellingCommission)
print('Profit (or loss if negative): $',profitOrLoss)
