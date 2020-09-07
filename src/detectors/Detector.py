import statistics
from abc import abstractmethod
from typing import List


class Detector:
    _reference: float
    _model: str
    _logs: List[float]

    def __init__(self, model: str, reference: float, logs: List[str]):
        self._model = model
        self._reference = reference
        self._logs = logs

    @abstractmethod
    def get_product_class(self) -> str:
        """Product Class should be defined in Child classes"""

    def get_product_model(self) -> str:
        return self._model

    def _mean_of_logs(self) -> float:
        return abs(statistics.mean(self._logs) - self._reference)

    def _stdev_of_logs(self) -> float:
        return statistics.stdev(self._logs)

    def _max_of_logs(self):
        return max(self._logs) - self._reference

    def _min_of_logs(self):
        return min(self._logs) - self._reference
