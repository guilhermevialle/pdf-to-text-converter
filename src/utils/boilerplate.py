def boilerplate(coordinates):
    text = "Inicia-se em "

    for i, coord in enumerate(coordinates, 1):
        if i == len(coordinates):
            text += f"terminando em V{i} "
        else:
            text += f"V{i} "

        # Handle both latlon and utm formats
        if "lat" in coord and "lon" in coord:
            text += f"{coord['lat']:.6f} {coord['lon']:.6f} altura 0"
        else:
            text += f"{coord['x']:.2f}m E {coord['y']:.2f}m N altura 0"

        if i < len(coordinates):
            text += ", "
        else:
            text += "..."

    return text
