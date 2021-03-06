from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    water_level_stations = stations_level_over_threshold(stations, 0.8)

    station_names = []

    for station, water_level in water_level_stations:
        details = (station.name, water_level)
        station_names.append(details)

    print(station_names)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()