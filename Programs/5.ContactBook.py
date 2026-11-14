#Contact book
contacts=[]
while True:
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        name=input("Enter the name: ")
        phone=input("Enter the phone number: ")
        email=input("Enter the email: ")
        contact={"name":name,"phone":phone,"email":email}
        contacts.append(contact)
    elif choice==2:
        print("The contacts present are: ")
        for i in contacts:
            print(i)
    elif choice==3:
        numandname=input("Enter the number or name of the contact: ")
        if numandname.isdigit():
            numandname=int(numandname)
            for i in contacts:
                if i["name"] == numandname:
                    print(i)
                    break
        else:
            for i in contacts:
                if i["name"] == numandname:
                    print(i)
                    break
    elif choice==4:
        numandname=input("Enter the number or name of the contact: ")
        if numandname.isdigit():
            numandname=int(numandname)
            for i in contacts:
                if i["name"] == numandname:
                    contacts.remove(i)
                    break
        else:
            for i in contacts:
                if i["name"] == numandname:
                    contacts.remove(i)
                    break
    else:
        break

