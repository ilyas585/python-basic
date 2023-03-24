from fastapi import FastAPI

from views.users.views import user_router
from views.ping import ping_router

app = FastAPI()
app.include_router(user_router)
app.include_router(ping_router)
