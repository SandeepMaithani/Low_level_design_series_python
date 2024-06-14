from strategy_design_pattern.with_strategy_pattern.strategy.normal_drive_strategy import NormalDriveStrategy
from strategy_design_pattern.with_strategy_pattern.vehicle import Vehicle


class GoodsVehicle(Vehicle):
    def __init__(self) -> None:
        driving_strategy_instance =  NormalDriveStrategy()
        super().__init__(driving_strategy_instance)