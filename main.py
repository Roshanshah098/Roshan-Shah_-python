import datetime
from sale import make_sale
from purchase import make_purchase

##  Welcome message of store
print("\n")  
print("++++++++------------------------------------------*********--------------------------------------+++++++++")
print("\t\t\t\t\t Welcome to RockyBhai Store!!!! ")
print("\t\t\t\t\t imadol,lalitpur|9822222223")
print("\n")
print("\t\t\t\t\t Today's Date: {} ".format(datetime.datetime.now().strftime("%Y-%m-%d")))
print("++++++++------------------------------------------*********--------------------------------------+++++++++")
print("\n")  

# Reading from a filetxt and adding them to a dictionary 
file = open("laptops.txt", "r")
store_disc = {}
laptops_id = 1
for line in file:
    line = line.replace("\n", "")
    store_disc.update({laptops_id: line.split(",")})
    laptops_id += 1
file.close()    #print(line)
print("\n")

# Loop inorder to display Main options stored in txtfile
loop = True
while loop == True:
    print("What option do you like to proceed?")
    print("******---------------------******")
    print("Press 1 for Selling")
    print("Press 2 for Buying")
    print("press 3 for Exit On")
    print("******---------------------******")
    
    user_in = int(input("Enter the option to continue: "))
    print("\n")

    if user_in == 1:
        make_sale(store_disc)
        print(" Thanks for Buying it")
       
    elif user_in == 2:
        make_purchase(store_disc)
        print(" Thanks for Ordering it") 
    
    elif user_in == 3:
         loop = False
         print("Thank you for Visiting our store!!!")
         print("See you again soon !!!")
    else:
        print("your option ",user_in , "is not included!!! Please enter a valid option.")
        print("\n")  
