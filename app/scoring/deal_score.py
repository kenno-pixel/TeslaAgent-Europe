from models.car import Car


class DealScore:

    @staticmethod
    def calculate(car: Car) -> int:

        score = 50

        # Price
        if car.price <= 35000:
            score += 10

        if car.price <= 33000:
            score += 5

        # Mileage
        if car.mileage <= 50000:
            score += 10

        if car.mileage <= 30000:
            score += 5

        # Equipment
        if car.heat_pump:
            score += 5

        if car.tow_hitch:
            score += 3

        if car.fsd:
            score += 8

        if car.eap:
            score += 4

        return min(score, 100)