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
    def persona_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['persona_agent'],
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
            context=[self.product_scrape_task(), self.product_image_signal_task()]
        )

    @task
    def finalize_value_task(self) -> Task:
        return Task(
            config=self.tasks_config['finalize_value_task'],
            context=[self.intelligence_install_task()]
        )

    @task
    def physics_guardrails_task(self) -> Task:
        return Task(
            config=self.tasks_config['physics_guardrails_task'],
            context=[self.finalize_value_task(), self.product_scrape_task()]
        )

    @task
    def fashion_aesthetic_task(self) -> Task:
        return Task(
            config=self.tasks_config['fashion_aesthetic_task'],
            context=[self.product_scrape_task()]
        )

    @task
    def execution_arc_task(self) -> Task:
        return Task(
            config=self.tasks_config['execution_arc_task'],
            context=[
                self.finalize_value_task(),
                self.physics_guardrails_task(),
                self.fashion_aesthetic_task(),
                self.product_scrape_task()
            ]
        )

    @task
    def persona_modulation_task(self) -> Task:
        return Task(
            config=self.tasks_config['persona_modulation_task'],
            context=[self.execution_arc_task()]
        )

    @task
    def physics_audit_task(self) -> Task:
        return Task(
            config=self.tasks_config['physics_audit_task'],
            context=[self.persona_modulation_task(), self.physics_guardrails_task()]
        )

    @task
    def finalize_order_brief_task(self) -> Task:
        return Task(
            config=self.tasks_config['finalize_order_brief_task'],
            context=[
                self.finalize_value_task(),
                self.persona_modulation_task(),
                self.physics_guardrails_task(),
                self.fashion_aesthetic_task(),
                self.physics_audit_task()
            ]
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


