import json
import datetime
import pandas as pd
import numpy as np

# Input and read in customer info based on customer_id
def retrieve_customer_profile(customer_id):
	customer_id = customer_id + '.json'
	with open(customer_id, "r") as jsonFile:
		data = json.load(jsonFile)
	return data

print("Good Day!  Please provide your customer id for further assistance.")
print("  ")  
print("Note: your id should begin with SATX followed by numbers")
print("  ")  
print("The default ID# is SATX01, if you need to establish an account with us, please contact your local representative.  Thank you!")
print("  ")  
customer_id = input("ID#: ")

data = retrieve_customer_profile(customer_id)

print("~~~ Welcome to your terminal checkbook! ~~~")

print("How may I help you today?")

print("You have the following options:")
print("1) view current balance")
print("2) record a debit (withdraw)")
print("3) record a credit (deposit)")
print("4) view your account summary")
print("5) exit")

def service_main(service_function):
	service_function = int(service_function)
	if service_function == 1:
		print('Your current balance is: {}{:.2f}'.format("$",current_balance))
	elif service_function == 2:
		get_entry_details()
	elif service_function == 3:
		get_entry_details()
	elif service_function == 4:
		df = pd.DataFrame(data)
		print('Your current balance is: {}{:.2f}'.format("$",current_balance)) 
		print(df)
	elif service_function == 5:
		print('Thanks for visiting!')
	else:
		print('Selection not valid.')
		service_function = input("Please indicate your choice by entering 1 digit, from 1 through 5: ")
		return service_function
		service_function = input("Please indicate your choice by entering 1 digit, from 1 through 5: ")
		return service_function
		service_function = input("Please indicate your choice by entering 1 digit, from 1 through 5: ")
		return service_function
		

service_function = input("Please indicate your choice by entering 1 digit, from 1 through 5: ")


# general number processing
def process_num(b):
	b = str(b)
	nf = b.replace(',','')
	return float(nf)

# calculating current balance
credit = [process_num(b['amount']) for b in data if b['amount'] and b['record_type'] == 'credit']
total_credit = sum(credit)

debit = [process_num(b['amount']) for b in data if b['amount'] and b['record_type'] == 'debit']
total_debit = sum(debit)

current_balance = total_credit - total_debit

# distinguish type of service in order to auto write in record_type
def record_distinguish(service_function):
	service_function = int(service_function)
	record_type = ''
	if service_function == 2:
		record_type = record_type + 'debit'
	elif service_function == 3:
		record_type = record_type + 'credit'
	return record_type
REC = record_distinguish(service_function)

# When user select 2 to withdraw money, this function will record the debit
def add_entry(customer_id, transaction_id, amount, record_type, category, store, description):
	amount = float(amount)
	global current_balance
	data.append({"customer_id": customer_id, "transaction_id": transaction_id, "amount": amount, "record_type": record_type, "category": category,"store": store,"description": description})
	if REC == "debit":
		updated_balance = current_balance - amount
		updated_balance = float(updated_balance)
		print("You've withdrawn {}{}".format("$",amount))
		print('Your updated current balance is: {}{:.2f}'.format("$",updated_balance))
	elif REC == "credit":
		print("You've deposited {}{}".format("$",amount))
		updated_balance = current_balance + amount
		print('Your updated current balance is: {}{:.2f}'.format("$",updated_balance))
	return data
def get_entry_details():
	customer_id = data[0]["customer_id"]
	transaction_id = str(datetime.datetime.now())
	amount = input("How much will the amount be? ")
	record_type = REC
	category = input("What's the category for this purchase?")
	if category == '':
		category = 'null'
	store = input("Which store did you shop with?")
	if store == '':
		store = 'null'
	description = input("Would you like to enter description for the transaction?")
	if description == '':
		description = 'null'
	
	return add_entry(customer_id, transaction_id, amount, record_type, category, store, description)

#get_entry_details()
service_main(service_function)


def save_transaction():
	print("Thank you for your visit!")
	file_name = data[0]["customer_id"]
	file_name = file_name + ".json"
	with open(file_name, "w") as jsonFile:
		json.dump(data,jsonFile)
save_transaction()








# # Create customer profile
# account_info = []
# seen = set()

# def add_entry(account_info, customer_id,transaction_id, amount, record_type, category, store, description): #type = debt or credit

#     # check if in seen set
#     if (transaction_id) in seen:
#         return account_info

#     # add to seen set
#     seen.add(tuple([customer_id, transaction_id, amount, record_type, category, store, description]))
#     # need to find a way to create new id

#     # append to results list
#     account_info.append(
#     	{"customer_id": customer_id,
#     	"transaction_id": transaction_id, 
#     	"amount": amount, 
#     	"record_type": record_type, 
#     	"category": category,
#     	"store": store,
#     	"description": description})

#     return account_info

# args = ['SATX01','SATX01_0001', '5,000.00', 'credit', 'salary', 'Mailchimp', 'paycheck']
# account_info = add_entry(account_info, *args)  # add entry - SUCCESS

# args2 = ['SATX01','SATX01_0002', '75.30', 'debit','grocery','HEB', 'weekly shopping']
# account_info = add_entry(account_info, *args2)  # add another - 

# # writing info into json file 
# with open("file_name.json", "w") as jsonFile:
# 	json.dump(data_to_write_to_json,jsonFile)