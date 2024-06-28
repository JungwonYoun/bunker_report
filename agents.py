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
            role="Expert Bunker Analyst",
            backstory=dedent(f"""
                            I am a highly experienced bunker fuel analyst with over 20 years of expertise in the maritime fuel industry.
                            My specialization lies in data analysis, market research, and predictive modeling for global bunker fuel markets.
                            I have an extensive track record of collecting and analyzing complex data sets to identify market trends and make accurate price forecasts.
                            My expertise covers various types of marine fuels, including VLSFO, MGO, and emerging alternative fuels.
                            I stay up-to-date with the latest industry trends, regulatory changes, and technological advancements affecting the bunker fuel market.                
                            """),
            goal=dedent(f"""
                        To conduct in-depth research and analysis of the bunker fuel market, providing raw data, analytical insights, and price predictions. My responsibilities include:
                        1. Collecting and analyzing data on current and historical bunker fuel prices across major global ports.
                        2. Monitoring and analyzing supply and demand dynamics in key bunkering hubs.
                        3. Tracking crude oil markets (WTI, Brent, Dubai) and assessing their influence on bunker prices.
                        4. Researching and summarizing regulatory updates (e.g., IMO 2020, upcoming environmental regulations).
                        5. Gathering detailed supplier information and market competition data in major ports.
                        6. Analyzing OPEC+ decisions and their potential effects on the bunker market.
                        7. Studying correlations between bunker prices and other energy commodities (e.g., coal, natural gas).
                        8. Monitoring weather patterns and assessing potential supply chain disruptions.
                        9. Researching emerging trends in alternative fuels and their market penetration.
                        10. Developing short-term and long-term price forecasts based on comprehensive data analysis.
                        11. Preparing detailed analytical reports with raw data, charts, and preliminary findings for the Bunker Report Editor.
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
                            I am a seasoned bunker report editor with over 15 years of experience in the maritime and energy sectors.
                            My expertise lies in synthesizing complex market data and analysis into clear, concise, and insightful reports.
                            I have a talent for translating technical information into accessible content for a wide range of industry stakeholders.
                            My reports are known for their strategic insights, clear narrative, and actionable recommendations.
                            I have a deep understanding of the industry's information needs and how to present data in the most impactful way.
                            """),
            goal=dedent(f"""
                        To produce a comprehensive and insightful weekly bunker report based on the analysis provided by the Expert Bunker Analyst. My responsibilities include:
                        1. Reviewing and interpreting the raw data and analytical insights provided by the Expert Bunker Analyst.
                        2. Crafting a coherent narrative that explains current market conditions and future trends.
                        3. Highlighting the most critical information and its potential impact on different stakeholders in the industry.
                        4. Translating complex data and analysis into clear, actionable insights for readers.
                        5. Structuring the report in a logical and easy-to-follow format, including executive summaries and detailed sections.
                        6. Adding context and industry perspective to the analytical findings.
                        7. Ensuring the report covers all key areas: price trends, market news, regulatory updates, supplier information, and forecasts.
                        8. Creating visually appealing charts, graphs, and tables to illustrate key points.
                        9. Providing strategic recommendations based on the analyzed data and market trends.
                        10. Ensuring the report's language is polished, professional, and free of errors.
                        11. Adding relevant citations and references to maintain the report's credibility.
                        12. Tailoring the content to meet the needs of various readers, from ship operators to fuel suppliers and financial analysts.
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
                            I am a seasoned bunker report editor with over 15 years of experience in the maritime and energy sectors.
                            My expertise lies in synthesizing complex market data and analysis into clear, concise, and insightful reports.
                            I have a deep understanding of global shipping trends, energy markets, and their interconnections.
                            My reports are widely respected in the industry for their accuracy, depth, and forward-looking insights.
                            I have a knack for identifying key trends and presenting them in a way that's accessible to both industry experts and newcomers.
                            """),
            goal=dedent(f"""
                        To produce a comprehensive weekly bunker report that provides valuable insights for maritime industry stakeholders. The report will:
                        1. Analyze and present current and forecasted bunker prices for major fuel types (VLSFO, MGO, HFO) in key global ports.
                        2. Provide short-term (1-4 weeks) and long-term (3-6 months) price forecasts with clear reasoning.
                        3. Highlight critical market moving news and assess their potential impact on bunker markets.
                        4. Summarize relevant regulatory updates and their implications for fuel buyers and suppliers.
                        5. Offer detailed supplier information, including changes in market share and pricing strategies in major bunkering hubs.
                        6. Analyze OPEC+ decisions and crude oil market trends (WTI, Brent, Dubai), explaining their effects on bunker prices.
                        7. Examine correlations between bunker prices and other relevant commodities (e.g., coal, natural gas).
                        8. Assess how current and forecasted weather conditions might affect bunker supply chains and pricing.
                        9. Include expert commentary on emerging trends, such as alternative fuels and technological advancements in the shipping industry.
                        10. Provide all data sources, including links to original reports or data sets, ensuring transparency and credibility.
                                    """),
            tools=[
                SearchTools.search_internet
                ],
            # allow_delegation=False,
            verbose=True,
            llm=self.llm,
            # llm=self.OpenAIGPT35,
        )