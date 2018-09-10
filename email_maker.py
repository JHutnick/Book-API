from string import Template
import os


from flask import jsonify


def read_template(file_name):
    with open(file_name, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def write_to_file(user_name,message):
    save_path = "/Emails"
    file_name = user_name + "_reminder.txt"
    full_path = os.path.join(save_path, file_name)
    file = open(file_name,"w")
    file.write(message)
    file.close()


def create_email(email, user_name, book_name, due_date):
    message_template = read_template('email_message.txt')
    message = message_template.substitute(USER_NAME=user_name,BOOK_TITLE=book_name,DUE_DATE=due_date)
    print(message)
    write_to_file(user_name, message)
#   return jsonify(message)
