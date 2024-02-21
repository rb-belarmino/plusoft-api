from plusoft_api.helpers.api_endpoint import ApiEndpoint
from decouple import config
from typing import Literal


class Consult(ApiEndpoint):

    def __init__(
            self,
            username: str = config("PLUSOFT_USERNAME"),
            password: str = config("PLUSOFT_PASSWORD")
        ) -> None:
        super().__init__(username, password, "/import/consult")
    
    def consult_status(self, consult_code: int) -> dict:
        params = {
            "code": consult_code
        }

        return self.base_requests.post(path=self.endpoint_path, parameters=params)


class RequisitionStatus:

    def __init__(self, status: Literal["P", "R", "S"], message: str) -> None:
        self.status = status,
        self.message = message
    
    @property
    def to_dict(self) -> dict:
        return {
            "status": self.status,
            "message": self.message
        }

class FutureProcessing:

    def __init__(
            self,
            message: str,
            consult_code: int,
            username: str = config("PLUSOFT_USERNAME"),
            password: str = config("PLUSOFT_PASSWORD"),
        ) -> None:
        self.message: str = message
        self.consult_code: int = consult_code
        self.consult_client: Consult = Consult(username=username, password=password)

    @property
    def requisition_status(self) -> RequisitionStatus:
        return RequisitionStatus(**self.consult_client.consult_status(self.consult_code))

