from subprocess import call
from behave import *
from lib.guestbook import GuestBook

@given('there is a guestbook with signatures')
def step_there_is_guestbook(context):
    context.guestbook = GuestBook()
    for person in context.table:
        context.guestbook.add(person['name'])

@then('a user will find "{name}" there')
def step_list_of_guests(context, name):
    names = []
    guest_list = context.guestbook.list()
    for person in guest_list:
        names.append(person[0])

    msg = "{} not found in {}".format(name, names)
    assert name in names, msg
