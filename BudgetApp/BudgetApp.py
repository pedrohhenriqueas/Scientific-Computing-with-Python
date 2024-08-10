class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:7.2f}\n"
            total += item["amount"]
        output = title + items + "Total: " + str(total)
        return output


def create_spend_chart(categories):
    spendings = []
    category_names = []
    for category in categories:
        withdrawals = sum(item['amount'] for item in category.ledger if item['amount'] < 0)
        spendings.append(withdrawals)
        category_names.append(category.name)

    total_spent = sum(spendings)
    percentages = [int(spent / total_spent * 100) for spent in spendings]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:3d}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    ------------\n     "
    longest_name_length = max(len(name) for name in category_names)
    for i in range(longest_name_length):
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < longest_name_length - 1:
            chart += "\n     "

    return chart


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)

entertainment = Category("Entertainment")
entertainment.deposit(500, "initial deposit")
entertainment.withdraw(150, "concert tickets")
entertainment.withdraw(50, "movie")

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(300, "car repairs")

# Adicione estas novas categorias ao gráfico
print(create_spend_chart([food, clothing, entertainment, auto]))
