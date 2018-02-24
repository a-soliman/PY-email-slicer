def get_username( email_address):
	if len(email_address) <= 0:
		return -1
	if email_address.find('@') == -1:
		return 'incorrect provided email adress'
		
	username = email_address[:email_address.index('@')]
	return username