import requests
import json
import re
from datetime import datetime

class Cafeteria:
    def __init__(self, school_info):
        self.school_info = school_info
        self.yearTime = datetime.now().strftime("%Y")
        self.monthTime = datetime.now().strftime("%m")
        self.dayTime = datetime.now().strftime("%d")
        self.url = f"https://open.neis.go.kr/hub/mealServiceDietInfo?Type=json&pIndex=1&pSize=100&ATPT_OFCDC_SC_CODE={self.school_info.atpt_code}&SD_SCHUL_CODE={self.school_info.schul_code}&MLSV_YMD={self.yearTime.zfill(4)}{self.monthTime.zfill(2)}{self.dayTime.zfill(2)}"

        self.response_cafe = requests.get(self.url)
        self.contents_cafe = self.response_cafe.text
        self.parsed_data_cafe = json.loads(self.contents_cafe)

    def cafe(self):
        if self.response_cafe.status_code == 200:
            dish_name = ""
            try:
                meal_list = []
                if "mealServiceDietInfo" in self.parsed_data_cafe:
                    for row in self.parsed_data_cafe["mealServiceDietInfo"][1]["row"]:
                        meal_name = row.get("MMEAL_SC_NM", "NULL")
                        meal_date = row.get("MLSV_YMD", "NULL")
                        dish_name = row.get("DDISH_NM", "NULL")
                        cal_info = row.get("CAL_INFO", "NULL")

                        meal_list.append({
                            "MMEAL_SC_NM": meal_name,
                            "MLSV_YMD": meal_date,
                            "CAL_INFO": cal_info,
                        })
            except KeyError:
                print("급식이 없습니다.")
                print("="*30)
                return
        else:
            print("API 연동 실패")

        data = dish_name

        # 줄바꿈과 특수문자 제거
        data = data.replace('\n', '').replace('*', '').replace('-', '').replace('<br/>','')

        # () 안의 내용 제거
        data = re.sub(r'\([^)]*\)', '', data)

        # 여러 줄의 문자열로 분리하여 리스트로 저장
        dish_name = data.split()

        # 결과 출력
        if meal_list != None or dish_name != None:
            for entry in meal_list:
                print(entry)

            print("'DISH_NAME'")
            for meal in dish_name:
                print(meal)
            print("="*30)
        else:
            print("급식이 없습니다.")

# ====================================================

# import school_info
# import requests
# import json
# import re
# from datetime import datetime

# yearTime = datetime.now().strftime("%Y")
# monthTime = datetime.now().strftime("%m")
# dayTime = datetime.now().strftime("%d")
# url = f"https://open.neis.go.kr/hub/mealServiceDietInfo?Type=json&pIndex=1&pSize=100&ATPT_OFCDC_SC_CODE={school_info.atpt_code}&SD_SCHUL_CODE={school_info.schul_code}&MLSV_YMD={yearTime.zfill(4)}{monthTime.zfill(2)}{dayTime.zfill(2)}"

# response_cafe = requests.get(url)
# contents_cafe = response_cafe.text
# parsed_data_cafe = json.loads(contents_cafe)

# print(parsed_data_cafe)

# def cafe():
#     if response_cafe.status_code == 200:
        
#         if "RESULT" in parsed_data_cafe:
#             print("급식이 없습니다.")
#             return

#         meal_list = []
#         if "mealServiceDietInfo" in parsed_data_cafe:
#             for row in parsed_data_cafe["mealServiceDietInfo"][1]["row"]:
#                 meal_name = row.get("MMEAL_SC_NM", "NULL")
#                 meal_date = row.get("MLSV_YMD", "NULL")
#                 dish_name = row.get("DDISH_NM", "NULL")
#                 cal_info = row.get("CAL_INFO", "NULL")

#                 meal_list.append({
#                     "MMEAL_SC_NM": meal_name,
#                     "MLSV_YMD": meal_date,
#                     "CAL_INFO": cal_info,
#                 })
#     else:
#         print("API 연동 실패")

#     data = dish_name

#     # 줄바꿈과 특수문자 제거
#     data = data.replace('\n', '').replace('*', '').replace('-', '').replace('<br/>','')

#     # () 안의 내용 제거
#     data = re.sub(r'\([^)]*\)', '', data)

#     # 여러 줄의 문자열로 분리하여 리스트로 저장
#     dish_name = data.split()

#     # 결과 출력
#     for entry in meal_list:
#         print(entry)

#     print("'DISH_NAME'")
#     for meal in dish_name:
#         print(meal)

# cafe()