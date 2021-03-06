from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


#runs for N=9 as required by the deliverables section
def run():
    stations = build_station_list()
    N = 9
    print(rivers_by_station_number(stations, N))

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()