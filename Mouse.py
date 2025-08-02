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
        self.wean_date: Optional[str] = wean_date
        self.alive: bool = alive
        self.death_date: Optional[str] = death_date
        
        # Injection history (list of Injection objects)
        self.injections: List[Injection] = []
    
    # ---------------------------
    # Utility Methods
    #----------------------------
    def calculate_age_days(self) -> int:
        dob_date = datetime.strptime(self.dob, "%Y-%m-%d")
        return (datetime.now() - dob_date).days

    def format_age(self, mode: str = "days"):
        total_days = self.calculate_age_days()
        parts = []
        
        if mode == "days":
            parts.append(f"{total_days} day{'s' if total_days != 1 else ''}")
        elif mode == "weeks":
            weeks, days = divmod(total_days, 7)
            parts.append(f"{weeks} week{'s' if weeks != 1 else ''}")
            parts.append(f"{days} day{'s' if days != 1 else ''}")
        elif mode == "months":
            months, remainder = divmod(total_days, 30)
            weeks, days = divmod(remainder, 7)
            parts.append(f"{months} month{'s' if months != 1 else ''}")
            parts.append(f"{weeks} week{'s' if weeks != 1 else ''}")
            parts.append(f"{days} day{'s' if days != 1 else ''}")
        elif mode == "years":
            years, remainder = divmod(total_days, 365)
            months, remainder = divmod(remainder, 30)
            weeks, days = divmod(remainder, 7)
            parts.append(f"{years} year{'s' if years != 1 else ''}")
            parts.append(f"{months} month{'s' if months != 1 else ''}")
            parts.append(f"{weeks} week{'s' if weeks != 1 else ''}")
            parts.append(f"{days} day{'s' if days != 1 else ''}")
        return " ".join(parts)
            
    # ---------------------------
    # Injection Methods
    # ---------------------------
    def add_injection(self, injection: Injection):
        self.injections.append(injection) # Add an Injection object to the mouse's injection history
        
    def get_injection_history(self) -> list:
        return [inj.to_dict() for inj in self.injections]