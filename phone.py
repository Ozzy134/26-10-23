class Phone:

    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight
        print(self.number, self.model, self.weight)

    def receiveCall(self, name):
        self.name = name
        print('Звонит:', self.name)