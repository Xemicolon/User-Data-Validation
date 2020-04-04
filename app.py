import random
import string

user_id = 0
users = []


# create a function to get user's details generate random password or use a password of your choice and password must
# be longer than 7 characters then add user details to our users containers

def create_user():
    # Get user's details
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    email = input('Enter your email: ')

    # Generate a random password using user's details

    def generate_password():
        letters = string.ascii_letters
        generated_password = first_name[0:2] + \
            last_name[-2:] + ''.join(random.sample(letters, 5))
        return generated_password

    random_password = generate_password()
    use_random_password = ''

    while True:
        use_random_password = input(
            f'Your random generated password is {random_password}. Do you want use it? (Y/N): ').lower()
        if use_random_password == 'n':
            use_random_password = input(
                'Enter a password of your choice then: ')
            user_password = use_random_password
            while len(user_password) < 7:
                user_password = input(
                    f'Password must be 7 characters or longer: ')
            users.append(
                {'First Name': first_name, 'Last Name': last_name, 'Email': email, 'Password': user_password})
            print(users)
            return users
        elif use_random_password == 'y':
            users.append(
                {'First Name': first_name, 'Last Name': last_name, 'Email': email, 'Password': random_password})
            print(f'{users}')
            return users
        else:
            print(f'Type Y or N')


# Use a while loop to create a list of new users.


while True:
    create_new_user = input(
        'Do you want to create a new user? (Y/N): ').lower()
    if create_new_user == 'y':
        create_new_user
        user_id += 1
        print(f'Please enter details below for User{user_id}')
        create_user()
    elif create_new_user == 'n':
        print(f'Have a nice time! \n')
        break
    else:
        print(f'Type Y or N')

# Finally, check if there's data or not in our users container, then display it.

if len(users) <= 0:
    print(f'There are no registered user at this moment')
else:
    print(f'Registered Users -  {users}')
