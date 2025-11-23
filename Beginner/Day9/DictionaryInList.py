
country=input("Enter the name of the country:\n")
visits=int(input("Enter the number of visits:\n"))
list_of_cities=["Son Paulo","Rio de jeniro"]


travel_log=[
    {
        "country":"France",
        "visits":5,
        "cities":["Paris","lilie","Dijon"]
    },
    {
        "country":"Germany",
        "visits":4,
        "cities":["Berlin","Hamburg","Frankfort"]
    }
]

def add_new_country(country,visits,list_of_cities):
    new_country={}
    new_country["country"]=country
    new_country["visits"]=visits
    new_country["cities"]=list_of_cities
    travel_log.append(new_country)


add_new_country(country,visits,list_of_cities)
print(f"I've been to {travel_log[2]["country"]} {travel_log[2]["visits"]} times.")
print(f"My favourite places were:{travel_log[2]["cities"][0]}, {travel_log[2]["cities"][1]}")