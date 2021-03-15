# -*- coding: utf-8 -*-
#
# Vincent Healy August 2019
# Written using Visual Studio Code v 1.37.0 with Python Extension
#
# Constructs the url for the geocode under test
#
def geofunction(x,y):
    # driver = self.driver
    str1 = 'https://eu1.locationiq.com/v1/reverse.php?key='
    str2 = '705c24e108bed8&lat='
    str3 = x # '48.853106'
    str4 = '&lon='
    str5 = y # '2.384202'
    str6 = '&format=json'
    rev_geo = str1+str2+str3+str4+str5+str6
    # print(rev_geo)
    return rev_geo
