from strategy_design_pattern.with_strategy_pattern.strategy.drive_strategy import DriveStrategy


class SportsDriveStrategy(DriveStrategy):

    def drive(self):
        """
        custom drive mode for sports vehicle
        """
        print("Strategy: Sports driving mode.")