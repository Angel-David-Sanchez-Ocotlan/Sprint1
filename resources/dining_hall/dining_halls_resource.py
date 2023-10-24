from resources.abstract_base_resource import BaseResource
from resources.students.student_models import DiningHallRspModel, DiningHallModel
from resources.rest_models import Link
from typing import List


class DiningHallsResource(BaseResource):
    #
    # This code is just to get us started.
    # It is also pretty sloppy code.
    #

    def __init__(self, config):
        super().__init__()

        self.data_service = config["data_service"]


    def get_dining_halls(self) -> List[DiningHallRspModel]:

        result = self.data_service.get_diningHalls()
        final_result = []

        for s in result:
            final_result.append(s)

        return final_result

