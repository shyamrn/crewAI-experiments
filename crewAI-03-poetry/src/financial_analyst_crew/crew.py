# Crew AI - v3.0

#* Import libararies
from crewai import Agent, Task, Process, Crew
from crewai.project import CrewBase, agent, task, crew
from langchain_groq import ChatGroq
from langchain_community.llms import Ollama

#* Define crew base
@CrewBase
class FinancialAnalystCrew():
    """FinancialAnalystCrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self) -> None:
        self.ollama_llm = Ollama(model='mistral')
    
    @agent
    def company_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['company_researcher'],
            llm=self.ollama_llm
        )
    
    @agent
    def company_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['company_analyst'],
            llm=self.ollama_llm
        )
        
    @task
    def research_company_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_company_task'],
            agent=self.company_researcher()
        )
        
    @task
    def analyze_company_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_company_task'],
            agent=self.company_analyst()
        )
    
    @crew
    def crew(self) -> Crew:
        """Create the FinancialAnalystCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2
        )