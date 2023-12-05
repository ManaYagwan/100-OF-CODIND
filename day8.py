
country = input("country visted ? ")
visit = int(input("number of time visited ? "))
list_of_country_visited = eval(input("how many state did you visit ? "))

travel_log = [
    {
        "country":"france",
        "visite":12,
        "cities":["paris","lille","dijon"]
    }
]

def vis (country_t,visite_t,cities_t):
    new_country = {}
    new_country["country"]= country_t
    new_country["visite"]= visite_t
    new_country["cities"]=cities_t
    travel_log.append(new_country)


vis(country,visit,list_of_country_visited)
print(travel_log)