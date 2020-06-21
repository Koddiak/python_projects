from abc import ABC, abstractmethod

class Label(ABC):
    company = 'American Technologies'
    address = '100 Midway Lane'
    city = 'Generic'
    state = 'CA'
    postalCode = '11111'
    
    def frm(self):
        print("\nFrom:\n{}\n{}\n{}, {} {}".format(self.company, self.address, self.city, self.state, self.postalCode))

    @abstractmethod
    def to(self, name, address, city, state, postalCode):
        pass

class PriorityMail(Label):
    description = 'Shipping in 1-3 Business Days'

    def getDesc(self, desc):
        print(description)
    
    def to(self, name, address, city, state, postalCode):
        print("\nTo:\n{}\n{}\n{}, {} {}".format(name, address, city, state, postalCode))

if __name__ == "__main__":
    obj = PriorityMail()
    obj.frm()
    obj.to('Bob Smith', '111 Fake St', 'City', 'CA', '22222')
