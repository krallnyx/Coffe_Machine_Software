from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


class CoffeeMachine:
    def __init__(self):
        self.money_machine = MoneyMachine()
        self.coffee_maker = CoffeeMaker()
        self.menu = Menu()

    def run(self):
        is_on = True

        while is_on:
            options = self.menu.get_items()
            choice = input(f"What would you like? ({options}): ").lower()
            if choice == "off":
                is_on = False
            elif choice == "report":
                self.coffee_maker.report()
                self.money_machine.report()
            else:
                drink = self.menu.find_drink(choice)
                if drink != "None":
                    is_enough_ingredients = self.coffee_maker.is_resource_sufficient(drink)
                    is_payment_successful = False
                    if is_enough_ingredients:
                        is_payment_successful = self.money_machine.make_payment(drink.cost)
                    if is_payment_successful:
                        self.coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    coffee_machine.run()