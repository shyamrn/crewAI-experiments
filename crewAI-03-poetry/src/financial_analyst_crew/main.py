# Crew AI - App - v3.0

#* Import libararies
import os
from dotenv import load_dotenv

#* Load environmant variables
load_dotenv()

from financial_analyst_crew.crew import FinancialAnalystCrew

def run():
    inputs = {
        'company_name': 'Tesla'
    }
    
    FinancialAnalystCrew().crew().kickoff(inputs=inputs)

if __name__ == '__main__':
    run()
