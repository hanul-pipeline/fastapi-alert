from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils.alert_utils import *

router = APIRouter()

# confirmed
@router.post('/alert/4/1', response_class=PlainTextResponse)
async def alert_4_1(data_received: dict):
    data_received["location_id"] = 4
    data_received["sensor_id"] = 1
    
    return do_alert(data_received = data_received)

@router.post('/alert/4/2', response_class=PlainTextResponse)
async def alert_4_2(data_received: dict):
    data_received["location_id"] = 4
    data_received["sensor_id"] = 2
    
    return do_alert(data_received = data_received)
