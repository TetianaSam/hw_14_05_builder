class Spaghetti(Pasta):
    def __init__(self):
        self.type = "Spaghetti"
        self.sauce = None
        self.topping = None
        self.dressing = None

    def set_sauce(self, sauce):
        self.sauce = sauce

    def set_topping(self, topping):
        self.topping = topping

    def set_dressing(self, dressing):
        self.dressing = dressing

    def get_details(self):
        return f"Pasta Type: {self.type}, Sauce: {self.sauce}, Topping: {self.topping}, Dressing: {self.dressing}"

class Penne(Pasta):
    def __init__(self):
        self.type = "Penne"
        self.sauce = None
        self.topping = None
        self.dressing = None

    def set_sauce(self, sauce):
        self.sauce = sauce

    def set_topping(self, topping):
        self.topping = topping

    def set_dressing(self, dressing):
        self.dressing = dressing

    def get_details(self):
        return f"Pasta Type: {self.type}, Sauce: {self.sauce}, Topping: {self.topping}, Dressing: {self.dressing}"

class Fettuccine(Pasta):
    def __init__(self):
        self.type = "Fettuccine"
        self.sauce = None
        self.topping = None
        self.dressing = None

    def set_sauce(self, sauce):
        self.sauce = sauce

    def set_topping(self, topping):
        self.topping = topping

    def set_dressing(self, dressing):
        self.dressing = dressing

    def get_details(self):
        return f"Pasta Type: {self.type}, Sauce: {self.sauce}, Topping: {self.topping}, Dressing: {self.dressing}"
