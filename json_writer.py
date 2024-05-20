# CS361
# Shenglan Li
# Microsevice: text file/json writer
# Description: get user input for a theater inventory list
#   (screens, seats, popcorn machine, ticket booth, self service ticket machine) and save the values to a json file.

from collections import defaultdict
import json
from time import sleep


def main():
    inventory_items = ['screen', 'seat', 'popcorn machine', 'ticket booth', 'self-service ticket machine']

    inventory = defaultdict(dict)
    for item in inventory_items:
        inventory[item] = {
            'quantity': 0,
            'value': 0
        }
    print("The json writer microservice is listening for request...")

    # Wait for user input
    def read_request():
        while True:
            data_file = open('jw-service.txt', 'r')
            data_str = data_file.readline().split(' ')
            if len(data_str) == len(inventory_items) * 2:
                break
            sleep(5)

        # Get user input to populate the inventory
        for i in range(len(data_str)):
            item_index = i // 2
            item_name = inventory_items[item_index]
            if i % 2 == 0:
                inventory[item_name]['quantity'] = data_str[i]
            else:
                inventory[item_name]['value'] = data_str[i]
        data_file.close()

    def write_file_path():
        # Write the json file path into the text file
        run_file = open('jw-service.txt', 'w')
        json_path = f'./inventory.json'
        run_file.write(json_path)
        run_file.close()

    read_request()

    # Store values to a json file
    with open('inventory.json', 'w') as outfile:
        json.dump(inventory, outfile)

    write_file_path()

    print("The inventory.json file is ready.")


if __name__ == '__main__':
    main()