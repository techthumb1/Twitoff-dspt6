import os
import basilica
from dotenv import load_dotenv

load_dotenv() # parse the .env file for environment variables
BASILICA_API_KEY = os.getenv("579a7484-3ec5-33f4-cd05-f72712c2590e")
connection = basilica.Connection(BASILICA_API_KEY)

#def basilica_api_client():
#    return basilica.Connection(BASILICA_API_KEY)

if __name__ == "__main__":
    print(type(connection)) #> <basilica.Connection object at 0x102081b10>
    sentences = ["Hello world!", "How are you?"]
    embeddings = connection.embed_sentences(sentences)
    print(list(embeddings))
