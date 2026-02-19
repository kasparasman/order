from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
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
    def market_research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['market_research_agent'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True
        )

    @agent
    def product_truth_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['product_truth_agent'],
            tools=[ScrapeWebsiteTool()],
            verbose=True
        )

    @agent
    def strategy_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['strategy_agent'],
            verbose=True
        )

    @agent
    def script_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['script_agent'],
            verbose=True
        )

    @agent
    def persona_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['persona_agent'],
            verbose=True
        )

    @agent
    def physics_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['physics_agent'],
            verbose=True
        )

    @task
    def phase_0_objective_lock(self) -> Task:
        return Task(
            config=self.tasks_config['phase_0_objective_lock'],
        )

    @task
    def phase_1_avatar_selection(self) -> Task:
        return Task(
            config=self.tasks_config['phase_1_avatar_selection'],
        )

    @task
    def phase_2_market_language_mining(self) -> Task:
        return Task(
            config=self.tasks_config['phase_2_market_language_mining'],
        )

    @task
    def phase_3_product_truth_extraction(self) -> Task:
        return Task(
            config=self.tasks_config['phase_3_product_truth_extraction'],
        )

    @task
    def phase_4_srw_selection(self) -> Task:
        return Task(
            config=self.tasks_config['phase_4_srw_selection'],
            context=[self.phase_3_product_truth_extraction()]
        )

    @task
    def phase_5_physics_template_commitment(self) -> Task:
        return Task(
            config=self.tasks_config['phase_5_physics_template_commitment'],
        )

    @task
    def phase_6_script_pack_generation(self) -> Task:
        return Task(
            config=self.tasks_config['phase_6_script_pack_generation'],
            context=[
                self.phase_2_market_language_mining(),
                self.phase_3_product_truth_extraction(),
                self.phase_4_srw_selection()
            ]
        )

    @task
    def phase_7_persona_modulation(self) -> Task:
        return Task(
            config=self.tasks_config['phase_7_persona_modulation'],
            context=[self.phase_6_script_pack_generation()]
        )

    @task
    def phase_8_physics_audit(self) -> Task:
        return Task(
            config=self.tasks_config['phase_8_physics_audit'],
            context=[
                self.phase_5_physics_template_commitment(),
                self.phase_7_persona_modulation()
            ]
        )

    @task
    def phase_9_final_order_assembly(self) -> Task:
        return Task(
            config=self.tasks_config['phase_9_final_order_assembly'],
            context=[
                self.phase_0_objective_lock(),
                self.phase_1_avatar_selection(),
                self.phase_2_market_language_mining(),
                self.phase_3_product_truth_extraction(),
                self.phase_4_srw_selection(),
                self.phase_6_script_pack_generation(),
                self.phase_8_physics_audit()
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


