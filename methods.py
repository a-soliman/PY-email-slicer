def get_username( email_address):
	if len(email_address) <= 0:
		return -1
	if email_address.find('@') == -1:
		return 'incorrect provided email adress'

	username = email_address[:email_address.index('@')]
	return username

# GET DOMAIN_NAME
def get_domain_name( email_address ):
	if len(email_address) <= 0:
		return -1

	if email_address.find('@') == -1:
		return 'incorrect provided email address.'

	domain_name = email_address[email_address.index('@')+1:]
	return domain_name

def get_user_info( email_address ):
	if len(email_address) <= 0:
		return 'Please provide email address.'

	if email_address.find('@') == -1:
		return 'Please provide a valid email address.'

	user = { 
		'username': get_username(email_address),
		'domain_name': get_domain_name(email_address)		
	}

	return 'Username: {}, Domain: {}.'.format(user['username'], user['domain_name'])