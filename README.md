# open-solar-system

Open, public Python + C++ foundation for a realistic solar system.

Built with the same deterministic rules as the SynerGro / Seraphina stack:
- Fixed NASA JPL DE421 kernel (Skyfield)
- Pure functions
- No randomness
- Identical inputs always produce identical outputs
- Honest errors

## Python core
`solar_system.py` provides heliocentric positions and velocities for:
- All major planets (Mercury through Pluto) + the Sun
- Earth's Moon
- Jupiter's Galilean moons (Io, Europa, Ganymede, Callisto)
- Saturn's major moons (Mimas, Enceladus, Tethys, Dione, Rhea, Titan, Hyperion, Iapetus)
- Uranus's major moons (Miranda, Ariel, Umbriel, Titania, Oberon)

```bash
pip install skyfield
python solar_system.py --date 2026-10-19
python solar_system.py --date 2026-10-19 --bodies uranus titania oberon miranda
```

### Galactic pull
DE421 is a solar-system barycentric ephemeris. It does **not** include the galactic tide or external stellar perturbations. Within the DE421 frame the results are fully deterministic. For applications that require galactic-scale forces, a higher-order ephemeris (e.g. DE440) or an explicit galactic potential model would be needed; that remains future work and must stay deterministic.

## C++ side
`include/solar_system.hpp` is a pure header stub ready for a future deterministic C++ implementation (or binding to the Python state).

## Seraphina.agi
This repo is designed to sit beside the open Seraphina.AGIv1.0.8 (MIT). The Python state can be consumed by Seraphina as an external deterministic sensor or decision input. No proprietary Glyph code is included here.

## Reference
Physics rules and craft-token ideas were informed by the companion repo: https://github.com/SynerGro-AI/oxal-solar-core

Physics stays tight. Everything is open and reproducible.
