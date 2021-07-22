from coins import Dime, Nickel, Penny, Quarter
from customer import Customer
from soda_machine import SodaMachine
import user_interface

class Simulation:


    def __init__(self):
        pass
    

    def run_simulation(self):
        """The central method called in main.py."""
        customer = Customer()
        customer.wallet.fill_wallet()
        soda_machine = SodaMachine()
        soda_machine.fill_inventory()
        soda_machine.fill_register()
        will_proceed = False
        while will_proceed == False:
            user_option = user_interface.simulation_main_menu()
            if user_option[0] == 1:
                soda_machine.begin_transaction(customer)
            elif user_option[0] == 2:
                customer.check_coins_in_wallet()
            elif user_option[0] == 3:
                customer.check_backpack()
            else:
                will_proceed = True
