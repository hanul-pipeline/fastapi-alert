# fastapi-alert
센서에서 감지된 위험 신호를 전송받고 2차 대응을 하는 레포지토리입니다.

# information
'hanul/kafka-stream' 서버로부터 cURL request를 수신받아 경보 로직을 수행합니다.
<br>
- 위험 등급에 따라 관리자 및 직원에게 LINE NOTI 경보 전송
- 위험 등급에 따라 해당 위치의 경광등 및 버저 가동 - 미완성 -
<br><br>

# requirements
### apt
``` shell

```
### pip
``` shell
pip install fastapi "uvicorn[standard]" mysql-connector-python requests
```
