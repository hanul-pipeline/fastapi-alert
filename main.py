from fastapi import FastAPI
from routers import alert_routers

app = FastAPI()
app.include_router(alert_routers.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=17000)
