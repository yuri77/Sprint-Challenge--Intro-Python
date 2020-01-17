# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    # root class
    pass


class FlightVehicle(Vehicle):
    # base class is vehicle
    pass


class Starship(FlightVehicle):
    # based om FlightVehicle
    pass


class Airplane(FlightVehicle):
    # based on FlightVehicle
    pass


class GroundVehicle(Vehicle):
    # base class Vehicle
    pass


class Car(GroundVehicle):
    # baseclass GroundVehicle
    pass


class Motorcycle(GroundVehicle):
    # base class GroundVehicle
    pass
