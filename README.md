# GmE 205 - Laboratory 3
Spatial Object Systems in Python

## Part A: Project Setup

### Folder Structure in VS Code

```text

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
```

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
## Part F: Runner, Structured Outputs, and Visualization
 

- **Reflection:**  
 - `output/lab3_report.json` contains structured evidence (points, parcel, relationships).  
  - `output/lab3_preview.png` shows a simple visualization of the parcel and points.  


## Part G: Testing and Debugging


  - **Tests verify:**  
  - Valid Point construction.  
  - Invalid longitude raises `ValueError`.  
  - `from_dict()` works for valid input and fails for invalid input.  
  - `bbox()` works for Point and Parcel.  
  - `intersects()` returns True/False correctly.  
  - `as_dict()` contains only JSON-ready values.
  ALL PASSED

## PART H: 
- **CHALLENGE 1- DATA -> OBJECT BOUNDARY**
- You gain a single, reusable entry point for converting external data into a validated object.
-  What it does is simplify external data loading and make the data → object boundary explicit. Without it, you duplicate parsing logic manually; with it, you centralize and cleanly separate responsibilities.

- **CHALLENGE 2- OBJECT -> STRUCTURED OUTPUT**
- Point.as_dict() gives you a clean dictionary.
- Parcel.as_dict() converts Shapely geometry into a list of coordinate pairs, plus bbox as a list.
Result: no duplication, clear object → structured output boundary.

-**CHALLENGE 3- SHARED SPATIAL BEHAVIOUR**
-  Shared spatial behavior belongs in the abstraction, ensuring consistency and avoiding duplication.

- **CHALLENGE 4- EXPLAIN DISTANCE DECISION**
- If your coordinates are longitude/latitude degrees, Shapely treats them as flat Cartesian values — not as positions on a sphere.
- The Haversine formula interprets longitude/latitude as positions on a sphere (Earth).
- It computes great‑circle distance, which matches geodesic meaning.

README Reflection and Submission
1. **Refactoring:**  
   - Changed: `Point` now uses a Shapely geometry object internally.  
   - Stable: External code still interacts with simple JSON‑ready values via `from_dict()` and `as_dict()`.

2. **Responsibility:**  
   - Shapely: low‑level geometry operations.  
   - SpatialObject: shared spatial behavior (`intersects`, `bbox`).  
   - Point/Parcel: domain meaning (identity, attributes, coordinate semantics).

3. **Data boundary:**  
   - `from_dict()` delegates validation to the constructor to avoid duplication and keep validation centralized.

4. **Output boundary:**  
   - `as_dict()` returns primitive, JSON‑ready values to ensure portability and avoid exposing non‑serializable Shapely objects.

5. **Inheritance:**  
   - `intersects()` belongs in `SpatialObject` to prevent duplication and guarantee consistent behavior across subclasses.

6. **Coordinate meaning:**  
   - Shapely’s `.distance()` is planar, not geodesic. Longitude/latitude require Haversine for real‑world distances in meters.

7. **Scale:**  
   - Maintainability: clear boundaries and shared behavior make the design extensible.  
   - Performance: Slow