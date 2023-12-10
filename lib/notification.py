
# confirmed
def send_line_noti(access_token:str, message:str):
    import requests

    try:
        url = "https://notify-api.line.me/api/notify"
        headers = {"Authorization": f"Bearer {access_token}"}
        data = {"message" : message}
        response = requests.post(url, headers=headers, data=data)
        status = response
    
    except Exception as e:
        status = e

    return status


def send_line_noti_thread(access_token:str, message:str):
    from threading import Thread
    
    thread = Thread(target=send_line_noti, args=(access_token, message))
    thread.start()


# confirmed
def create_message(grade:str, time:str, location_name:str, type_name:str, information:dict):
    # create inspection message
    if grade == "inspection":
        safety_manager = information["safety_manager"]
        location_manager = information["employee"]
        message = f"""
[상황 알림]
{time} {location_name}에서 {type_name}상황 발생. 관리자께서는 해당 시설에 대한 점검 및 조치를 부탁드립니다.

[관리자 연락망]"""
        
        for person in safety_manager:
            message += f"\n안전 관리자 연락처: call:{person['phone_number']}"
        for person in location_manager:
            message += f"\n시설 관리자 연락처: call:{person['phone_number']}"

    # create evacuation message
    elif grade == "evacuation":
        address_building = information["building"]
        message = f"""
[재난 알림]
{time} {location_name}에서 {type_name}상황 발생. 침착하게 대피할 준비를 하시고, 주변인분들께 신속한 상황 전파 부탁드립니다.
        
[119] 
call:119

[도로명 주소]
{address_building}
        
[비상 연락망]
call:175-1234-5678"""

    return message


# test
if __name__ == "__main__":
    from configparser import ConfigParser

    config = ConfigParser()
    config.read("/Users/kimdohoon/git/fastapi-alert/config/config.ini")
    
    access_token = config.get("LINE", "access_token")

    # grade = "inspection"
    grade = "evacuation"
    time = "18:08:30"
    location_name = "우주선"
    type_name = "외계인 침공"
    information = {
        "building": "서울특별시 양천구 어딘가",
        "safety_manager": [{"access_token": access_token, "phone_number": "010-2740-3581"}],
        "employee": [{"access_token": access_token, "phone_number": "010-2740-3581"}]
    }

    message = create_message(grade=grade, time=time, location_name=location_name, type_name=type_name, information=information)
    status = send_line_noti(access_token=access_token, message=message)
    print(status)