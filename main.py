import tornado.ioloop
import tornado.locks
import tornado.options
import tornado.web


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', 'handlers.HomeHandler'),
        ]
        settings = {
            'debug': True,
        }
        super().__init__(handlers, **settings)


async def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(8000)

    shutdown = tornado.locks.Event()
    await shutdown.wait()


if __name__ == '__main__':
    ioloop = tornado.ioloop.IOLoop.current()
    ioloop.run_sync(main)
