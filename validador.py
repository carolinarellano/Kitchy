
def signup(username, username_valid, password, password_valid):
    import usuario
    import passw

    if usuario.username(username) == '' or passw.password(password) == '':
            print('No valido')
            correct = False

    else:
        if usuario.username(username) == True:
            if username == username_valid and username != '':
                    correct = True
                    print("User created")

        if passw.password(password) == True:
            if password == password_valid and password != '':
                    correct = True             
                    print("Password created")

       

def usuario(username,password):
    users_pass_file = 'users.txt'
    f = open(users_pass_file,'r')
    usuarios = f.readlines()
    for i in range(len(usuarios)):
        if username and password in usuarios[i]:
            print("Usuario Encontrado")
        else:
            print("Usuario no Encontrado")
