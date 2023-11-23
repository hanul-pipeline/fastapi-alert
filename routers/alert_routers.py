from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils.alert_utils import *

router = APIRouter()

# confirmed
@router.post('/alert/7/2', response_class=PlainTextResponse)
async def alert_7_2(data_received: dict):
    return do_alert(data_received)

@router.post('/alert/7/3', response_class=PlainTextResponse)
async def alert_7_3(data_received: dict):
    return do_alert(data_received)

@router.post('/alert/7/4', response_class=PlainTextResponse)
async def alert_7_4(data_received: dict):
    return do_alert(data_received)

@router.post('/alert/8/1', response_class=PlainTextResponse)
async def alert_8_1(data_received: dict):
    return do_alert(data_received)

@router.post('/alert/10/2', response_class=PlainTextResponse)
async def alert_10_2(data_received: dict):
    return do_alert(data_received)

@router.post('/alert/11/2', response_class=PlainTextResponse)
async def alert_11_2(data_received: dict):
    return do_alert(data_received)