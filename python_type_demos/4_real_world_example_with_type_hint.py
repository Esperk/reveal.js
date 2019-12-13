class HoebaRequest(object):

    pickup_number: str

    def __init__(self):
        food_number = "7fc012d"
        print(f'going to set {food_number}')
        self.pickup_number = food_number,  # note that mypy doesn't pick this up!
        print(f"just set {food_number} result is {self.pickup_number}")


print(HoebaRequest())
