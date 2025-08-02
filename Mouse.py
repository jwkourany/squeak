from datetime import datetime, timedelta
from typing import Optional, List
from Injection import Injection

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
        self.wean_date: Optional[str] = wean_date or self.calculate_default_wean_date()
        self.alive: bool = alive
        self.death_date: Optional[str] = death_date
        
        # Injection history (list of Injection objects)
        self.injections: List[Injection] = []
    
    # ---------------------------
    # Utility Methods
    #----------------------------
    def calculate_age(self) -> int:
        dob_date = datetime.strptime(self.dob, "%Y-%m-%d")
        return (datetime.now() - dob_date).days
    
    # ---------------------------
    # Injection Methods
    # ---------------------------
    def add_injection(self, injection: Injection):
        self.injections.append(injection) # Add an Injection object to the mouse's injection history
        
    def get_injection_history(self) -> list:
        return [inj.to_dict() for inj in self.injections]