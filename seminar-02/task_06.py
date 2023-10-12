"""
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""

balance = 0
tax = 0


class ATM:
    __TAX_LIMIT_MULTIPLICITY = 50
    __START_TAX_RATE = 0.015
    __CAP = 3
    __TAX_RATE_AFTER_CAP_OPERATIONS = 0.03
    __WEALTH_CAP = 5_000_000
    __TAX_RATE_AFTER_WEALTH_CAP = 0.1

    def __init__(self):
        self.__tax = self.__START_TAX_RATE
        self.__balance = 0
        self.__operations = 0
        self.__wealth_tax = False

    def __print_balance(self):
        print(f"Сумма денег на счёте: {self.__balance}")

    def __check_tax(self):
        if self.__operations >= self.__CAP:
            self.__operations = 0
            self.__tax += self.__TAX_RATE_AFTER_CAP_OPERATIONS

        if self.__balance > self.__WEALTH_CAP:
            self.__wealth_tax = True
        else:
            self.__wealth_tax = False
        return self.__tax

    def __check_amount(self, amount):
        try:
            int(amount)
        except ValueError:
            raise ValueError("Сумма должна быть целым числом")
        amount = int(amount)
        if amount % self.__TAX_LIMIT_MULTIPLICITY != 0:
            raise ValueError(f"Введена неверная сумма, сумма должна быть кратна {self.__TAX_LIMIT_MULTIPLICITY}")
        return amount

    def __deposit(self, amount):
        self.__balance += amount
        self.__operations += 1
        return amount

    def calculate_tax(self, amount):
        tax_amount = amount * self.__tax
        if tax_amount <= 30:
            return 30
        if tax_amount > 600:
            return 600
        return tax_amount

    def __withdraw(self, amount):
        tax_amount = self.calculate_tax(amount)
        amount += tax_amount
        if self.__balance < amount:
            raise ValueError(f"Нельзя снять данную сумму, должно быть денег на балансе для снятия: {amount}")
        self.__balance -= amount
        self.__operations += 1
        return amount

    def __get_tax(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            return amount
        return 0

    def start(self):
        action = "0"
        while action not in ("1", "2"):
            self.__print_balance()
            action = input("Введите цифру с действием, которое хотите совершить? 1 - пополнить, 2 - снять, 3 - выход\n")
            if action not in ("1", "2", "3"):
                print("Введена неверная цифра")
                continue
            if action == "3":
                break
            else:
                try:
                    amount = input("Введите сумму: ")
                    if self.__wealth_tax:
                        print(f"Изъят налог на богатство, "
                              f"{self.__get_tax(self.__balance * self.__TAX_RATE_AFTER_WEALTH_CAP)}")
                    amount = self.__check_amount(amount)
                    if action == "1":
                        print(f"Счёт пополнен на {self.__deposit(amount)}")
                    else:
                        self.__withdraw(amount)
                except ValueError as ve:
                    print(ve)
                self.__check_tax()
                print(f"Текущая процентная ставка: {self.__tax * 100}%")
                if self.__wealth_tax:
                    print("Перед началом следующей операции будет изъят налог на богатство "
                          "- 10 процентов от суммы на балансе")
                action = "0"

        self.__print_balance()


if __name__ == '__main__':
    atm_1 = ATM()
    atm_1.start()
