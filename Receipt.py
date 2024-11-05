import csv
from datetime import datetime

def read_prod(filename):
    products = {}
    with open(filename, "r", newline="") as csv_file:
        reader=csv.reader(csv_file)
        next (reader)
        
        
        for row in reader:
            key=row[0]
            prod_desc=row[1]
            prod_price=row[2]
            products[key]=[prod_desc, prod_price]
            
        return products
    
    
def read_order(filename):
    products_ids=[]
    quantities=[]
    with open(filename, "rt") as csv_request:
        reader = csv.reader(csv_request)
        next (reader)
        
        
        for row in reader:
            products_ids.append(row[0])
            quantities.append(csv_request)
            
            
    return products_ids, quantities


def main():
    products = read_prod("products.csv")
    products_ids = read_order("request.csv")[0]
    quantities = read_order("request.csv")[1]
    
    print ()
    print ("SUPER EL CUÑAO ")
    print ()
    print (f"Current date and time: {current_date}")
    print ()
    
    
    subtotal = 0
    total_items = 0
    
    for item in range (len(products_ids)):
        product = products[products_ids[item]]
        name = product [0]
        price = float(product[1])
        quantity = quantities[1]
        print (f"{name}: {quantity} @ {price}")
        subtotal =  subtotal + (int(quantity * price))
        total_items += quantity
        
        
        
        print ()
        print(f"Subtotal:.${subtotal:.2f}")        
        print(f"Total items:  (int{total_items})")
        print(f"Tax:. ${subtotal * 0.06:.2f}")
        print(f"Total:.${subtotal * 1.06:.2f}")
        
        
        print()
        payment = float(input["Payment:.$"])
        charge = payment - (subtotal * 1.06)
    if charge > 0:
        print (f"Your charge is:.${charge:.2f}")
        print()
        print("Thank you for your purchase")
        current_date = datetime.now()
        
    else:    
        print("Error, you need to pay the trait!")

        
        
        
      
        
        
          
main()
    
    
