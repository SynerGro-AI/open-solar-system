#!/usr/bin/env python3
"""
Open solar system core.
Authoritative JPL DE421 positions and velocities.
Deterministic, pure, no external calls after kernel download.
"""

import argparse
from datetime import datetime
from skyfield.api import load

print("Loading JPL DE421...")
eph = load('de421.bsp')
ts = load.timescale()

BODIES = {
    'sun': eph['sun'],
    'earth': eph['earth'],
    'mars': eph['mars'],
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
    args = parser.parse_args()

    if args.date:
        dt = datetime.fromisoformat(args.date)
        t = ts.utc(dt.year, dt.month, dt.day)
    else:
        t = ts.now()

    print(f"Time: {t.utc_strftime('%Y-%m-%d %H:%M:%S')} UTC\n")
    for name in ['earth', 'mars', 'pluto']:
        s = get_state(name, t)
        print(f"{name:6s} pos {s['pos_au']}")
        print(f"       vel {s['vel_au_per_day']} AU/day")

if __name__ == '__main__':
    main()
