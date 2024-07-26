# Interview Bot

This project is a chat bot that was placed on [my personal website](https://xavierpark.com). It uses similarity search and a language model (LLM) to generate responses that mimic my own written answers to common interview questions.

## Overview

The bot leverages the following technologies:
- **CSVLoader** from `langchain_community.document_loaders` to load questions and answers from a CSV file.
- **Facebook AI Similarity Search** (FAISS) from `langchain_community.vectorstores` for efficient similarity search.
- **OpenAIEmbeddings** and **ChatOpenAI** from `langchain_openai` to embed documents and generate responses using OpenAI's GPT-4o-mini model.
- **PromptTemplate** from `langchain.prompts` to structure prompts for the LLM.

## Features

1. **Knowledge Embedding:** The bot processes questions and answers from a CSV file and stores them in a FAISS vector database for fast similarity search.
2. **Similarity Search:** The bot retrieves the most similar past answers to a given query using the FAISS vector database.
3. **LLM Chain:** The bot generates interview responses by combining similar past answers and using a language model to produce coherent and relevant answers.

## Usage

1. **Load Questions and Answers:**
    Place your `questions_answers.csv` file in the root directory. Ensure it is formatted with questions and corresponding answers.

2. **Vectorize Questions and Answers:**
    The script will load the questions and answers from the CSV file and create embeddings using the OpenAI API.

3. **Run the Bot:**
    You can use the `generate_response` function to generate responses to interview questions.
    ```python
    from interview_bot import generate_response

    response = generate_response('Can you tell me about your experience at CHEQ?')
    print(response)
    ```

## Disclaimers

1. The system prompt in the `interviewer.py` file will likely differ from what is currently used on my portfolio website.

2. The questions and answers found in the provided `questions_answers.csv` should only be used as a guideline, and differ from what I am actually using.
   This is because I want to keep at least *some* of the information on my personal experiences to myself.

3. I used [this YouTube video](https://www.youtube.com/watch?v=c_nCjlSB1Zk&t=1s) from [AI Jason](https://www.youtube.com/@AIJasonZ) as a guide for this project. Many of the dependencies he used in that video were outdated at the time I wrote this bot, but some of the code may be derivative.
   
