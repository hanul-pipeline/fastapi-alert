import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, "../lib")

sys.path.append(lib_dir)


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
        send_line_noti(access_token=access_token, message=message)
  

# test
if __name__ == "__main__":
    pass