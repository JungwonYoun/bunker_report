from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py

'''
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Delelope a detailed itinerary, including city selection, attractions, and practical travel advice.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
- A detailed 7 day travel itinerary.

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
- Itnerary Planning: develop a detailed plan for each day of the trip.
- City Selection: Analyze and pick the best cities to visit.
- Local Tour Guide: Find a local expert to provide insights and recommendations.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.


4. Task Description Template:
- Use this template as a guide to define each task in your CrewAI application.
- This template helps ensure that each task is clearly defined, actiionable, and alighed with the desired outcome.

Template:
---------
def [task_name](self, agent, [parameters]):
    return Task(description=dedent(f"""
    **Task**: [Provide a concise name or summary of the task.]
    **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outputs.]
    **Parameters**:
    - [Parameter 1]: [Description of the parameter 1.]
    - [Parameter 2]: [Description of the parameter 2.]
    - [Parameter 3]: [Description of the parameter 3.]
    **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tops, addtional tasks, or awards.]
    """), agent=agent)
'''

class BunkerTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $100,000 bonus!"

    def bunker_market_research(self, agent, region, period_range, grade):
        return Task(
            description=dedent(
                f"""
                **Task**: Understanding bunker market for the region / grade / period

                **Description**: 
                Research various sources and predict bunker price which will be used in the weekly bunker report by the bunker report editor for the Region, Grade, Period.
                The contents will be including price trend, import news, regulation, supplier information, OPEC related information, WTI, BRENT, Dubai bunker oil spot price, weather conditions, coal price. etc.
                You MUST research actual data, actual news, and actual bunker information what are valid for the Region, Grade, and Period.

                **Parameters**:
                - Region: {region}
                - Period Range: {period_range}
                - Grade: {grade}

                **Note**: {self.__tip_section()}
                """
                ), 
            agent=agent,
            expected_output="Detailed report on the chosen data for the Region, Grade, and Period"
            )


    def predicting_bunker_trend(self, agent, region, period_range, grade):
        return Task(
            description=dedent(
                f"""
                **Task**: Predicting bunker trend for region / grade / period

                **Description**: 
                Analyze and the results of research. Predict the bunker price trend for the Region, Grade, and Period.
                This task involves comparing multiple bunker prices, considering factors like current weather conditions, upcoming seasonal events, and overall bunker supply circumstances.
                Your final answer must be a detailed report on the chosen data for the Region, Grade, and Period, including actual bunker price, weather forecast, and market trends.
                Predict the bunker price upto next 30 days for the Region, and Grade.
                You MUST use actual data, actual news, and actual bunker information what are valid for the Region, Grade, and Period.

                **Parameters**:
                - Region: {region}
                - Period Range: {period_range}
                - Grade: {grade}

                **Note**: {self.__tip_section()}
                """
                ), 
            agent=agent,
            expected_output="Detailed report on the chosen data for the Region, Grade, and Period"
            )


    def generating_bunker_report(self, agent, region, period_range, grade):
        return Task(
            description=dedent(
                f"""
                **Task**: Generate very intuitive and comprehensive bunker report

                **Description**: 
                Generate bunker in markdown format for easy understanding the contents by well organized layout.
                Compile an in-depth report based on the research results and predict bunker price trend for the Region, Grade, and Period. 
                The report will include price trend, importants news, regulation, supplier information, OPEC related information, WTI, BRENT, Dubai bunker oil spot price, weather conditions, forecasted bunker price in short term and long term.
                Need to consider the report's content, structure and layout.
                When creating the contents, make is as detail as possible and include the source of the data together with the links.

                **Parameters**:
                - Region: {region}
                - Period Range: {period_range}
                - Grade: {grade}

                **Note**: {self.__tip_section()}
                """
                ), 
            agent=agent,
            expected_output="intuitive and comprehensive bunker report"
            )