from hash_function import hashit
import hashlib

while True:
    texte=str(input('insert your text ')) # we take the text the user wants to hash
    hash_disponible=hashlib.algorithms_available
    print(hash_disponible) # swhow all the hash type possible
    while texte=='':
        print('please put a text ')
        texte = str(input('write your text: '))

    
    # for the hash_type
    hash_type=str(input('choose a hash-type: '))
    while hash_type=='' or hash_type not in hash_disponible:
        print('please choose the hash_type: ')
        hash_type=str(input('choose a hash_type: '))
    
    if hash_type=='shake_256' or hash_type=='shake_128':
        
        # for the length
        length=int(input('write the willing length of the hash function '))
        while length<=0:
            print('insert a valid length ')
            length=int(input('new length: '))
        
        texte=texte.encode('utf-8') # for the encodage
        hash_1=hashlib.new(hash_type) #the type of the hash
        hash_1.update(texte)
        print('the hash function is : ',hash_1.hexdigest(length))
    else:
        # doing the hash function
        Hash=hashit() # we put our class hashit in the variable hash so that his use will be easier
        result_hash=Hash.hashing(texte,hash_type)
        print(result_hash)
    
    break
    
