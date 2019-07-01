from django.test import TestCase

from receiver.service import create_measurement_from_json


class ServiceTest(TestCase):

    def test_object_creation(self):
        data = self.get_test_data()

        measurement = create_measurement_from_json(data)

        self.assertEqual(measurement.area, 21)
        self.assertEqual(measurement.conveyor_speed, 100)
        self.assertEqual(measurement.material_density, 22)
        self.assertEqual(measurement.volume_sum, 512)
        self.assertEqual(measurement.volume_stream, 1124)
        self.assertEqual(measurement.mass_sum, 11440)
        self.assertEqual(measurement.mass_stream, 25115)
        self.assertEqual(measurement.conveyor_deviation, 100)
        self.assertEqual(measurement.count_valid_pts, 98)
        self.assertEqual(measurement.upper_limit, 30000)
        self.assertEqual(measurement.lower_limit, 10000)
        self.assertEquals(measurement.timestamp, "2008-02-01T09:08:30+05")



    def get_test_data(self):
        return {
            "ID": 15,
            "Counter": 1550,
            "Reset": "true",
            "CalibFinished": "false",
            "NullScanFinished": "true",
            "AppStartTime": "2008-02-01T09:00:22+05",
            "LastReset": "2008-02-01T09:05:25+05",
            "TgmTime": "2008-02-01T09:08:30+05",
            "ScannerStatus": {
                "ScannerOK": "true",
                "Malfunction": "false",
                "FaultyInterface": "false",
                "PollutionError": "false",
                "DataNotPlausible": "false",
                "ScannerNoValues": "false"
            },
            "ApplicationStatus": {
                "Measuring": "true",
                "NullScanNeeded": "false",
                "NullScanRuns": "false",
                "NullScanFailed": "false",
                "CalibNeeded": "false",
                "CalibRuns": "false",
                "CalibFailed": "false"
            },
            "ConveyorSpeed": 100,
            "CalculatedArea": 21,
            "AveragingInterval": 10000,
            "AvgVolumeFlow": 1124,
            "AvgMassFlow": 25115,
            "VolumeSum": 512,
            "MassSum": 11440,
            "Barycenter": 100,
            "LimitVolumeSum": 15000,
            "LimitMassSum": 335164,
            "BulkDensity": 22,
            "RectSignalVolumeLimit": "false",
            "RectSignalMassLimit": "false",
            "LimitStatus": {
                "VolumeFlowUsedForLimit": "true",
                "MassFlowUsedForLimit": "false",
                "FlowLimitFallenShortOf": "false",
                "FlowLimitExceeded": "false"
            },
            "LowerLimitFlow": 10000,
            "UpperLimitFlow": 30000,
            "ThresholdPollution": 80,
            "CurrPollution": 3,
            "AvgVolumeFlowPerHour": 1124,
            "ValidPoints": 98
        }
