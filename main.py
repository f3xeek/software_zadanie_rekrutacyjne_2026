from pathlib import Path

from utils import yaml_import, init_all_feeds
from communication_library.communication_manager import CommunicationManager, TransportType
from communication_library.frame import Frame
from communication_library.tcp_transport import TcpSettings
from communication_library import ids
from communication_library.exceptions import TransportTimeoutError, UnregisteredCallbackError

CONFIGFILE = Path('./simulator_config.yaml')


def main():
    config = yaml_import(CONFIGFILE)
    cm = CommunicationManager()
    init_all_feeds(cm, config)

    cm.change_transport_type(TransportType.TCP)
    cm.connect(TcpSettings("127.0.0.1", 3000))

    while True:
        try:
            _ = cm.receive() 
        except TransportTimeoutError:
            pass
        except UnregisteredCallbackError as e:
            print(f"unregistered frame received: {e.frame}")

main()
