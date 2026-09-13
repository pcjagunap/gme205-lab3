import json
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from spatial import Point, Parcel

def main():
    # Construct objects
    inside = Point("IN", 2, 2)
    outside = Point("OUT", 12, 2)
    attributes = {"area": 50.0, "zone": "Residential", "is_active": True}
    geom = Polygon([(0,0), (10,0), (10,5), (0,5)])
    parcel = Parcel(101, geom, attributes)

    # Build report dictionary
    report = {
        "point_inside": inside.as_dict(),
        "point_outside": outside.as_dict(),
        "parcel": parcel.as_dict(),
        "relationships": {
            "inside_intersects_parcel": inside.intersects(parcel),
            "outside_intersects_parcel": outside.intersects(parcel)
        }
    }

    # Write JSON output
    with open("output/lab3_report.json", "w") as f:
        json.dump(report, f, indent=2)

    # Visualization
    fig, ax = plt.subplots()
    x, y = geom.exterior.xy
    ax.plot(x, y, color="blue", label="Parcel")
    ax.scatter(inside.lon, inside.lat, color="green", label="Inside")
    ax.scatter(outside.lon, outside.lat, color="red", label="Outside")
    ax.legend()
    plt.title("Lab 3 Preview")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.savefig("output/lab3_preview.png")

if __name__ == "__main__":
    main()