using System;

public class SpaceAge
{
    private const double EARTH_ORBITAL_PERIOD_DAYS = 365.25;
    private const int TOTAL_DAY_SECONDS = 86400;
    private const double MERCURY_ORBITAL_PERIOD_IN_EARTH_YEARS = 0.2408467;
    private const double VENUS_ORBITAL_PERIOD_IN_EARTH_YEARS = 0.61519726;
    private const double MARS_ORBITAL_PERIOD_IN_EARTH_YEARS = 1.8808158;
    private const double JUPITER_ORBITAL_PERIOD_IN_EARTH_YEARS = 11.862615;
    private const double SATURN_ORBITAL_PERIOD_IN_EARTH_YEARS = 29.447498;
    private const double URANUS_ORBITAL_PERIOD_IN_EARTH_YEARS = 84.016846;
    private const double NEPTUNE_ORBITAL_PERIOD_IN_EARTH_YEARS = 164.79132;

    private readonly int _seconds;

    public SpaceAge(int seconds)
    {
        _seconds = seconds;
    }

    public double CalculateOrbitalPeriodSeconds(double planetYearsInEarthYears)
    {
        double planetOrbitalPeriodInEarthSeconds = (EARTH_ORBITAL_PERIOD_DAYS * planetYearsInEarthYears) * TOTAL_DAY_SECONDS;
        return _seconds / planetOrbitalPeriodInEarthSeconds;
    }

    public double OnEarth()
    {
        return CalculateOrbitalPeriodSeconds(1);
    }

    public double OnMercury()
    {
        return CalculateOrbitalPeriodSeconds(MERCURY_ORBITAL_PERIOD_IN_EARTH_YEARS);
    }

    public double OnVenus()
    {
        return CalculateOrbitalPeriodSeconds(VENUS_ORBITAL_PERIOD_IN_EARTH_YEARS);
    }

    public double OnMars()
    {
        return CalculateOrbitalPeriodSeconds(MARS_ORBITAL_PERIOD_IN_EARTH_YEARS);
    }

    public double OnJupiter()
    {
        return CalculateOrbitalPeriodSeconds(JUPITER_ORBITAL_PERIOD_IN_EARTH_YEARS);
    }

    public double OnSaturn()
    {
        return CalculateOrbitalPeriodSeconds(SATURN_ORBITAL_PERIOD_IN_EARTH_YEARS);
    }

    public double OnUranus()
    {
        return CalculateOrbitalPeriodSeconds(URANUS_ORBITAL_PERIOD_IN_EARTH_YEARS);
    }

    public double OnNeptune()
    {
        return CalculateOrbitalPeriodSeconds(NEPTUNE_ORBITAL_PERIOD_IN_EARTH_YEARS);
    }
}