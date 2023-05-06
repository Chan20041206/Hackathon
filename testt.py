import csv

with open('재료목록full.csv', newline='', encoding='UTF8') as csvfile:
    reader = csv.reader(csvfile)
    data = [row for row in reader]
    pork = []
    peaches =  []
    peanuts = []
    pork_ribs = []
    pineapples = []
    pork_tenderloin = []
    pork_shoulder = []
    pears = []
    oat_flour = []
    sausage = []
    beef_chuck = []
    beef = []
    seafood = []
    oats = []
    quinoa = []
    nectarines = []
    mushroom = []
    prime_rib = []
    wild_rice = []
    ground_beef = []
    cornish_hens = []
    corn_flour = []
    goat = []
    chocolate = []
    fish = []
    chia_seeds = []
    chicken = []
    flax_seeds = []
    coconut = []
    chicken_legs = []
    ground_pork = []
    ground_chicken = []
    chicken_breasts = []
    ground_turkey = []
    chicken_thighs = []
    chicken_wings = []
    lamb = []
    brisket = []
    brown_rice = []
    beef_tenderloin = []
    millet = []
    mangos = []
    beef_ribs = []
    cornmeal = []
    buckwheat = []
    bulgur = []
    duck = []
    cherries = []
    cheese = []
    venison = []
    sirloin = []
    bananas = []
    barley = []
    shellfish = []
    veal = []
    white_rice_flour = []
    avocados = []
    apricots = []
    wild_game = []
    turkey = []
    almond_meal = []
    almonds = []
    tapioca_flour = []
    plums = []
    spelt = []
    apples = []
    amaranth = []
    steak = []
    pomegranates = []
    for row in data:
        pork.append(row[0])
        peaches.append(row[1])
        peanuts.append(row[2])
        pork_ribs.append(row[3])
        pineapples.append(row[4])
        pork_tenderloin.append(row[5])
        pork_shoulder.append(row[6])
        pears.append(row[7])
        oat_flour.append(row[8])
        sausage.append(row[9])
        beef_chuck.append(row[10])
        beef.append(row[11])
        seafood.append(row[12])
        oats.append(row[13])
        quinoa.append(row[14])
        nectarines.append(row[15])
        mushroom.append(row[16])
        prime_rib.append(row[17])
        wild_rice.append(row[18])
        ground_beef.append(row[19])
        cornish_hens.append(row[20])
        corn_flour.append(row[21])
        goat.append(row[22])
        chocolate.append(row[23])
        fish.append(row[24])
        chia_seeds.append(row[25])
        chicken.append(row[26])
        flax_seeds.append(row[27])
        coconut.append(row[28])
        chicken_legs.append(row[29])
        ground_pork.append(row[30])
        ground_chicken.append(row[31])
        chicken_breasts.append(row[32])
        ground_turkey.append(row[33])
        chicken_thighs.append(row[34])
        chicken_wings.append(row[35])
        lamb.append(row[36])
        brisket.append(row[37])
        brown_rice.append(row[38])
        beef_tenderloin.append(row[39])
        millet.append(row[40])
        mangos.append(row[41])
        beef_ribs.append(row[42])
        cornmeal.append(row[43])
        buckwheat.append(row[44])
        bulgur.append(row[45])
        duck.append(row[46])
        cherries.append(row[47])
        cheese.append(row[48])
        venison.append(row[49])
        sirloin.append(row[50])
        bananas.append(row[51])
        barley.append(row[52])
        shellfish.append(row[53])
        veal.append(row[54])
        white_rice_flour.append(row[55])
        avocados.append(row[56])
        apricots.append(row[57])
        wild_game.append(row[58])
        turkey.append(row[59])
        almond_meal.append(row[60])
        almonds.append(row[61])
        tapioca_flour.append(row[62])
        plums.append(row[63])
        spelt.append(row[64])
        apples.append(row[65])
        amaranth.append(row[66])
        steak.append(row[67])
        pomegranates.append(row[68])

print(pork, '\n')
print(pomegranates, '\n')
print(ground_beef, '\n')
print(ground_pork)
