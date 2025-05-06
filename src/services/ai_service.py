import streamlit as st
from agents.analysis_agent import AnalysisAgent

def init_analysis_state():
    """Initialize analysis-related session state variables."""
    if 'analysis_agent' not in st.session_state:
        st.session_state.analysis_agent = AnalysisAgent()

def check_rate_limit():
    # Ensure analysis agent is initialized
    init_analysis_state()
    return st.session_state.analysis_agent.check_rate_limit()

def generate_analysis(data, system_prompt, check_only=False, session_id=None):
    """Generate analysis if within rate limits."""
    # Ensure analysis agent is initialized
    init_analysis_state()
    
    # For check_only, we just need to check rate limits
    if check_only:
        return st.session_state.analysis_agent.check_rate_limit()
    
    # Get chat history if needed
    # Don't pass chat_history for now as it's causing issues
    # chat_history = None
    # if session_id and 'auth_service' in st.session_state:
    #     success, messages = st.session_state.auth_service.get_session_messages(session_id)
    #     if success:
    #         chat_history = messages
    
    # Call analyze_report without the chat_history parameter
    return st.session_state.analysis_agent.analyze_report(
        data=data,
        system_prompt=system_prompt,
        check_only=False
    )