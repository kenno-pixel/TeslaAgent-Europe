from config import SearchConfig
from models.car import Car
from scoring.deal_score import DealScore


def main():

    config = SearchConfig()

    car = Car(
        source="TEST",
        listing_id="1",
        url="https://example.com",
        model="Tesla Model Y",
        version="Long Range",
        price=34900,
        mileage=28000,
        registration="2023-05",
        battery="Long Range",
        drivetrain="AWD",
        country="DE",
        heat_pump=True,
        tow_hitch=True,
        fsd=False,
        eap=True,
    )

    score = DealScore.calculate(car)

    print("=" * 50)
    print("TeslaAgent Europe")
    print("=" * 50)
    print()

    print(car.model)
    print(car.version)
    print()

    print(f"Price     : €{car.price}")
    print(f"Mileage   : {car.mileage} km")
    print(f"Country   : {car.country}")

    print()
    print(f"Deal Score : {score}/100")

    print()
    print("Search configuration")
    print("--------------------")
    print(config.model)
    print(config.battery)
    print(config.drivetrain)

    print()
    print("System ready.")


if __name__ == "__main__":
    main()