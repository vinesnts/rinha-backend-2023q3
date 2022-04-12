import os
import hashlib
import base64

class PasswordUtils:

    algorithm = 'sha256'
    iterations = 100000

    def encode(self, password) -> tuple:
        key = os.urandom(64)
        password  = str(password).encode('utf-8')

        hash = hashlib.pbkdf2_hmac(
            self.algorithm,
            password,
            key,
            self.iterations
        )

        hash = base64.b64encode(hash).decode('ascii').strip()
        key = base64.b64encode(key).decode('ascii').strip()
        return hash, key

    def verify(self, password, key, encoded) -> bool:
        key = base64.b64decode(str(key).encode('ascii'))
        password  = str(password).encode('utf-8')

        hash = hashlib.pbkdf2_hmac(
            self.algorithm,
            password,
            key,
            self.iterations
        )

        hash = base64.b64encode(hash).decode('ascii').strip()

        return hash == encoded