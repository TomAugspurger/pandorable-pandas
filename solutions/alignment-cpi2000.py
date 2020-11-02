cpi_2000_average = cpi.loc["2000"].mean()

# *renormalize* the entire `cpi` series to "Index 2000" units.
cpi_2000 = 100 * (cpi / cpi_2000_average)

# Compute real GDP again, this time in "year 2000 dollars".
rgdp_2000 = gdp / cpi_2000
rgdp_2000
