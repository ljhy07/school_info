import school_info
import cafeteria
import schedule

class Main:
    def run(self):
        school_info_instance = school_info.SchoolInfo()
        cafeteria_instance = cafeteria.Cafeteria(school_info_instance)
        schedule_instance = schedule.Schedule(school_info_instance)

        school_info_instance.sch_info()
        cafeteria_instance.cafe()
        schedule_instance.sche()

if __name__ == "__main__":
    main_instance = Main()
    main_instance.run()