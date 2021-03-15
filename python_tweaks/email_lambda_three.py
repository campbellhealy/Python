# Use Terminal
# Variables
user1_email = input('What is your username?')
user2_email = input('What is your friends username?')
fixed_domain = '@gmail.com'

# lambda expression
email_address = lambda username, fixed_domain: f'Email Address: {username}{fixed_domain}'

# function requests
user1 = email_address(user1_email, fixed_domain)
user2 = email_address(user2_email, fixed_domain)

# outputs
print(user1)
print(user2)
