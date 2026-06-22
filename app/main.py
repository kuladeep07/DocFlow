import uvicorn
from fastapi import FastAPI

from app.api.documents import documents_router
from app.db.base import Base
from app.db.session import engine

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(documents_router)

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)