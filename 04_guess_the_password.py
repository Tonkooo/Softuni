password = str(input())
secret_password = str('s3cr3t!P@ssw0rd')

if password == secret_password:
    print(f'Welcome')
else:
    print(f"Wrong password!")
