# 5-9===================================================================
# ----------------------------------------------------------------------
users = ['Admin', 'Eric', 'Steven', 'David', 'Keven']
print(users)
users.sort(reverse = True)
print(users)
for user in users:
    if user == 'Admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print("Hello " + user + ", thank you logging in again.")

# 5-10===================================================================
# ----------------------------------------------------------------------
users = ['Admin', 'Eric', 'Steven', 'David', 'Keven']
print(users)
users.sort(reverse = True)
print(users)
if users:
    for user in users:
        if user == 'Admin':
            print("Hello Admin, would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you logging in again.")
else:
    print("We need to find some users!")
# ----------------------------------------------------------------------
users = []
if users:
    for user in users:
        if user == 'Admin':
            print("Hello Admin, would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you logging in again.")
else:
    print("We need to find some users!")












