"""Test configuration for CRM Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "crm-agent", "category": "Customer Service"}
