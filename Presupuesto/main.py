class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': -amount, 'description': description})
        return True

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, '*')
        lines = [title]
        for item in self.ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:.2f}"[:7]
            lines.append(f"{description:<23}{amount:>7}")
        lines.append(f"Total: {self.get_balance()}")
        return '\n'.join(lines)


def create_spend_chart(categories):
    # Gasto total por categoría (solo retiros)
    spent = []
    for category in categories:
        total = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        spent.append(total)

    total_spent = sum(spent)

    # Porcentaje redondeado hacia abajo a la decena más cercana
    percentages = [int(s / total_spent * 100) // 10 * 10 for s in spent]

    chart = 'Percentage spent by category\n'

    # Eje Y y barras
    for level in range(100, -1, -10):
        chart += f'{level:>3}|'
        for p in percentages:
            chart += ' o ' if p >= level else '   '
        chart += ' \n'

    # Línea horizontal
    chart += '    ' + '-' * (3 * len(categories) + 1) + '\n'

    # Nombres verticales
    names = [category.name for category in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        chart += '    '
        for name in names:
            chart += f' {name[i]} ' if i < len(name) else '   '
        chart += ' '
        if i < max_len - 1:
            chart += '\n'

    return chart
