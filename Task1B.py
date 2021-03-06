from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    # Build list of stations
    stations = build_station_list()
    
    #setting the coordinates of the cambridge city centre to measure from
    p = (52.2053, 0.1218)

    #getting the distances from the centre of cambridge and creating lists
    distances = stations_by_distance(stations, p)
    station_names = []
    for (station, distance) in distances:
        details = (station.name, station.town, distance)
        station_names.append(details)

    #printing edge 10 values
    print(station_names[:10])
    print(station_names[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()