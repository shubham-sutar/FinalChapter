# problem 06
# 6. Can You changed the self-parameter inside a class to something else(say "harry"). Try to self to "slf" or
# "harry" amd see the effects.

from random import randint


class Train:

    def __init__(slf, train_no):
        slf.train_no = train_no

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.train_no}\n from {fro} to {to}.")

    def get_status(self):
        print(f"Train no: {self.train_no} is running on time")

    def get_fair_info(self, fro, to):
        print(f"Ticket is booked in train no: {self.train_no}\n from {fro} to {to} is {randint(222, 5555)}.")


obj = Train(1250)
obj.book("kolhapur", "sangli")
obj.get_status()
obj.get_fair_info("kolhapur", "sangli")
