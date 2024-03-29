from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils.alert_utils import *

router = APIRouter()

@router.post('/alert/7/3', response_class=PlainTextResponse)
async def alert_7_3(data_received: dict):
    data_received["location_id"] = 7
    data_received["sensor_id"] = 3
    
    return do_alert(data_received = data_received)

@router.post('/alert/7/4', response_class=PlainTextResponse)
async def alert_7_4(data_received: dict):
    data_received["location_id"] = 7
    data_received["sensor_id"] = 4
    
    return do_alert(data_received = data_received)

@router.post('/alert/7/5', response_class=PlainTextResponse)
async def alert_7_5(data_received: dict):
    data_received["location_id"] = 7
    data_received["sensor_id"] = 5
    
    return do_alert(data_received = data_received)

@router.post('/alert/7/6', response_class=PlainTextResponse)
async def alert_7_6(data_received: dict):
    data_received["location_id"] = 7
    data_received["sensor_id"] = 6
    
    return do_alert(data_received = data_received)