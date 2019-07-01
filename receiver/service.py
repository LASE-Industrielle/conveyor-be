from api.models import Measurement, Job


def create_measurement_from_json(json):
    values = {
        "area": json["CalculatedArea"],
        "conveyor_speed": json["ConveyorSpeed"],
        "material_density": json["BulkDensity"],
        "volume_sum": json["VolumeSum"],
        "volume_stream": json["AvgVolumeFlow"],
        "mass_stream": json["AvgMassFlow"],
        "mass_sum": json["MassSum"],
        "conveyor_deviation": json["Barycenter"],
        "count_valid_pts": json["ValidPoints"],
        "upper_limit": json["UpperLimitFlow"],
        "lower_limit": json["LowerLimitFlow"],
        "timestamp": json["TgmTime"],


    }
    job = Job.objects.filter(id=1).first()
    m = Measurement(**values, job=job)
    return m
