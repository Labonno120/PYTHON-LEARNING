def main():
    plotter = Vault(10,20)
    weasly = Vault(30,40)
    total = plotter + weasly
    print(total)
class Vault:
    def __init__(self, galleons=0, knuts=0):
        self.galleons = galleons
        self.knuts = knuts
    def __str__(self):
        return f"{self.galleons} Galleons, {self.knuts} Knuts"
    def __add__(self,other):
        n1 = self.galleons + other.galleons
        n2 = self.knuts + other.knuts
        return Vault(n1,n2)
main()