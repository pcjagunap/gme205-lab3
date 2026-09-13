import math
from shapely.geometry import Point as ShapelyPoint

class Point:
    def __init__(self, id, lon, lat, name=None, tag=None):
        # Validation
        if not (-180 <= lon <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        if not (-90 <= lat <= 90):
            raise ValueError("Latitude must be between -90 and 90")

        self.id = id
        self.geometry = ShapelyPoint(lon, lat)  # Shapely stores geometry
        self.name = name
        self.tag = tag

    @property
    def lon(self):
        return self.geometry.x

    @property
    def lat(self):
        return self.geometry.y

    def to_tuple(self) -> tuple[float, float]:
        return (self.lon, self.lat)

    def distance_to(self, other) -> float:
        """Compute geodesic distance to another Point using Haversine."""
        return Point.haversine_m(self.lon, self.lat, other.lon, other.lat)

    @staticmethod
    def haversine_m(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
        """Static method: Haversine formula in meters."""
        R = 6_371_000.0  # Earth radius in meters
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)
        a = (math.sin(dphi / 2) ** 2 +
             math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c


    @classmethod
    def from_dict(cls, d: dict):
        """Construct Point from a dictionary. Validation still happens in __init__."""
        return cls(
            d["id"],
            d["lon"],
            d["lat"],
            name=d.get("name"),
            tag=d.get("tag")
        )

    def as_dict(self):
        """Return JSON-ready representation of the Point."""
        return {
            "id": self.id,
            "name": self.name,
            "tag": self.tag,
            "geometry": [self.lon, self.lat],
            "bbox": list(self.geometry.bounds)
        }