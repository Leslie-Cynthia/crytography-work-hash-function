import hashlib
class hashit:
    def hashing(self,texte,hash_type):
        texte=texte.encode('utf-8') # for the encodage
        hash_1=hashlib.new(hash_type) #the type of the hash
        hash_1.update(texte)
        return hash_1.hexdigest() # final encodage

