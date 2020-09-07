import re
from typing import List, Dict
from src.detectors.ThermometerDetector import ThermometerDetector
from src.detectors.HumidityDetector import HumidityDetector
from src.detectors.MonoxideDetector import MonoxideDetector
from src.detectors.Detector import Detector


class ProcessLogs:
    REFERENCE_REGEX = r'^reference (?P<thermometer>[0-9.]+?) (?P<humidity>[0-9.]+?) (?P<monoxide>[0-9.]+?)$'
    START_OF_LOGFILE_REGEX = r'^(?P<type>[a-z]+) (?P<model>.*)$'
    PARSE_LOG_REGEX = r'^(?P<time>[0-9T\-:]+) (?P<value>[0-9.]+)$'
    LIST_OF_DETECTORS = {
        ThermometerDetector.NAME: ThermometerDetector,
        HumidityDetector.NAME: HumidityDetector,
        MonoxideDetector.NAME: MonoxideDetector,
    }

    __detectors: List[Detector] = []

    def __init__(self, logs: List[str]):
        reference: List = self.__parse_reference(logs[0])
        self.__process_logs(logs[1:], reference)

    def get_product_classes(self) -> Dict:
        products = {}
        for detector in self.__detectors:
            product_class = detector.get_product_class()
            product_model = detector.get_product_model()
            products[product_model] = product_class

        return products

    def __process_logs(self, logs: List[str], reference: List[str]):
        parsed_log_file = []
        log_file_header = []
        for index, line in enumerate(logs):
            head_of_log = self.__get_head_of_logfile(line)
            if head_of_log is None:
                parsed_log = self.__get_logged_value(line)
                parsed_log_file.append(parsed_log)
                continue

            if len(log_file_header) > 0:
                self.__add_detector(
                                    log_file_header,
                                    parsed_log_file,
                                    float(reference[log_file_header['type']])
                                )

            log_file_header = head_of_log
            parsed_log_file = []

        self.__add_detector(
            log_file_header,
            parsed_log_file,
            float(reference[log_file_header['type']])
        )

    def __add_detector(self, head_of_log: Dict, parsed_log_file: List[float], reference: float):
        model = head_of_log['model']
        detector_type = head_of_log['type']

        if detector_type not in self.LIST_OF_DETECTORS:
            return None

        detector_class = self.LIST_OF_DETECTORS[detector_type]
        detector = detector_class(model, reference, parsed_log_file)
        self.__detectors.append(detector)

    def __parse_reference(self, reference_definition: str) -> Dict:
        reference = re.match(self.REFERENCE_REGEX, reference_definition)
        return reference.groupdict()

    def __get_head_of_logfile(self, log_line: str) -> List[str]:
        start_of_log = re.match(self.START_OF_LOGFILE_REGEX, log_line)

        if start_of_log is None:
            return None

        return start_of_log.groupdict()

    def __get_logged_value(self, log_line: str) -> float:
        logged_value = re.match(self.PARSE_LOG_REGEX, log_line)

        return float(logged_value.group('value'))
