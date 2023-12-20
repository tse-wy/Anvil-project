# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 17:51:37 2023

@author: Mog
"""
#econ_cost = econ_ticket * econ_price 
#prem_cost = prem_ticket * prem_price
#firstc_cost= firstc_ticket * firstc_price

#!pip install anvil-uplink

import anvil.server

anvil.server.connect("XVIDYE7SDVJO5JASJY6O2KKO-P4VBOHYPYF74CE6I")

#pip install anvil-uplink


import pandas as pd
import pyodbc

    # Connect to the SQL Server database

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-9KS360F\SQLEXPRESS;'
                      'Database=Assignment;'
                      'Trust_Connection=yes;')

cursor = conn.cursor()

#put results into a db 

#ticket type total into flight_customer

#create the new able without the 'not null' in order to insert one column (done)

#test the data is inserted into into a dummy db

#to total on the booking form page for customer

#got to add together

#function to work out total based on num x the ticket type

#

#function for total of available tickets

@anvil.server.callable
def available_tickets ():
    query ="SELECT * FROM tickets"
    dataframe = pd.read_sql_query(query, conn) 
    my_list=[]
    for i in dataframe['available_tickets']:
        my_list.append(str(i))

    return my_list
print(available_tickets())



#function for ticket updates:
@anvil.server.callable
def ticket_updates():
    cursor.execute('SELECT * FROM tickets')
    data = cursor.fetchall()
    list_1 = []
    for i in data:
        list_1.append(list(i))
    return list_1

#print (ticket_updates())


#function for displaying the total of ticket cost per type

@anvil.server.callable
def total_ticket_cost ():
    query ="SELECT * FROM tickets"
    dataframe = pd.read_sql_query(query, conn) 
    my_list=[]
    for i in dataframe['price_per_ticket']:
        my_list.append(str(i))

    return my_list
#print(total_ticket_cost())




#econ type total cost

@anvil.server.callable
def econ_total(num_tickets_booked, econ_ticket):
    return num_tickets_booked * econ_ticket

#to test it:
num_tickets = 5
econ_ticket_price = 100

total_econ_cost = econ_total(num_tickets, econ_ticket_price)
#print("Total Economy Ticket Cost:", total_econ_cost)




#insert data econ total into econ ticket in flight_customer table

@anvil.server.callable
def insert_into_flight_customer_econ(econ_total):
    cursor.execute(f'INSERT into flight_customer (economy_tickets) values ({econ_total})')
    conn.commit()
    return 'successfully inserted'
#test
#print(insert_into_flight_customer_econ(200))




#prem type total cost
prem_ticket_price = 200

@anvil.server.callable
def prem_total(num_tickets_booked, prem_ticket):
    return num_tickets_booked * prem_ticket

#to test it:
#num_tickets = 5
prem_ticket = 200

total_prem_cost = prem_total(num_tickets, prem_ticket)
print("Total Premium Economy Ticket Cost:", total_prem_cost)





#insert data prem total into prem ticket in flight_customer table

@anvil.server.callable
def insert_into_flight_customer_prem(prem_total):
    cursor = conn.cursor()
    cursor.execute(f'INSERT into flight_customer (premium_economy) values ({prem_total})')
    conn.commit()
    return 'successfully inserted'
#test
#print(insert_into_flight_customer_prem(200))





#firstc type total cost

@anvil.server.callable
def firstc_total(num_tickets_booked, firctc_ticket):
    return num_tickets_booked * firstc_ticket

#to test it:
#num_tickets = 5
firstc_ticket = 300

firstc_total = firstc_total(num_tickets, firstc_ticket)
#print("Total First Class Ticket Cost:", firstc_total)





#insert data firstc total into first class ticket in flight_customer table
@anvil.server.callable
def insert_into_flight_customer_firstc(firstc_total):
    cursor.execute(f'INSERT into flight_customer (first_class) values ({firstc_total})')
    conn.commit()
    return 'successfully inserted'
#test
#print(insert_into_flight_customer_firstc(140))





#total value function

@anvil.server.callable
def econ_total(num_tickets_booked, econ_ticket):
    return num_tickets_booked * econ_ticket

def prem_total(num_tickets_booked, prem_ticket):
    return num_tickets_booked * prem_ticket

def firstc_total(num_tickets_booked, firstc_ticket):
    return num_tickets_booked * firstc_ticket

num_tickets = ()
econ_ticket_price = 100
prem_ticket_price = 200
firstc_ticket_price = 300

total_econ_cost = econ_total(num_tickets, econ_ticket_price)
total_prem_cost = prem_total(num_tickets, prem_ticket_price)
total_firstc_cost = firstc_total(num_tickets, firstc_ticket_price)

@anvil.server.callable
def total_all(total_econ_cost, total_prem_cost, total_firstc_cost):
   
    return total_econ_cost + total_prem_cost + total_firstc_cost

total_all = total_all(total_econ_cost, total_prem_cost, total_firstc_cost)
#print("Overall Total Cost:", total_all)





#to enter full amount in db 
@anvil.server.callable
def insert_into_flight_customer_price_total(total_all):
    cursor.execute(f'INSERT into flight_customer (price_total) values ({total_all})')
    conn.commit()
    return 'successfully inserted'

#print(insert_into_flight_customer_price_total(2000))



#total quantity

@anvil.server.callable
def total_quant (econ_qaunt, prem_quant, firstc_quant):
    return econ_qaunt + prem_quant + firstc_quant

#total_quant = total_qaunt(econ_qaunt, prem_quant, firstc_quant)


#enter total quantity to customer feedback db

@anvil.server.callable
def insert_into_flight_customer_quant(total_quant):
    cursor.execute(f'INSERT into flight_customer (number_of_tickets_booked) values ({total_quant})')
    conn.commit()
    return 'successfully inserted'

#print(insert_into_dummy_feedback(12))

#overall cost with discount based on quantity of tickets:
    
@anvil.server.callable
def discount_total(total_all, total_quant):
    if total_quant == 2:
        return total_all * 0.8
    elif total_quant == 3:
        return total_all * 0.7
    elif total_quant >= 4:
        return total_all * 0.6
    else: 
        return total_all
   
    
   
    
   
#to show the discount percentage

@anvil.server.callable
def percentage_discount(total_quant):
    if total_quant == 2:
        return ("20%")
    elif total_quant == 3:
        return ("30%")
    elif total_quant >= 4:
        return ("40%")
    else: 
        return ("0%") 
#print (percentage_discount(5))  
    
#enter discount total to flight customer db

@anvil.server.callable
def insert_into_flight_customer_discount(discount_all):
    cursor.execute(f'INSERT into flight_customer (price_total) values ({total_all})')
    conn.commit()
    return 'successfully inserted'
    
#econ_ticket = dataframe['economy'].iloc[0]
#prem_ticket = dataframe['premium_economy'].iloc[0]
#firstc_ticket = datafram['first_class'].iloc[0]

#print(insert_into_dummy_feedback(12))


#unique ticket code and storing the booking data as a function


import random
import string

booking_data = {}

@anvil.server.callable
def generate_unique_code():
    code = "UTC" + ''.join(random.choices(string.digits, k=5))
    return code

def store_booking_info(unique_code, booking_info):
    booking_data[unique_code] = booking_info

def retrieve_booking_info(unique_code):
    return booking_data.get(unique_code)  
 

unique_code = generate_unique_code()
#print(unique_code)

   


#insterting the unique code into the db tables        
@anvil.server.callable
def insert_unique_ticket_code(generate_unique_code):
    cursor.execute(f'INSERT into flight_customer (unique_ticket_code) values (\'{generate_unique_code}\')')
    cursor.execute(f'INSERT into feedback (unique_ticket_code) values (\'{generate_unique_code}\')')
    #test table
    #cursor.execute(f'INSERT into dummy_table2 (unique_ticket_code) values (\'{generate_unique_code}\')')

    conn.commit()
    return 'successfully inserted'
    
#print(insert_unique_ticket_code("UTC60345"))


#booking info into flight customer table
@anvil.server.callable
def booking_customer_info(first_name, last_name, email, number_of_tickets_booked, economy, premium_economy, first_class, price_total, discount_total, unique_ticket_code):
    """
    first_name 
    last_name 
    email 
    number_of_tickets_booked 
    economy 
    premium_economy 
    first_class 
    price_total 
    discount_total
    unique_ticket_code
    """
    return (first_name, last_name, email, number_of_tickets_booked, economy, premium_economy, first_class, price_total, discount_total, unique_ticket_code)



@anvil.server.callable
def insert_bookinginfo_flight_customer(first_name, last_name, email, number_of_tickets_booked, economy, premium_economy, first_class, price_total, discount_total, unique_ticket_code):
    cursor.execute(f"INSERT INTO flight_customer (first_name, last_name, email, number_of_tickets_booked, economy, premium_economy, first_class, price_total, discount_total, unique_ticket_code) VALUES ('{first_name}', '{last_name}', '{email}', {number_of_tickets_booked}, {economy}, {premium_economy}, {first_class}, {price_total}, {discount_total}, '{unique_ticket_code}')")
    
    #cursor.execute(f"INSERT INTO dummytable (first_name, last_name, email, number_of_tickets_booked, economy, premium_economy, first_class, price_total, discount_total, unique_ticket_code) VALUES ('{first_name}', '{last_name}', '{email}', {number_of_tickets_booked}, {economy}, {premium_economy}, {first_class}, {price_total}, {discount_total}, '{unique_ticket_code}')")
    conn.commit()
    return 'successfully inserted'

booking_info_flight_customer = {
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'jonde@example.com',
    'number_of_tickets_booked': 4,
    'economy': 100,
    'premium_economy': 400,
    'first_class': 300,
    'price_total': 800,
    'discount_total': 480,
    'unique_ticket_code': 'UTC4636373'
}

#test
#print(insert_bookinginfo_flight_customer(**booking_info_flight_customer))



###############

#insert feedback into feedback db   
#need to def each argument 
@anvil.server.callable
def submit_feedback(first_name, last_name, email, feedback_text):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-9KS360F\SQLEXPRESS;'
                          'Database=Assignment;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()

    # Insert feedback into the database
    query = """
        INSERT INTO feedback (first_name, last_name, email, unique_ticket_code, feedback)
        VALUES (?, ?, ?, 'N/A', ?)
    """
    cursor.execute(query, (first_name, last_name, email, feedback_text))

    conn.commit()
  

    # Print the submitted feedback details
    print("Feedback submitted successfully!")
    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("Email:", email)
    print("Feedback:", feedback_text)

    return 'Successfully submitted'

# Example usage of the function
submit_feedback("John", "Doe", "john1122@example.com", "The service provided was excellent.")




#test
#result = insert_feedback_db('John', 'Doe', 'john@example.com', 2, 'UTC112233', 'Subject', 'Feedback', 'Response')
#print(result)


#admin response

@anvil.server.callable
def feedback_response(email, response_text):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-9KS360F\SQLEXPRESS;'
                          'Database=Assignment;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()

    # Update response in the database
    query = """
        UPDATE feedback
        SET response = ?
        WHERE email = ?
    """
    cursor.execute(query, (response_text, email))

    conn.commit()

    #Print feedback response information
    print("Feedback response updated successfully!")
    print("Email:", email)
    print("Response:", response_text)

    return True

# Example usage
success = feedback_response("john1122@example.com", "Thank you for your feedback!")
if success:
    print("Response updated successfully!")

# Example use
feedback_response("johndoe@example.com", "Thank you for your feedback!")




@anvil.server.callable
def search_response_by_email(email):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-9KS360F\SQLEXPRESS;'
                          'Database=Assignment;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()

    # Search for response by email
    query = """
        SELECT first_name, last_name, email, feedback, response
        FROM feedback
        WHERE email = ?
    """
    cursor.execute(query, email)
    response_info = cursor.fetchone()

    if response_info:
        
        # Print response information
        print("Response found for email:", email)
        print("first_name:", response_info[0])
        print("last_name:", response_info[1])
        print("email:", response_info[2])
        print("feedback:", response_info[3])
        print("response:", response_info[4])
        
        response_data = {
            "first_name": response_info[0],
            "last_name": response_info[1],
            "email": response_info[2],
            "feedback": response_info[3],
            "response": response_info[4]
        }
        return response_data
    
    else:
        print("No response found for email:", email)

   

# Example use
response_data = search_response_by_email("john1122@example.com")
if response_data:
    print("Response found for email:", response_data["Email"])
    print("First Name:", response_data["First Name"])
    print("Last Name:", response_data["Last Name"])
    print("Feedback:", response_data["Feedback"])
    print("Response:", response_data["Response"])

# Example email use
search_response_by_email("johndoe@example.com")

@anvil.server.callable
def search_response_by_email_1(email):
  conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-9KS360F\SQLEXPRESS;'
                        'Database=Assignment;'
                        'Trusted_Connection=yes;')

  cursor = conn.cursor()

  # Search for response by email
  query = """
      SELECT first_name, last_name, email, feedback, response
      FROM feedback
      WHERE email = ?
  """
  cursor.execute(query, email)
  response_info = cursor.fetchone()

  if response_info:
      response_data = {
          "first_name": response_info[0],
          "last_name": response_info[1],
          "email": response_info[2],
          "feedback": response_info[3],
          "response": response_info[4]
      }
      return response_data
  else:
      return print("No response found for email:", email)






 #display feedback info on admin page
@anvil.server.callable
def admin_feedback():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-9KS360F\SQLEXPRESS;'
                          'Database=Assignment;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()

    # Retrieve feedback information with first name, last name, email, feedback, and response
    query = """
        SELECT u.first_name, u.last_name, f.email, f.feedback, f.response
        FROM users u
        LEFT JOIN feedback f ON u.email = f.email
    """
    cursor.execute(query)
    feedback_info = cursor.fetchall()

    if feedback_info:
        feedback_data = []
        # Print feedback information
        for feedback in feedback_info:
            feedback_data.append({
                "First Name": feedback[0],
                "Last Name": feedback[1],
                "Email": feedback[2],
                "Feedback": feedback[3],
                "Response": feedback[4] 
                if len(feedback) > 4 
                else "No response available"
            })

        return feedback_data
    else:
        print("No feedback available.")

    
# Example
#admin_feedback()



# Example use of the functions
feedback_response("johndoe@example.com", "Thank you for your feedback!")
search_response_by_email("johndoe@example.com")


#########

#Admin side of assignment:
    
#to add tickets


@anvil.server.callable
def add_tickets_1(add_num, ticket_type):
    return add_num + ticket_type

# Adding to available tickets to the tickets db  
      
@anvil.server.callable
def add_to_tickets_1(ticket_type, add_tickets):
    cursor.execute(f"UPDATE tickets SET available_tickets = available_tickets + {add_tickets} WHERE ticket_type = '{ticket_type}'")
    conn.commit()
    return 'Successfully updated'

#print(add_to_tickets_1('economy', 3))


#subtracting the availability
@anvil.server.callable
def sub_tickets (sub_num, ticket_type):   
    return sub_num - ticket_type

#db insert to tickets

@anvil.server.callable
def update_subtract_tickets(ticket_type, sub_tickets):
    cursor.execute(f"UPDATE tickets SET available_tickets = available_tickets - {sub_tickets} WHERE ticket_type = '{ticket_type}'")
    #cursor.execute(f"UPDATE dummy_tickets_1 SET available_tickets = available_tickets - {sub_tickets} WHERE ticket_type = '{ticket_type}'")

    conn.commit()
    return 'Successfully updated'

#print(update_subtract_tickets('economy', 2))

#to display the tickets in admin
#by fetching from ticket db

#method for individual components in anvil
@anvil.server.callable
def ticket_display():
    cursor.execute('SELECT * FROM tickets')
    data = cursor.fetchall()
    list_1 = []
    for i in data:
        list_1.append(list(i))
    return list_1

#print(ticket_display())
    #except Exception as e:
        # Handle any exceptions that occur during the process
        #print(f"Error retrieving table data: {e}")
        #cursor.close()
        #conn.close()
        #return None    
 
print (ticket_display())       


#search booking info by utc:
    
@anvil.server.callable
def search_booking_by_ticket_code(unique_ticket_code):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-9KS360F\SQLEXPRESS;'
                          'Database=Assignment;'
                          'Trust_Connection=yes;')
    cursor = conn.cursor()

    # Execute the SQL query
    query = """
        SELECT *
        FROM flight_customer
        WHERE unique_ticket_code = ?
    """
    cursor.execute(query, unique_ticket_code)
    booking_info = cursor.fetchone()
    result = []
    
    if booking_info:
        item = {
            'first_name': booking_info[0],
            'last_name': booking_info[1],
            'email': booking_info[2],
            'number_of_tickets_booked': booking_info[3],
            'economy': booking_info[4],
            'premium_economy': booking_info[5],
            'first_class': booking_info[6],
            'price_total': booking_info[7],
            'discount_total': booking_info[8],
            'unique_ticket_code': booking_info[9] 
        }
        result.append(item)

   
    
    return result 

    #return booking_info

print(search_booking_by_ticket_code('UTC445566'))

# print example:
ticket_code = 'UTC445566'  # Replace with any unique ticket code
booking_info = search_booking_by_ticket_code(ticket_code)

if len(booking_info) > 0:
    print("Booking Information:")
    for row in booking_info:
        print("First Name:", row.first_name)
        print("Last Name:", row.last_name)
        print("Email:", row.email)
        print("Number of Tickets Booked:", row.number_of_tickets_booked)
        print("Economy:", row.economy)
        print("Premium Economy:", row.premium_economy)
        print("First Class:", row.first_class)
        print("Price Total:", row.price_total)
        print("Discount Total:", row.discount_total)
        print("Unique Ticket Code:", row.unique_ticket_code)
        print("--------------------------------------")
else:
    print("No booking found for the provided ticket code.")
    


#search by code:
    


print(search_booking_by_ticket_code)

#search booking by email:
        
@anvil.server.callable
def search_by_email(email):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-9KS360F\SQLEXPRESS;'
                          'Database=Assignment;'
                          'Trust_Connection=yes;')
    cursor = conn.cursor()

    # Execute the SQL query
    query = """
        SELECT *
        FROM flight_customer
        WHERE email = ?
    """
    cursor.execute(query, email)
    booking_info = cursor.fetchone()
    result = []
    
    if booking_info:
        item = {
            'first_name': booking_info[0],
            'last_name': booking_info[1],
            'email': booking_info[2],
            'number_of_tickets_booked': booking_info[3],
            'economy': booking_info[4],
            'premium_economy': booking_info[5],
            'first_class': booking_info[6],
            'price_total': booking_info[7],
            'discount_total': booking_info[8],
            'unique_ticket_code': booking_info[9] 
        }
        result.append(item)

    conn.close()
    
    return result

#display ticket booking:
#for admin
    
    

#another way to do this

@anvil.server.callable
def display_booking_info():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM flight_customer')
    rows = cursor.fetchall()
    data = []
    #print("ROOOOOWS ")
    #print(rows)
    for row in rows:
        item = {
            'first_name': row[0],
            'last_name': row[1],
            'email': row[2],
            'number_of_tickets_booked': row[3],
            'economy':row[4],
            'premium_economy':row[5] ,
            'first_class':row[6],
            'price_total':row[7],
            'discount_total':row[8],
            'unique_ticket_code':row[9] 

            }
        
        data.append(item)
    return data
   
    
print(display_booking_info())


@anvil.server.callable
def let_user_in(email, password):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-9KS360F\SQLEXPRESS;'
                          'Database=Assignment;'
                          'Trust_Connection=yes;')

    cursor = conn.cursor()
    ret = True

    sql_query = (f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}'")
    cursor.execute(sql_query)
   
    if cursor.fetchall() == []:
        ret = False
    return ret

#print(let_user_in('johndoe@hotmail.com', 'letmein12345')) 


#for Admin only access:
    
@anvil.server.callable
def let_admin_in(email, password):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-9KS360F\SQLEXPRESS;'
                          'Database=Assignment;'
                          'Trust_Connection=yes;')

    cursor = conn.cursor()
    ret = False  # Initialize as False

    # Check if the provided email and password match the admin credentials
    if email == 'Admin1' and password == 'adminpass':
        ret = True

    return ret


#retrieving booking info as a customer:



import pyodbc

@anvil.server.callable
def customer_booking(customer_email):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-9KS360F\SQLEXPRESS;'
                          'Database=Assignment;'
                          'Trust_Connection=yes;')

    cursor = conn.cursor()

    # Execute the SQL query
    query = """
        SELECT fc.first_name, fc.last_name, fc.email, fc.number_of_tickets_booked, fc.economy, fc.premium_economy, fc.first_class
        FROM flight_customer fc
        WHERE fc.email = ?
    """
    cursor.execute(query, (customer_email,))

    # Fetch the results
    booking_details = cursor.fetchall()

    # Close the database connection
    #cursor.close()
    #conn.close()

    return booking_details

    #test
    #customer_email = 'johndoe@hotmail.com'  
    #booking_info = customer_booking(customer_email)
    #print(booking_info)
    
    
    
    # Retrieve customer email from flight_customer table
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-9KS360F\SQLEXPRESS;'
                          'Database=Assignment;'
                          'Trust_Connection=yes;')
    
    cursor = conn.cursor()
    
    # Execute the SQL query to retrieve customer email
    
    # Get the password from user inputing it
    password = input("Enter your password: ")
    
    # Execute the SQL query to retrieve customer email based on password
    
    query = """
        SELECT email
        FROM users
        WHERE password = ? AND user_role = 'customer'
    """
    cursor.execute(query, (password,))
    
    # Fetch the customer email
    customer_email = cursor.fetchone()

    if customer_email:
        customer_email = customer_email[0]
        # Call the customer_booking function with the retrieved email
        booking_info = customer_booking(customer_email)
    
        # Display the retrieved customer email
        print("Customer email:", customer_email)
    
        # Display the booking information
        print("Booking details:", booking_info)
    else:
        print("Invalid password. Unable to retrieve booking details.")

    return customer_booking()




#retrieving all booking information as admin:
    

@anvil.server.callable
def admin_booking(admin_email, admin_password):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-9KS360F\SQLEXPRESS;'
                          'Database=Assignment;'
                          'Trust_Connection=yes;')

    cursor = conn.cursor()

    # Check if the provided email and password match the admin credentials
    query = """
        SELECT *
        FROM users
        WHERE email = ? AND password = ? AND user_role = 'admin'
    """
    cursor.execute(query, (admin_email, admin_password))

    admin = cursor.fetchone()

    if admin:
        # Execute the SQL query to retrieve all booking information
        query = """
            SELECT fc.first_name, fc.last_name, fc.email, fc.number_of_tickets_booked, fc.economy, fc.premium_economy, fc.first_class
            FROM flight_customer fc
        """
        cursor.execute(query)

        # Fetch the results
        booking_details = cursor.fetchall()

        # Close the cursor and database connection
        #cursor.close()
        #conn.close()

        
        return booking_details
    else:
        # Close the cursor and database connection
        cursor.close()
        conn.close()

        return None
    

#generating the reports for admin
@anvil.server.callable
def generate_booking_report():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-9KS360F\SQLEXPRESS;'
                          'Database=Assignment;'
                          'Trust_Connection=yes;')

    cursor = conn.cursor()

    # Execute the SQL query
    query = """
        SELECT
            fc.first_name,
            fc.last_name,
            fc.number_of_tickets_booked,
            fc.economy,
            fc.premium_economy,
            fc.first_class,
            (fc.economy + fc.premium_economy + fc.first_class) AS total_tickets,
            fc.discount_total,
            fc.unique_ticket_code,
            fb.subject_fb,
            fb.feedback,
            fb.response
        FROM
            flight_customer fc
        LEFT JOIN
            feedback fb ON fc.unique_ticket_code = fb.unique_ticket_code;
    """
    cursor.execute(query)

    # Fetch the results
    booking_report = cursor.fetchall()

    # Close the cursor and database connection
    cursor.close()
    conn.close()

    return booking_report

# Call the function to generate the booking report
report = generate_booking_report()

# Print the report
for row in report:
    print("First Name:", row.first_name)
    print("Last Name:", row.last_name)
    print("Number of Tickets Booked:", row.number_of_tickets_booked)
    print("Economy:", row.economy)
    print("Premium Economy:", row.premium_economy)
    print("First Class:", row.first_class)
    print("Total Tickets:", row.total_tickets)
    print("Discount Total:", row.discount_total)
    print("Unique Ticket Code:", row.unique_ticket_code)
    print("Subject:", row.subject_fb)
    print("Feedback:", row.feedback)
    print("Response:", row.response)
    print("--------------------------------------")
  
    
 # booking stats for reports on sales 
@anvil.server.callable
def get_booking_statistics():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-9KS360F\SQLEXPRESS;'
                          'Database=Assignment;'
                          'Trust_Connection=yes;')

    cursor = conn.cursor()

    # Get number of tickets booked
    query_tickets_booked = "SELECT SUM(number_of_tickets_booked) FROM flight_customer"
    cursor.execute(query_tickets_booked)
    tickets_booked = cursor.fetchone()[0]

   

    # Get total and total with discount
    query_totals = "SELECT SUM((economy * 100) + (premium_economy * 200) + (first_class * 300)) AS total, SUM((economy * 100 + premium_economy * 200 + first_class * 300) - discount_total) AS total_with_discount FROM flight_customer"
    cursor.execute(query_totals)
    totals = cursor.fetchone()
    total = totals.total
    total_with_discount = totals.total_with_discount

    # Get unit per transaction
    query_unit_per_transaction = "SELECT AVG(economy + premium_economy + first_class) FROM flight_customer"
    cursor.execute(query_unit_per_transaction)
    unit_per_transaction = cursor.fetchone()[0]

    # Get average transaction value
    query_average_transaction_value = "SELECT AVG((economy * 100 + premium_economy * 200 + first_class * 300) - discount_total) FROM flight_customer"
    cursor.execute(query_average_transaction_value)
    average_transaction_value = cursor.fetchone()[0]

    # Get highest customer
    query_highest_customer = "SELECT CONCAT(first_name, ' ', last_name) AS highest_customer, (economy + premium_economy + first_class) AS total_tickets FROM flight_customer ORDER BY total_tickets DESC"
    cursor.execute(query_highest_customer)
    highest_customer = cursor.fetchone()
    highest_customer_name = highest_customer.highest_customer
    highest_customer_total_tickets = highest_customer.total_tickets

    # Get highest tickets booked per customer
    query_highest_tickets_per_customer = "SELECT CONCAT(first_name, ' ', last_name) AS highest_tickets_customer, MAX(economy + premium_economy + first_class) AS highest_tickets FROM flight_customer GROUP BY first_name, last_name ORDER BY highest_tickets DESC"
    cursor.execute(query_highest_tickets_per_customer)
    highest_tickets_per_customer = cursor.fetchone()
    highest_tickets_customer_name = highest_tickets_per_customer.highest_tickets_customer
    highest_tickets_customer_tickets = highest_tickets_per_customer.highest_tickets

    # Close the cursor and database connection
    cursor.close()
    conn.close()

    # Return the statistics as a dictionary
    statistics = {
        "Tickets Booked": tickets_booked,
        "Total": total,
        "Total with Discount": total_with_discount,
        "Unit per Transaction": unit_per_transaction,
        "Average Transaction Value": average_transaction_value,
        "Highest Customer Name": highest_customer_name,
        "Highest Customer Total Tickets": highest_customer_total_tickets,
        "Highest Tickets Customer Name": highest_tickets_customer_name,
        "Highest Tickets Customer Tickets": highest_tickets_customer_tickets
    }

    return statistics


statistics = get_booking_statistics()

# Print the statistics
print("Booking Statistics:")
print("Tickets Booked:", statistics["Tickets Booked"])
print("Total:", statistics["Total"])
print("Total with Discount:", statistics["Total with Discount"])
print("Unit per Transaction:", statistics["Unit per Transaction"])
print("Average Transaction Value:", statistics["Average Transaction Value"])
print("Highest Customer Name:", statistics["Highest Customer Name"])
print("Highest Customer Total Tickets:", statistics["Highest Customer Total Tickets"])
print("Highest Tickets Customer Name:", statistics["Highest Tickets Customer Name"])
print("Highest Tickets Customer Tickets:", statistics["Highest Tickets Customer Tickets"])


#"Economy Tickets": economy_tickets,
#"Premium Economy Tickets": premium_economy_tickets,
#"First Class Tickets": first_class_tickets,

#print("Economy Tickets:", statistics["Economy Tickets"])
#print("Premium Economy Tickets:", statistics["Premium Economy Tickets"])
#print("First Class Tickets:", statistics["First Class Tickets"])

#signup user

@anvil.server.callable
def signup(first_name, last_name, email, password):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-9KS360F\SQLEXPRESS;'
                          'Database=Assignment;'
                          'Trust_Connection=yes;')
    cursor = conn.cursor()

    # Execute the SQL query
    sql_query = "INSERT INTO [users] (first_name, last_name, email, password, user_role) VALUES (?, ?, ?, ?, 'customer')"
    cursor.execute(sql_query, (first_name, last_name, email, password))
    conn.commit()
   
    return "Successfully Signed Up"







#cancel a booking by utc:

@anvil.server.callable  
def delete_booking(unique_ticket_code):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-9KS360F\SQLEXPRESS;'
                          'Database=Assignment;'
                          'Trust_Connection=yes;')
    cursor = conn.cursor()

   
    query = "DELETE FROM flight_customer WHERE unique_ticket_code = ?"
    cursor.execute(query, (unique_ticket_code,))

   
    conn.commit()


    return "Booking deleted successfully"


# print example
#ticket_code = 'UTC445566'
#result = delete_booking(ticket_code)
#print(result)


##admin reports and cvs:
    


import csv
import pyodbc

def get_booking_statistics():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-9KS360F\SQLEXPRESS;'
                          'Database=Assignment;'
                          'Trust_Connection=yes;')

    cursor = conn.cursor()

    # Get number of tickets booked
    query_tickets_booked = "SELECT SUM(number_of_tickets_booked) FROM flight_customer"
    cursor.execute(query_tickets_booked)
    tickets_booked = cursor.fetchone()[0]

    # Get total and total with discount
    query_totals = "SELECT SUM((economy * 100) + (premium_economy * 200) + (first_class * 300)) AS total, SUM((economy * 100 + premium_economy * 200 + first_class * 300) - discount_total) AS total_with_discount FROM flight_customer"
    cursor.execute(query_totals)
    totals = cursor.fetchone()
    total = totals.total
    total_with_discount = totals.total_with_discount

    # Get unit per transaction
    query_unit_per_transaction = "SELECT AVG(economy + premium_economy + first_class) FROM flight_customer"
    cursor.execute(query_unit_per_transaction)
    unit_per_transaction = cursor.fetchone()[0]

    # Get average transaction value
    query_average_transaction_value = "SELECT AVG((economy * 100 + premium_economy * 200 + first_class * 300) - discount_total) FROM flight_customer"
    cursor.execute(query_average_transaction_value)
    average_transaction_value = cursor.fetchone()[0]

    # Get highest customer
    query_highest_customer = "SELECT CONCAT(first_name, ' ', last_name) AS highest_customer, (economy + premium_economy + first_class) AS total_tickets FROM flight_customer ORDER BY total_tickets DESC"
    cursor.execute(query_highest_customer)
    highest_customer = cursor.fetchone()
    highest_customer_name = highest_customer.highest_customer
    highest_customer_total_tickets = highest_customer.total_tickets

    # Get highest tickets booked per customer
    query_highest_tickets_per_customer = "SELECT CONCAT(first_name, ' ', last_name) AS highest_tickets_customer, MAX(economy + premium_economy + first_class) AS highest_tickets FROM flight_customer GROUP BY first_name, last_name ORDER BY highest_tickets DESC"
    cursor.execute(query_highest_tickets_per_customer)
    highest_tickets_per_customer = cursor.fetchone()
    highest_tickets_customer_name = highest_tickets_per_customer.highest_tickets_customer
    highest_tickets_customer_tickets = highest_tickets_per_customer.highest_tickets

    # Close the cursor and database connection
    cursor.close()
    conn.close()

    # Return the statistics as a dictionary
    statistics = {
        "Tickets Booked": tickets_booked,
        "Total": total,
        "Total with Discount": total_with_discount,
        "Unit per Transaction": unit_per_transaction,
        "Average Transaction Value": average_transaction_value,
        "Highest Customer Name": highest_customer_name,
        "Highest Customer Total Tickets": highest_customer_total_tickets,
        "Highest Tickets Customer Name": highest_tickets_customer_name,
        "Highest Tickets Customer Tickets": highest_tickets_customer_tickets
    }

    # Generate CSV file
    csv_filename = "booking_statistics.csv"
    with open(csv_filename, "w", newline="") as csvfile:
        fieldnames = ["Statistic", "Value"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for stat, value in statistics.items():
            writer.writerow({"Statistic": stat, "Value": value})

    return statistics

# Call the function
booking_statistics = get_booking_statistics()
print(booking_statistics)

##

import anvil.media

@anvil.server.callable
def downloadCSV():
    arr = []
    choices = ["users", "tickets", "flight_customer" , "feedback"]
    for i in choices:
        df = pd.DataFrame(cursor.execute((f"Select * FROM {i}")))
        df.to_csv(f"{i}.csv", index=False)


import pandas as pd

def downloadCSV_flight(cursor):
    sql_query = "SELECT * FROM flight_customer"
    cursor.execute(sql_query)
    val = cursor.fetchall()
    cols = ['first_name', 'last_name', 'total_all']
    df = pd.DataFrame(val, columns=cols)
    df.to_csv('test.csv', index=False)


#another example



import pandas as pd
import anvil.media
@anvil.server.callable
def downloadcsv_stats(cursor):
    sql_query = "SELECT AVG(economy + premium_economy + first_class) FROM flight_customer"
    cursor.execute(sql_query)
    val = cursor.fetchall()
    
    df = pd.DataFrame(val)
    df.to_csv('stat.csv', index=False)
    
    return anvil.media.from_file('stat.csv')




