#pragma once

#include <array>
#include <string>
#include <cstdint>

// Open solar system C++ foundation stub.
// Deterministic interface for future pure C++ ephemeris or Python binding.
// No external dependencies. Ready for expansion with fixed kernels.

struct BodyState {
    std::array<double, 3> pos_au;
    std::array<double, 3> vel_au_per_day;
    std::string time_utc;
};

// Placeholder pure function signature.
// Implementation can later load a fixed DE421-derived table or call into Python.
BodyState get_state(const std::string& body_name, int year, int month, int day);

// Example bodies
inline constexpr const char* EARTH = "earth";
inline constexpr const char* MARS = "mars";
inline constexpr const char* PLUTO = "pluto";
