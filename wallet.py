from coins import Quarter
from coins import Dime
from coins import Nickel
from coins import Penny

class Wallet:
    def __init__(self):
        self.money = []
        self.fill_wallet = []


def fill_wallet(self):
    """Method will fill wallet's money list with certain amount of each type of coin when called."""
    for index in range(8):
        self.money.append(Quarter())
    for index in range(10):
        self.money.append(Dime())
    for index in range(20):
        self.money.append(Nickel())
    for index in range(50):
        self.money.append(Penny())
