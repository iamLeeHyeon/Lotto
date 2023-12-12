
import csv
import requests
from datetime import datetime
from bs4 import BeautifulSoup

def getWinNumbers(round_num:int):
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={round_num}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    win_result_tag = soup.find(name ='div', attrs= {'class': 'win_result'})

    # Game Round
    strong_tags = win_result_tag.find_all("strong")
    round_num_text = strong_tags[0].text.replace("회", "")
    round_num_query = int(round_num_text)

    # Game Round Date
    p_tags = win_result_tag.find_all('p', 'desc')
    draw_date = datetime.strptime(p_tags[0].text, "(%Y년 %m월 %d일 추첨)")

    # Game data
    win_num_tags = win_result_tag.find(name='div', attrs={'class': 'num win'})
    p_tags = win_num_tags.find('p')
    win_nums = [int(x.text) for x in p_tags.find_all('span')]

    # Bonus data
    bonus_num_tag = win_result_tag.find(name='div', attrs={'class' : 'num bonus'})
    p_tags = bonus_num_tag.find('p')
    bonus_num = int(p_tags.find('span').text)

    # Sum of win_nums and bonus_num
    sum_nums = sum(win_nums) + bonus_num

    return {
        "round_num": round_num_query,
        "draw_date": draw_date,
        "win_nums": win_nums,
        "bonus_num": bonus_num,
        "sum_nums": sum_nums
    }

# CSV save
filename = 'Lotto.csv'
with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)

    # Write Header
    header = ['draw_date'] + [f'win_num_{i+1}' for i in range(6)] + ['bonus_num', 'sum']
    writer.writerow(header)

    # Write data
    for round_num in range(1, 1097):
        Lotto_data = getWinNumbers(round_num)
        row = [Lotto_data['draw_date']] + Lotto_data['win_nums'] + [Lotto_data['bonus_num'], Lotto_data['sum_nums']]
        writer.writerow(row)
        print(round_num, Lotto_data)

print("Succeed.")
