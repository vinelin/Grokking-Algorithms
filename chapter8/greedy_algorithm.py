states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])  # 需要覆盖的州
stations = {}
#  广播台清单以及所它所覆盖的州
stations['knoe'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])
final_stations = set()
while states_needed:
    best_station = None
    states_coverd = set()
    for station, states in stations.items():
        coverd = states_needed & states
        if len(coverd) > len(states_coverd):
            best_station = station
            states_coverd = coverd
    states_needed -= states_coverd
    final_stations.add(best_station)

print(final_stations)