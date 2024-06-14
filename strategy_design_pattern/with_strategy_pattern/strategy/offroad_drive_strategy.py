from strategy_design_pattern.with_strategy_pattern.strategy.drive_strategy import DriveStrategy


class OffroadDriveStrategy(DriveStrategy):

    def drive(self):
        """
        custom drive mode for sports vehicle
        """
        print("Strategy: Offroad driving mode.")