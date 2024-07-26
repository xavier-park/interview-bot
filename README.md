# Interview Bot

This project is an interview preparation bot designed for entry-level data scientists. It uses similarity search and a language model (LLM) to generate responses that mimic past answers to interview questions.

## Overview

The bot leverages the following technologies:
- **CSVLoader** from `langchain_community.document_loaders` to load questions and answers from a CSV file.
- **FAISS** from `langchain_community.vectorstores` for efficient similarity search.
- **OpenAIEmbeddings** and **ChatOpenAI** from `langchain_openai` to embed documents and generate responses using OpenAI's GPT-4o-mini model.
- **PromptTemplate** from `langchain.prompts` to structure prompts for the LLM.

## Features

1. **Knowledge Embedding:** The bot processes questions and answers from a CSV file and stores them in a FAISS vector database for fast similarity search.
2. **Similarity Search:** The bot retrieves the most similar past answers to a given query using the FAISS vector database.
3. **LLM Chain:** The bot generates interview responses by combining similar past answers and using a language model to produce coherent and relevant answers.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/interview-bot.git
    cd interview-bot
    ```

2. **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**
    Create a `.env` file in the root directory and add your OpenAI API key:
    ```bash
    OPENAI_API_KEY=your_openai_api_key
    ```

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
