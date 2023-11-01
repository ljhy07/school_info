import cafeteria

data = cafeteria.dish_name

# 줄바꿈과 특수문자 제거
data = data.replace('\n', '').replace('*', '').replace('-', '').replace('<br/>','')

# () 안의 내용 제거
import re
data = re.sub(r'\([^)]*\)', '', data)

# 여러 줄의 문자열로 분리하여 리스트로 저장
meal_list = data.split()

# 결과 출력
for meal in meal_list:
    print(meal)
