import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, "../lib")
log_dir = os.path.join(current_dir, "../log")

sys.path.append(lib_dir)



def update_mysql_alert(dictionary:dict):
    from database import mysql_conn

    conn = mysql_conn("measurement")
    cursor = conn.cursor()

    # get datas
    date = dictionary["date"]
    time = dictionary["time"]
    location_id = dictionary["location"]["id"]
    sensor_id = dictionary["sensor"]["id"]
    type_id = dictionary["type"]["id"]
    grade = dictionary["grade"]

    # update table
    QUERY = f"INSERT INTO alert "
    QUERY += """
        (date, time, location_id, sensor_id, type_id, grade)
        VALUES
        (%s, %s, %s, %s, %s, %s)
    """
    VALUES = (date, time, location_id, sensor_id, type_id, grade)
    cursor.execute(QUERY, VALUES)
    conn.commit()

    # close connector
    conn.close()


def send_noti(dictionary:dict):
    from database import return_informations
    from notification import send_line_noti_thread, create_message

    grade = dictionary["grade"]
    time = dictionary["time"]
    location_id = dictionary["location"]["id"]
    location_name = dictionary["location"]["name"]
    type_name = dictionary["type"]["name"]

    information = return_informations(grade=grade, location_id=location_id)
    message = create_message(grade=grade, time=time, location_name=location_name, type_name=type_name, information=information)

    access_tokens = [safety_manager["access_token"] for safety_manager in information["safety_manager"]] + [employee["access_token"] for employee in information["employee"]]
    for access_token in access_tokens:
        print(access_token)
        send_line_noti_thread(access_token=access_token, message=message)
        

def do_alert(dictionary:dict):
    from log_libs import setup_logger, remove_logger
    from os_libs import check_mkdirs
    
    import logging
    from datetime import datetime, timedelta
    from time import time
    
    start_time = time()
    location_id = dictionary['location']['id']
 
    def custom_converter(self, timestamp):
        current_time = datetime.fromtimestamp(timestamp) + timedelta(hours=9)
        return current_time.timetuple()
    
    log_file_dir = f"{log_dir}/time_spend/{location_id}"
    check_mkdirs(log_file_dir) # module

    logging.Formatter.converter = custom_converter
    
    logger = setup_logger(name="alert", level=logging.INFO, log_dir=log_file_dir) # module
    
    update_mysql_alert(dictionary=dictionary) # module
    send_noti(dictionary=dictionary) # module
    
    end_time = time()
    
    logger.info(f"{end_time - start_time} sec")
    remove_logger(logger) # module


# test
if __name__ == "__main__":
    dict = {
        "grade": "evacuation",
        "date": "2023-11-23",
        "time": "12:20:00",
        "sensor":{
            "id": 100
        },
        "location":{
            "id": 7, 
            "name": "도장공정"
        },
        "type":{
            "id": 1,
            "name": "화재"
        }
    }

    do_alert(dictionary=dict)