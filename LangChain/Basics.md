### ChatModels : GPT,Gemini etc 

#### Parameters in Chat Models 

- Model  

- Temperature 

- Timeout 

- Max_tokens 

- Stop 

- Max_retries 

- Api_key 

- base_url 

- Rate_limiter 

 

#### Structured Outputs : 

Structured output in LangChain refers to generating LLM outputs in a predefined format (like a dictionary, JSON, or Pydantic model) using output parsers, making the data machine-readable and easy to work with. 

**Returning Structured Output**

**Using tool calling**

**Example**

from pydantic import BaseModel, Field 

class ResponseFormatter(BaseModel): 

    """Always use this tool to structure your response to the user.""" 

    answer: str = Field(description="The answer to the user's question") 

    followup_question: str = Field(description="A followup question the user could ask") 

 

from langchain_openai import ChatOpenAI model = ChatOpenAI(model="gpt-4o", temperature=0) 

#Bind responseformatter schema as a tool to the model 

model_with_tools = model.bind_tools([ResponseFormatter]) 

#Invoke the model 

ai_msg = model_with_tools.invoke("What is the powerhouse of the cell?") 

 

 

**JSON Mode**

**Example**

from langchain_openai import ChatOpenAI model = ChatOpenAI(model="gpt-4o").with_structured_output(method="json_mode") ai_msg = model.invoke("Return a JSON object with key 'random_ints' and a value of 10 random ints in [0-99]") ai_msg {'random_ints': [45, 67, 12, 34, 89, 23, 78, 56, 90, 11]} 

**Document Loaders** 

Document loaders are designed to load document objects. LangChain has hundreds of integrations with various data sources to load data from: Slack, Notion, Google Drive, etc. 

**PDFs:**

from langchain_community.document_loaders import PyPDFLoader 
 
loader = PyPDFLoader(file_path) 
pages = [] 
async for page in loader.alazy_load(): 
 pages.append(page) 

print(f"{pages[0].metadata}\n") 

print(pages[0].page_content) 

 

**Loading Web Pages:** 

Web pages contain text, images, and other multimedia elements, and are typically represented with HTML. They may include links to other pages or resources. For the "simple and fast" parsing, we will need langchain-community and 	the beautifulsoup4 library: 

 

**Example:**

import bs4 from langchain_community.document_loaders import WebBaseLoader 

page_url = "https://python.langchain.com/docs/how_to/chatbots_memory/" 

loader = WebBaseLoader(web_paths=[page_url]) docs = [] async for doc in loader.alazy_load(): docs.append(doc) 

assert len(docs) == 1 doc = docs[0] 

**Loading CSV files:**

 

from langchain_community.document_loaders.csv_loader import CSVLoader 

file_path = "../integrations/document_loaders/example_data/mlb_teams_2012.csv" 

loader = CSVLoader(file_path=file_path) data = loader.load() 

for record in data[:2]: print(record) 

 

**Loading HTML Data:**  

 

**(i)Using UnstructuredHTMLLoader:**

**Command** : pip install unstructured 

**Example** 

from langchain_community.document_loaders import UnstructuredHTMLLoader 

file_path = "../../docs/integrations/document_loaders/example_data/fake-content.html" 

loader = UnstructuredHTMLLoader(file_path) data = loader.load() 

print(data) 

 

**(ii)Using BeautifulSoup4**

**Command :** pip install bs4 

**Example :**

from langchain_community.document_loaders import BSHTMLLoader 

loader = BSHTMLLoader(file_path) data = loader.load() 

print(data) 

 

**Loading documents from a directory :**

**Example :**

from langchain_community.document_loaders import DirectoryLoader 

loader = DirectoryLoader("../", glob="**/*.md") docs = loader.load() len(docs) 

print(docs[0].page_content[:100]) 

 

**Loading JSON Data :** 

**Command :** pip install jq 

from langchain_community.document_loaders import JSONLoader 

import json from pathlib import Path from pprint import pprint 

file_path='./example_data/facebook_chat.json' data = json.loads(Path(file_path).read_text()) 

pprint(data) 

 

**Embedding :**

Embedding is a way of converting complex data (like words, images, or videos) into dense numerical vectors that capture their meaning, features, or relationships. 

**📌 Why we use embeddings:**

Machine learning models need numeric input 

Embeddings help models understand similarity and context 

**✅ Example:**

**Word Embedding:** 

“king” → [0.21, -0.42, 0.33, ...] 

“queen” → [0.24, -0.39, 0.35, ...] 

→ Vectors for related words are close together. 

**Embedding Model :**

An embedding model is a neural network trained to convert data into embeddings. 

**🔧 What it does:** 

Takes input (text, image, audio, etc.) 

Processes it with layers (CNNs, Transformers, etc.) 

Outputs a vector that captures essential meaning or structure 

**Type of Data**

**Model Examples** 



**Text** 

Word2Vec, BERT, OpenAI Embeddings 

NLP, chatbots, search 

**Image**

ResNet, CLIP, ViT 

Image search, tagging 

**Video** 

I3D, TimeSformer 

Action recognition, summaries 

**Audio**

Wav2Vec, Whisper 

Voice recognition, search 

 

 

**Measure Similarity :**

**Cosine Similarity :** Measures the cosine of the angle between two vectors. 

**Euclidean Distance:** Measures the straight-line distance between two points. 

**Dot Product :** Measures the projection of one vector onto another. 

 

The choice of similarity metric should be chosen based on the model. As an example, OpenAI suggests cosine similarity for their embeddings, which can be easily implemented: 

 

**Vector Stores :** 

Vector stores are specialized data stores that enable indexing and retrieving information based on vector representations. These vectors, called embeddings, capture the semantic meaning of data that has been embedded. 

**The key methods are:**

**add_documents:** Add a list of texts to the vector store. 

**delete:** Delete a list of documents from the vector store. 

**similarity_search:** Search for similar documents to a given query. 

 

**Retrievers :**

 

Vector stores are a powerful and efficient way to index and retrieve unstructured data. A vectorstore can be used as a retriever by calling the as_retriever() method. 

 

vectorstore = MyVectorStore() 

retriever = vectorstore.as_retriever() 

 

**Text Splitters :** 

 

Text splitters split documents into smaller chunks for use in downstream applications. 

 

**Length Based :** 

 

The most intuitive strategy is to split documents based on their length. 

 

Token-based: Splits text based on the number of tokens, which is useful when working with language models. 

Character-based: Splits text based on the number of characters, which can be more consistent across different types of text. 

 

**Example :**

from langchain_text_splitters import CharacterTextSplitter  

text_splitter = CharacterTextSplitter.from_tiktoken_encoder( encoding_name="cl100k_base", chunk_size=100, chunk_overlap=0 )  

texts = text_splitter.split_text(document) 

**Text-structured based :** 

Tries to split on sentences, then paragraphs, then characters — more natural 

**Example :**

from langchain_text_splitters import RecursiveCharacterTextSplitter  

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)  

texts = text_splitter.split_text(document) 

 

 

 

 


 
