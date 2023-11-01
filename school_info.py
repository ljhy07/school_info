import requests
import json

class SchoolInfo:
    def __init__(self):
        self.local_name = input("지역 : ")
        self.school_name = input("학교 : ")
        self.grade_num = int(input("학년 : "))
        self.class_num = int(input("반 : "))

        self.url = f"https://open.neis.go.kr/hub/schoolInfo?Type=json&pIndex=1&pSize=100&SCHUL_NM={self.school_name}&ATPT_OFCDC_SC_NM={self.local_name}"

        self.response_info = requests.get(self.url)
        self.data = self.response_info.json()
        self.school_list = self.data.get("schoolInfo", [])
        self.atpt_code = None
        self.atpt_name = None
        self.schul_code = None
        self.schul_name = None
        self.schul_kind = None
        self.fond = None

    def sch_info(self):
        if self.response_info.status_code == 200:
            for school_data in self.school_list:
                row_data = school_data.get("row", [])
                for school_info in row_data:
                    self.atpt_code = school_info.get("ATPT_OFCDC_SC_CODE", "NULL")
                    self.atpt_name = school_info.get("ATPT_OFCDC_SC_NM", "NULL")
                    self.schul_code = school_info.get("SD_SCHUL_CODE", "NULL")
                    self.schul_name = school_info.get("SCHUL_NM", "NULL")
                    self.schul_kind = school_info.get("SCHUL_KND_SC_NM", "NULL")
                    self.fond = school_info.get("FOND_SC_NM", "NULL")
                    
                    if (self.atpt_name == self.local_name+"교육청"):
                        print("ATPT_OFCDC_SC_CODE:", self.atpt_code)
                        print("ATPT_OFCDC_SC_NM:", self.atpt_name)
                        print("SD_SCHUL_CODE:", self.schul_code)
                        print("SCHUL_NM:", self.schul_name)
                        print("SCHUL_KND_SC_NM:", self.schul_kind)
                        print("FOND_SC_NM:", self.fond)
                        print("=" * 30)
                        break
        else:
            print("API 요청 실패")

# ==========================================================

# import requests
# import json

# local_name = input("지역 : ")
# school_name = input("학교 : ")
# grade_num = int(input("학년 : "))
# class_num = int(input("반 : "))

# url = f"https://open.neis.go.kr/hub/schoolInfo?Type=json&pIndex=1&pSize=100&SCHUL_NM={school_name}&ATPT_OFCDC_SC_NM={local_name}"

# response_info = requests.get(url)
# data = response_info.json()
# school_list = data.get("schoolInfo", [])
# atpt_code = None; atpt_name = None; schul_code = None; schul_name = None; schul_kind = None; fond = None;
    
# def sch_info():
#     if response_info.status_code == 200:
        
#         for school_data in school_list:
#             row_data = school_data.get("row", [])
#             for school_info in row_data:
#                 atpt_code = school_info.get("ATPT_OFCDC_SC_CODE", "NULL")
#                 atpt_name = school_info.get("ATPT_OFCDC_SC_NM", "NULL")
#                 schul_code = school_info.get("SD_SCHUL_CODE", "NULL")
#                 schul_name = school_info.get("SCHUL_NM", "NULL")
#                 schul_kind = school_info.get("SCHUL_KND_SC_NM", "NULL")
#                 fond = school_info.get("FOND_SC_NM", "NULL")
                
#                 if (atpt_name == local_name+"교육청"):
#                     print("ATPT_OFCDC_SC_CODE:", atpt_code)
#                     print("ATPT_OFCDC_SC_NM:", atpt_name)
#                     print("SD_SCHUL_CODE:", schul_code)
#                     print("SCHUL_NM:", schul_name)
#                     print("SCHUL_KND_SC_NM:", schul_kind)
#                     print("FOND_SC_NM:", fond)
#                     print("=" * 30)
#                     break;
#     else:
#         print("API 요청 실패")

# sch_info()