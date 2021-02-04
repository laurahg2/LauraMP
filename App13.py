products_file = '/Users/lauraherreragarcia/PycharmProjects/pythonProjectGeneration/couriers.txt'
couriers_file = '/Users/lauraherreragarcia/PycharmProjects/pythonProjectGeneration/couriers.txt'
orders_file = '/Users/lauraherreragarcia/PycharmProjects/pythonProjectGeneration/orders.txt'

products_list = []
courier_list = []
order_list = []
order_dictionary = {"name": "",
            "address": "",
            "phone": "",
            "courier": "",
            "status": "",}

def write_products_file():
    with open('products.txt', 'w') as file:
        for name in products_list:
            file.write(name + '\n')


def read_products_file():
    with open('products.txt', 'r') as file:
        for line in file:
            line = line.strip()
            products_list.append(line)


def print_products_list():
    print("products")
    print(products_list)
    write_products_file()

def write_couriers_file():
    with open('couriers.txt', 'w') as file:
        for name in courier_list:
            file.write(name + '\n')


def read_couriers_file():
    with open('couriers.txt', 'r') as file:
        for line in file:
            line = line.strip()
            courier_list.append(line)


def print_couriers_list():
    print("couriers")
    print(courier_list)
    write_couriers_file()

def write_orders_file():
    with open('orders.csv', 'w') as file:
        for name in order_list:
            file.write(name + '\n')


def read_orders_file():
    with open('orders.csv', 'r') as file:
        for line in file:
            line = line.strip()
            order_list.append(line)


def print_orders_list():
    import csv

    with open('orders.csv', mode='w') as file:
        fieldnames = ['name', 'address', 'phone', 'courier', 'status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({
            "name": "",
            "address": "",
            "phone": "",
            "courier": "",
            "status": "",
        })


    print("orders")
    print(order_list)
    write_orders_file()


def product_available():
    print()
    print("•••DRINKS LIST•••")
    for i in products_list:
        print("* " + i)



def create_product():
    item = input("Enter the product you wish to add: ")
    products_list.append(item)
    print(item + " has been added to the basket.")


def update_product_list():
    try:
        item_change_name = print("Choose the product you want to changed:")
        products_list.remove(input())
        print("Please enter the new name:")
        products_list.append(input())
    except:
        print("That was not in the List")
        update_product_list()
    product_options()


def remove_product_list():
    item = input("Which item would you like to remove from the basket: ")
    products_list.remove(item)
    print(item + " has been removed from the basket.")
    print(products_list)


def courier_available():
    print()
    print("•••COURIERS•••")
    for i in courier_list:
        print("* " + i)


def create_courier():
    item = input("Enter the courier you wish to add: ")
    courier_list.append(item)
    print(item + " has been added.")


def update_courier_list():
    try:
        item_change_name = print("Choose the courier you want to update:")
        courier_list.remove(input())
        print("Please enter the new courier:")
        courier_list.append(input())
    except:
        print("That was not in the List")
        update_courier_list()
    courier_options()


def remove_courier_list():
    item = input("Which courier would you like to remove: ")
    courier_list.remove(item)
    print(item + " has been removed from the courier list.")
    print(courier_list)


def order_available():
    print()
    print("•••ORDERS•••")
    for item in order_dictionary:
        print(item,":",order_dictionary[item])


def create_order():
    # order_dictionary = {}
    name = input("Enter the name of the customer: ")
    address = input("Enter the address of the customer: ")
    phone = input("Enter the phone of the customer: ")
    courier = input("Enter the name of the courier: ")
    status = input("status: Preparing ... ")
    writefile = open("orders.csv", "a")
    writefile.write(name + "," + address + "," + phone + "," + courier + "," + status + "\n")
    writefile.close()
    print("order has been added")

# print_orders_list


def update_order_status():
    # name = input("Enter the name of the customer: ")
    # address = input("Enter the address of the customer: ")
    # phone = input("Enter the phone of the customer: ")
    # courier = input("Enter the name of the courier: ")
    # file = open("orders.csv", "r")
    #     default = "In Progress")
    #     choices = (('Received', 'Received'),
    #                ('Scheduled', 'Scheduled'),
    #                ('Shipped', 'Shipped'),
    #                ('In Progress', 'In Progress'),
    #                ) ```


    # order_dictionary = {}
    name = input("Enter the name of the customer: ")
    address = input("Enter the address of the customer: ")
    phone = input("Enter the phone of the customer: ")
    courier = input("Enter the name of the courier: ")
    file = open("orders.csv", "r")
    found = False
    for line in file:
        order = line.split(",")
        if order[0] == name:  # checks if the name entered is in the list
            found = True  # if it is changes found to True
    file.close()
    if found == True:  # after the loop checks if the order is found
        print("Order already exists")
    else:
        writefile = open("orders.csv", "a")  # open the file in append mode
        writefile.write(
            name + "," + address + "," + phone + "," + courier)  # write the new information to the file
        writefile.close()
        print("order updated.")
