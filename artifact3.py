
import numpy as np

goal = {
    "HP" : 0.0,
    "ATK" : 0.0,
    "DEF" : 0.0,
    "EM" : 0.0,
    "HP%" : 0.0,
    "ATK%" : 60.0,
    "DEF%" : 0.0,
    "ER" : 40.0,
    "CR%" : 20.0,
    "CDMG%" : 120.0,
    "PhDMG%" : 0.0,
    "AnDMG%" : 0.0,
    "GeDMG%" : 0.0,
    "ElDMG%" : 0.0,
    "HyDMG%" : 0.0,
    "PyDMG%" : 0.0,
    "CrDMG%" : 46.5,
    "HB%" : 0.0
}

class artifact():
    def __init__(self):
        self.type = np.random.randint(0,5)
        self.art_set = np.random.randint(0,2)
        substat_list = [["HP",209+np.random.randint(0,4)*30,[209,239,269,299]],
                ["ATK",np.random.choice([14,16,18,19]),[14,16,18,19]],
                ["DEF",np.random.choice([16,19,21,23]),[16,19,21,23]],
                ["EM",np.random.choice([16,19,21,23]),[16,19,21,23]],
                ["HP%",np.random.choice([4.1,4.7,5.3,5.8]),[4.1,4.7,5.3,5.8]],
                ["ATK%",np.random.choice([4.1,4.7,5.3,5.8]),[4.1,4.7,5.3,5.8]],
                ["DEF%",np.random.choice([5.1,5.8,6.6,7.3]),[5.1,5.8,6.6,7.3]],
                ["ER",np.random.choice([4.5,5.2,5.8,6.5]),[4.5,5.2,5.8,6.5]],
                ["CR%",2.7+0.4*np.random.randint(0,4),[2.7,3.1,3.5,3.9]],
                ["CDMG%",5.4+0.8*np.random.randint(0,4),[5.4,6.2,7.0,7.8]]
            ]
        self.substat_name = [x[0] for x in substat_list]
        

        
        def main_stat(type):
            if type == 0:
                return ["HP",4780]
            elif type == 1:
                return ["ATK",311]
            elif type == 2:
                return [
                    ["HP%",46.6],
                    ["ATK%",46.6],
                    ["DEF%",58.3],
                    ["EM",187],
                    ["ER",51.8],
                ][np.random.randint(0,5)]
            elif type == 3:
                return [
                    ["HP%",46.6],
                    ["ATK%",46.6],
                    ["DEF%",58.3],
                    ["EM",187],
                    ["PhDMG%",58.3],
                    ["AnDMG%",46.6],
                    ["GeDMG%",46.6],
                    ["ElDMG%",46.6],
                    ["HyDMG%",46.6],
                    ["PyDMG%",46.6],
                    ["CrDMG%",46.6],
                ][np.random.randint(0,11)]
            elif type == 4:
                return [
                    ["HP%",46.6],
                    ["ATK%",46.6],
                    ["DEF%",58.3],
                    ["EM",187],
                    ["CR%",31.1],
                    ["CDMG%",62.2],
                    ["HB%",35.9]
                ][np.random.randint(0,7)]
        

        
        def substatroll(sub_stat,slist,main_stat):
            roll = 5 if np.random.randint(0,5) == 4 else 4
            check = []
            while len(sub_stat) < 4:
                ssroll = slist[np.random.randint(0,10)]
                if ssroll[0] != main_stat[0] and ssroll[0] not in check:
                    check.append(ssroll[0])
                    sub_stat.append(ssroll)
            return roll
        

        
        def weight(goal,stats):
            coef = {
            "HP" : 25/4780/4780*goal["HP"],
            "ATK" : 25/311/311*goal["ATK"],
            "DEF" : 25/311/311*goal["DEF"],
            "EM" : 25/187/187*goal["EM"],
            "HP%" : 25/46.6/46.6*goal["HP%"],
            "ATK%" : 25/46.6/46.6*goal["ATK%"],
            "DEF%" : 25/58.3/58.3*goal["DEF%"],
            "ER" : 25/51.8/51.8*goal["ER"],
            "CR%" : 25/31.1/31.1*goal["CR%"],
            "CDMG%" : 25/62.2/62.2*goal["CDMG%"],
            "PhDMG%" : 100*25/58.3/58.3*goal["PhDMG%"],
            "AnDMG%" : 100*25/46.6/46.6*goal["AnDMG%"],
            "GeDMG%" : 100*25/46.6/46.6*goal["GeDMG%"],
            "ElDMG%" : 100*25/46.6/46.6*goal["ElDMG%"],
            "HyDMG%" : 100*25/46.6/46.6*goal["HyDMG%"],
            "PyDMG%" : 100*25/46.6/46.6*goal["PyDMG%"],
            "CrDMG%" : 100*25/46.6/46.6*goal["CrDMG%"],
            "HB%" : 100*25/35.9/35.9*goal["HB%"]
            }
            weight = []
            for key in coef:
                weight.append(coef[key]*stats[key]) if goal[key] else 0 
            else:
                return sum(weight)
        
        stats = {
            "HP" : 0.0,
            "ATK" : 0.0,
            "DEF" : 0.0,
            "EM" : 0.0,
            "HP%" : 0.0,
            "ATK%" : 0.0,
            "DEF%" : 0.0,
            "ER" : 0.0,
            "CR%" : 0.0,
            "CDMG%" : 0.0,
            "PhDMG%" : 0.0,
            "AnDMG%" : 0.0,
            "GeDMG%" : 0.0,
            "ElDMG%" : 0.0,
            "HyDMG%" : 0.0,
            "PyDMG%" : 0.0,
            "CrDMG%" : 0.0,
            "HB%" : 0.0
        }
        main_stat = main_stat(self.type)
        sub_stat = []
        roll = substatroll(sub_stat,substat_list,main_stat)
        for i in range(roll):
            chosen = np.random.randint(0,4)
            sub_stat[chosen][1] += np.random.choice(sub_stat[chosen][2])
            
        sub_stat = [x[:2] for x in sub_stat]
        
        stats[main_stat[0]] += main_stat[1]
        for x in sub_stat:
            stats[x[0]] += x[1]
            
        self.weight = weight(goal,stats)
        self.stats = stats
        self.main_stat = main_stat
        self.sub_stat = sub_stat
