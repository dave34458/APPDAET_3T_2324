stations = {
    "lrt1": ["Baclaran", "EDSA", "Libertad", "Buendia", "Vito Cruz"
             "Quirino", "United Nations", "Central", "Carriedo",
             "Doroteo Jose"],
    "lrt2": ["Santolan", "Anonas", "Katipunan", "Betty Go-Belmonte",
             "Cubao"],
    "mrt3": ["Taft", "Magallanes", "Ayala", "Buendia"]
}

def find_railway_network(destination: str):
    railway_networks = []
    for line in stations:
        if destination in stations[line]:
            railway_networks.append(line)
    return railway_networks

destination = input("Please enter your destination: ")

railway_networks = find_railway_network(destination)
print(f"Your destination ({destination}) is near {railway_networks}")
# determine which railway network your destination is
