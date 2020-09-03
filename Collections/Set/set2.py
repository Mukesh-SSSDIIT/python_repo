# difference()
set1 = {10,20,30,40,50}
set2  = {20,40,50,60,70,80}

set3 = set1.difference(set2)

print(set3)

# difference_update()
set1 = {10,20,30,40,50}
set2  = {30,40,60,70,80}

set1.difference_update(set2)

print(set1)

# intersaction
set1 = {10,20,30,40,50}
set2  = {30,40,60,70,80}

set3 = set1.intersection(set2)

print(set3)

# intersection_update
set1 = {10,20,30,40,50}
set2  = {30,40,60,70,80}

set1.intersection_update(set2)

print(set1)

# isdisjoint
set1 = {10,20,30,40,50,60}
set2  = {60,70,80}

rv = set1.isdisjoint(set2)

print(rv)

# issubset
set1 = {40,50,60,70}
set2  = {10,20,30,40,50,60,70}

rv = set1.issubset(set2)

print(rv)

# issuperset
set1 = {10,20,30,40,50,60,70}
set2  = {40,50,60,80}

rv = set1.issuperset(set2)

print(rv)

# symmetric_difference
set1 = {10,20,30,40,50,60,70}
set2  = {40,50,60,80}

set3 = set1.symmetric_difference(set2)

print(set3)

# symmetric_difference_update
set1 = {10,20,30,40,50,60,70}
set2  = {40,50,60,80}

set1.symmetric_difference_update(set2)

print(set1)