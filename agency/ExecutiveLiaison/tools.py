"""
ExecutiveLiaison Agent Tools

Contains the core functionality for executive communication and reporting.
Extracted from Agent_ProjectManager and related agent communication patterns.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional, Any
from collections import defaultdict


class ExecutiveReportingTool:
    """
    Tool for generating executive-level reports and communications.
    """
    
    def __init__(self):
        self.tool_name = "executive_reporting"
        self.report_history: List[Dict[str, Any]] = []
    
    def generate_executive_brief(self, agent_statuses: Dict[str, Any],
                                metrics: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Generate a daily executive brief with high-level status.
        
        Args:
            agent_statuses: Dictionary of agent status information
            metrics: Optional business metrics (ROI, performance, etc.)
            
        Returns:
            Executive brief dictionary with key sections
        """
        active_agents = sum(1 for status in agent_statuses.values() 
                          if status.get('status') == 'ACTIVE')
        total_agents = len(agent_statuses)
        
        brief = {
            "report_type": "Daily Executive Brief",
            "generated_at": datetime.now().isoformat(),
            "summary": {
                "total_agents": total_agents,
                "active_agents": active_agents,
                "idle_agents": total_agents - active_agents,
                "system_status": "OPERATIONAL" if active_agents > 0 else "STANDBY"
            },
            "key_metrics": metrics or {},
            "agent_status": agent_statuses,
            "critical_issues": self._extract_critical_issues(agent_statuses),
            "next_steps": self._generate_next_steps(agent_statuses, metrics)
        }
        
        self.report_history.append(brief)
        return brief
    
    def generate_strategic_report(self, workflow_data: Dict[str, Any],
                                 performance_metrics: Dict[str, Any],
                                 contract_status: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a comprehensive weekly strategic report.
        
        Args:
            workflow_data: Information about active workflows
            performance_metrics: Performance and efficiency metrics
            contract_status: Contract compliance and status information
            
        Returns:
            Strategic report dictionary
        """
        report = {
            "report_type": "Weekly Strategic Report",
            "generated_at": datetime.now().isoformat(),
            "executive_summary": {
                "period": "Weekly",
                "overall_status": "ON_TRACK",
                "key_achievements": self._extract_achievements(workflow_data),
                "challenges": self._identify_challenges(workflow_data)
            },
            "performance_analysis": performance_metrics,
            "workflow_progress": workflow_data,
            "contract_compliance": contract_status,
            "resource_utilization": self._calculate_resource_utilization(performance_metrics),
            "strategic_recommendations": self._generate_strategic_recommendations(
                workflow_data, performance_metrics
            )
        }
        
        self.report_history.append(report)
        return report
    
    def format_for_executive(self, technical_data: Dict[str, Any]) -> str:
        """
        Translate technical data into executive-friendly language.
        
        Args:
            technical_data: Raw technical metrics or status
            
        Returns:
            Formatted executive summary string
        """
        lines = []
        lines.append("EXECUTIVE SUMMARY")
        lines.append("=" * 50)
        lines.append("")
        
        # Translate technical metrics
        if 'agent_status' in technical_data:
            active = sum(1 for s in technical_data['agent_status'].values() 
                        if s.get('status') == 'ACTIVE')
            lines.append(f"System Status: {active} agents actively operating")
        
        if 'key_metrics' in technical_data:
            metrics = technical_data['key_metrics']
            if 'roi' in metrics:
                lines.append(f"ROI: {metrics['roi']}%")
            if 'completion_rate' in metrics:
                lines.append(f"Completion Rate: {metrics['completion_rate']}%")
        
        lines.append("")
        lines.append("Business Impact:")
        if 'critical_issues' in technical_data:
            issues = technical_data['critical_issues']
            if issues:
                lines.append(f"- {len(issues)} issue(s) requiring attention")
            else:
                lines.append("- All systems operating normally")
        
        return "\n".join(lines)
    
    def aggregate_agent_status(self, agents: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Aggregate status from multiple agents into a unified view.
        
        Args:
            agents: List of agent status dictionaries
            
        Returns:
            Aggregated status dictionary
        """
        aggregated = {
            "total_agents": len(agents),
            "status_breakdown": defaultdict(int),
            "by_role": defaultdict(list),
            "contract_status": defaultdict(int),
            "token_usage_total": 0
        }
        
        for agent in agents:
            status = agent.get('status', 'UNKNOWN')
            role = agent.get('role', 'Unknown')
            
            aggregated['status_breakdown'][status] += 1
            aggregated['by_role'][role].append(agent)
            
            contract_id = agent.get('contract_id')
            if contract_id:
                contract_status = agent.get('contract_status', 'UNKNOWN')
                aggregated['contract_status'][contract_status] += 1
            
            token_usage = agent.get('token_usage', 0)
            aggregated['token_usage_total'] += token_usage
        
        return aggregated
    
    def _extract_critical_issues(self, agent_statuses: Dict[str, Any]) -> List[str]:
        """Extract critical issues from agent statuses."""
        issues = []
        for agent_name, status in agent_statuses.items():
            if status.get('status') == 'ERROR':
                issues.append(f"{agent_name}: {status.get('error_message', 'Unknown error')}")
            if status.get('token_usage', 0) > status.get('token_budget_max', 0) * 0.9:
                issues.append(f"{agent_name}: Approaching token budget limit")
        return issues
    
    def _generate_next_steps(self, agent_statuses: Dict[str, Any],
                            metrics: Optional[Dict[str, Any]]) -> List[str]:
        """Generate recommended next steps based on current status."""
        steps = []
        
        # Check for idle agents
        idle_count = sum(1 for s in agent_statuses.values() 
                        if s.get('status') == 'IDLE')
        if idle_count > 0:
            steps.append(f"Assign tasks to {idle_count} idle agent(s)")
        
        # Check metrics for recommendations
        if metrics:
            if metrics.get('roi', 0) < 0:
                steps.append("Review and optimize low-performing campaigns")
            if metrics.get('completion_rate', 100) < 80:
                steps.append("Investigate workflow completion bottlenecks")
        
        if not steps:
            steps.append("Continue monitoring and maintain current operations")
        
        return steps
    
    def _extract_achievements(self, workflow_data: Dict[str, Any]) -> List[str]:
        """Extract key achievements from workflow data."""
        achievements = []
        completed = workflow_data.get('completed_workflows', 0)
        if completed > 0:
            achievements.append(f"Completed {completed} workflow(s) successfully")
        
        success_rate = workflow_data.get('success_rate', 0)
        if success_rate > 90:
            achievements.append(f"Maintained {success_rate}% success rate")
        
        return achievements
    
    def _identify_challenges(self, workflow_data: Dict[str, Any]) -> List[str]:
        """Identify challenges from workflow data."""
        challenges = []
        if workflow_data.get('failed_workflows', 0) > 0:
            challenges.append(f"{workflow_data['failed_workflows']} workflow failure(s)")
        
        avg_duration = workflow_data.get('avg_duration_seconds', 0)
        if avg_duration > 300:  # 5 minutes
            challenges.append("Workflow duration above target threshold")
        
        return challenges
    
    def _calculate_resource_utilization(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate resource utilization from metrics."""
        utilization = {
            "token_utilization_percent": 0,
            "agent_utilization_percent": 0,
            "compute_utilization_percent": 0
        }
        
        if 'token_budget' in metrics and 'token_used' in metrics:
            budget = metrics['token_budget']
            used = metrics['token_used']
            if budget > 0:
                utilization['token_utilization_percent'] = (used / budget) * 100
        
        if 'total_agents' in metrics and 'active_agents' in metrics:
            total = metrics['total_agents']
            active = metrics['active_agents']
            if total > 0:
                utilization['agent_utilization_percent'] = (active / total) * 100
        
        return utilization
    
    def _generate_strategic_recommendations(self, workflow_data: Dict[str, Any],
                                          performance_metrics: Dict[str, Any]) -> List[str]:
        """Generate strategic recommendations."""
        recommendations = []
        
        # Based on performance
        if performance_metrics.get('efficiency_score', 100) < 80:
            recommendations.append("Optimize agent workflows to improve efficiency")
        
        # Based on resource utilization
        if performance_metrics.get('resource_utilization', 0) < 50:
            recommendations.append("Consider scaling up operations to maximize ROI")
        
        # Based on workflow patterns
        if workflow_data.get('bottleneck_count', 0) > 0:
            recommendations.append("Address workflow bottlenecks to improve throughput")
        
        return recommendations


class ExecutiveCommunicationTool:
    """
    Tool for managing executive communication channels and preferences.
    """
    
    def __init__(self):
        self.tool_name = "executive_communication"
        self.communication_log: List[Dict[str, Any]] = []
        self.executive_preferences: Dict[str, Any] = {}
    
    def log_communication(self, executive_name: str, channel: str,
                         message_type: str, content: str) -> Dict[str, Any]:
        """
        Log executive communication for tracking and analysis.
        
        Args:
            executive_name: Name of the executive
            channel: Communication channel (email, meeting, dashboard)
            message_type: Type of communication (brief, report, update)
            content: Communication content summary
            
        Returns:
            Communication log entry
        """
        entry = {
            "executive_name": executive_name,
            "channel": channel,
            "message_type": message_type,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "status": "DELIVERED"
        }
        
        self.communication_log.append(entry)
        return entry
    
    def update_executive_preferences(self, executive_name: str,
                                    preferences: Dict[str, Any]) -> None:
        """
        Update stored preferences for an executive.
        
        Args:
            executive_name: Name of the executive
            preferences: Dictionary of preference settings
        """
        if executive_name not in self.executive_preferences:
            self.executive_preferences[executive_name] = {}
        
        self.executive_preferences[executive_name].update(preferences)
    
    def get_executive_preferences(self, executive_name: str) -> Dict[str, Any]:
        """
        Get stored preferences for an executive.
        
        Args:
            executive_name: Name of the executive
            
        Returns:
            Dictionary of executive preferences
        """
        return self.executive_preferences.get(executive_name, {
            "reporting_frequency": "weekly",
            "preferred_channel": "dashboard",
            "detail_level": "executive_summary",
            "metrics_focus": ["ROI", "performance", "compliance"]
        })


# Singleton instances
reporting_tool = ExecutiveReportingTool()
communication_tool = ExecutiveCommunicationTool()
