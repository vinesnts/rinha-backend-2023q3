from email.mime import application
import falcon

# from core.middleware.auth import AuthMiddleware
from app.routes import Routes
from core.middleware.auth import AuthMiddleware


# Starts the falcon application
app = application = falcon.App()
# app = application = falcon.App(middleware=[
#     AuthMiddleware()
# ])

router = Routes(app)