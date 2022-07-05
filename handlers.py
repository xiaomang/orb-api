import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    """ HTTP请求处理程序的基类 """
    pass


class HomeHandler(BaseHandler):
    """ 首页 """

    async def get(self):
        self.write({'status': 'running'})
