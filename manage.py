import sys
import os

def args_to_dict(args):
    args = args[1:]
    args_dict = {}
    for arg in args:
        arg = arg.split('=')
        args_dict[arg[0]] = arg[1] if len(arg) > 1 else None

    return args_dict

if __name__ == '__main__':
  args = args_to_dict(sys.argv)
  if args['view'] in os.listdir('./app/'):
    print('View já existe')
  else:
    captalize = ''.join([w[0].upper() + w[1:] for w in args['view'].split('_')])
    os.mkdir(f'./app/{args["view"]}')
    with open(f'./app/{args["view"]}/views.py', 'w') as file:
      file.write(f'''import falcon

class {captalize}:

  def on_get(self, req, resp):
    pass

  def on_post(self, req, resp):
    pass

  def on_patch(self, req, resp):
    pass

  def on_delete(self, req, resp):
    pass''')
    with open(f'./app/{args["view"]}/queries.py', 'w') as file:
      file.write('')

    with open(f'./app/{args["view"]}/__init__.py', 'w') as file:
      file.write('')
    with open(f'./app/routes.py', 'r+') as file:
      content = file.read()
      file.seek(0)
      file.write(f'''from app.{args['view']}.views import {captalize}
{content}

    # {captalize}
    app.add_route(f'{{BASE_URL}}/{args['view'].replace('_', '-')}', {captalize}())''')