import swagger_client
from swagger_client.rest import ApiException
from django.conf import settings
from swagger_client.configuration import Configuration
from apps import logger


class BalancerCommunicator:
    def __init__(self):
        self.api_instance = swagger_client.ServiceApi()
        configuration = Configuration()
        configuration.host = 'http://' + settings.BALANCER_ADDRESS + settings.BALANCER_BASE_URL
        self.api_instance.api_client.configuration = configuration

    def post_to_server(self):
        body = swagger_client.ServerAddressRequest(ip=settings.SERVICE_IP_ADDRESS,
                                                   port=settings.SERVICE_PORT,
                                                   port_iperf=settings.IPERF_PORT)
        try:
            self.api_instance.service_create(data=body)
        except ApiException as e:
            logger.exception('Exception when calling ServerApi->server_post_ip: %s\n' % e)

    def delete_from_server(self):
        body = swagger_client.ServerAddressRequest(ip=settings.SERVICE_IP_ADDRESS,
                                                   port=settings.SERVICE_PORT,
                                                   port_iperf=settings.IPERF_PORT)
        try:
            self.api_instance.service_delete(data=body)
        except ApiException as e:
            logger.exception('Exception when calling ServerApi->server_delete_ip: %s\n' % e)


balancer_communicator = BalancerCommunicator()
