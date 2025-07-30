from datetime import datetime, timedelta
from typing import Optional

class Mouse:
    DEFAULT_WEANING_DAYS = 21
    
    def __init__(
        self,
        mouse_id: str,
        sex: str,
        dob: str,
        genotype: Optional[str] = None,
        generation: Optional[str] = None,
        coat_color: Optional[str] = None,
        notes: Optional[str] = "",
        wean_date: Optional[str] = None,
        alive: bool = True,
        death_date: Optional[str] = None
    ):
        self.mouse_id: str = mouse_id
        self.sex: str = sex
        self.dob: str = dob
        self.genotype: Optional[str] = genotype
        self.notes: str = notes
        self.alive: bool = alive
        self.death_date: Optional[str] = death_date