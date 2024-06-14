from strategy_design_pattern.with_strategy_pattern.strategy.offroad_drive_strategy import OffroadDriveStrategy
from strategy_design_pattern.with_strategy_pattern.vehicle import Vehicle

class OffroadVehicle(Vehicle):

    def __init__(self) -> None:
        driving_strategy_instance = OffroadDriveStrategy()
        super().__init__(driving_strategy_instance)