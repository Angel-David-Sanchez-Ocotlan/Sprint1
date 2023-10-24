from resources.abstract_base_data_service import BaseDataService
import json


class DiningHallsDataService(BaseDataService):

    def __init__(self, config: dict):
        """

        :param config: A dictionary of configuration parameters.
        """
        super().__init__()

        self.data_dir = config['data_directory']
        self.data_file = config["data_file"]
        self.diningHalls = []

        self._load()

    def _get_data_file_name(self):
        # DFF TODO Using os.path is better than string concat
        result = self.data_dir + "/" + self.data_file
        return result

    def _load(self):

        fn = self._get_data_file_name()
        with open(fn, "r") as in_file:
            self.diningHalls = json.load(in_file)

    def _save(self):
        fn = self._get_data_file_name()
        with open(fn, "w") as out_file:
            json.dump(self.diningHalls, out_file)

    def get_diningHalls(self) -> list:
        result = []

        for d in self.diningHalls:
                result.append(d)
        return result

