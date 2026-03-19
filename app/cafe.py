import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        vaccine_day = visitor["vaccine"]["expiration_date"]
        if vaccine_day < datetime.date.today():
            raise OutdatedVaccineError("Visitor is not vaccinated")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor should wear a mask")
        return f"Welcome to {self.name}"
