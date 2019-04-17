def my_dictionary(key):
    items = {"AB": "Alberta", "BC": "British Columbia",
             "ON": "Ontario", "SK": "Sask"}

    print(items[key])


value = input(
    "Enter a province with two letter code: (ie AB, BC etc) ").upper()
my_dictionary(value)
