from spatial import Point

p = Point("A", 121.0, 14.6, name="Gate", tag="POI")
q = Point("B", 120.98, 14.62, name="Nearby", tag="POI")

print(p.id, p.lon, p.lat)
print(p.to_tuple())
print("Distance (m):", p.distance_to(q))  # Haversine distance

# Construct from dict
data = {"id": "X", "lon": 121.05, "lat": 14.65, "name": "Test", "tag": "POI"}
p = Point.from_dict(data)
print("From dict:", p.id, p.lon, p.lat)

# Convert to dict
print("As dict:", p.as_dict())

from spatial import Point

p = Point("A", 121.0, 14.6)
print("BBox:", p.bbox())  # inherited from SpatialObject

from spatial import Point, Parcel
from shapely.geometry import Polygon

# Create a parcel
attributes = {"area": 50.0, "zone": "Residential", "is_active": True}
geom = Polygon([(0,0), (10,0), (10,5), (0,5)])
parcel = Parcel(101, geom, attributes)
print("Parcel bbox:", parcel.bbox())

# Intersects test
inside = Point("IN", 2, 2)
outside = Point("OUT", 12, 2)
print("Inside intersects parcel:", inside.intersects(parcel))   # True
print("Outside intersects parcel:", outside.intersects(parcel)) # False