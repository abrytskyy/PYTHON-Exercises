class Message:
    def __init__(self, text, fl_like= False):
        self.text = text
        self.fl_like = fl_like

    def __str__(self):
        return f"Text: {self.text} Like: {self.fl_like}"

class Viber:
    messages = []

    @classmethod
    def add_message(cls, message):
        cls.messages.append(message)

    @classmethod
    def remove_message(cls, message):
        cls.messages.remove(message)

    @staticmethod
    def set_like(message):
        message.fl_like = False if message.fl_like else True

    @classmethod
    def show_last_message(cls, quantity):
        print(*(message for message in cls.messages[:]), sep="\n")

    @classmethod
    def total_messages(cls):
        return len(cls.messages)

msg = Message("Hello world")
Viber.add_message(Message("It is Python course"))
Viber.add_message(msg)
Viber.add_message(Message("What do yuo think about it?"))
Viber.show_last_message(4)
print()

Viber.set_like(msg)
Viber.show_last_message(4)
print()

Viber.remove_message(msg)
Viber.show_last_message(4)
print()






