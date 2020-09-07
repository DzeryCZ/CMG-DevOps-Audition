from src.detectors.Detector import Detector


class MonoxideDetector(Detector):
    NAME: str = 'monoxide'

    def get_product_class(self) -> str:

        if self._max_of_logs() <= 3 and self._min_of_logs() >= -3:
            return 'keep'

        return 'discard'
