class SpaghettiFactory(PastaFactory):
    def create_pasta(self):
        return Spaghetti()

class PenneFactory(PastaFactory):
    def create_pasta(self):
        return Penne()

class FettuccineFactory(PastaFactory):
    def create_pasta(self):
        return Fettuccine()
