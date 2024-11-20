class Expense:
    def __init__(self, name, category, amount) -> None:
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self):  #default classes comes with all classes that tells how to represent an string when u try to print it out with print(expense) 
        return f"<Expense : {self.name}, {self.category}, ${self.amount:.2f} >"