from src.detectors.Detector import Detector


class HumidityDetector(Detector):
    NAME: str = 'humidity'

    def get_product_class(self) -> str:

        if self._max_of_logs() <= 0.5 and self._min_of_logs() >= -0.5:
            return 'keep'

        return 'discard'
