# CrewAI Experiment - 02

#* Import libarraies
from crewai import Agent, Task, Process, Crew
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv

#* Load environment variables
load_dotenv()

#* Declare llm model
llm = Ollama(model='llama2')

#* Query
query_1 = """
I need a new member in my AI team.
The person should be capable of critical thinking and should understand business.
The person should know technology enough to convert business requirements into technology solutions.
The person should closely work with business and technology team.
"""

query_2 = """
I need a new member in my AI team.
The person should be capable of writing python codes and should be familiar with AI frameworks.
The person should be able to develop POCs faster to gain confidence of business teams.
The person should closely work with cloud and architect team to deploy the solutions in multiple ways.
"""

query_3 = """
I need a new member in my AI team.
The person should be capable of writing python codes and should be familiar with AI frameworks.
The person should be able to develop robust AI systems and be able to perform continuous improvement on the same.
The person should closely work with cloud and architect team to deploy the solutions in multiple ways.
"""

#* Define agents
talent_role_advisor = Agent(
    role="Talent Role Advisor",
    goal=f"Generate a role name based on the requirement provided by the user.",
    backstory="You are an expert talent acquisition role advisor who is capable of suggesting appropriate roles based on a high level requirement from various teams.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

talent_requirement_advisor = Agent(
    role="Talent Requirement Advisor",
    goal=f"Generate a set of expected skill requirements for the role generated by 'talent_role_advisor' based on the requirement provided by the user.",
    backstory="You are an expert talent acquisition requirement advisor who is capable of suggesting appropriate set of skill requirements for specific roles.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

talent_work_allocation_advisor = Agent(
    role="Talent Work Allocation Advisor",
    goal=f"Generate a set of expected list of work/job description for the role generated by 'talent_role_advisor' based on the requirement provided by the user.",
    backstory="You are an expert talent acquisition work allocation advisor who is capable of suggesting appropriate set list of work/job description for specific roles.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

#* Declare tasks
task_generate_role = Task(
    description=f"Generate a role for the following requirement: {query_3}",
    agent=talent_role_advisor,
    expected_output="Any role that is relevant to the requirement such as Consultant, Business Analyst, Engineer, Product Owner etc."
)

task_generate_requirement = Task(
    description=f"Generate a list of skill requirements for the role generated for following requirement: {query_3}",
    agent=talent_requirement_advisor,
    expected_output="List of expected skills for the role based on the user requirement."
)

task_generate_work_allocation = Task(
    description=f"Generate a list of work/job description for the role generated for following requirement: {query_3}",
    agent=talent_requirement_advisor,
    expected_output="List of expected skills for the role based on the user requirement."
)

#* Define crew
crew = Crew(
    agents=[talent_role_advisor, talent_requirement_advisor, talent_work_allocation_advisor],
    tasks=[task_generate_role, task_generate_requirement, task_generate_work_allocation],
    verbose=2,
    process=Process.sequential
)

output = crew.kickoff()
print(output)