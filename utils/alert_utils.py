from configparser import ConfigParser
import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(current_dir, "../config/config.ini")
config = ConfigParser()
config.read(config_dir)

lib_dir = os.path.join(current_dir, "../lib")
sys.path.append(lib_dir)

def do_alert(data_received:dict):
    from mysql_lib import return_names
    from threading import Thread
    
    grade = data_received["grade"]
    insert_date = data_received["insert_date"]
    sensor_id = data_received["sensor_id"]
    location_id = data_received["location_id"]
    alert_id = data_received["alert_id"]
    
    (location_name, alert) = return_names(location_id = location_id,
                                                alert_id = alert_id)
    threads = []
    threads.append(Thread(target = send_noti, args = (grade, location_id, location_name, insert_date, alert)))
    # threads.append(Thread(target = run_alertbox, args = (location_id, target_id, grade)))
    for thread in threads:
        thread.start()

def send_noti(grade, location_id, location_name, insert_date, alert):
    from mysql_lib import return_informations
    from notification import send_line_noti, create_message
    
    information = return_informations(grade=grade, location_id=location_id)
    message = create_message(grade=grade, insert_date=insert_date, location_name=location_name, alert=alert, information=information)

    access_tokens = [safety_manager["access_token"] for safety_manager in information["safety_manager"]] \
        + [employee["access_token"] for employee in information["employee"]]
    for access_token in access_tokens:
        send_line_noti(access_token=access_token, message=message)

# need to test & refactor
# def run_alertbox(location_id, target_id, grade):
#     import requests
    
#     # send get curl
#     url = f"{config.get("alertbox", f"location_{location_id}")}/{target_id}?grade={grade}"
#     requests.get(url)

