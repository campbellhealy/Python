email_address = lambda username, domain: f'Email Address: {username}{domain}'

# def email_address(
#     username, domain): return f'Email Address: {username}{domain}'


user1 = email_address('username', '@gmail.com')
user2 = email_address('username2', '@gmail.com')

print(user1)
print(user2)
