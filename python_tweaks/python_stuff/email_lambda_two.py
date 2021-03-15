user1_email = input('What is your username?')
user2_email = input('What is your friends username?')

email_address = lambda username, domain: f'Email Address: {username}{domain}'

user1 = email_address(user1_email, '@gmail.com')
user2 = email_address(user2_email, '@gmail.com')



print(user1)
print(user2)
