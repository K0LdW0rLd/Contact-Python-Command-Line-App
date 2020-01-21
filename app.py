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

def contact_list():
    i = int(input('Enter \'1\' to add a contact,\n \'2\' to search through contacts,\n \'3\' to update a contact,\n \'4\' to delete a contact: '))
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
            contact_list()
        else:
            return
    # Read
    elif i==2:
        print('You selected to search a contact.')
        search_input = int(input('Enter 1 to see all contacts or 2 to search contact by name: '))
        if search_input == 1:
            contact = Contact.select()
            for contact in contact:
                print(f'Name: {contact.name} Number: {contact.number} Email: {contact.email}')

            res = input('Would you like to restart y/n: ')
            if res == 'y':
                contact_list()
            else:
                return
        elif search_input == 2:
            input_name = input('Enter the name of the person you would like to find: ')
            search_name = Contact.select().where(Contact.name == input_name)
            for contact in search_name:
                print(contact.name)
                print(contact.number)
                print(contact.email)
            res = input('Would you like to restart y/n: ')
            if res == 'y':
                contact_list()
            else:
                return
    # Update
    elif i==3:
        print('You selected to update a contact.')
        upd = int(input('Enter 1 to update name, 2 to update phone number, and 3 to update email: '))
        if upd == 1:
            upd_nam = input('Enter the name of the person you would like to update: ')
            new_name = input('Enter new name of the contact: ')
            find_upd_name = Contact.get(Contact.name == upd_nam)
            find_upd_name.name = new_name
            find_upd_name.save()
            print(f'Name changed to {find_upd_name.name}')
            res = input('Would you like to restart y/n: ')
            if res == 'y':
                contact_list()
            else:
                return
        elif upd == 2:
            upd_num = input('Enter the name of the person you would like to update: ')
            new_num = int(input('Enter the new number of the contact: '))
            find_upd_num = Contact.get(Contact.name == upd_num)
            find_upd_num.number = new_num
            find_upd_num.save()
            print(f'{find_upd_num.name} number changed to {find_upd_num.number}')
            res = input('Would you like to restart y/n: ')
            if res == 'y':
                contact_list()
            else:
                return
        elif upd == 3:
            upd_email = input('Enter the name of the person you would like to update: ')
            new_email = input('Enter the new email of the contact: ')
            find_upd_email = Contact.get(Contact.name == upd_email)
            find_upd_email.email = new_email
            find_upd_email.save()
            print(f'{find_upd_email.name} email changed to {find_upd_email.email}')
            res = input('Would you like to restart y/n: ')
            if res == 'y':
                contact_list()
            else:
                return
        else:
            print('You did not enter 1, 2, or 3')
            return
    # Delete
    elif i==4:
        print('You selected to delete a contact.')
        del_name = input('Enter the name of the contact you would like to delete: ')
        del_cnt = Contact.get(Contact.name == del_name)
        del_cnt.delete_instance()
        print('Contact has been deleted.')
        res = input('Would you like to restart y/n: ')
        if res == 'y':
            contact_list()
        else:
            return
    else:
        print('You did not enter 1, 2, 3, or 4')
        contact_list()

# Call the function
contact_list()

# def all_contact():
#     contact = Contact.select()
#     for contact in contact:
#         print(contact.first_name)


