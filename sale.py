
import datetime
from updatesale import update_stock

def make_sale(store_disc):
        print("\n")    
        print("++++++++------------------------------------------------------------------------------------+++++++++++")
        print("                               |      LAPTOPS DETAILED INFO          |                               ")
        print("++++++++------------------------------------------------------------------------------------+++++++++++")
        print("\n")   
        
        # Available laptops for sale  
        print("+++++++++--------------------------------------------------------------------------------------------------+++++++++++")
        print("laptopID\tLaptop Name\tBrand Name\tPrice\tRemaining Quantity\tProcessor info\tGraphic info")
        print("+++++++++--------------------------------------------------------------------------------------------------+++++++++++")
        print("\n")  
         #read_laptops info
        file = open("laptops.txt", "r")
        a  = 1
        for line in file:
            print( a,line.replace(",", "\t")) 
            a  +=1
        file.close()   
        print("+++++++++---------------------------------------------------------------------------------------------------+++++++++++")
        print("\n")  

        # prompt where user need to select laptop ID
        laptop_id = int(input("Enter a laptops ID, You want to make purchased: "))
        while not laptop_id:
            print("laptop ID doenot matched.")
            laptop_id = input("Please!!! enter laptopID correctly: ")
        laptop_info = store_disc.get(laptop_id) 

        if laptop_info:  
            name = input("Enter a name of the customer: ")
            phoneNumber = input("Enter a phoneNumber of the customer: ")
            brand = input("Enter the name of brand: ")
            quantity = int(input("Enter a Quantity of laptops you want to make purchased: ")) #typecasting
            cost = int(input("Enter a cost of Laptops: "))  #typecasting
            print("\n")
            totalAmount = cost * quantity      # calculate total amount
            print("\n")

            # Receive laptop info from the dictionary
            update_stock(store_disc ,laptop_id , quantity)
            laptop_info = store_disc[laptop_id]
           
            # Shipping cost based on quantity is calulated
            if quantity < 8 :
                shippingCost = 500.0
            elif quantity < 18:
                shippingCost = 200.0
            else:
                shippingCost = 0.0

            totalAmount += shippingCost              # totalamount with shipping cost
            
            # generate bill as text file
            file_name = laptop_info[0] + "-" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".txt"
            with open(file_name , 'w')as file:
                file.write("******--------------------|      Sale laptops Invoice           |-----------------------------------------******")
                file.write("\n\n")
                file.write("******-------------------------------*************--------------------------------------------------------******")
                file.write("\n")
                file.write("******--------------------|              INFO                   |--------------------------------------*********")
                file.write("\n")
                #file.write("laptopID\tLaptop Name\tBrand Name\tPrice\tRemaining Quantity\tProcessor Details\tGraphic info")
        
                file.write("\n\n")
                file.write("Laptop Name        : {}\n".format(laptop_info[0]))
                file.write("Brand Name         : {}\n".format(brand))
                file.write("Price              : {}\n".format(laptop_info[2]))
                file.write("Remaining Quantity : {}\n".format(quantity))
                file.write("Processor Details  : {}\n".format(laptop_info[3]))
                file.write("Graphic info       : {}\n".format(laptop_info[4]))
                file.write("*******------------------------------------------------------------------------------------------------*********")
                
                file.write("\n\n")
                file.write("*******--------------------|       Customer Details             |--------------------------------------*********")
                file.write("\n\n")
                file.write("Customer Name      : {}\n".format(name))
                file.write("Phone Number       : {}\n".format(phoneNumber))
                file.write("\n")
                file.write("*******------------------------------------------------------------------------------------------------*********")
                file.write("\n\n")
                file.write("++++++---------------------|          Transaction Details       |----------------------------------------++++++-")
                file.write("\n\n")
                file.write("Date&Time of Purchase   : {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                file.write("Price per Laptop:       : {}\n".format(laptop_info[2] )) 
                file.write("Quantity:               : {}\n".format(quantity))
                file.write("\n\n")
                #file.write("Total Amount")
                
                file.write("Total Amount            : {}\n".format(totalAmount - shippingCost )) 
                file.write("Shipping Cost           : {}\n".format(shippingCost))
                file.write("\n\n")
                file.write("++++++++------------------------------------**************--------------------------------------------+++++++++++")
                file.close()
                print("Invoice is generated and it got saved as {}".format(file_name))
                print("\n")