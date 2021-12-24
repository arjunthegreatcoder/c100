class Car(object):
    def __init__(self,model,color,company,power):
        self.model = model
        self.color = color
        self.company = company
        self.power = power
    def start(self):
        print("CarStarted") 
    def stop(self):
        print("CarStopped")
    def acc(self):
        print("CarAcc")
    
lambo = Car("SV","jetBlack","Lamborgini",300)
print(lambo.stop())
    







