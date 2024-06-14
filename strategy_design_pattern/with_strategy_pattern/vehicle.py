class Vehicle():

    def __init__(self, driving_strategy) -> None:
        self.driving_strategy = driving_strategy

    def drive(self):
        self.driving_strategy.drive()