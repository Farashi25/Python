class Product(object):
    def __init__(self, price, itemname, weight, brand, cost, status):
        self.itemname = itemname
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
        self.price = price 
        self.tax = .05         
    
    def sell(self):
        self.status = "Sold"
    def addtax(self):
        tax = self.price*self.tax
        print 'the tax is',tax,'the total is', tax + self.price
    def productreturn(self, reason):
        if reason == 'Defective':
            self.status = 'Defective'
            self.cost = 0
            print 'this product is defective'
        elif reason == 'Inbox':
            self.cost = self.cost
            self.status = 'For Sale'
            print 'item is on Sale'
        elif reason == 'Openbox':
            self.cost = self.price - ((self.price) * .2)
            self.status = 'Used'
            print self.status, self.cost, ': and this product is discounted 20%'
            return self
        
    
    def displayinfo(self):
        print 'Price is: $' + str(self.price)
        print 'Itemname: ' + str(self.itemname)
        print 'Weight: ' + str(self.weight) + 'lbs'
        print 'Brand: ' + str(self.brand)
        print 'Cost is: $'  + str(self.cost)
        print 'Status: ' + str(self.status)
       
    
        
product1 = Product(300, 'HandBag', 10, 'Coach', 200, 'For Sale')
product1.displayinfo()
product1.sell()
product1.addtax()
product1.productreturn('openbox')
product1.displayinfo()

product2 = Product(2000, 'Shoes',10, 'RedBottom', 1500, 'For Sale')
product2.displayinfo()
product2.sell()
product2.addtax()
product2.productreturn('inbox')
product2.displayinfo()

product3 = Product(2000, 'Shirt', 10, 'Gucci', 1000, 'For Sale')
product3.displayinfo()
product3.sell()
product3.addtax()
product3.productreturn('defective')
product3.displayinfo()


product4 = Product(2000, 'Pants',10, 'Lois Vinton', 1500, 'For Sale')
product4.displayinfo()
product4.sell()
product4.addtax()
product4.productreturn('openbox')
product4.displayinfo()

product2 = Product(2000, 'Shoes',10, 'RedBottom', 1500, 'For Sale')
product3 = Product(2000, 'Shirt', 10, 'Gucci', 1000, 'For Sale')
product4 = Product(2000, 'Pants',10, 'Lois Vinton', 1500, 'For Sale')
# product5 = product(2000, 'Loafers',10, 'Prada', 1500, 'for sale')
# product6 = product(2000, 'Jacket',10, 'Guess', 1500, 'for sale')