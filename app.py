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

db.create_tables([Contact])

# kelly = Contact(name= 'Kelly' , number= 757-339-7428 , email= '90kcol@gmail.com')
# kelly.save()

# Ask Question of what they want to do

i = int(input('Enter \'1\' to add a contact, \'2\' to search through contacts, \'3\' to update a contact, and \'4\' to delete a contact: '))


# If and else to get the correct input
# Create
if i==1:
    print('You selected to add a contact.')
    # Get the data to add 
    nm = input('Enter Name: ')
    ph = int(input('Enter Number: '))
    em = input('Enter Email: ')
    # Add data then save it
    nms = Contact(name= nm , number= ph , email=em)
    nms.save()
# Read
elif i==2:
    print('You selected to search a contact.')
    inputname = input('Enter the name of the person you would like to find: ')
    searchName = Contact.get(Contact.name == inputname)
    print(searchName)
# Update
elif i==3:
    print('You selected to update a contact.')
    upd = int(input('Enter 1 to update name, 2 to update phone number, and 3 to update email: '))
    if upd == 1:
        updnam = input('Enter the name of the person you would like to update: ')
        newname = input('Enter new name of the contact: ')
        findupdname = Contact.get(Contact.get == updnam)
        findupdname.name = newname
        findupdname.save()
    elif upd == 2:
        updnum = input('Enter the name of the person you would like to update: ')
        newnum = input('Enter the new number of the contact: ')
        findupdnum = Contact.get(Contact.get == updnum)
        findupdnum.number = newnum
        findupdnum.save()
    elif upd == 3:
        updemail = input('Enter the name of the person you would like to update: ')
        newemail = input('Enter the new email of the contact: ')
        findupdemail = Contact.get(Contact.get == updemail)
        findupdemail.email = newemail
        findupdemail.save()
    else:
        print('You did not enter 1, 2, or 3')
# Delete
elif i==4:
    print('You selected to delete a contact.')
    delcont = input('Enter the name of the contact you would like to delete: ')
    delcont.delete_instance()
else:
    print('You did enter 1, 2, 3, or 4')