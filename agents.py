from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI


"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee
   You need to hire to get the job done
- Define the captain of the crew who orient the other agents towards the goal
- Define which experts the captain needs to communicate with and delegate tasks to.
   Build a top down structure of the crew
   
Goal:
  - This Project Goal is Create a 7-day travel itinerary with detailed per-day plans,including budget, packing suggeestion, and safety tips.

Captain/Manager/Boss:
  - Expert Travel Agent
  
Employees/Experts to hire:
 - City Selection Expert (Agent1)
 - Local Tour Guide (Agent2)


Notes:
- Agent should be results driven amd have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resumes
"""

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py

class CustomAgents:
    def __init__(self):
        # self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="llama3")
    
    # def expert_travel_agent(self):
    # return Agent(
    #     role="Define agent 1 role here",
    #     backstory=dedent(f"""Define agent 1 backstory here"""),
    #     goal=dedent(f"""Define agent 1 goal here"""),
    #     # tools=[tool_1, tool_2],
    #     allow_delegation=False,
    #     verbose=True,
    #     llm=self.OpenAIGPT35,
    # )
    
    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logistics.
                             I have decades of experience making travel 
                             iteneraries"""),
            goal=dedent(f"""Create a 7-day travel itinerary with detailed
                            per-day plans, includes budget, packing sugeestion, and safety tips"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )

    def city_selection_expert(self):
        return Agent(
            role="  City Selection Expert",
            backstory=dedent(f"""Expert at analyzing travel data to pick 
                                 idea destinations"""),
            goal=dedent(f"""Select the ebst cities based on weather ,
                        season,prices, and traveler interests"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )
    
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Knowledgeable local guide with extensive information
                             about the city, it's attractions and cusions"""),
            goal=dedent(f"""Provide the Best insights about the selected city"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )


