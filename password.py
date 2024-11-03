# Sign up page
print('Sign up page')
un = input('Set a username: ')
pw = input('Set your password: ')
print('Good job, now sign in')

# Prompt for username and password
in_un = input('Username: ')
in_pw = input('Password: ')

# Check credentials
if in_un == un and in_pw == pw:
    print('Good Job, ' + un + '!')
else:
    print('Wrong')
    in_un = input('Username: ')
    in_pw = input('Password: ')
    if in_un == un and in_pw == pw:
        print('Good Job, ' + un + '!')
    else:
        print('Wrong no more chances!')
