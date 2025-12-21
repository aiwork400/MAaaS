# Chat Ops Integration - Real Agent Communication

## Overview

The Chat Ops tab in the Dashboard and the API Server are now fully wired to communicate with the actual **Nexus_PM** agent, replacing the previous mock responses.

## Implementation Details

### 1. Nexus_PM Agent Enhancement (`clients/Nexus/Nexus_PM.py`)

Added two new methods:

#### `load_project_context() -> Dict[str, Any]`
- Reads `project_status.md` to understand current project state
- Loads `nexus_deployment_plan.json` for deployment context
- Returns structured context including:
  - Project status (FABRICATION PHASE, DEPLOYED, etc.)
  - Client information
  - Active agents list
  - Active workflows
  - SLA metrics

#### `process_chat_request(user_message: str) -> str`
- Processes user chat messages
- Automatically loads project context before responding
- Provides intelligent responses based on keywords:
  - **Status/Health queries**: System status, agent health, SLA uptime
  - **Workflow queries**: WF-AUDIT-01 progress and steps
  - **Budget queries**: Token usage, contract status, financials
  - **Agent queries**: Swarm status, trust ledger, subordinate agents
  - **General queries**: Helpful responses with available commands
- Logs all interactions to provenance log (C5 compliance)

### 2. Dashboard Integration (`dashboard.py`)

#### `get_nexus_pm_agent()` (Cached Resource)
- Uses `@st.cache_resource` to maintain agent instance across reruns
- Automatically loads and signs contract from deployment plan
- Registers known subordinate agents (Researcher, Compliance, NetSec)
- Handles initialization errors gracefully

#### `render_chat_ops_tab()` Updates
- Displays agent status (Agent ID, Contract Status, Trust Score)
- Uses real `agent.process_chat_request()` instead of mock function
- Shows loading spinner while agent processes request
- Displays error messages if agent fails
- Maintains chat history in session state

### 3. API Server Integration (`api_server.py`)

#### New Endpoints

**`POST /chat`**
- Accepts `ChatRequest` with user message
- Returns `ChatResponse` with agent response, agent_id, and timestamp
- Uses cached Nexus_PM instance

**`GET /chat/history`** (Capabilities)
- Returns agent information and available chat capabilities
- Useful for frontend integration

#### Agent Caching
- Global `_nexus_pm_cache` maintains single agent instance
- Contract is automatically loaded and signed on first use
- Subordinate agents are registered automatically

## Usage

### Dashboard (Streamlit)

1. Navigate to **Chat Ops** tab
2. Type your message in the chat input
3. Nexus_PM will:
   - Load current project context
   - Process your message
   - Return intelligent response
   - Log the interaction

### API Server

```bash
# Send a chat message
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "What is the system status?"}'

# Get chat capabilities
curl "http://localhost:8000/chat/history"
```

## Example Queries

### System Status
```
User: "What is the system status?"
Nexus_PM: Returns current status, active agents, workflows, SLA uptime
```

### Workflow Progress
```
User: "How is WF-AUDIT-01 progressing?"
Nexus_PM: Returns workflow steps, current phase, agent assignments
```

### Budget Information
```
User: "What is our token budget status?"
Nexus_PM: Returns token usage, budget allocation, contract status
```

### Agent Swarm
```
User: "Show me the agent swarm status"
Nexus_PM: Returns list of active agents, trust scores, provenance log stats
```

## Context Loading

The agent automatically loads context from:

1. **`clients/project_status.md`**
   - Current project phase
   - Completed artifacts
   - Pending tasks

2. **`clients/nexus_deployment_plan.json`**
   - Client information
   - Industry and market
   - Agent instances and contracts

3. **Agent Internal State**
   - Active contract
   - Token usage
   - Trust ledger
   - Provenance log

## Error Handling

- **Agent Initialization Failure**: Shows error message in Dashboard
- **Contract Loading Failure**: Agent still functions, but contract status shows as UNSIGNED
- **Context Loading Failure**: Agent continues with available context
- **Processing Errors**: Error message returned to user with details

## Provenance Tracking

All chat interactions are logged to the agent's provenance log with:
- Action type: `chat_request`
- User message (truncated to 100 chars)
- Timestamp
- Agent ID

This ensures full audit trail (C5 compliance).

## Future Enhancements

1. **LLM Integration**: Replace keyword-based routing with actual LLM via MCP
2. **Multi-turn Conversations**: Maintain conversation context across messages
3. **Agent Delegation**: Allow Nexus_PM to delegate complex queries to specialized agents
4. **Real-time Updates**: Stream responses as agent processes
5. **Voice Interface**: Add speech-to-text and text-to-speech capabilities

## Testing

To test the integration:

```python
# Test agent directly
from clients.Nexus.Nexus_PM import Nexus_PM

agent = Nexus_PM()
response = agent.process_chat_request("What is the system status?")
print(response)
```

## Notes

- Agent instance is cached to maintain state across requests
- Contract is automatically loaded from deployment plan
- All responses include project context for accuracy
- Chat history is maintained in Streamlit session state
- API responses are stateless (each request gets fresh context)

