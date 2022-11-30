import random


batch_number = 0
batch =[]
while len(batch) < 5000:
    rand_ = random.randint(1,100)
    if rand_ < 2:
        batch.append("Blotch")
    elif rand_ > 2 and rand_ < 4:
        batch.append("Rot")
    elif rand_ > 4 and rand_ < 6:
        batch.append("Scab")
    else:
        batch.append("Normal")


normal = 0
rot = 0
scab = 0
blotch = 0

accepted = 0


for x in batch:
    if x == "Normal":
        normal += 1
        accepted += 1
    elif x == "Rot":
        rot += 1
    elif x == "Scab":
        scab += 1
    else:
        blotch += 1

rejected = 5000 - accepted
print("Normal", normal)
print("Scab", scab)
print("Blotch", blotch)
print("Rot",rot)
print("Accepted", accepted)
print("Rejected", rejected)