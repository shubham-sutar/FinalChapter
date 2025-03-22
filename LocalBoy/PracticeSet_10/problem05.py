# problem 05
# 5. Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of
# train running under indian railways.

from random import randint


class Train:

    def __init__(self, train_no):
        self.train_no = train_no

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
