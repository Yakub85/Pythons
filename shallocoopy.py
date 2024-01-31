countries = ["India","Austrelia","Turkey"]
nations = countries[:]#The highlighted line creates nations as a shallow copy of countries by using the slicing operator with one colon only.
                      # This operation takes a slice from the beginning to the end of countries.
print(nations)#. In this case, nations and countries have different identities.
print(id(nations)==id(countries))