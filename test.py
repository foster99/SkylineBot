import skyline as sky

a = sky.Skyline()
a.insert_building(1,5,4)
a.insert_building(4,9,8)

b = sky.Skyline()
b.insert_building(3,7,6)

i = a.clone()
i.intersection(b)