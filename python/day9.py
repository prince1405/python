#NESTING
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"], #if we will not use the square brackets the we are able to store only one key value, so to store multiple key value we have to use the square bracket.
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

#nesting a Dictionary in a Dictionary
travel_log = {
 "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visits": 10}
}

#nesting a Dictionary in a List
travel_log = [
{
  "Country": "Germany",
  "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 10
},
{
    "Country": "France",
    "Cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 10
}
]

