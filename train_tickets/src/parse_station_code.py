#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from url_request import get_page_source
from config import station_code_url, station_code_headers
import re
#import pprint


def get_station_code():
    station_code_page = get_page_source(station_code_url, station_code_headers)
    pattern = "([\u4e00-\u9fa5]+)\|([A-Z]+)"
    station_code = re.findall(pattern, station_code_page)

    #return dict(station_code)

    #station_names = [name for name, value in [s for s in station_code]]
    #station_telecodes = [value for name, value in [s for s in station_code]]
    #return station_names, station_telecodes

    station_code = dict(station_code)
    return station_code.keys(), station_code.values()


if __name__ == "__main__":    
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(get_station_code())

    station_names, station_telecodes = get_station_code()
    print(station_names)
    print(station_telecodes)



