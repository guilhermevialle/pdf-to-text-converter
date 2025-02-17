from utils.boilerplate import sigef_memorial_boilerplate, boilerplate


def boilerplate_switch(
    memorial_type: str,
    coordinates,
    epsg: int,
    include_height: bool,
    vertex_id: str = None,
):
    if memorial_type.upper() == "SIGEF":
        return sigef_memorial_boilerplate(coordinates, epsg, include_height, vertex_id)
