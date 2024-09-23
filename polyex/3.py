class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            return "please use int for amount"
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    def __reversed__(self):
        return self._transactions[::-1]

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __add__(self, other):
        new_owner = f'{self.owner}&{other.owner}'
        new_starting_amount = self.amount + other.amount
        new_acc = Account(new_owner, new_starting_amount)
        new_acc._transactions = self._transactions + other._transactions
        return new_acc

acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))

acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))

for transaction in acc:
    print(transaction)

print(acc[1])
print(list(reversed(acc)))
print(acc + acc2)