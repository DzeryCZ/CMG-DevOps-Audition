from src.detectors.Detector import Detector


class ThermometerDetector(Detector):
    NAME: str = 'thermometer'

    def get_product_class(self) -> str:

        if self._mean_of_logs() <= 0.5 and self._stdev_of_logs() <= 3:
            return 'ultra precise'
        elif self._mean_of_logs() <= 0.5 and self._stdev_of_logs() <= 5:
            return 'very precise'

        return 'precise'
