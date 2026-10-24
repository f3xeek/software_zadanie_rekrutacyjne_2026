import yaml 
from models import ConfigFile
from pathlib import Path

from typing import cast
from functools import partial

from communication_library.communication_manager import CommunicationManager
from communication_library.frame import Frame
from communication_library import ids
from models import Sensor, Sensors, Servos, Servo

def yaml_import(config_path: Path) -> ConfigFile:
        with open(config_path, 'r') as config_file:
            config = ConfigFile.model_validate(yaml.safe_load(config_file))
        return config

def log_data(name: str, frame:Frame):
    #IDK what the plan is with the data so will leave it like that for now
    print(name, frame.payload , " ",)

def init_sensors(cm: CommunicationManager, sensors: Sensors ):
    for name in Sensors.model_fields:
        sensor = cast(Sensor, getattr(sensors, name))
        sensor_frame = Frame(ids.BoardID.SOFTWARE, 
                               ids.PriorityID.LOW, 
                               ids.ActionID.FEED, 
                               ids.BoardID.ROCKET, 
                               ids.DeviceID.SENSOR, 
                               sensor.device_id,
                               ids.DataTypeID.FLOAT,
                               ids.OperationID.SENSOR.value.READ)
        cm.register_callback(partial(log_data, name), sensor_frame)

def init_servos(cm: CommunicationManager, servos: Servos ):
    for name in Servos.model_fields:
        servo = cast(Servo, getattr(servos, name))
        sensor_frame = Frame(ids.BoardID.SOFTWARE, 
                               ids.PriorityID.LOW, 
                               ids.ActionID.FEED, 
                               ids.BoardID.ROCKET, 
                               ids.DeviceID.SERVO, 
                               servo.device_id,
                               ids.DataTypeID.FLOAT,
                               ids.OperationID.SERVO.value.POSITION)
        cm.register_callback(partial(log_data, name), sensor_frame)

def init_all_feeds(cm:CommunicationManager, config: ConfigFile ):
    init_sensors(cm, config.devices.sensor)
    init_servos(cm, config.devices.servo)
