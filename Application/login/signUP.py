import os

__all__ = ['signup']

user_dir = os.getcwd()
_signup_dict = {}

def checkusername(fn):
    def inner(*args,**kwargs):
        print("Verifying User...")
        print(args)
        with open (f'{user_dir}/login/users.txt', 'r') as fp:
            verify_user = f'username={args[0]}'
            for line in fp:
                if line.__contains__(verify_user):
                    # print(f'user exists')
                    inner.userexist = True
                else:
                    inner.userexist = False
        return fn(*args, **kwargs)
    return inner

# TODO: extend it to retype_password,email_id,phone
@checkusername
def signup(user_name, password):
    global _signup_dict
    if not signup.userexist:
        _signup_dict['username'] = user_name
        _signup_dict['password'] = password
        _save_creds()
    else:
        print(f'User Name:{user_name} exists already')
    # signup.username = user_name
    # return signup_dict

def _save_creds():
    with open (f'{user_dir}/login/users.txt', 'a+') as fp:
        for item in _signup_dict:
            fp.write(str(f'{item}={_signup_dict[item]}|'))
        fp.write("\n")
    print ("User: {} signed up".format (_signup_dict['username']))


# signup('ravi1','123')
