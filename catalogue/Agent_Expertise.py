"""
AGENT EXPERTISE MODULE
======================

Manages persistent mental models for agents using YAML storage.

This module implements the "Agentic Expertise" pattern where agents maintain
a persistent mental model of their domain expertise to avoid relearning tasks.

Research Context:
- Agents transition from "Stateless" to "Expert" mode
- Mental models are stored persistently across sessions
- Domain-specific insights are accumulated over time
"""

import os
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime


class Agent_Expertise:
    """
    Manages persistent mental model storage and retrieval for agents.
    
    Each agent maintains a YAML file containing their domain expertise,
    learned patterns, and insights. This enables agents to build upon
    previous knowledge rather than starting from scratch each session.
    
    File Structure:
        memory/{agent_id}_expertise.yaml
    
    YAML Format:
        agent_id: <uuid>
        role: <agent_role>
        last_updated: <iso_timestamp>
        expertise:
            <topic_key>:
                insights: [list of insight strings]
                patterns: [list of pattern strings]
                last_learned: <iso_timestamp>
    """
    
    def __init__(self, agent_id: str, role: str = "BaseAgent", memory_dir: str = "memory"):
        """
        Initialize the expertise manager for an agent.
        
        Args:
            agent_id: Unique identifier for the agent
            role: Agent role (for context)
            memory_dir: Directory where expertise files are stored
        """
        self.agent_id = agent_id
        self.role = role
        self.memory_dir = Path(memory_dir)
        self.expertise_file = self.memory_dir / f"{agent_id}_expertise.yaml"
        self.mental_model: Dict[str, Any] = {}
        
        # Ensure memory directory exists
        self.memory_dir.mkdir(exist_ok=True)
        
        # Load existing mental model or initialize empty one
        self.load_mental_model()
    
    def load_mental_model(self) -> Dict[str, Any]:
        """
        Load the mental model from YAML file at startup.
        
        If the file doesn't exist, initializes an empty mental model structure.
        
        Returns:
            Dictionary containing the loaded mental model
        """
        if not self.expertise_file.exists():
            # Initialize empty mental model
            self.mental_model = {
                "agent_id": self.agent_id,
                "role": self.role,
                "created_at": datetime.now().isoformat(),
                "last_updated": datetime.now().isoformat(),
                "expertise": {}
            }
            # Save initial structure
            self._save_mental_model()
            return self.mental_model
        
        try:
            with open(self.expertise_file, 'r', encoding='utf-8') as f:
                self.mental_model = yaml.safe_load(f) or {}
            
            # Ensure required keys exist
            if "expertise" not in self.mental_model:
                self.mental_model["expertise"] = {}
            if "agent_id" not in self.mental_model:
                self.mental_model["agent_id"] = self.agent_id
            if "role" not in self.mental_model:
                self.mental_model["role"] = self.role
            
            return self.mental_model
        
        except Exception as e:
            print(f"[{self.role}-EXPERTISE-ERROR] Failed to load mental model: {e}")
            # Fallback to empty model
            self.mental_model = {
                "agent_id": self.agent_id,
                "role": self.role,
                "created_at": datetime.now().isoformat(),
                "last_updated": datetime.now().isoformat(),
                "expertise": {}
            }
            return self.mental_model
    
    def update_mental_model(self, key: str, insight: str) -> bool:
        """
        Write new findings to the mental model.
        
        Examples:
            key="API_Endpoints"
            insight="API Endpoint X requires Auth Header Y"
            
            key="Database_Queries"
            insight="Customer table uses composite key (id, region)"
        
        Args:
            key: Topic or domain key (e.g., "API_Endpoints", "Common_Bugs")
            insight: The learned insight or pattern to store
            
        Returns:
            True if update was successful, False otherwise
        """
        try:
            # Initialize expertise structure if it doesn't exist
            if "expertise" not in self.mental_model:
                self.mental_model["expertise"] = {}
            
            # Initialize topic if it doesn't exist
            if key not in self.mental_model["expertise"]:
                self.mental_model["expertise"][key] = {
                    "insights": [],
                    "patterns": [],
                    "last_learned": datetime.now().isoformat()
                }
            
            # Add insight to the topic
            topic_data = self.mental_model["expertise"][key]
            if "insights" not in topic_data:
                topic_data["insights"] = []
            
            # Avoid duplicates
            if insight not in topic_data["insights"]:
                topic_data["insights"].append(insight)
                topic_data["last_learned"] = datetime.now().isoformat()
            
            # Update last_updated timestamp
            self.mental_model["last_updated"] = datetime.now().isoformat()
            
            # Save to file
            self._save_mental_model()
            
            print(f"[{self.role}-EXPERTISE] Updated mental model: {key} (+1 insight)")
            return True
        
        except Exception as e:
            print(f"[{self.role}-EXPERTISE-ERROR] Failed to update mental model: {e}")
            return False
    
    def query_mental_model(self, topic: str) -> List[str]:
        """
        Query the mental model for relevant insights on a topic.
        
        Args:
            topic: Topic key to query (e.g., "API_Endpoints", "Common_Bugs")
            
        Returns:
            List of insights related to the topic, empty list if topic not found
        """
        try:
            if "expertise" not in self.mental_model:
                return []
            
            topic_data = self.mental_model["expertise"].get(topic, {})
            insights = topic_data.get("insights", [])
            patterns = topic_data.get("patterns", [])
            
            # Return combined insights and patterns
            return insights + patterns
        
        except Exception as e:
            print(f"[{self.role}-EXPERTISE-ERROR] Failed to query mental model: {e}")
            return []
    
    def get_all_expertise_topics(self) -> List[str]:
        """
        Get all topics that have expertise data.
        
        Returns:
            List of topic keys
        """
        try:
            if "expertise" not in self.mental_model:
                return []
            return list(self.mental_model["expertise"].keys())
        except Exception:
            return []
    
    def get_mental_model_summary(self) -> str:
        """
        Get a formatted summary of the mental model for inclusion in prompts.
        
        Returns:
            Formatted string summarizing current expertise
        """
        if not self.mental_model.get("expertise"):
            return "No expertise data available yet. Start learning!"
        
        summary_lines = ["Current Mental Model:"]
        summary_lines.append("=" * 50)
        
        for topic, data in self.mental_model["expertise"].items():
            insights = data.get("insights", [])
            patterns = data.get("patterns", [])
            total_items = len(insights) + len(patterns)
            last_learned = data.get("last_learned", "Unknown")
            
            summary_lines.append(f"\nTopic: {topic}")
            summary_lines.append(f"  Total Insights: {total_items}")
            summary_lines.append(f"  Last Learned: {last_learned}")
            
            # Include recent insights (up to 3)
            if insights:
                summary_lines.append("  Recent Insights:")
                for insight in insights[-3:]:
                    summary_lines.append(f"    - {insight}")
        
        summary_lines.append("\n" + "=" * 50)
        return "\n".join(summary_lines)
    
    def _save_mental_model(self) -> None:
        """Internal method to save mental model to YAML file."""
        try:
            with open(self.expertise_file, 'w', encoding='utf-8') as f:
                yaml.dump(self.mental_model, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        except Exception as e:
            print(f"[{self.role}-EXPERTISE-ERROR] Failed to save mental model: {e}")
            raise

