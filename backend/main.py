from fastapi import FastAPI
from routes import company_lookup, job_scraper

app = FastAPI()

app.include_router(company_lookup.router)
app.include_router(job_scraper.router)

@app.get("/")
def root():
    return {"status": "JobHawk backend running"}
