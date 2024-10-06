import pymongo
import sys
from lightphe import LightPHE
# Restore data from database
cs = LightPHE(algorithm_name = "Exponential-ElGamal", key_file = "public.txt")


# Retrieve users data from the cloud
try:
  client = pymongo.MongoClient("mongodb+srv://simomaimashoaib3023:<password>@cluster0.plbjo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  
except pymongo.errors.ConfigurationError:
  print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
  sys.exit(1)

# use a database named "customerbalancetrialtwo"
db = client.Test
my_collection = db["customerbalancetrialtwo"]

# FIND DOCUMENTS
result = my_collection.find()
if result:    
  for doc in result:
    nid = doc['NID']
    print('User balance:')
    print(  cs.create_ciphertext_obj(doc['balance']).value)
else:
  print("No documents found.")



c1=(200972612941316741397144270532372320538732966506098159515903604622594468413606165967377025903485956410702246996123842898260644194580105352792178753974197, 1620787256405329844269630430247249180161213258441413326689940128158047311384676068295234803875269501649644935521377136085013579235484408460457746699549435)


c2=(3250871614751240594064954546479762413337106942999877278372984251717588013191363306589019835638836786540515506844781549016207038276126892047181080666143187, 6118640694078578131362029276666156663607941216315188549109070857412495420348695876689053755783723956525029325908978708569109553717332606855483575553641498)
c1=cs.create_ciphertext_obj(c1)
c2=cs.create_ciphertext_obj(c2)

print("c1")
print(c1)


print("c2")
print(c2)


# perfrom sum operation on the ciphers
print("sum")
c3=c1+c2
print(c3)
# send encrytped sum c3 to the client
# Cloud will not be able to decrypt the sum since it doesn't have the private key
print(cs.decrypt(c1+c2))
