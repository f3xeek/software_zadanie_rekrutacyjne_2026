from typing import Literal
from pydantic import BaseModel

class ConfigFile(BaseModel):
    devices: "Devices"

class Devices(BaseModel):
    servo: "Servos"
    sensor: "Sensors"
    relay: "Relays"

class Servo(BaseModel):
    open_pos: int
    closed_pos: int
    board: Literal["rocket"]
    device_id: int

class Servos(BaseModel):
    fuel_intake: Servo
    oxidizer_intake: Servo
    fuel_main: Servo
    oxidizer_main: Servo

class Relay(BaseModel):
    board: Literal["rocket"]
    device_id: int

class Relays(BaseModel):
    oxidizer_heater: Relay 
    igniter: Relay
    parachute: Relay

class Sensor(BaseModel):
    board: Literal["rocket"]
    device_id: int
    data_type: Literal["float"]
    recording: Literal["off", "on"]
    units: str
    scale: float 
    a: float
    b: float

class Sensors(BaseModel):
    oxidizer_level: Sensor 
    fuel_level: Sensor
    altitude: Sensor
    oxidizer_pressure: Sensor
    angle: Sensor
