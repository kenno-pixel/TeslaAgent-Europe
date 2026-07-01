from dataclasses import dataclass


@dataclass
class SearchConfig:
    model: str = "Tesla Model Y"
    battery: str = "Long Range"
    drivetrain: str = "AWD"

    max_price: int = 35000
    max_mileage: int = 50000

    require_heat_pump: bool = True
    require_warranty: bool = True

    countries = [
        "EE",
        "FI",
        "SE",
        "NO",
        "DK",
        "DE",
        "NL",
        "BE",
        "PL",
        "LV",
        "LT",
    ]