def main ():

#Calculate total price of block of stocks CalcAmount = NumberStock * PurchasePrice entered from user
  def CalcAmount (shares,price): #numberShares * PurchasePrice
    return shares * price 

#Calculate commission CalcAmount * CommissionRate (0.015)
  def CalcCommission (amount,rate): #CalcAmount * CommissionRate
    return amount * rate 



  #commission rate constant
  COMMISSION_RATE = 0.015

#input from user, number of shares in the block, purchase price per share, and sell price per share 
  numberShares= float (input ('Please enter the number of shares in the block '))

  PurchasePrice= float (input ('Please enter the purchase price per share $'))

  SellPrice= float (input ('Please enter the selling price per share $ '))


#process
#calcAmount cost of purchase of shares
  blockPurchasePrice = CalcAmount (numberShares,PurchasePrice)


  #calcCommission block shares bought 
  blockPurchaseCommission = CalcCommission (blockPurchasePrice, COMMISSION_RATE)


#calcAmount sales price of block of shares
  blockSalePrice = CalcAmount (numberShares, SellPrice)

#calcCommission on sale of block of shares
  blockSaleCommission = CalcCommission (blockSalePrice, COMMISSION_RATE)

#calculate profit
  profit = blockSalePrice - blockPurchasePrice - blockPurchaseCommission - blockSaleCommission 

  #output
  print ('Total amount of purchase was $ ', blockPurchasePrice)
  print ('Total amount of Commission for purchase was $ ' , blockPurchaseCommission)
  print ('Total amount of sale price was $ ', blockSalePrice)
  print ('Total amount of commission on the sale of shares was $ ', blockSaleCommission)
  print ('The total profit was $ ' , profit)

main ()