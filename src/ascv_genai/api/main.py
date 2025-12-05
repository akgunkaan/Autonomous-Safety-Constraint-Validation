from fastapi import FastAPI

app = FastAPI(
    title="ASCV-GenAI API",
    description="API for the Autonomous Safety Constraint Validation - Generative AI Pipeline",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {"message": "Welcome to the ASCV-GenAI API"}

# Include routers from the routers directory
# from .routers import ingestion, query

# app.include_router(ingestion.router)
# app.include_router(query.router)

