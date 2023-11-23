import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, "../lib")

sys.path.append(lib_dir)


# confirmed
def update_mysql_alert(dictionary:dict):
    from database import mysql_conn

    # open connector
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


# confirmed
def send_noti(dictionary:dict):
    from database import return_informations
    from notification import send_line_noti, create_message

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
        send_line_noti(access_token=access_token, message=message)
        

def do_alert(dictionary:dict):
    from time import time
    start_time = time()
    update_mysql_alert(dictionary=dictionary)
    send_noti(dictionary=dictionary)
    end_time = time()
    print(end_time - start_time)

# test
if __name__ == "__main__":
    dict = {
        "grade": "inspection",
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

    update_mysql_alert(dict)
    send_noti(dict)