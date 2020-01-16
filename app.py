from peewee import *

db = PostgresqlDatabase('contact', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    name = CharField()
    number = CharField()
    email = CharField()

# db.drop_tables([Contact])
# db.create_tables([Contact])

# kelly = Contact(name= 'Kelly' , number= 7573397428 , email= '90kcol@gmail.com')
# kelly.save()

# Ask Question of what they want to do

def contactList():
    i = int(input('Enter \'1\' to add a contact, \'2\' to search through contacts, \'3\' to update a contact, and \'4\' to delete a contact: '))
    # If and else to get the correct input
    # Create
    if i==1:
        print('You selected to add a contact.')
        # Get the data to add 
        nm = input('Enter Name: ')
        ph = int(input('Enter the Phone Number(No hyphen or spaces): '))
        em = input('Enter Email: ')
        # Add data then save it
        nms = Contact(name= nm , number= ph , email=em)
        nms.save()
        res = input('Would you like to restart y/n: ')
        if res == 'y':
            contactList()
        else:
            return
    # Read
    elif i==2:
        print('You selected to search a contact.')
        inputName = input('Enter the name of the person you would like to find: ')
        searchName = Contact.select().where(Contact.name == inputName)
        for contact in searchName:
            print(contact.name)
            print(contact.number)
            print(contact.email)
        res = input('Would you like to restart y/n: ')
        if res == 'y':
            contactList()
        else:
            return
    # Update
    elif i==3:
        print('You selected to update a contact.')
        upd = int(input('Enter 1 to update name, 2 to update phone number, and 3 to update email: '))
        if upd == 1:
            updNam = input('Enter the name of the person you would like to update: ')
            newName = input('Enter new name of the contact: ')
            findUpdName = Contact.get(Contact.name == updNam)
            findUpdName.name = newName
            findUpdName.save()
            print(f'Name changed to {findUpdName.name}')
            res = input('Would you like to restart y/n: ')
            if res == 'y':
                contactList()
            else:
                return
        elif upd == 2:
            updNum = input('Enter the name of the person you would like to update: ')
            newNum = int(input('Enter the new number of the contact: '))
            findUpdNum = Contact.get(Contact.name == updNum)
            findUpdNum.number = newNum
            findUpdNum.save()
            print(f'{findUpdNum.name} number changed to {findUpdNum.number}')
            res = input('Would you like to restart y/n: ')
            if res == 'y':
                contactList()
            else:
                return
        elif upd == 3:
            updEmail = input('Enter the name of the person you would like to update: ')
            newEmail = input('Enter the new email of the contact: ')
            findUpdEmail = Contact.get(Contact.name == updEmail)
            findUpdEmail.email = newEmail
            findUpdEmail.save()
            print(f'{findUpdEmail.name} email changed to {findUpdEmail.email}')
            res = input('Would you like to restart y/n: ')
            if res == 'y':
                contactList()
            else:
                return
        else:
            print('You did not enter 1, 2, or 3')
            return
    # Delete
    elif i==4:
        print('You selected to delete a contact.')
        delName = input('Enter the name of the contact you would like to delete: ')
        delCont = Contact.get(Contact.name == delName)
        delCont.delete_instance()
        print('Contact has been deleted.')
        res = input('Would you like to restart y/n: ')
        if res == 'y':
            contactList()
        else:
            return
    else:
        print('You did not enter 1, 2, 3, or 4')
        contactList()

# Call the function
contactList()




