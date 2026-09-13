from spatial import Point

p = Point("A", 121.0, 14.6, name="Gate", tag="POI")
q = Point("B", 120.98, 14.62, name="Nearby", tag="POI")

print(p.id, p.lon, p.lat)
print(p.to_tuple())
print("Distance (m):", p.distance_to(q))  # Haversine distance