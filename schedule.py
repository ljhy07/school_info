import requests
from datetime import datetime
import json

class Schedule:
    def __init__(self, school_info_instance):
        self.school_info = school_info_instance

    def sche(self):
        yearTime = datetime.now().strftime("%Y")
        monthTime = datetime.now().strftime("%m")
        dayTime = datetime.now().strftime("%d")
        url = f"https://open.neis.go.kr/hub/misTimetable?Type=json&pIndex=1&pSize=100&ATPT_OFCDC_SC_CODE={self.school_info.atpt_code}&SD_SCHUL_CODE={self.school_info.schul_code}&GRADE={self.school_info.grade_num}&CLASS_NM={self.school_info.class_num}&ALL_TI_YMD={yearTime.zfill(4)}{monthTime.zfill(2)}{dayTime.zfill(2)}"

        response_sche = requests.get(url)
        contents_sche = response_sche.text
        parsed_data_sche = json.loads(contents_sche)

        try:
            timetable_list = []
            for row in parsed_data_sche["misTimetable"][1]["row"]:
                schul_name = row.get("SCHUL_NM", "NULL")
                sem = row.get("SEM", "NULL")
                grade = row.get("GRADE", "NULL")
                class_name = row.get("CLASS_NM", "NULL")
                perio = row.get("PERIO", "NULL")
                itrt_cntnt = row.get("ITRT_CNTNT", "NULL")

                timetable_list.append({
                    "SCHUL_NM": schul_name,
                    "SEM": sem,
                    "GRADE": grade,
                    "CLASS_NM": class_name,
                    "PERIO": perio,
                    "ITRT_CNTNT": itrt_cntnt
                })
        except KeyError:
            print("등록된 시간표가 없습니다.")
            print("="*30)
            return

        # 결과 리스트 출력
        for entry in timetable_list:
            print(entry)
        print("="*30)
