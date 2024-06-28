# coding: utf-8

"""
    Galang Suara API

    Documentation Galang Suara API v0.1
"""

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

from app.routers.member_router import router as MemberRouter

app = FastAPI(
    title="EIGEN API",
    description="Documentation EIGEN API v0.1",
    version="0.1",
    swagger_ui_parameters={"operationsSorter": "method"}
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    # print(exc.body)
    return PlainTextResponse(str(exc), status_code=422)


app.include_router(MemberRouter)