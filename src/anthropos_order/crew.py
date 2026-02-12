from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import ScrapeWebsiteTool
from typing import List

@CrewBase
class AnthroposOrder():
    """AnthroposOrder crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def manager(self) -> Agent:
        return Agent(
            config=self.agents_config['manager'],
            verbose=True,
            allow_delegation=True
        )

    @agent
    def visual_dna_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['visual_dna_agent'],
            verbose=True
        )

    @agent
    def product_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['product_agent'],
            tools=[ScrapeWebsiteTool()],
            verbose=True
        )

    @agent
    def venora_persona_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['venora_persona_agent'],
            verbose=True
        )

    @agent
    def physics_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['physics_agent'],
            verbose=True
        )

    @agent
    def value_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['value_agent'],
            verbose=True
        )

    @agent
    def marketing_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['marketing_agent'],
            verbose=True
        )

    @task
    def product_scrape_task(self) -> Task:
        return Task(
            config=self.tasks_config['product_scrape_task'],
        )

    @task
    def product_image_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['product_image_analysis_task'],
        )

    @task
    def product_strategic_intelligence_task(self) -> Task:
        return Task(
            config=self.tasks_config['product_strategic_intelligence_task'],
        )

    @task
    def visual_dna_definition_task(self) -> Task:
        return Task(
            config=self.tasks_config['visual_dna_definition_task'],
        )

    @task
    def distill_high_impact_value_task(self) -> Task:
        return Task(
            config=self.tasks_config['distill_high_impact_value_task'],
        )

    @task
    def calculate_framework_laws_task(self) -> Task:
        return Task(
            config=self.tasks_config['calculate_framework_laws_task'],
        )

    @task
    def create_narrative_essence_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_narrative_essence_task'],
        )

    @task
    def finalize_videographer_brief_task(self) -> Task:
        return Task(
            config=self.tasks_config['finalize_videographer_brief_task'],
            output_file='final_order.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AnthroposOrder crew"""
        return Crew(
            agents=[agent for agent in self.agents if agent.role != self.manager().role],
            tasks=self.tasks,
            process=Process.hierarchical,
            manager_agent=self.manager(),
            verbose=True,
            output_log_file='crew_execution.log',
            tracing=True
        )


