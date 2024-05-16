def update_stock(store_disc, laptop_id, quantity):
    laptop_info = store_disc[laptop_id]
    stock = int(laptop_info[3])
    new_stock = stock - quantity
    laptop_info[3] = str(new_stock)
    # Update laptops.txt with new stock
    with open("laptops.txt", "w") as fno:
        for key, value in store_disc.items():
            fno.write(value[0] + "," + value[1] + "," + value[2] + "," + value[3] + "," + value[4] + ","+ value[5] + "\n")
