def http_response(status_code, model):
    response = {
        # 200: {"model": ResultModel, "description": "OK"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
    }
    if str(status_code) == '200':
        response[200] = {"model": model, "description": "OK"}
    elif str(status_code) == '201':
        response[201] = {"model": model, "description": "Created"}
    return response
