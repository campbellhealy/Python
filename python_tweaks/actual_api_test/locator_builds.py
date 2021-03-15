# -*- coding: utf-8 -*-
#
# Vincent Healy August 2019
# Written using Visual Studio Code v 1.37.0 with Python Extension
# 
# Data under test & request to build url to geofunction
#
# from geofunction import geofunction
from geofunction_two import geofunction

Location_1x, Location_1y = '48.853106','2.384202'
location1 = geofunction(Location_1x, Location_1y)

Location_2x, Location_2y = '48.858539','2.294438'
location2 = geofunction(Location_2x, Location_2y)

Location_3x, Location_3y = '48.860754','2.337632'
location3 = geofunction(Location_3x, Location_3y)
