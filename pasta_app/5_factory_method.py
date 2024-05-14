
from pasta_factory_interface import PastaFactory
from pasta_interface import Pasta
from pasta_classes import

class PastaCookingApp:
    def __init__(self, factory: PastaFactory):
        self.factory = factory

    def prepare_pasta(self, sauce, topping, dressing):
        pasta = self.factory.create_pasta()
        pasta.set_sauce(sauce)
        pasta.set_topping(topping)
        pasta.set_dressing(dressing)
        return pasta.get_details()

def main():
    spaghetti_factory = SpaghettiFactory()
    penne_factory = PenneFactory()
    fettuccine_factory = FettuccineFactory()

    app = PastaCookingApp(spaghetti_factory)
    print(app.prepare_pasta("Tomato", "Meatballs", "Parmesan"))

    app = PastaCookingApp(penne_factory)
    print(app.prepare_pasta("Alfredo", "Chicken", "Parsley"))

    app = PastaCookingApp(fettuccine_factory)
    print(app.prepare_pasta("Pesto", "Shrimp", "Basil"))

if __name__ == "__main__":
    main()
