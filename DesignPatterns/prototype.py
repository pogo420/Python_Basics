from enum import Enum, auto
from copy import deepcopy


class SensorType(Enum):
    FACTORY = auto()
    HOME = auto()


class RepairStatus(Enum):
    WIP = auto()
    NOT_ASSIGNED = auto()
    COMPLETED = auto()


class DeviceStatus:
    def __init__(self, device_id: str, sensor_type: SensorType, repair_status: RepairStatus):
        self.device_id = device_id
        self.repair_status = repair_status
        self.sensor_type = sensor_type

    def __str__(self):
        return f"""DeviceStatus{ {
        "device_id": self.device_id,
        "repair_status": self.repair_status,
        "sensor_type": self.sensor_type} 
        }"""


class DeviceStatusProtoFactory:

    type1 = DeviceStatus(device_id="",
                         sensor_type=SensorType.FACTORY,
                         repair_status=RepairStatus.WIP)

    type2 = DeviceStatus(device_id="",
                         sensor_type=SensorType.HOME,
                         repair_status=RepairStatus.NOT_ASSIGNED)

    @staticmethod
    def __create_proto(proto: DeviceStatus, device_id: str) -> DeviceStatus:
        proto.device_id = device_id
        return deepcopy(proto)

    @staticmethod
    def get_type1(device_id: str):
        return DeviceStatusProtoFactory.__create_proto(
            DeviceStatusProtoFactory.type1,
            device_id)

    @staticmethod
    def get_type2(device_id: str):
        return DeviceStatusProtoFactory.__create_proto(
            DeviceStatusProtoFactory.type2,
            device_id)


if __name__ == "__main__":
    t1_1 = DeviceStatusProtoFactory.get_type1("6788")
    t1_2 = DeviceStatusProtoFactory.get_type1("67-90")
    t2_1 = DeviceStatusProtoFactory.get_type2("67-90")

    print(t1_2, "\n", t1_1, "\n", t2_1)
