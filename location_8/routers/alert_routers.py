from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils.alert_utils import *

router = APIRouter()

@router.post('/alert/8/7', response_class=PlainTextResponse)
async def alert_8_7(data_received: dict):
    data_received["location_id"] = 8
    data_received["sensor_id"] = 7
    
    return do_alert(data_received = data_received)

@router.post('/alert/8/8', response_class=PlainTextResponse)
async def alert_8_8(data_received: dict):
    data_received["location_id"] = 8
    data_received["sensor_id"] = 8
    
    return do_alert(data_received = data_received)

@router.post('/alert/8/9', response_class=PlainTextResponse)
async def alert_8_9(data_received: dict):
    data_received["location_id"] = 8
    data_received["sensor_id"] = 9
    
    return do_alert(data_received = data_received)
