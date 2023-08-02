from manager import Manager
def menu():
    print("pick an option: ")
    print("1. generate password")
    print("2. update password")
    print("3. delete password")
    print("4. get password")
    print("5. Quit ")
    choice=input("eneter option: ")
    return choice

def generate_pass(m):
    site=input("eneter site name: ")
    usr=input("eneter username: ")
    length=input("password length: ")
    print("password: "+m.generate_passwor)
     
    usr= input("eneter username: ")
    print("username:",usr)
    print("password: ",m.get_password(site,usr))

def get_pass(m):
    site=input("enter site: ")
    usr=input("enter username: ")
    m.delete(site,usr)

def delete(m):
    site=input("enter site: ")
    usr=input("eneter username: ")
    m.delete(site,usr)

PIN ="0000"
def login():
    while True:
        p= input("enter pin:  ")
        if p==PIN:
            break
def update(m):
    site=input+("enter site")
    usr=input("enter user")
    p=input("enter new purs")
    m.update(site,usr,p)
    print("password update")
def main():
    login()
    m=Manager()
    m.load()
    while True:
        choice=menu(m)
        if choice==1:
            generate_pass(m)
        elif choice==2:
            update(m)
        elif choice==3:
            delete(m)
        elif choice==4:
            get_pass(m)
        else:
            m.save()
            break


main()