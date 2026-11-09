from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import try_conn

app = FastAPI()
app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost:5173"],
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
def root():
    # tests if backend can be reached, and also can connect to the db
    return {"message": f"Hello we are Team Hot Honey! {try_conn()}"}
