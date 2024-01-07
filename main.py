import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", password="harsh@5898", database="hms"
)
cursor = db.cursor()


def costumerDetails():
    print(
        """====================
          Enter customer details"""
    )
    cid = input("Enter Customer Identification Number : ")
    name = input("Enter Customer Name : ")
    address = input("Enter Customer Address : ")
    age = input("Enter Customer Age : ")
    nationality = input("Enter Customer Country : ")
    phoneno = input("Enter Customer Contact Number : ")
    email = input("Enter Customer Email : ")
    qry = "INSERT INTO cust_details VALUES(%s,%s,%s,%s,%s,%s,%s)"
    values = (cid, name, address, age, nationality, phoneno, email)
    cursor.execute(qry, values)
    db.commit()
    print("\nNew Customer Entered In The System Successfully !")
    print("====================")
    print()


def booking():
    print(
        """====================
          Enter booking details"""
    )
    cid = input("Enter Customer Identification Number : ")
    name = input("Enter Customer Name:")
    print("\n ##### We have The Following Rooms For You #####")
    print(" 1. Ultra Royal ----> ₹10000/-")
    print(" 2. Royal ----> ₹5000/- ")
    print(" 3. Elite ----> ₹3500/- ")
    print(" 4. Budget ----> ₹2500/- ")
    r_choice = int(input("Enter Your Option : "))
    r_no = int(input("Enter Customer Room No : "))
    nights = int(input("Enter No. Of nights you will stay: "))
    checkIn = input("Enter checkin date(YYYY-MM-DD) : ")
    checkOut = input("Enter checkout date(YYYY-MM-DD) : ")
    if r_choice == 1:
        room = "Ultra royal"
        r_price = nights * 10000
    elif r_choice == 2:
        room = "Royal"
        r_price = nights * 5000
    elif r_choice == 3:
        room = "Elite"
        r_price = nights * 3500
    elif r_choice == 4:
        room = "Budget"
        r_price = nights * 2500

    qry = "INSERT INTO roomBooking values(%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (cid, name, room, r_no, r_price, nights, checkIn, checkOut)
    cursor.execute(qry, values)
    db.commit()
    print("Thank You , Your Room Has Been Booked For : ", nights, "nights")
    print("Your Total price of room is : Rs. ", r_price)

    print("====================")
    print()


def restaurant():
    print("====================")
    cid = input("Enter Customer Identification Number : ")
    print("1. Vegetarian Combo -----> 300 Rs.")
    print("2. Non-Vegetarian Combo -----> 500 Rs.")
    print("3. Vegetarian & Non-Vegetarian Combo -----> 750 Rs.")
    choice_dish = int(input("Enter Your Cusine : "))
    quantity = int(input("Enter Quantity : "))
    if choice_dish == 1:
        dish = "Vegetarian combo"
        price = quantity * 300
    elif choice_dish == 2:
        dish = "Non-Vegetarian combo"
        price = quantity * 500
    elif choice_dish == 3:
        dish = "Vegetarian and Non-Vegetarian combo"
        price = quantity * 750
    qry = "INSERT INTO restaurant values(%s,%s,%s,%s)"
    values = (cid, dish, quantity, price)
    cursor.execute(qry, values)
    db.commit()
    print("Your order of", quantity, dish, "has been placed\nThank you for ordering")
    print("Your total price : ₹", price)
    print()


def showAll():
    cursor.execute("SELECT * from cust_details")
    # details = data.fetchall()
    print("customer id, name, address, age, country, phone no., email ID")
    for record in cursor:
        print(record)
    print()


def search():
    cid = input("Enter Customer Identification Number : ")
    cursor.execute("SELECT * from cust_details where C_id = %s", [cid])
    data = cursor.fetchone()
    if data:
        print("Customer details found:\n", data)
    else:
        print("Customer not found!")
    print()


def showCustomer():
    cid = input("Enter cid : ")
    print()
    qry = "select cust_details.C_id, cust_details.C_name, cust_details.C_address,\
    cust_details.C_age, cust_details.C_country, cust_details.C_phone,\
    cust_details.C_email, roomBooking.r_type, roomBooking.r_no,\
    roomBooking.r_price, roomBooking.no_of_days, roomBooking.checkIn,\
    roomBooking.checkOut \
    from cust_details,roomBooking \
    where cust_details.C_id = %s and cust_details.C_id=roomBooking.C_id"
    cursor.execute(qry, [cid])
    data = cursor.fetchone()
    if data:
        print("customer details")
        print("Customer ID :", data[0])
        print("name :", data[1])
        print("address :", data[2])
        print("age :", data[3])
        print("country :", data[4])
        print("pno :", data[5])
        print("email :", data[6])
        print("room :", data[7])
        print("room no. :", data[8])
        print("room price :", data[9])
        print("no_of_days :", data[10])
        print("checkIn :", data[11])
        print("checkIn :", data[12])
    else:
        print("Customer not found!")
    print()


def rBill():
    cid = input("Enter cid : ")
    print()
    qry = "select * from restaurant where C_id = %s"
    cursor.execute(qry, [cid])
    data = cursor.fetchall()
    
    if data:
        sum = 0
        print("Bill of customer ID", cid)
        print()
        for cid, item, quantity, price in data:
            print(item, "\t", quantity, "quantity\t₹", price)
            sum += price
        print("====================")
        print("Total price : ", sum)
        print()
    else:
        print("Customer not found!")        
    print()


while True:
    print(
        """==================================================
          1--> Enter costumer details
          2--> Room Booking
          3--> Restaurant
          4--> Show all customer details
          5--> Search customer
          6--> Show customer all details
          7--> Show customer restaurant bill
          8--> Exit
"""
    )
    action = int(input("Enter your choice:"))
    print("==================================================\n")
    if action == 1:
        costumerDetails()
    elif action == 2:
        booking()
    elif action == 3:
        restaurant()
    elif action == 4:
        showAll()
    elif action == 5:
        search()
    elif action == 6:
        showCustomer()
    elif action == 7:
        rBill()
    else:
        break
    