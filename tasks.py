from crewai import Task
from textwrap import dedent

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
 - Develop a detailed itinerary, including city selection, attratcions and pratical travel advice.
 
Key Steps for Task Creation:
1. Identify the Desired Outcomes: Define what sucess looks like for your project.
    - A detailed 7 day travel itenerary
2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Itenerary Planning: Develop a detailed plan for reach day of the trip
    -  City selection: Analayze and pick the best cities to visit.
    - Local Tour Guide: Find a local expert to provide insights and recommendations.
    
    
3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.
4. Task Descriptions Template:
     - Use this template  as a guide to define each task in your CrewAI application.
     - This template helps ensure that task is clearly defined, actionable and aligned with specific goals of
     
     
  TEMPLATE
------------
def [task_name](self, agent,[parameters]):
    return Task(description=dedent(f'''
    **Task**: [Provide a concise name or summary of the task]
    **Description**:[Detailed description of what the agent is expected to do, including actionable steps and examples]
    
    **Parameters**:
    - [Parameter 1]: [Description]
    - [Parameter 2]: [Description]
    ... [Add more parameters as needed.]

    **Note**:
     [Optinal section for incentives or encouragement for high-quality work.This can include tips,]
'''), agent=agent)
"""
# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates, interest):
        return Task(description=dedent(f'''
    **Task**: Develop a 7-Day Travel Itinerary
    
    **Description**:Expand the city guide into a full 7-day travel itinerary with detailed per-day plans, including weather forecasts, places to eat, packing suggestions, and a budget breakdown.You MUST suggest actual places tovist, actual hotels to stay, and actual restaurants to go to.This itinerary should cover all aspects of the trip,
    from arrival to departure, integrating the city guide informationj with practical travel logistics.
    
    **Parameters**:
    - [Parameter 1]: [Description]
    - [Parameter 2]: [Description]
    ... [Add more parameters as needed.]

    **Note**:
     [Optinal section for incentives or encouragement for high-quality work.This can include tips,]
'''),
    agent=agent,
        )

    def task_2_name(self, agent):
        return Task(
            description=dedent(
                f"""
            Take the input from task 1 and do something with it.
                                       
            {self.__tip_section()}

            Make sure to do something else.
        """
            ),
            agent=agent,
        )
