# GmE 205 - Laboratory 3
Spatial Object Systems in Python

## Part A: Project Setup

### Folder Structure in VS Code

When opened in VS Code, the project tree should look like this:

gme205-lab3/
├── data/
│   └── points.csv
├── output/
├── src/
│   ├── spatial.py
│   ├── demo.py
│   └── run_lab3.py
├── tests/
│   └── test_spatial.py
├── .gitignore
├── README.md
├── requirements.txt
└── .venv/

**Reflection:**  
This structure makes responsibilities visible before coding.  
- `src/` holds reusable domain definitions and runner scripts.  
- `data/` stores input files.  
- `output/` stores generated reports
- `.venv/` isolates dependencies.  
- GitHub tracks progress with meaningful commits.

---

## Part B: Refactor Point with Shapely
- Refactored `Point` to store geometry as a Shapely object (`self.geometry = ShapelyPoint(lon, lat)`).
- Preserved validation rules for longitude/latitude in the constructor.
- Added properties `lon` and `lat` to maintain public interface.
- Implemented `to_tuple()` for coordinate access.
- Preserved geodesic semantics with `distance_to()` using the Haversine formula.

**Reflection:**  
Internal representation changed (geometry now lives in Shapely), but external usage (`p.lon`, `p.lat`) remained stable. This demonstrates refactoring without breaking public meaning.

---

## Part C: Structured Data Boundaries
- Implemented `from_dict()` to construct a `Point` from structured dictionary input.
- Implemented `as_dict()` to return JSON-ready values (id, name, tag, geometry, bbox).
- Verified that invalid input still fails through constructor validation.
- Demo confirmed correct behavior.

**Reflection:**  
Data boundaries prevent duplication of validation logic. `as_dict()` ensures outputs are serializable and do not expose Shapely internals.

---

## Part D: Shared Spatial Abstraction
- Introduced `SpatialObject` base class to store geometry and shared behavior (`bbox()`, `intersects()`).
- Refactored `Point` to inherit from `SpatialObject` and use `super().__init__(geometry)`.
- Verified that `Point` can call `bbox()` without duplicating code.

**Reflection:**  
Shared spatial behavior belongs in `SpatialObject`. Domain-specific meaning remains in subclasses. This separation improves maintainability.

---

## Part E: Parcel Implementation
- Implemented `Parcel` class inheriting from `SpatialObject`.
- Stores structured attributes (e.g., area, zone, is_active) in a dictionary.
- Implemented `as_dict()` for JSON-ready output.
- Verified that both `Point` and `Parcel` use inherited `bbox()` and `intersects()`.
- Demo showed one True and one False intersection case.

**Reflection:**  
Parcel demonstrates how multiple spatial types can share abstraction. Inheritance avoids duplication, while attributes capture domain-specific meaning.

---