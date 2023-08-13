from app.pessoa.views import Pessoa, ContagemPessoa
from core.settings import BASE_URL

class Routes:

  def __init__(self, app) -> None:
    # Pessoa
    app.add_route(f'{BASE_URL}/pessoas/{{id}}', Pessoa())
    app.add_route(f'{BASE_URL}/pessoas', Pessoa())
    app.add_route(f'{BASE_URL}/contagem-pessoas', ContagemPessoa())