from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Vectorize my questions/answers
loader = CSVLoader(file_path="questions_answers.csv")
documents = loader.load()

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(documents, embeddings)

# Similarity search
def retrieve_info(query):
    similar_response = db.similarity_search(query, k=3)

    array_answers = [doc.page_content for doc in similar_response]

    return array_answers

# results = retrieve_info()
# print(results)

# LLMChain
llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

template = """
You are an exceptional entry-level data scientist preparing for an interview. Your interviewer will ask you a question, and you will provide the best answer that you can give based on your past answers and experiences. Please follow these guidelines:

    The response should be very similar or even identical to my past answers in terms of length, tone of voice, logical arguments, and other details.
    If the past answer is irrelevant, mimic the style and approach of my past answers to respond to the interviewer's question.

Below is the question you received from the interviewer:
{question}

Here are examples of best answers to similar questions in past interviews:
{best_answers}

Write your best response to this interviewer:
"""

prompt = PromptTemplate(
    input_variables=["question","best_answers"],
    template = template
)

chain = prompt | llm


# 4. Retrieval augmented generation
def generate_response(question):
    best_answers = retrieve_info(question)
    response = chain.invoke({"question":question, "best_answers":best_answers})
    return response.content

# gen_ans = generate_response('Can you tell me about your experience at CHEQ?')

# print(gen_ans.content)