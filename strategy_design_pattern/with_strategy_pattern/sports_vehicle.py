from strategy_design_pattern.with_strategy_pattern.strategy.sports_drive_strategy import SportsDriveStrategy
from strategy_design_pattern.with_strategy_pattern.vehicle import Vehicle


class SportsVehicle(Vehicle):

    def __init__(self) -> None:
        driving_strategy_instance = SportsDriveStrategy()
        super().__init__(driving_strategy_instance)


