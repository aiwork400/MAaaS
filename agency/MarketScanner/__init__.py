from agency_swarm import Agent
from .tools import ScanTerritory

class MarketScanner(Agent):
    def __init__(self):
        super().__init__(
            name="MarketScanner",
            description="Autonomous reconnaissance unit for exhaustive market data collection.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[ScanTerritory],
            tools_folder="./tools",
            temperature=0.5,
            max_prompt_tokens=4000,
        )