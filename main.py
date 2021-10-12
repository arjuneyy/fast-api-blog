import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from domain.model.exception import BaseException
from presentation import article


app = FastAPI()
app.include_router(article.router)


# Error handler
@app.exception_handler(BaseException)
def exception_handler(request: Request, exc: BaseException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.code,
        content={'message': exc.message})


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=5000,
                log_level='info', reload=True)
