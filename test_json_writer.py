# CS361
# Shenglan Li
# Microsevice: test app for json writer
# Description: a test app gets user input to use json_writer microservice
from time import sleep

# current list of inventory - if the inventory_items variable changes,
# we need to update the inventory_items variable in json_writer.py
inventory_items = ['screen', 'seat', 'popcorn machine', 'ticket booth', 'self-service ticket machine']

user_input = input("Welcome to Theater Inventory Management Microservice.\n "
                   "Please type 1 to run the program, or any key to exit.\n")

if user_input == '1':

    print("Welcome to Theater Inventory Management Microservice.\n "
          "Please input the number and value of each inventory item:\n")

    current_item_idx = 0
    run_file = open('jw-service.txt', 'w')
    while current_item_idx < len(inventory_items):
        current_item = inventory_items[current_item_idx]
        try:
            quant = int(input(f"How many {current_item}s?\n"))
            run_file.write(str(quant) + ' ')
        except ValueError:
            print("Please enter an integer.\n")
            continue

        current_done = 0
        while current_done != 1:
            try:
                cost = int(input(f"What is the value of the {current_item}s?\n"))
                if current_item_idx != len(inventory_items) - 1:
                    run_file.write(str(cost) + ' ')
                else:
                    run_file.write(str(cost))
                current_done = 1
                current_item_idx += 1
            except ValueError:
                print("Please enter an integer.\n")

    run_file.close()

    # Confirm the json file is ready
    print("One moment...we are getting the json file ready.")
    while True:
        comm_file = open('jw-service.txt', 'r')
        confirm_msg = comm_file.readline()
        if confirm_msg == './inventory.json':
            print("Your data is saved. The inventory.json file is all set!")
            break
        sleep(5)

    comm_file.close()

