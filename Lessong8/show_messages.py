"""
Создайте список с серией коротких сообщений. Передацте список функции show_messages(),
которая выводит текст каждого сообщения в списке.

"""

def show_messages(messages):
  for message in messages:
    print(message)


def send_message(messages):
  for message in messages:
    print(message)

messages = ["Hello world!", "Hello Python world!", "Hello C++ world!"]

show_messages(messages)
