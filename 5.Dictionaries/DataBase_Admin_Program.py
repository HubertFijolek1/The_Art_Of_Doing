#Dictionaries Challenge 22: Database Admin Program

print("Welcome to the Database Admin Program")

log_on_information = {
    'admin00':'Hubertq25',
    'admin2':'Witam12345',
    'admin3':'Poland123',
    'admin4':'Hello123',
    'admin5':'water'
}

print(log_on_information.keys())
print(log_on_information.values())
for x in log_on_information.items():
    print(x)
# First Output
username = input("Enter your username: ")
correct_password = log_on_information[username]
if username in log_on_information and username=="admin00":
    password = input("Enter your password: ")
    if password == correct_password:
        for x,y in log_on_information.items():
            print("Username: "+str(x)+"\t\tPassword: "+str(y))



# Second,Third,Fourth and Five Output
elif username in log_on_information:
    password = input("Enter your password: ")
    if password == correct_password:
        print("\nHello "+str(username)+"! You are logged in. ")
        change_passwd = input("would you like to change your password: ").lower()
        if change_passwd=="yes":
            changed_password = input("What would you like your new password to be: ")
            if len(changed_password) <8:
                print("Your password is too short!")
            elif len(changed_password) >=8:
                print("\n" +str(username)+"your password is "+str(changed_password))
        else:
            print("Okey, so that's all :D")

    else:
        print("Your password is wrong, i think you are not the person , \nwho you say that you are... that's why fuck off!!!!")
else:
    print("Your not in database, sorry and bye")