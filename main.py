import tkinter as tk
import csv
import random

# csv 파일을 열어서 리스트로 만들어주기
with open('재료목록.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # 임의의 리스트 만들기
    ingre = []
    
    for row in csvreader:
        ingre.append(row)

# \n 제거해주기
ingre = [[s.strip() if isinstance(s, str) else s for s in row] for row in ingre]

# 2차원 리스트를 1차원 리스트로 바꿔주기
ingre = [item[0] for item in ingre]

# 모든 알파벳을 소문자로 만들어주기
ingre = [i.lower() for i in ingre]

# 재료목록 리스트가 잘 저장되었는지 확인
# print(ingre)

# 메인 창 만들기
window = tk.Tk()

# 안내문 추가
label = tk.Label(window, text='한 줄에 재료 하나씩 모두 영어 소문자로, 띄어쓰기는 그대로 띄어서 적어주세요')
label.pack()

# 각 리스트를 입력받는 공간 만들기
input_fields = []
for i in range(10): # 열개의 입력 공간 만들기
    input_field = tk.Entry(window, width=50)
    input_fields.append(input_field)
    input_field.pack()

# 안내문 추가
label = tk.Label(window, text='각 재료마다 추천받을 음식 갯수를 정수로 입력해주세요')
label.pack()

# 숫자를 입력받는 공간 만들기
count_field = tk.Entry(window, width=10)
count_field.pack()

# 입력받은 정보를 저장 할 임의의 리스트 만들기
input_list = []

# 버튼을 누르면 입력되게, 그리고 꺼지도록 만들기
def button_click():
    global x
    for input_field in input_fields:
        input_list.append(input_field.get()) # 각 입력 공간의 입력된 값 저장
    x = int(count_field.get())
    window.destroy()

# 버튼 만들기
button = tk.Button(window, text="Add", command=button_click)

# 창에 버튼 추가
button.pack()

# Start the window's event loop
window.mainloop()

# 리스트가 잘 저장되었는지 확인
# print(input_list)


# 크롤링 받은 각 재료마다 음식 리스트 만들기
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

# 각 재료 리스트에 있는 아무 값이 없는 인덱스 제거 코드
for lst in [pork, peaches, peanuts, pork_ribs, pineapples, pork_tenderloin, pork_shoulder, pears, oat_flour, sausage,  beef_chuck, beef, seafood, oats, quinoa, nectarines, mushroom, prime_rib, wild_rice, ground_beef, cornish_hens, corn_flour, goat, chocolate, fish, chia_seeds, chicken, flax_seeds, coconut, chicken_legs, ground_pork, ground_chicken, chicken_thighs, chicken_wings, lamb, brisket, brown_rice, beef_tenderloin, millet, mangos, beef_ribs, cornmeal, buckwheat, bulgur, duck, cherries, cheese, venison, sirloin, bananas, barley, shellfish, veal, white_rice_flour, avocados, apricots, wild_game, turkey, almond_meal, almonds, tapioca_flour, plums, spelt, amaranth, steak, pomegranates]:
    lst[:] = [x for x in lst if x !='']


# 입력받은 리스트에 요소가 ingre 리스트에 존재한다면
# 재료의 음식 랜덤이로 4개 출력


if "pork" in input_list and "pork" in ingre:
    pork_choices = random.sample(pork, x)
    print(pork_choices, '\n')

if "peaches" in input_list and "peaches" in ingre:
    peaches_choices = random.sample(peaches, x)
    print(peaches_choices, '\n')
    
if "peanuts" in input_list and "peanuts" in ingre:
    peanuts_choices = random.sample(peanuts, x)
    print(peanuts_choices, '\n')
    
if "pork ribs" in input_list and "pork ribs" in ingre:
    pork_ribs_choices = random.sample(pork_ribs, x)
    print(pork_ribs_choices, '\n')
    
if "pineapples" in input_list and "pineapples" in ingre:
    pineapples_choices = random.sample(pineapples, x)
    print(pineapples_choices, '\n')
    
if "pork tenderloin" in input_list and "pork tenderloin" in ingre:
    pork_tenderloin_choices = random.sample(pork_tenderloin, x)
    print(pork_tenderloin_choices, '\n')
    
if "pork shoulder" in input_list and "pork shoulder" in ingre:
    pork_shoulder_choices = random.sample(pork_shoulder, x)
    print(pork_shoulder_choices, '\n')
    
if "pears" in input_list and "pears" in ingre:
    pears_choices = random.sample(pears, x)
    print(pears_choices, '\n')
    
if "oat flour" in input_list and "oat flour" in ingre:
    oat_flour_choices = random.sample(oat_flour, x)
    print(oat_flour_choices, '\n')
    
if "sausage" in input_list and "sausage" in ingre:
    sausage_choices = random.sample(sausage, x)
    print(sausage_choices, '\n')
    
if "beef chuck" in input_list and "beef chuck" in ingre:
    beef_chuck_choices = random.sample(beef_chuck, x)
    print(beef_chuck_choices, '\n')
    
if "beef" in input_list and "beef" in ingre:
    beef_choices = random.sample(beef, x)
    print(beef_choices, '\n')
    
if "seafood" in input_list and "seafood" in ingre:
    seafood_choices = random.sample(seafood, x)
    print(seafood_choices, '\n')
    
if "oats" in input_list and "oats" in ingre:
    oats_choices = random.sample(oats, x)
    print(oats_choices, '\n')

if "quinoa" in input_list and "quinoa" in ingre:
    quinoa_choices = random.sample(quinoa, x)
    print(quinoa_choices, '\n')

if "nectarines" in input_list and "nectarines" in ingre:
    nectarines_choices = random.sample(nectarines, x)
    print(nectarines_choices, '\n')

if "mushroom" in input_list and "mushroom" in ingre:
    mushroom_choices = random.sample(mushroom, x)
    print(mushroom_choices, '\n')

if "prime rib" in input_list and "prime rib" in ingre:
    prime_rib_choices = random.sample(prime_rib, x)
    print(prime_rib_choices, '\n')

if "wild rice" in input_list and "wild rice" in ingre:
    wild_rice_choices = random.sample(wild_rice, x)
    print(wild_rice_choices, '\n')

if "ground beef" in input_list and "ground beef" in ingre:
    ground_beef_choices = random.sample(ground_beef, x)
    print(ground_beef_choices, '\n')

if "cornish hens" in input_list and "cornish hens" in ingre:
    cornish_hens_choices = random.sample(cornish_hens, )
    print(cornish_hens_choices, '\n')

if "corn flour" in input_list and "corn flour" in ingre:
    corn_flour_choices = random.sample(corn_flour, x)
    print(corn_flour_choices, '\n')

if "goat" in input_list and "goat" in ingre:
    goat_choices = random.sample(goat, x)
    print(goat_choices, '\n')

if "chocolate" in input_list and "chocolate" in ingre:
    chocolate_choices = random.sample(chocolate, x)
    print(chocolate_choices, '\n')

if "fish" in input_list and "fish" in ingre:
    fish_choices = random.sample(fish, x)
    print(fish_choices, '\n')

if "chia seeds" in input_list and "chia seeds" in ingre:
    chia_seeds_choices = random.sample(chia_seeds, x)
    print(chia_seeds_choices, '\n')

if "chicken" in input_list and "chicken" in ingre:
    chicken_choices = random.sample(chicken, x)
    print(chicken_choices, '\n')

if "flax seeds" in input_list and "flax seeds" in ingre:
    flax_seeds_choices = random.sample(flax_seeds, x)
    print(flax_seeds_choices, '\n')

if "coconut" in input_list and "coconut" in ingre:
    coconut_choices = random.sample(coconut, x)
    print(coconut_choices, '\n')

if "chicken legs" in input_list and "chicken legs" in ingre:
    chicken_legs_choices = random.sample(chicken_legs, x)
    print(chicken_legs_choices, '\n')

if "ground pork" in input_list and "ground pork" in ingre:
    ground_pork_choices = random.sample(ground_pork, x)
    print(ground_pork_choices, '\n')

if "ground chicken" in input_list and "ground chicken" in ingre:
    ground_chicken_choices = random.sample(ground_chicken, x)
    print(ground_chicken_choices, '\n')

if "chicken breasts" in input_list and "chicken breasts" in ingre:
    chicken_breasts_choices = random.sample(chicken_breasts, x)
    print(chicken_breasts_choices, '\n')

if "ground turkey" in input_list and "ground turkey" in ingre:
    ground_turkey_choices = random.sample(ground_turkey, x)
    print(ground_turkey_choices, '\n')

if "chicken thighs" in input_list and "chicken thighs" in ingre:
    chicken_thighs_choices = random.sample(chicken_thighs, x)
    print(chicken_thighs_choices, '\n')

if "chicken wings" in input_list and "chicken wings" in ingre:
    chicken_wings_choices = random.sample(chicken_wings, x)
    print(chicken_wings_choices, '\n')

if "lamb" in input_list and "lamb" in ingre:
    lamb_choices = random.sample(lamb, x)
    print(lamb_choices, '\n')

if "brisket" in input_list and "brisket" in ingre:
    brisket_choices = random.sample(brisket, x)
    print(brisket_choices, '\n')

if "brown rice" in input_list and "brown rice" in ingre:
    brown_rice_choices = random.sample(brown_rice, x)
    print(brown_rice_choices, '\n')

if "beef tenderloin" in input_list and "beef tenderloin" in ingre:
    beef_tenderloin_choices = random.sample(beef_tenderloin, x)
    print(beef_tenderloin_choices, '\n')

if "millet" in input_list and "millet" in ingre:
    millet_choices = random.sample(millet, x)
    print(millet_choices, '\n')

if "mangos" in input_list and "mangos" in ingre:
    mangos_choices = random.sample(mangos, x)
    print(mangos_choices, '\n')

if "cornmeal" in input_list and "cornmeal" in ingre:
    cornmeal_choices = random.sample(cornmeal, x)
    print(cornmeal_choices, '\n')

if "buckwheat" in input_list and "buckwheat" in ingre:
    buckwheat_choices = random.sample(buckwheat, x)
    print(buckwheat_choices, '\n')

if "bulgur" in input_list and "bulgur" in ingre:
    bulgur_choices = random.sample(bulgur, x)
    print(bulgur_choices, '\n')

if "duck" in input_list and "duck" in ingre:
    duck_choices = random.sample(duck, x)
    print(duck_choices, '\n')

if "cherries" in input_list and "cherries" in ingre:
    cherries_choices = random.sample(cherries, x)
    print(cherries_choices, '\n')

if "cheese" in input_list and "cheese" in ingre:
    cheese_choices = random.sample(cheese, x)
    print(cheese_choices, '\n')

if "venison" in input_list and "venison" in ingre:
    venison_choices = random.sample(venison, x)
    print(venison_choices, '\n')

if "sirloin" in input_list and "sirloin" in ingre:
    sirloin_choices = random.sample(sirloin, x)
    print(sirloin_choices, '\n')
    
if "bananas" in input_list and "bananas" in ingre:
    bananas_choices = random.sample(bananas, x)
    print(bananas_choices, '\n')
    
if "barley" in input_list and "barley" in ingre:
    barley_choices = random.sample(barley, x)
    print(barley_choices, '\n')
    
if "shellfish" in input_list and "shellfish" in ingre:
    shellfish_choices = random.sample(shellfish, x)
    print(shellfish_choices, '\n')
    
if "veal" in input_list and "veal" in ingre:
    veal_choices = random.sample(veal, x)
    print(veal_choices, '\n')
    
if "white rice flour" in input_list and "white rice flour" in ingre:
    white_rice_flour_choices = random.sample(white_rice_flour, x)
    print(white_rice_flour_choices, '\n')
    
if "avocados" in input_list and "avocados" in ingre:
    avocados_choices = random.sample(avocados, x)
    print(avocados_choices, '\n')
    
if "apricots" in input_list and "apricots" in ingre:
    apricots_choices = random.sample(apricots, x)
    print(apricots_choices, '\n')
    
if "wild game" in input_list and "wild game" in ingre:
    wild_game_choices = random.sample(wild_game, x)
    print(wild_game_choices, '\n')
    
if "turkey" in input_list and "turkey" in ingre:
    turkey_choices = random.sample(turkey, x)
    print(turkey_choices, '\n')
    
if "almond meal" in input_list and "almond meal" in ingre:
    almond_meal_choices = random.sample(almond_meal, x)
    print(almond_meal_choices, '\n')
    
if "almonds" in input_list and "almonds" in ingre:
    almonds_choices = random.sample(almonds, x)
    print(almonds_choices, '\n')
    
if "tapioca flour" in input_list and "tapioca flour" in ingre:
    tapioca_flour_choices = random.sample(tapioca_flour, x)
    print(tapioca_flour_choices, '\n')
    
if "plums" in input_list and "plums" in ingre:
    plums_choices = random.sample(plums, x)
    print(plums_choices, '\n')
    
if "spelt" in input_list and "spelt" in ingre:
    spelt_choices = random.sample(spelt, x)
    print(spelt_choices, '\n')
    
if "apples" in input_list and "apples" in ingre:
    apples_choices = random.sample(apples, x)
    print(apples_choices, '\n')
    
if "amaranth" in input_list and "amaranth" in ingre:
    amaranth_choices = random.sample(amaranth, x)
    print(amaranth_choices, '\n')
    
if "steak" in input_list and "steak" in ingre:
    steak_choices = random.sample(steak, x)
    print(steak_choices, '\n')
    
if "pomegranates" in input_list and "pomegranates" in ingre:
    pomegranates_choices = random.sample(pomegranates, x)
    print(pomegranates_choices, '\n')

