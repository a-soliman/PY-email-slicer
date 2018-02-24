from methods import *

# GET USER'S EMAIL ADDRESS
email_address = input('PLease enter your email address : ').strip()
email_address = email_address.lower()

# SLICE OUT THE USER NAME


# SLICE THE DOMAIN NAME
#print(get_domain_name(email_address))
# DISPLAY OUTPUT MESSAGE
print(get_user_info(email_address))