class Car:

    def __init__(self,
                 brand: str,
                 model: str,
                 color: str,
                 license_plate: str,
                 fuel_efficiency: float = 15,
                 max_fuel: float = 50
                 ):

        # Validate parameters received by the constructor
        assert len(license_plate) == 7
        assert fuel_efficiency > 0
        assert max_fuel > 0

        # Set object parameters
        self._brand: str = brand
        self._model: str = model
        self._color: str = color
        self._license_plate: str = license_plate
        self.__fuel_efficiency: float = fuel_efficiency
        self.__max_fuel: float = max_fuel
        self._engine_is_on: bool = False
        self.__fuel: float = 0

    # Object property Getters
    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @property
    def color(self):
        return self._color

    @property
    def license_plate(self):
        return self._license_plate

    @property
    def fuel_indicator(self):
        return self.__fuel / self.__max_fuel

    def switch_engine(self):
        """
        Turns the engine on or off, depending on the state of _engine_is_on property and current __fuel.
        """
        if self._engine_is_on:
            self._engine_is_on = False
            print("Car engine is now off.")
        elif self.__fuel:
            self._engine_is_on = True
            print("Car engine is now on.")
        else:
            print("The car has no fuel. Please refill.")

    def fuel_refill(self, fuel: float):
        """
        Refills the car with fuel.
        :param fuel: Liters of fuel to refill.
        """
        assert 0 < fuel
        if fuel < self.__max_fuel - self.__fuel:
            print("Refilling the car")
            self.__fuel = self.__fuel + fuel
        else:
            print("Cant refill more than fuel tank capacity.")

    def move(self, distance: float):
        """
        Moves the car a given distance, depending on __engine_is_on and __fuel state.
        :param distance:
        """
        assert distance > 0
        fuel_required = distance / self.__fuel_efficiency
        if self._engine_is_on:
            if self.__fuel > fuel_required:
                print("Moving the car")
                self.__fuel = self.__fuel - fuel_required
            else:
                print("Not enough fuel. Please refill or lower distance.")
        else:
            print("Turn on engine first")
