from customer import Customer
from soda_machine import SodaMachine
import user_interface

class Simulation:


    def __init__(self):
        pass
    

    def run_simulation(self):
        """The central method called in main.py."""
        customer = Customer()
        soda_machine = SodaMachine()
        will_proceed = False
        while will_proceed == False:
            user_option = user_interface.simulation_main_menu()
            print(user_option)
            if user_option[0] == 1:
                soda_machine.begin_transaction(Customer)
            elif user_option[0] == 2:
                customer.check_coins_in_wallet()
            elif user_option[0] == 3:
                customer.check_backpack()
            else:
                will_proceed = False
