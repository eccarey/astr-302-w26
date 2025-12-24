import numpy as np

def gc_dist(lon1, lat1, lon2, lat2):
    """Return the great circle distance between (lon1, lat1) and (lon2, lat2)
       Both the inputs and the outputs are in degrees.
    """
    from numpy import sin, cos, arcsin, sqrt

    lon1 = np.radians(lon1); lat1 = np.radians(lat1)
    lon2 = np.radians(lon2); lat2 = np.radians(lat2)

    return np.degrees(2*arcsin(sqrt( (sin((lat1-lat2)*0.5))**2 + cos(lat1)*cos(lat2)*(sin((lon1-lon2)*0.5))**2 )));

if __name__ == "__main__":
    print(gc_dist(0, 45, 0, 90))
