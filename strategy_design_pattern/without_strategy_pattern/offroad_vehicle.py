from strategy_design_pattern.without_strategy_pattern.vehicle import Vehicle

class OffroadVehicle(Vehicle):

    def drive(self):
        """
        custom drive mode for offroad vehicle
        """
        print("Offroad driving mode.")