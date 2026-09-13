import pytest
from shapely.geometry import Polygon
from spatial import Point, Parcel

def test_valid_point():
    p = Point("A", 121.0, 14.6)
    assert p.lon == 121.0
    assert p.lat == 14.6

def test_invalid_longitude():
    with pytest.raises(ValueError):
        Point("B", 999, 14.6)

def test_from_dict_valid():
    d = {"id": "C", "lon": 120.0, "lat": 15.0}
    p = Point.from_dict(d)
    assert p.id == "C"
    assert p.to_tuple() == (120.0, 15.0)

def test_from_dict_invalid():
    d = {"id": "D", "lon": 999, "lat": 15.0}
    with pytest.raises(ValueError):
        Point.from_dict(d)

def test_point_bbox():
    p = Point("E", 121.0, 14.6)
    assert p.bbox() == (121.0, 14.6, 121.0, 14.6)

def test_parcel_bbox_and_intersects():
    geom = Polygon([(0,0), (10,0), (10,5), (0,5)])
    parcel = Parcel(101, geom, {"zone": "Residential"})
    inside = Point("IN", 2, 2)
    outside = Point("OUT", 12, 2)
    assert parcel.bbox() == (0.0, 0.0, 10.0, 5.0)
    assert inside.intersects(parcel)
    assert not outside.intersects(parcel)

def test_as_dict_no_shapely_objects():
    p = Point("F", 121.0, 14.6)
    d = p.as_dict()
    assert isinstance(d["geometry"], list)
    assert isinstance(d["bbox"], list)