from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.transfers import router as transfers_router

app = FastAPI(title="Tolveris Launchpad API", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"], allow_methods=["*"], allow_headers=["*"])
app.include_router(transfers_router)

@app.get("/health")
def health(): return {"status": "ok", "ledger": "simulated"}
