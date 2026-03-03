from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import logging
from ratelimit import RateLimitMiddleware

# Initialize FastAPI
app = FastAPI()

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Update with your allowed origins
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Rate limiting middleware
app.add_middleware(RateLimitMiddleware, rate_limit='100/hour')

@app.get("/status")
async def read_status():
    logger.info('Status endpoint called')
    return JSONResponse(content={"status": "Running"})

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    logger.info(f'Item requested: {item_id}')
    if item_id < 0:
        logger.error(f'Invalid item_id: {item_id}')
        raise HTTPException(status_code=400, detail="Item ID must be a non-negative integer.")
    return JSONResponse(content={"item_id": item_id, "name": f"Item {item_id}"})

@app.post("/items/")
async def create_item(item: dict):
    logger.info('Creating item')
    return JSONResponse(content={"message": "Item created successfully!", "item": item})

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logger.error(f'An error occurred: {exc}')
    return JSONResponse(content={"detail": "An unexpected error occurred."}, status_code=500)