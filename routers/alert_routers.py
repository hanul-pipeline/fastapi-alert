from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
import asyncio
from utils.alert_utils import *

router = APIRouter()

# test
def update_mysql_alert(data_received: dict):
    return update_mysql_alert(data_received)

def send_noti(data_received: dict):
    return send_noti(data_received)

@router.post('/alert/7/1', response_class=PlainTextResponse)
async def alert_7_1(data_received: dict):
    # 비동기적으로 두 함수를 실행
    task1 = asyncio.create_task(update_mysql_alert(data_received))
    task2 = asyncio.create_task(send_noti(data_received))

    # 두 함수의 실행이 끝날 때까지 기다림
    result1 = await task1
    result2 = await task2

    # 두 함수의 결과를 합칠 수도 있음
    combined_result = f"{result1}\n{result2}"

    return combined_result


# @router.post('/alert/7/2', response_class=PlainTextResponse)
# async def alert_7_2(data_received: dict):
#     return update_mysql_alert(data_received)

# @router.post('/alert/7/3', response_class=PlainTextResponse)
# async def alert_7_3(data_received: dict):
#     return update_mysql_alert(data_received)

# @router.post('/alert/7/4', response_class=PlainTextResponse)
# async def alert_7_4(data_received: dict):
#     return update_mysql_alert(data_received)

# @router.post('/alert/8/1', response_class=PlainTextResponse)
# async def alert_8_1(data_received: dict):
#     return update_mysql_alert(data_received)

# @router.post('/alert/10/2', response_class=PlainTextResponse)
# async def alert_10_2(data_received: dict):
#     return update_mysql_alert(data_received)

# @router.post('/alert/11/2', response_class=PlainTextResponse)
# async def alert_11_2(data_received: dict):
#     return update_mysql_alert(data_received)