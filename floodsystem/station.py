# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return 
        
    def typical_range_consistent(self):
        """Checks typical high/low range data for consistency"""
        if self.typical_range is None:
            return False
        (low, high) = self.typical_range
        return high >= low
    
    def relative_water_level(self):
        """Returns latest water level as a fraction of the typical range"""
        if self.latest_level is None:
            return None
        if not self.typical_range_consistent():
            return None
        (low, high) = self.typical_range
        if low == high:
            return None
        return (self.latest_level - low)/(high - low)


def inconsistent_typical_range_stations(stations):
    '''Returns list of stations that have inconsistent data'''
    inconsistent_stations = []
    for station in stations:
        consistent = station.typical_range_consistent()
        if not consistent:
            inconsistent_stations.append(station)

    return inconsistent_stations
