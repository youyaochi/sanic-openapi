from datetime import date
from sanic_openapi.doc import String, Date


class Manufacturer:
    name = str
    start_date = date


class Driver:
    name = String(description='Name of driver', required=True, at='formData')
    birthday = Date(description='birthday of driver', required=False, at='formData')
    Authorization = String(description='Token TOKEN', required=True, at='header')


class Car:
    on = bool
    doors = int
    color = str
    make = Manufacturer
    driver = Driver
    passengers = [Driver]


class Garage:
    spaces = int
    cars = [Car]


class Status:
    success = bool