# complex parts
# subsystem ClassA
# subsystem ClassB
# subsystem ClassC


class CarModel():
    def SetModel(self):
        print(" CarModel - SetModel")


class CarEngine():
    def SetEngine(self):
        print(" CarModel - SetEngine")


class CarBody():
    def SetBody(self):
        print(" CarModel - SetBody")


# facade
class CarFacade():
    def __init__(self):
        self.carModel = CarModel()
        self.carEngine = CarEngine()
        self.carBody = CarBody()

    def CreateCompleteCar(self):
        self.carModel.SetModel()
        self.carEngine.SetEngine()
        self.carBody.SetBody()


# client
CARFACADE = CarFacade()
CARFACADE.CreateCompleteCar()
