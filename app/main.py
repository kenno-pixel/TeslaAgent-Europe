"""
TeslaAgent Europe
Created by Kenno Nilisk
AI-assisted development
"""

from dataclasses import dataclass


@dataclass
class SearchConfig:
    model: str = "Tesla Model Y"
    battery: str = "Long Range"
    drivetrain: str = "AWD"
    max_mileage: int = 50000
    max_price: int = 35000
    require_heat_pump: bool = True
    require_warranty: bool = True


def main():
    config = SearchConfig()

    print("=" * 45)
    print("🚗 TeslaAgent Europe v0.1")
    print("=" * 45)
    print(f"Model: {config.model}")
    print(f"Battery: {config.battery}")
    print(f"Drive: {config.drivetrain}")
    print(f"Max mileage: {config.max_mileage:,} km")
    print(f"Max price: €{config.max_price:,}")
    print(f"Heat pump required: {config.require_heat_pump}")
    print(f"Warranty required: {config.require_warranty}")
    print("=" * 45)
    print("System ready.")


if __name__ == "__main__":
    main()