# print_orders_list


# def order_tracker(request):
#     if request.method=="POST":
#         orderId = request.POST.get('orderId', '')
#         try:
#             order=Order.objects.filter(pk=orderId)
#
#             if len(order)>0:
#                 update = Order.objects.filter(pk=orderId)
#                 updates = []
#                 for order in update:
#                     # change order status to scheduled
#                     if order.status == 'processing':
#                         order.status = 'scheduled'
#                         order.save()
#                     updates.append({'status' : order.status})
#                     response = json.dumps(updates)
#                     return HttpResponse(response)
#             else:
#                 return HttpResponse('{}')
#         except Exception as e:
#             return HttpResponse('{}')
#     return render(request,"tracker.html")

def update_order_list():
    # order_dictionary = {}
    name = input("Enter the name of the customer: ")
    address = input("Enter the address of the customer: ")
    phone = input("Enter the phone of the customer: ")
    courier = input("Enter the name of the courier: ")
    file = open("orders.csv", "r")
    found = False
    for line in file:
        order = line.split(",")
        if order[0] == name:  # checks if the name entered is in the list
            found = True  # if it is changes found to True
    file.close()
    if found == True:  # after the loop checks if the order is found
        print("Order already exists")
    else:
        writefile = open("orders.csv", "a")  # open the file in append mode
        writefile.write(
            name + "," + address + "," + phone + "," + courier)  # write the new information to the file
        writefile.close()
        print("order updated.")
# print_orders_list

def remove_order_list():
    item = input("Which order would you like to remove: ")
    import csv
    with open('couriers.csv', 'rb') as inp, open('couriers.csv', 'wb') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row == "input":
                writer.writerow(row)
                print(item + " has been removed from the order list.")
                print(order_dictionary)

    # file = open("orders.csv", "r")
    # # orders.csv.remove(item)
    # print(item + " has been removed from the order list.")
    # print("orders.csv")

    # item = input("Which order would you like to remove: ")
    # order_list.remove(item)
    # print(item + " has been removed from the order list.")
    # print(order_list)

def product_options():
    choice = 1
    while choice != 0:
        choice = input(
            "\nEnter 0 to return to main menu\nEnter 1 to show product menu.\nEnter 2 Add a product.\nEnter 3 to update product\nEnter 4 to delete product")
        if choice == '1':
            product_available()
        elif choice == '2':
            create_product()
        elif choice == '3':
            update_product_list()
        elif choice == '4':
            remove_product_list()
        elif choice == '0':
            print("\nThanks for visiting us. See you soon!.\n")
            return
        else:
            print("\nI don't understand that choice, please try again.\n")

def courier_options():
    choice = 1
    while choice != 0:
        choice = input(
            "\nEnter 0 to return to main menu\nEnter 1 to show courier menu.\nEnter 2 Choose a new courier.\nEnter 3 to update courier\nEnter 4 to delete courier")
        if choice == '1':
            courier_available()
        elif choice == '2':
            create_courier()
        elif choice == '3':
            update_courier_list()
        elif choice == '4':
            remove_courier_list()
        elif choice == '0':
            print("\nThanks for visiting us. See you soon!.\n")
            return
        else:
            print("\nI don't understand that choice, please try again.\n")

def order_options():
    choice = 1
    while choice != 0:
        choice = input(
            "\nEnter 0 to return to main menu\nEnter 1 to show orders menu\nEnter 2 create a new order\nEnter 3 to update order status\nEnter 4 to update order\nEnter 5 to delete order")
        if choice == '1':
            order_available()
        elif choice == '2':
            create_order()
        elif choice == '3':
            update_order_status()
        elif choice == '4':
             update_order_list()
        elif choice == '5':
            remove_order_list()
        elif choice == '0':
            print("\nThanks for visiting us. See you soon!.\n")
            return
        else:
            print("\nI don't understand that choice, please try again.\n")


def main_menu():
    main_menu = 1
    while main_menu != 0:
        main_menu = int(input(
            "*** WELCOME TO THE BEST COFFEE SHOP IN YOUR AREA ***\nMain Menu\nSelect the following:\n0: Exit\n1: View Product Options\n2: View Courier Options\n3: View order Options"))
        if main_menu == 1:
            product_options()
        elif main_menu == 2:
            courier_options()
        elif main_menu == 3:
            order_options()
        elif main_menu == 0:
            write_products_file()
            write_couriers_file()
            write_orders_file()
            read_products_file()
            read_couriers_file()
            read_orders_file()
            print_products_list()
            print_couriers_list()
            print_orders_list()


            exit("Thank you")

main_menu()

