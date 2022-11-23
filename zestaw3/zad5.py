class Bug:
    ilosc = 0

    '''hey I'm a Bug'''

    def __init__(self) -> None:
        Bug.ilosc += 1
        self.id = Bug.ilosc

    def __str__(self) -> str:
        return "Ilosc: " + str(Bug.ilosc) + " Id: " + str(self.id)

    def __del__(self) -> None:
        print("Życie kończy robak o numerze " + str(self.id) + ". Ilosc jeszcze żyjących: " + str(Bug.ilosc))
        Bug.ilosc -= 1
        del self

bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])