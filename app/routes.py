from core.settings import BASE_URL
from app.test.views import TestResource as test

class Routes:

  def __init__(self, app) -> None:
    app.add_route(f'{BASE_URL}/test', test())