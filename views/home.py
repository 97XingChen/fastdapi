from fastapi import Request, Form


async def home(request: Request, id: str):
    return request.app.state.views.templates.get_template("index.html").render({"request": request, "id": id})


async def reg_page(req: Request):
    """
    注册页面
    :param req:
    :return:html
    """
    return req.app.state.views.templates.get_template("index.html").render({"request": req})


async def result_page(req: Request, usernmae: str = Form(...),password:str = Form(...)):
    """
    注册结果页面
    :param usernmae:
    :param req:
    :return:html
    """
    return req.app.state.views.templates.get_template("index.html").render({"request": req})
