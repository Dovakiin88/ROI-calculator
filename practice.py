places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

y = filter(lambda x: x != " " and x != "" and x != "  ", places)
print(list(y))