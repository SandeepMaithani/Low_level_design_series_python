from strategy_design_pattern.with_strategy_pattern.strategy.drive_strategy import DriveStrategy


class NormalDriveStrategy(DriveStrategy):
    
    def drive(self):
        """
        Generic drive mode for all vehicle
        """
        print("Strategy: Generic/Common driving mode.")