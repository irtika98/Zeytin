### Introduction
**Zeytin** is my personal AI assistant I created for my Robotics course to interact with my e-book. The knowledge base for the assistant is **Introduction to Robotics: Mechanics and Control (3rd Edition)** by John J. Craig. Zeytin fetches precise topics and page numbers from the book, and provides curated responses, letting me focus on learning without the hassle of manual searching the book. 
### High Level Design

![architecture ](https://github.com/irtika98/Zeytin/blob/512aebd66d3e0c5eccd1ac205eba6409e310b8af/HLD.png)

### Tech stacks

1. Backend : Django
2. Database : SQlite
3. Vector Database : Pinecone
4. LLM : OpenAI

### Installation

## 1. Clone the repository

```bash
    git clone https://github.com/irtika98/Zeytin.git

```

## 2. Install dependencies

# If you don't have poetry, run this:
```bash
    pip install poetry
```

# Install dependencies
```bash
    poetry install
```

## 3. Update OpenAI API Key in .env file
```bash
    OPENAI_API_KEY='<YOUR_KEY>'
```

## 4. Run the Django server
```bash
    python manage.py runserver
```

## 5. Access the app
Once the server is up, open your browser and navigate to:
```bash
    http://127.0.0.1:8000/register
```

## 6. Register!
Register yourself.



