import random
from random import sample

# 1. Genereer een lijst met functionele lampen (hoeveel?)
# 2. Vul de lijst aan met defecte lampen (hoeveel?)
# 3. batch of 25 lampen to testen
# Randomizer with 2%
# if else statement with defect or functional Lamps
# 4. while loop 10x




# Aantal Lamps
allLamps = 75000
defectLamps = (75000 / 100) * 2
functionalLamps = allLamps - defectLamps
defectLamps = int(defectLamps)
functionalLamps = int(functionalLamps)

# Randomize
f = "functional"
d = "defect"
functionalLamps = ["Functional"] * functionalLamps
defectLamps = ["Defect"] * defectLamps
AllLamps = functionalLamps + defectLamps

# print(sample(AllLamps,10))

# Opslag
defect = []
functional = []

def test():
    rounds = 1
    while rounds < 26:
        rand = sample(AllLamps,1)
        if rand[0] == "Functional":
            result = "Functional Lamp"
            functional_result = True
            functional.append(functional_result)
            # print(result)
        else:
            result = "Defect lamp *"
            defection = False
            defect.append(defection)
            # print(result)

        rounds += 1
    print("Total Functional Lamps ", len(functional))
    print("Total Defect Lamps ",len(defect))        


# 10 Herhalingen
for i in range(10):
    test()
                