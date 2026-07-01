from dataclasses import dataclass
from typing import Optional


@dataclass
class Car:
    source: str
    listing_id: str
    url: str

    model: str
    version: str

    price: int
    mileage: int
    registration: str

    battery: str
    drivetrain: str

    country: str

    color: Optional[str] = None
    interior: Optional[str] = None

    vin: Optional[str] = None

    heat_pump: bool = False
    tow_hitch: bool = False

    fsd: bool = False
    eap: bool = False

    factory: Optional[str] = None
    cpu: Optional[str] = None

    warranty_until: Optional[str] = None

    score: int = 0