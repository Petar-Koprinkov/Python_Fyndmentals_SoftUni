class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent:{self.is_send}"


emails = []
data = input()

while data != "Stop":
    sender, receiver, content = data.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    data = input()

indexes = [int(el) for el in input().split(", ")]

for index, email in enumerate(emails):
    if index in indexes:
        email.send()
    print(f"{email.sender} says to {email.receiver}: {email.content}. Sent: {email.is_send}")





