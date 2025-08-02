from datetime import datetime
from typing import Optional

class Injection:
    def __init__(
        self,
        date: str,
        substance: str,
        dose: Optional[str] = None,
        notes: Optional[str] = ""
    ):
        self.date: str = date #format YYYY-MM-DD
        self.substance: str = substance
        self.dose: Optional[str] = dose
        self.notes: str = notes
    
    def to_dict(self) -> dict:
        return {
            "date" : self.date,
            "substance" : self.substance,
            "dose" : self.dose,
            "notes" : self.notes
        }
        
    @classmethod
    def from_dict(cls, data: dict):
        return cls (
            date = data["date"],
            substance = data["substance"],
            dose = data["dose"],
            notes = data.get["notes", ""]
        )