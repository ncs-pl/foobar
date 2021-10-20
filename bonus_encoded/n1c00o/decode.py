from base64 import b64decode
from itertools import cycle

message = "FU4QGg8CFgMSUkwOFRNXQgsIF0hAQVQTDhkAUVRTRVVJSVlPSwQABAQQAVFRExwQSQwFCQMTBwNG VVYUEl1eUxwMBwYODRZXTVVLVVZcWVUYDA4KAhVUUFtVS0FbWF9TBQwHSEBBVAIAFw5dQUcXEFRJ RBwNBxZXTVVLUlpbFxBUSUQYBQ9SVxw="

key = input("key for decode: ")
for m, k in zip(b64decode(message), cycle(key)):
    print(chr(m ^ ord(k)), end="")
print()
