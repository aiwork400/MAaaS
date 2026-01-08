-- SCMS Table: Audit Logs (For Financial Compliance)
CREATE TABLE IF NOT EXISTS audit_logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    agent_name VARCHAR(50),
    action_type VARCHAR(50),
    details TEXT,
    severity VARCHAR(20) -- 'INFO', 'WARNING', 'CRITICAL'
);

-- SCMS Table: Agent Memory (For Token Minimization)
CREATE TABLE IF NOT EXISTS agent_memory (
    id SERIAL PRIMARY KEY,
    agent_id VARCHAR(50),
    memory_type VARCHAR(20), -- 'strategic', 'artifact_pointer'
    content TEXT,
    artifact_ref VARCHAR(100), -- The hash reference (e.g., [REF:1234])
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
