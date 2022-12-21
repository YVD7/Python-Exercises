# balance = 500

# def deposit(amount):
#     global balance
#     balance += amount
#     return balance

# def withdraw(amount):
#     global balance
#     balance -= amount
#     return balance

# print(deposit(500))

def make_account():
    return{'balance':0}

def deposit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']

a = make_account()
print(deposit(a,5000))