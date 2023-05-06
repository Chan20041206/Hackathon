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
label = tk.Label(window, text='각 재료마다 추천받을 음식 갯수를 정수로  입력해주세요')
label.pack()

# 숫자를 입력받는 공간 만들기
count_field = tk.Entry(window, width=10)
count_field.pack()

# 입력받은 정보를 저장 할 임의의 리스트 만들기
input_list = []

# 버튼을 누르면 입력되게, 그리고 꺼지도록 만들기
def button_click():
    global count
    for input_field in input_fields:
        input_list.append(input_field.get()) # 각 입력 공간의 입력된 값 저장
    count = int(count_field.get())  # 입력된 숫자 값을 count 변수에 저장
    window.destroy()

# 버튼 만들기
button = tk.Button(window, text="Add", command=button_click)

# 창에 버튼 추가
button.pack()

# Start the window's event loop
window.mainloop()


print(input_list)
print(count)
