# Crew AI with Ollama

#* Import libraries
from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew, Process

#* Declare llm model
llm = Ollama(model="mistral")

#* Query
query_1 = "I am satisfied with the serive and would like to subscribe to few of the services."
query_2 = "The service was very bad and the food quality was mediocre"
query_3 = "You have won $100,000,000. Click on the following link to claim!"

classifier = Agent(
    role="email classifier",
    goal="Analyse and acccurately classify emails based on the contents into one of the following: Review, Casual, Info requested, Spam",
    backstory="You are an expert AI system whose job is to analyse emails and correctly classify them.",
    verbose=True,
    allow_dlegation=False,
    llm=llm
)

responder = Agent(
    role="email responder",
    goal="Based on the importance of the email, write a concise and simple response.",
    backstory="You are an expert AI system whose job is to respond to emails in a concise and simple manner.",
    verbose=True,
    allow_dlegation=False,
    llm=llm
)

classify_email = Task(
    description=f"Classify the following email: {query_1}",
    agent=classifier,
    expected_output="One of these four options: Review, Casual, Info requested, Spam"
)

response_email = Task(
    description=f"Respond to the following email: {query_1}",
    agent=responder,
    expected_output="A concise and short response to the email."
)

crew = Crew(
    agents=[classifier, responder],
    tasks=[classify_email, response_email],
    verbose=2,
    process=Process.sequential
)

output = crew.kickoff()
print(output)
