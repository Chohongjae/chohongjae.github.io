from typing import List, Text


class NoAgentFoundException(Exception):
    def __str__(self):
        return "There isn't Agent"


class Agent(object):
    def __init__(self, name: Text, skills: List[Text], load: int):
        self.name = name
        self.skills = skills
        self.load = load

    def __str__(self):
        return "<Agent: {}>".format(self.name)


class Ticket(object):
    def __init__(self, id: Text, restrictions: List[Text]):
        self.id = id
        self.restrictions = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        raise NotImplemented

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        available_agents = [agent for agent in agents if agent.load < 4]
        if not available_agents:
            raise NoAgentFoundException

        index_of_agent = 0
        min_load_of_agent = available_agents[index_of_agent].load
        for idx, agent in enumerate(available_agents):
            if agent.load < min_load_of_agent:
                min_load_of_agent = agent.load
                index_of_agent = idx
        return available_agents[index_of_agent]


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        required_skills = ticket.restrictions
        available_agents = []
        for agent in agents:
            for required_skill in required_skills:
                if agent.load > 3 or required_skill not in agent.skills:
                    break
            else:
                available_agents.append(agent)

        if not available_agents:
            raise NoAgentFoundException

        available_agents = sorted(available_agents, key=lambda agent: (len(agent.skills), agent.load))

        index_of_agent = 0
        min_skills_of_agent = len(available_agents[index_of_agent].skills)
        for idx, agent in enumerate(available_agents):
            if len(agent.skills) < min_skills_of_agent:
                min_skills_of_agent = agent.skills
                index_of_agent = idx
        return available_agents[index_of_agent]


if __name__ == "__main__":
    pass
    ticket = Ticket(id="1", restrictions=["English"])
    agent1 = Agent(name="A", skills=["English"], load=4)
    agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)

    least_loaded_policy = LeastLoadedAgent()
    least_flexible_agent = LeastFlexibleAgent()
    least_flexible_agent.find(ticket, [agent1, agent2])
    # print(least_loaded_policy.find(ticket, [agent1, agent2]))