total_roll = 0
count = 20

for nfdsele in range(count):
    name = r"C:\Users\ASUS\Desktop\ggez\round" + str(nfdsele) + r".txt"
    f = open(name,"w+")
    f.write("attempt" + str(nfdsele+1) + "\n")
    art_pool = [[],[],[],[],[]]
    roll_count = 0
    while True:
        # Artifact drop
        print(roll_count)
        cstats = {
            "HP" : 0.0,
            "ATK" : 0.0,
            "DEF" : 0.0,
            "EM" : 0.0,
            "HP%" : 0.0,
            "ATK%" : 0.0,
            "DEF%" : 0.0,
            "ER" : 0.0,
            "CR%" : 0.0,
            "CDMG%" : 0.0,
            "PhDMG%" : 0.0,
            "AnDMG%" : 0.0,
            "GeDMG%" : 0.0,
            "ElDMG%" : 0.0,
            "HyDMG%" : 0.0,
            "PyDMG%" : 0.0,
            "CrDMG%" : 0.0,
            "HB%" : 0.0
        }
        roll_count += 1
        Artifacts = []
        num = (2 if np.random.randint(0,99) < 7 else 1)
        
        for i in range(num):
            Artifacts.append(artifact())
            
        for n in Artifacts:
            if(n.art_set):
                art_pool[n.type].append(n)
        
        #eleminate less weight artifact
        for i in art_pool:
            if len(i) > 1:
                i.sort(key=lambda x : x.weight, reverse=True)

                i = [i[0]]
            if len(i) == 1:
                for j in cstats:
                    cstats[j] += i[0].stats[j]
        fin = True
        for j in cstats:
            if cstats[j] >= goal[j]:
                fin = fin and True
            else:
                break
        else:
            if fin:
                break

    f.write(str(roll_count) + "\n")
    total_roll += roll_count

    type_to_name = [ "Flower of Life", "Plume of Death", "Sands of Eon", "Goblet of Eonothem", "Circlet of Logos"]
    for key in cstats:
        f.write(f"{key} goal : {goal[key]} | result : {cstats[key]} \n")
    for i in art_pool:
        if i != []:
            f.write(str(type_to_name[i[0].type]) + "\n")
            f.write(f"main stat : {i[0].main_stat}\n")
            f.write("sub stat : \n")
            for j in range(len(i[0].sub_stat)):
                f.write(f"{i[0].sub_stat[j]}\n")
    f.close()            
avg_roll = total_roll/count
print(avg_roll)