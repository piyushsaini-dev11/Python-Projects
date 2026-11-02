master_pwd = input("interface of password manager: ")


def add():
    name =input("Account Name: ")
    pwd =input("Password: ")
    
    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")
  
    
def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            print(repr(data))
            user, passw = data.split("|")
            print("User:", user, "| Password:", passw)
   
       
       
while True:
    mode = input("would you like add a new password or view existing ones, add/view, type q for quit   ").lower()
    
    if mode == "q":
        break
    
    if mode == "add":
        add()
    
    elif mode == "view":
        view()
    
    else:
        print("invalid mode")
        continue
    
        