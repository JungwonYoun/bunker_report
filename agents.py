import os
from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools



# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
'''
Creating Agents Cheat Sheet:
- Think like a boss, Work backwards from the goal and think which employee you need to hire to ge the job done.
- Define the Captain of the crew who orient the other agents towards the goal.
- Define which experts the captain needs to communicate with and delegate tasks to.

Build a top down structure of the crew.

Goal: 
- Create a 7-day travel itinerary with detailed per-day plans, including budget, packing suggestions, and safety tips.

Captain/Manager/Boss:
- Expert Travel Agent

EmployeesExperts to hire:
- City Selection Expert
- Local Tour Guide

Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume

'''

class BunkerAgents:
    def __init__(self):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            # model="llama3-70b-8192"
            model="llama3-8b-8192"
        )

        # self.llm = ChatOpenAI(
        #     model="crewai-llama3-8b",
        #     base_url="http://localhost:11434/v1",
        #     api_key="NA"
        # )

        # self.llm = ChatOpenAI(
        #     model="QuantFactory/Meta-Llama-3-8B-Instruct-GGUF",
        #     base_url="http://localhost:1234/v1",
        #     api_key="lm-studio"
        # )

        # self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        # self.llm = ChatOpenAI(model_name="gpt-4o", temperature=0.7)
        # self.Ollama = Ollama(model="openhermes")

    def expert_bunker_agent(self):
        return Agent(
            role="Expert Bunker Agent",
            backstory=dedent(f"""
                            Expert in bunker planning and research.
                            I have decades of experience making bunker analysis reports.
                            Especially, I have experience in container ship's bunker price and supply.
                            """),
            goal=dedent(f"""
                        Research various sources and predict bunker price which will be used in the weekly bunker report by the bunker report editor.
                        The contents will be including price trend, import news, regulation, supplier information, OPEC related information, WTI, BRENT, Dubai bunker oil spot price, weather conditions, coal price. etc.
                        """),
            tools=[
                SearchTools.search_internet, 
                CalculatorTools.calculate
                ],
            # allow_delegation=False,
            verbose=True,
            llm=self.llm,
            # llm=self.OpenAIGPT4,
        )

    def bunker_report_editor(self):
        return Agent(
            role="Bunker Report Editor",
            backstory=dedent(f"""
                            Expert at generating bunker reports based on the research by the expert bunker agent.
                            I have years of experience making bunker analysis reports.
                            I have experience in container ship's bunker price and supply under consideration global material prices.
                            """),
            goal=dedent(f"""
                        Generate contents for weekly bunker report.
                        The report will include price trend, importants news, regulation, supplier information, OPEC related information, WTI, BRENT, Dubai bunker oil spot price, weather conditions, forecasted bunker price in short term and long term.
                        When creating the contents, make is as detail as possible and include the source of the data together with the links.
                        """),
            tools=[
                SearchTools.search_internet
                ],
            # allow_delegation=False,
            verbose=True,
            llm=self.llm,
            # llm=self.OpenAIGPT35,
        )

    def bunker_report_designer(self):
        return Agent(
            role="Bunker Report Designer",
            backstory=dedent(f"""
                            Expert at generating bunker reports based on the contents by bunker report editor.
                            I have years of experience making bunker analysis reports.
                            I can generate markdown bunker report.
                            """),
            goal=dedent(f"""
                        Generate markdown bunker report.
                        The report will include price trend, importants news, regulation, supplier information, OPEC related information, WTI, BRENT, Dubai bunker oil spot price, weather conditions, forecasted bunker price in short term and long term.
                        Need to consider the report's content, structure and layout.
                        """),
            tools=[
                SearchTools.search_internet
                ],
            # allow_delegation=False,
            verbose=True,
            llm=self.llm,
            # llm=self.OpenAIGPT35,
        )