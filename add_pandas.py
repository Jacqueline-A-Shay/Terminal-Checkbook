import json
import datetime
import pandas as pd

def retrieve_customer_profile(customer_id):
	customer_id = customer_id + '.json'
	return customer_id

print("Good Day!  Please provide your customer id for further assistance.")
print("  ")  
print("Note: your id should begin with SATX followed by numbers")
print("  ")  
print("The default ID# is SATX01, if you need to establish an account with us, please contact your local representative.  Thank you!")
print("  ")  
customer_id = input("ID#: ")

data = retrieve_customer_profile(customer_id)

df = pd.read_json (retrieve_customer_profile(customer_id))
print (df)
