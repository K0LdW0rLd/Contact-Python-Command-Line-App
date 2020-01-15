from peewee import *

db = PostgresqlDatabase('people', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModal):
    name = CharField()
    number = IntegerField()
    email = CharField()

db.create_tables([Contact])




# Ask Question of what they want to do

i = int(input('Enter \'1\' to add a contact, \'2\' to search through contacts, \'3\' to update a contact, and \'4\' to delete a contact: '))



# If and else to get the correct input
if i==1:
    print('I printed 1')
    # Get the data to add 
    nm = input('Enter Name: ')
    ph = input('Enter Number: ')
    em = input('Enter Email: ')
    # Add data then save it
    nms = Person(name = nm , number = ph , email=em)
    nms.save()
elif i==2:
    print('I printed 2')
    inputname = input('Enter the name of the person you would like to find: ')
    searchName = Contact.get(Contact.name == inputname)
    print(searchName)
elif i==3:
    print('I printed 3')
    upd = int(input('Enter 1 to update name, 2 to update phone number, and 3 to update email: '))
    if upd == 1:
        updnam = input('Enter name of person you would like to update: ')
        newname = input('Enter new name of contact: ')
        findupdname = Contact.get(Contact.get == updnam)
        findupdname.name = newname
        findupdname.save()

    elif upd == 2:
        pass
    elif upd == 3:
        pass
    else:
        print('You did not enter 1, 2, or 3')

elif i==4:
    print('I printed 4')
else:
    print('You did enter 1, 2, 3, or 4')