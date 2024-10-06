
import pymongo
import sys
from lightphe import LightPHE
# encryption
# provided Algorithms by the library
algorithms = [
  "RSA",
  "ElGamal",
  "Exponential-ElGamal",
  "Paillier",
  "Damgard-Jurik",
  "Okamoto-Uchiyama",
  "Benaloh",
  "Naccache-Stern",
  "Goldwasser-Micali",
  "EllipticCurve-ElGamal"
]

cs = LightPHE(algorithm_name = algorithms[0])
# generate private-public key pair
cs = LightPHE(algorithm_name = "Exponential-ElGamal")

# export public key to build same cryptosystem with only public key in the cloud
# cs.export_keys(target_file = "public.txt", public = True)

# export private key to build same cryptosystem on-prem later
# cs.export_keys(target_file = "private.txt", public = False)

# Add users data

# user one
userNID = 203023
balance=100
user2NID = 202020
balance2= 200

# calculate ciphertexts of the values
# balance of user 1

c1 = cs.encrypt(balance).value 
c1id=cs.encrypt(userNID).value

# balance of user 2
c2 = cs.encrypt(balance2).value
c2id=cs.encrypt(user2NID).value





# convert cipher texts to ciphertext_object
# send c1 and c2 pair to a cloud system
c1=cs.create_ciphertext_obj(c1)
c2=cs.create_ciphertext_obj(c2)
print("c1")
print(c1)
print("c2")
print(c2)


# This section is extra 
print('encrypted sum')
print(c1+c2)
print(cs.decrypt(c1+c2))



# Insert encrypted users data in the cloud
try:
  client = pymongo.MongoClient("mongodb+srv://simomaimashoaib3023:<databasePassword>@cluster0.plbjo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  
# return a friendly error if a URI error is thrown 
except pymongo.errors.ConfigurationError:
  print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string? or internet connection error")
  sys.exit(1)

# use a database named "myDatabase"
db = client.Test

# use a collection named ""
my_collection = db["customerbalancetrialtwo"]
values = [
                    { "NID": str(c1id), "balance":str(c1)},
                    { "NID": str(c2id), "balance":str(c2)},              
                   ]

# # drop the collection in case it already exists
# try:
#   my_collection.drop()  

# # return a friendly error if an authentication error is thrown
# except pymongo.errors.OperationFailure:
#   print("An authentication error was received. Are your username and password correct in your connection string?")
#   sys.exit(1)
try: 
 result = my_collection.insert_many(values)

# return a friendly error if the operation fails
except pymongo.errors.OperationFailure:
  print("An authentication error was received. Are you sure your database user is authorized to perform write operations?")
  sys.exit(1)
else:
  inserted_count = len(result.inserted_ids)



