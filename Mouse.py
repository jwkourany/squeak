from datetime import datetime, timedelta
from typing import Optional

class Mouse:    
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
        
        # Core info
        self.mouse_id: str = mouse_id
        self.sex: str = sex
        self.dob: str = dob #format YYYY-MM-DD
        
        # Genetics/appearance
        self.genotype: Optional[str] = genotype
        self.generation: Optional[str] = generation
        self.coat_color: Optional[str] = coat_color
        
        # Notes & status
        self.notes: str = notes
        self.wean_date: Optional[str] = wean_date
        self.alive: bool = alive
        self.death_date: Optional[str] = death_date