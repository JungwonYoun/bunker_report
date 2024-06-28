import os
from crewai import Crew
from textwrap import dedent
from agents import BunkerAgents
from tasks import BunkerTasks
from dotenv import load_dotenv
load_dotenv()

class BunkerCrew:
    def __init__(self, region, period_range, grade):
        self.region = region
        self.period_range = period_range
        self.grade = grade

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = BunkerAgents()
        tasks = BunkerTasks()

        # Define your custom agents and tasks here
        expert_bunker_agent = agents.expert_bunker_agent()
        bunker_report_editor = agents.bunker_report_editor()
        bunker_report_designer = agents.bunker_report_designer()

        # Custom tasks include agent name and variables as input
        bunker_market_research = tasks.bunker_market_research(
            expert_bunker_agent,
            self.region,
            self.period_range,
            self.grade,
        )

        predicting_bunker_trend = tasks.predicting_bunker_trend(
            bunker_report_editor,
            self.region,
            self.period_range,
            self.grade,
        )

        generating_bunker_report = tasks.generating_bunker_report(
            bunker_report_designer,
            self.region,
            self.period_range,
            self.grade,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_bunker_agent,
                    bunker_report_editor,
                    bunker_report_designer],
            tasks=[bunker_market_research, 
                    predicting_bunker_trend, 
                    generating_bunker_report],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
  print("## Welcome to Bunker Reporting Crew")
  print('-------------------------------')
  region = input(
    dedent("""
      Which region are you interest for bunker reporting?
    """))
  period_range = input(
    dedent("""
      What is the period range you are interested for bunker reporting?
    """))
  grade = input(
    dedent("""
      What is the grade you are interested for bunker reporting?
    """))
  
  bunker_crew = BunkerCrew(region, period_range, grade)
  result = bunker_crew.run()
  print("\n\n########################")
  print("## Here is you Bunker Report")
  print("########################\n")
  print(result)
