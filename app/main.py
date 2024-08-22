from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


from app.config import settings
# from app.database import BaseModel, engine
from app.deposit.router import router as deposit_router
from app.deposit.schemas import ErrorDepositResponse



@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Async context manager for startup and shutdown lifecycle events.
    - Creates database tables.
    - Sets up bot commands and webhook.

    Yields control during application's lifespan and performs cleanup on exit.
    - Disposes all database connections.
    - Deletes bot webhook and commands.
    - Closes aiohttp session
    """ 

    yield

    # # When an appliction is created
    # async with engine.begin() as connection:
    #     # Create tables
    #     await connection.run_sync(BaseModel.metadata.create_all)
    # try:
    #     yield
    # finally:
    #     await engine.dispose()


application = FastAPI(title="MA_test", lifespan=lifespan)
application.include_router(deposit_router, prefix=settings.api_prefix)

# Custom error handler for validation error. Works for the whole application
@application.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Create custom error message
    error_details = exc.errors()[0]
    loc = error_details.get('loc', [])
    msg = error_details.get('msg', '')
    field = loc[-1] if len(loc) > 1 else 'unknown field'
    
    clean_msg = msg.replace('Value error,', '').strip()
    error_message = f'Field "{field}". {clean_msg}'

    return JSONResponse(
        status_code=400,
        content=ErrorDepositResponse(error=error_message).model_dump()
    )
