"""CRM Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_update_contact():
    """Test Update customer contact record with new information."""
    tools = AgentTools()
    result = await tools.update_contact(customer_id="test", updates="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_log_interaction():
    """Test Log a customer interaction in the CRM."""
    tools = AgentTools()
    result = await tools.log_interaction(customer_id="test", interaction_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_calculate_health_score():
    """Test Calculate customer health score based on engagement signals."""
    tools = AgentTools()
    result = await tools.calculate_health_score(customer_id="test", signals="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_trigger_workflow():
    """Test Trigger an automated engagement workflow for a customer."""
    tools = AgentTools()
    result = await tools.trigger_workflow(customer_id="test", workflow="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.crm_agent_agent import CrmAgentAgent
    agent = CrmAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
