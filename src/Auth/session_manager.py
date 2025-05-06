import streamlit as st
from datetime import datetime, timedelta
from config.app_config import SESSION_TIMEOUT_MINUTES

class SessionManager:
    @staticmethod
    def init_session():
        """Initialize or validate session."""
        # Clear all session state if it's a new browser session
        if 'session_initialized' not in st.session_state:
            SessionManager.clear_session_state()
            st.session_state.session_initialized = True
            
        if 'auth_service' not in st.session_state:
            from auth.auth_service import AuthService
            st.session_state.auth_service = AuthService()
        
        # Check session timeout
        if 'last_activity' in st.session_state:
            idle_time = datetime.now() - st.session_state.last_activity
            if idle_time > timedelta(minutes=SESSION_TIMEOUT_MINUTES):
                SessionManager.clear_session_state()
                st.error("Session expired. Please log in again.")
                st.rerun()
        
        # Update last activity
        st.session_state.last_activity = datetime.now()
        
        # Validate token and user data
        if 'user' in st.session_state:
            user_data = st.session_state.auth_service.validate_session_token()
            if not user_data:
                SessionManager.clear_session_state()
                st.error("Invalid session. Please log in again.")
                st.rerun()

    @staticmethod
    def clear_session_state():
        """Clear all session state data."""
        keys_to_keep = ['session_initialized']
        for key in list(st.session_state.keys()):
            if key not in keys_to_keep:
                del st.session_state[key]

    @staticmethod
    def is_authenticated():
        """Check if user is authenticated."""
        return bool(st.session_state.get('user'))
    
    @staticmethod
    def create_chat_session():
        """Create a new chat session."""
        if not SessionManager.is_authenticated():
            return False, "Not authenticated"
        return st.session_state.auth_service.create_session(
            st.session_state.user['id']
        )
    
    @staticmethod
    def get_user_sessions():
        """Get user's chat sessions."""
        if not SessionManager.is_authenticated():
            return False, []
        return st.session_state.auth_service.get_user_sessions(
            st.session_state.user['id']
        )
    
    @staticmethod
    def delete_session(session_id):
        """Delete a chat session."""
        if not SessionManager.is_authenticated():
            return False, "Not authenticated"
        return st.session_state.auth_service.delete_session(session_id)
    
    @staticmethod
    def logout():
        """Logout user and clear session."""
        if 'auth_service' in st.session_state:
            st.session_state.auth_service.sign_out()
        SessionManager.clear_session_state()
    
    @staticmethod
    def login(email, password):
        """Handle user login."""
        if 'auth_service' not in st.session_state:
            from auth.auth_service import AuthService
            st.session_state.auth_service = AuthService()
            
        return st.session_state.auth_service.sign_in(email, password)
