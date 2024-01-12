
def create_message(grade:str, insert_date:str, location_name:str, alert:str, information:dict):
    # create inspection message
    if grade == "inspection":
        safety_manager = information["safety_manager"]
        location_manager = information["employee"]
        message = f"""
[상황 알림]
{insert_date} {location_name}에서 {alert}상황 발생. 관리자께서는 해당 시설에 대한 점검 및 조치를 부탁드립니다.

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
{insert_date} {location_name}에서 {alert}상황 발생. 침착하게 대피할 준비를 하시고, 주변인분들께 신속한 상황 전파 부탁드립니다.
        
[119] 
call:119

[도로명 주소]
{address_building}
        
[비상 연락망]
call:175-1234-5678"""

    return message

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

# test
if __name__ == "__main__":
    pass