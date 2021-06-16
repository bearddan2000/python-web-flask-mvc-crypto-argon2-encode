from argon2 import PasswordHasher

class Encode:
    ph = PasswordHasher()

    def hash_password(self, password):
        return self.ph.hash(password)

    def verify(self, hash, password):
        try:
            return self.ph.verify(hash, password)
        except:
            return False
