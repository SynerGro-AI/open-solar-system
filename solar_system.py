#!/usr/bin/env python3
"""
Open solar system core.
Authoritative JPL DE421 positions and velocities for all major planets,
Earth's Moon, and Jupiter's Galilean moons.
Deterministic, pure, no external calls after kernel download.

Galactic pull: DE421 is a solar-system barycentric ephemeris. The galactic
tide and stellar perturbations are not included in the kernel. For full
determinism at galactic scales, a higher-order model (e.g. DE440 or a
galactic potential) would be required. This module remains strictly
deterministic within the DE421 frame.
"""

import argparse
from datetime import datetime
from skyfield.api import load

print("Loading JPL DE421...")
eph = load('de421.bsp')
ts = load.timescale()

# All major bodies available in DE421
BODIES = {
    'sun': eph['sun'],
    'mercury': eph['mercury'],
    'venus': eph['venus'],
    'earth': eph['earth'],
    'moon': eph['moon'],
    'mars': eph['mars'],
    'jupiter': eph['jupiter barycenter'],
    'io': eph['io'],
    'europa': eph['europa'],
    'ganymede': eph['ganymede'],
    'callisto': eph['callisto'],
    'saturn': eph['saturn barycenter'],
    'uranus': eph['uranus barycenter'],
    'neptune': eph['neptune barycenter'],
    'pluto': eph['pluto barycenter'],
}

def get_state(body_name, t):
    """Heliocentric position (AU) and velocity (AU/day)."""
    body = BODIES[body_name]
    state = body.at(t)
    pos = state.position.au
    vel = state.velocity.au_per_d
    return {
        'pos_au': (float(pos[0]), float(pos[1]), float(pos[2])),
        'vel_au_per_day': (float(vel[0]), float(vel[1]), float(vel[2])),
        'time': t.utc_strftime('%Y-%m-%d %H:%M:%S'),
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', default=None, help='YYYY-MM-DD (default now)')
    parser.add_argument('--bodies', nargs='*', default=list(BODIES.keys()),
                        help='Bodies to report (default: all)')
    args = parser.parse_args()

    if args.date:
        dt = datetime.fromisoformat(args.date)
        t = ts.utc(dt.year, dt.month, dt.day)
    else:
        t = ts.now()

    print(f"Time: {t.utc_strftime('%Y-%m-%d %H:%M:%S')} UTC\n")
    print("Note: DE421 is solar-system barycentric. Galactic tide is not included.\n")
    for name in args.bodies:
        if name not in BODIES:
            print(f"{name}: not available in DE421")
            continue
        s = get_state(name, t)
        print(f"{name:10s} pos {s['pos_au']}")
        print(f"           vel {s['vel_au_per_day']} AU/day")

if __name__ == '__main__':
    main()
