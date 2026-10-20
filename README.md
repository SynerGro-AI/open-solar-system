# open-solar-system

Open, public Python + C++ foundation for a realistic solar system.

Built with the same deterministic rules as the SynerGro / Seraphina stack:
- Fixed NASA JPL DE421 kernel (Skyfield)
- Pure functions
- No randomness
- Identical inputs always produce identical outputs
- Honest errors

## Python core
`solar_system.py` provides heliocentric positions and velocities for Earth, Mars, and Pluto using the real DE421 ephemeris.

```bash
pip install skyfield
python solar_system.py --date 2026-10-19
```

## C++ side
`solar_system.hpp` is a pure header stub ready for a future deterministic C++ implementation (or binding to the Python state).

## Seraphina.agi
This repo is designed to sit beside the open Seraphina.AGIv1.0.8 (MIT). The Python state can be consumed by Seraphina as an external deterministic sensor or decision input. No proprietary Glyph code is included here.

## Reference
Physics rules and craft-token ideas were informed by the companion repo: https://github.com/SynerGro-AI/oxal-solar-core

Physics stays tight. Everything is open and reproducible.
