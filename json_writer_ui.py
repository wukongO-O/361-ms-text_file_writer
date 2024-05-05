from time import sleep

user_input = input("Welcome to Theater Inventory Management Microservice.\n "
                   "Please type 1 to run the program, or any key to exit.\n")

if user_input == '1':
    run_file = open('jw-service.txt', 'w')
    run_file.write('run')
    run_file.close()
    print("Welcome to Theater Inventory Management Microservice.\n "
          "Please input the number and value of each inventory item:\n")

inventory_items = ['screen', 'seat', 'popcorn machine', 'ticket booth', 'self-service ticket machine']

current_item_idx = 0
run_file2 = open('jw-service.txt', 'w')
while current_item_idx < len(inventory_items):
    current_item = inventory_items[current_item_idx]
    try:
        quant = int(input(f"How many {current_item}s?\n"))
        run_file2.write(str(quant))

    except ValueError:
        print("Please enter an integer.\n")
        continue

    current_done = 0
    while current_done != 1:
        try:
            cost = int(input(f"What is the value of the {current_item}s?\n"))
            run_file2.write(str(cost))
            current_done = 1
            current_item_idx += 1
        except ValueError:
            print("Please enter an integer.\n")

run_file2.close()

