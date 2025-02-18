from utils.build_memorial import build_sigef_memorial
from utils.math.index import calculate_area, calculate_perimeter
from utils.helpers.index import get_epsg_info
from utils.indetifiers.index import coordinates_system_identifier


def generate_memorial(
    memorial_type: str,
    coordinates,
    epsg: int,
    include_altitude: bool,
    vertex_id: str = None,
):
    if memorial_type.upper() == "SIGEF":
        return build_sigef_memorial(coordinates, epsg, include_altitude, vertex_id)
