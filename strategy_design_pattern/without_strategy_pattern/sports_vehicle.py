from strategy_design_pattern.without_strategy_pattern.vehicle import Vehicle


class SportsVehicle(Vehicle):

    def drive(self):
        """
        custom drive mode for sports vehicle
        """
        print("Sports driving mode.")

