#CONTACT BOOK
#1.Add contact(name,phone,email)
#2.view all contacts
#3.update contact
#4.delete contact
#5.search contact
#6.count total contacts
#7.exit program


''' contacts={
     'name1':{'phone':12354,'email':1@gmail.com}
     'name2':{'phone':12364,'email':2@gmail.com}
     }'''

contacts={}

def addcontact():
    name=input('Enter name: ')
    if name in contacts:
        print('contact already exist!')
    else:
        phone=input('enter phone number: ')
        email=input('enter email: ')
        contacts[name]={'phone':phone, 'email':email}
        print('contact added successfully')
        

def menu():
  while True:
    print('-'*5,'CONTACT BOOK MENU','-'*5)
    print('1.Add contact')
    print('2.View all contacts')
    print('3.Update contact')
    print('4.Delete contact')
    print('5.Search contact')
    print('6.Count total contacts')
    print('7.Exit')

    choice=input('Enter your choice(1-7): ')

    if choice=='1':
        addcontact()
    elif choice=='2':
        viewcontact()
    elif choice=='3':
        updatecontact()

    elif choice=='4':
        deletecontact()
    elif choice=='5':
        searchcontact()
    elif choice=='6':
        counttotalcontacts()
    elif choice=='7':
        print('Exiting contact book')
    else:
        print('Invalid choice')
    

    
menu()
