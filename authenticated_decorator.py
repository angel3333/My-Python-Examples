# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Admin',
    'valid': True
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        user = args[0]
        if user['valid'] and user['name'] == 'Admin':
            return fn(*args, **kwargs)
        else:
            print(f"User '{user['name']}' is not authenticated")
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
