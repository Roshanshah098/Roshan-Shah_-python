import datetime
import random 
from update import updateStock

def make_purchase(store_disc):
    print("*******-----------------------------------------------------*********")
    print("\t\t\tPurchased laptops info")
    print("*******-----------------------------------------------------*********")
    print("\n")
  #name and phonenumber detailed asked before showing laptops info
    name = input("Enter your name here: ")
    phoneNumber = input("Enter your phone number: ")
    print("\n")

    print("**************-------------------------------------------------------------------------------***********")
    print("                    |            +++  AVAILABLE LAPTOPS  +++                      |   ")
    print("**************-------------------------------------------------------------------------------***********")

    #reading from a file in order to display in the IDLE shell
    #read_laptops info
    file = open("laptops.txt", "r")
    a  = 1
    for line in file:
        print( a,line.replace(",", "\t")) 
        a  +=1
    file.close()
    print("**************-------------------------------------------------------------------------------***********")
    print("\n")
    
    # user input for selecting the laptop and its quantity
    laptops_id = int(input("Enter the laptop ID which you want: "))
    while not laptops_id:
        print("Laptop id not found!!!")
        laptops_id = input("Please!! Enter laptopID  correctly: ")
    
    while True:
        try:
            quantity = int(input("Enter the quantity : "))
            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero.")
            #elif quantity > store_disc[laptops_id][laptop_info[3]]:
            #    raise ValueError("Quantity must be less than or equal to the available quantity.")
            break
        except ValueError as e:
            print(e)
            print("Please enter a valid quantity.")
            print()
    
    # Receive laptop info from the dictionary
    updateStock(store_disc ,laptops_id , quantity)
    laptop_info = store_disc[laptops_id]

    # calculate total amount
    laptop_price = laptop_info[2].replace("$", "").strip()
    totalAmount = float(laptop_price) * quantity  

    # ShippingCost based on quantity
    if quantity < 8 :
        shippingCost = 500.0
    elif quantity < 18 :
        shippingCost = 220.0
    else :
        shippingCost = 0.0
    totalAmount += shippingCost    # Ask user for shipping cost and netamount is calculated

    bill_number = random.randint(00000, 99999)   #random bill number is generated by importing random method

    # generate purchase bill as text file
    file_name = laptop_info[0] + "-" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".txt"
    with open(file_name , 'w')as file:
        file.write("*******-------------------------------------------------------------*********\n")
        file.write("       |           Laptop Purchase Invoice            |           ")    
        file.write("\n")                         
        file.write("*******-------------------------------------------------------------*********\n")
        file.write("Customer Name: {}\n".format(name))
        file.write("Phone Number: {}\n".format(phoneNumber))
        file.write("Bill Number: {}\n".format(bill_number))
        file.write("Laptop Name: {}\n".format(laptop_info[0]))
        file.write("Brand Name: {}\n".format(laptop_info[1]))
        
        file.write("Date and Time of Purchase: {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        file.write("Price perLaptop: {}\n".format(laptop_info[2]))
        file.write("Quantity: {}\n".format(quantity))
        
        file.write("ShippingCost: ${}\n".format(shippingCost))
        file.write("Total Amount: ${}\n".format(totalAmount))
        file.write("*******-------------------------------------------------------------*********\n")
        file.write("\t\tThank you for choosing our store!\n")
        file.write("*******-------------------------------------------------------------*********\n")
        file.close()
        print("     Invoice for purchased bill has been generated and saved as {}".format(file_name))
        print("\n")
