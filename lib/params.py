#ver=1.4
import rclpy
from rclpy.node import Node

class GenericParams(Node):
    def __init__(self, nodeName : str):
        super().__init__(nodeName)

        self.nodeName = 'node'
        self.ns = ''
        self.id = 0
        self.devInfoService = ''# devinfo_0
        self.devInterface = 'eth0'
        self.devMultiNode = False
        self.qosService = ''# qos_0
        self.qosDirPath = 'qos'
        self.safetyService = ''# safety_0
        self.timesyncService = ''# timesync_0
        self.timesyncPeriod_ms = 10000.0
        self.timesyncAccuracy_ms = 2.0
        self.timesyncWaitService = False

        self.declare_parameter('nodeName', self.nodeName)
        self.declare_parameter('ns', self.ns)
        self.declare_parameter('id', self.id)
        self.declare_parameter('devInfoService', self.devInfoService)
        self.declare_parameter('devInterface', self.devInterface)
        self.declare_parameter('devMultiNode', self.devMultiNode)
        self.declare_parameter('qosService', self.qosService)
        self.declare_parameter('qosDirPath', self.qosDirPath)
        self.declare_parameter('safetyService', self.safetyService)
        self.declare_parameter('timesyncService', self.timesyncService)
        self.declare_parameter('timesyncPeriod_ms', self.timesyncPeriod_ms)
        self.declare_parameter('timesyncAccuracy_ms', self.timesyncAccuracy_ms)
        self.declare_parameter('timesyncWaitService', self.timesyncWaitService)
        self.__getParam()

    def __getParam(self):
        self.nodeName = self.get_parameter('nodeName').get_parameter_value().string_value
        self.ns = self.get_parameter('ns').get_parameter_value().string_value
        self.id = self.get_parameter('id').get_parameter_value().integer_value
        self.devInfoService = self.get_parameter('devInfoService').get_parameter_value().string_value
        self.devInterface = self.get_parameter('devInterface').get_parameter_value().string_value
        self.devMultiNode = self.get_parameter('devMultiNode').get_parameter_value().bool_value
        self.qosService = self.get_parameter('qosService').get_parameter_value().string_value
        self.qosDirPath = self.get_parameter('qosDirPath').get_parameter_value().string_value
        self.safetyService = self.get_parameter('safetyService').get_parameter_value().string_value
        self.timesyncService = self.get_parameter('timesyncService').get_parameter_value().string_value
        self.timesyncPeriod_ms = self.get_parameter('timesyncPeriod_ms').get_parameter_value().double_value
        self.timesyncAccuracy_ms = self.get_parameter('timesyncAccuracy_ms').get_parameter_value().double_value
        self.timesyncWaitService = self.get_parameter('timesyncWaitService').get_parameter_value().bool_value