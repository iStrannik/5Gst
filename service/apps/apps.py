import signal
import sys

from balancer_communicator import balancer_communicator
from django.apps import AppConfig
from iperf_wrapper import iperf
from watchdog import Watchdog
from django.conf import settings
from apps import logger


watchdog = Watchdog(5)


class MyAppConfig(AppConfig):
    name = 'apps'

    def ready(self):
        if 'runserver' not in sys.argv:
            return True

        def TimeoutHandler():
            if iperf.is_started:
                iperf.stop()
            balancer_communicator.post_to_server()
            watchdog.reset()

        def signal_handler(sig, frame):
            watchdog.stop()
            balancer_communicator.delete_from_server()
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)

        logger.info(f'Environment settings:\n'
                    f'SERVICE_IP_ADDRESS: {settings.SERVICE_IP_ADDRESS}\n'
                    f'BALANCER_ADDRESS: {settings.BALANCER_ADDRESS}\n'
                    f'BALANCER_BASE_URL: {settings.BALANCER_BASE_URL}\n'
                    f'IPERF_PORT: {str(settings.IPERF_PORT)}\n'
                    f'SERVICE_PORT: {str(settings.SERVICE_PORT)}\n'
                    f'CONNECTING_TIMEOUT: {str(settings.CONNECTING_TIMEOUT)}'
                    )

        global watchdog
        watchdog = Watchdog(settings.CONNECTING_TIMEOUT, TimeoutHandler)
        balancer_communicator.post_to_server()
