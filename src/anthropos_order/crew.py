from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import ScrapeWebsiteTool
from typing import List

@CrewBase
class AnthroposOrder():
    """AnthroposOrder crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def manager(self) -> Agent:
        return Agent(
            config=self.agents_config['manager'],
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

    @agent
    def venora_persona_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['venora_persona_agent'],
            verbose=True
        )

    @agent
    def visual_dna_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['visual_dna_agent'],
            verbose=True
        )

    @task
    def product_scrape_task(self) -> Task:
        return Task(
            config=self.tasks_config['product_scrape_task'],
        )

    @task
    def product_image_signal_task(self) -> Task:
        return Task(
            config=self.tasks_config['product_image_signal_task'],
        )

    @task
    def intelligence_install_task(self) -> Task:
        return Task(
            config=self.tasks_config['intelligence_install_task'],
        )

    @task
    def market_frame_task(self) -> Task:
        return Task(
            config=self.tasks_config['market_frame_task'],
        )

    @task
    def physics_guardrails_task(self) -> Task:
        return Task(
            config=self.tasks_config['physics_guardrails_task'],
        )

    @task
    def execution_arc_task(self) -> Task:
        return Task(
            config=self.tasks_config['execution_arc_task'],
        )

    @task
    def physics_audit_task(self) -> Task:
        return Task(
            config=self.tasks_config['physics_audit_task'],
        )

    @task
    def finalize_order_brief_task(self) -> Task:
        return Task(
            config=self.tasks_config['finalize_order_brief_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AnthroposOrder crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            output_log_file='crew_execution.log'
        )


