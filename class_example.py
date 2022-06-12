import csv

class item:
    # the pay rate after discount
    pay_rate = 0.8
    def __init__(self,name: str,quant: int,price: float):
        #Validations to the received arguements
        assert quant >=0, f"{quant} is not greater than zero"
        assert price >=0, f"{price} is not greater than zero"

    # Assigning to self object
        self.name = name
        self.price = price
        self.quant = quant
    # Actions to execute
        item.all.append(self)
    def calculate_total_price(self):
        return self.price * self.quant
    
    '''Since Pay_rate attribute is defined inside of a class,
    it has to be pass in the method separately. The attribute 
    has no relation with self instance level attributes that we 
    receieve.'''
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('data.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for i in items:
            item(
                name = i.get('name'),
                quant = int(i.get('quant')),
                price = int(i.get('price'))
            )
    
    @staticmethod
    def is_integer(num):
        # counting floating numbers which are point zero
        # Ex: 5.0, 7.0
        if isinstance(num, float):
            #count the number/integer that point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    #representation of item.all using __repr__ method
    def __repr__(self):
        return f"'{self.name}','{self.quant}','{self.price}'"

#class inheriting item class
class phones(item):
    all = []
    def __init__(self,name: str,quant: int,price: float, ):
        #Validations to the received arguements
        assert quant >=0, f"{quant} is not greater than zero"
        assert price >=0, f"{price} is not greater than zero"

        # Assigning to self object
        self.name = name
        self.price = price
        self.quant = quant

#print(item.is_integer(7.0))

#item.instantiate_from_csv()

#pay rate is added from class level
#item1 = item()
#item1.apply_discount()
#print(item1.price)

#pay rate is added from instance level
#item2 = item()
#item2.pay_rate = 0.7
#item2.apply_discount()
#print(item2.price)
#item3 = item()
#item4 = item()
#item5 = item()

'''To find name attribute inside "all" items list 
we used for loop to travers the list holding all items
and then filterting/printing name attribute from it.'''
#for i in item.all:
#    print(i.name)

#print(f"You bought a {item1.name} for price {item1.price}! The total is {item1.calculate_total_price()} for quantity of {item1.quant}")
#print(f"You bought a {item2.name} for price {item2.price}! The total is {item2.calculate_total_price()} for quantity of {item2.quant}")

#print(item.all)