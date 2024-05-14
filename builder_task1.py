from abc import ABC, abstractmethod


class Product: #step 1 Define the Product Class
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def show_parts(self):
        return ', '.join(self.parts)


class Builder(ABC): #step2 Define the Builder Interface
    @abstractmethod
    def build_part_a(self):
        pass

    @abstractmethod
    def build_part_b(self):
        pass

    @abstractmethod
    def build_part_c(self):
        pass

    @abstractmethod
    def build_part_d(self):
        pass

    @abstractmethod
    def get_result(self):
        print("The product has 4 parts")




class ConcreteBuilder(Builder): #step3  Implement the ConcreteBuilder Class
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add_part("PartA")

    def build_part_b(self):
        self.product.add_part("PartB")

    def build_part_c(self):
        self.product.add_part("PartC")

    def build_part_d(self):
        self.product.add_part("PartD")

    def get_result(self):
        return self.product
class Director: #step4 Define the Director Class
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()
        self.builder.build_part_d()


def main(): #step5 Test the Implementation
    # Create a ConcreteBuilder instance
    builder = ConcreteBuilder()

    # Create a Director instance and pass the builder to it
    director = Director(builder)

    # Construct the product using the director
    director.construct()

    # Get the constructed product
    product = builder.get_result()

    # Show the parts of the product
    print(f"Product parts: {product.show_parts()}")


if __name__ == "__main__":
    main()
