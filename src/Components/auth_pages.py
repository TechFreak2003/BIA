import streamlit as st
from auth.session_manager import SessionManager
from config.app_config import APP_ICON, APP_NAME, APP_TAGLINE, APP_DESCRIPTION
from utils.validators import validate_signup_fields
import time
import re

def show_login_page():
    # IMPORTANT: Initialize form_type immediately, no code before this!
    if 'form_type' not in st.session_state:
        st.session_state['form_type'] = 'login'  # Use dict-style access to be safer
    
    # From now on, form_type is guaranteed to exist
    current_form = st.session_state['form_type']  # Use dict-style access for consistency

    # Hide form submission helper text
    st.markdown("""
        <style>
            /* Hide form submission helper text */
            div[data-testid="InputInstructions"] > span:nth-child(1) {
                visibility: hidden;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div style='text-align: center; padding: 2rem;'>
            <h1>{APP_ICON} {APP_NAME}</h1>
            <h3>{APP_DESCRIPTION}</h3>
            <p style='font-size: 1.2em; color: #666; margin-bottom: 1em;'>{APP_TAGLINE}</p>
            <h3>{("Welcome Back!" if current_form == 'login' else "Welcome!")}</h3>
        </div>
    """, unsafe_allow_html=True)

    # Center the form
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Use the stored current_form value
        if current_form == 'login':
            show_login_form()
        else:
            show_signup_form()
        
        # Toggle button at bottom
        st.markdown("---")
        toggle_text = "Don't have an account? Sign up" if current_form == 'login' else "Already have an account? Login"
        if st.button(toggle_text, use_container_width=True, type="secondary"):
            # Toggle form type (use dict access for safety)
            st.session_state['form_type'] = 'signup' if current_form == 'login' else 'login'
            st.rerun()

def show_login_form():
    with st.form("login_form"):
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        
        if st.form_submit_button("Login", use_container_width=True, type="primary"):
            if email and password:
                success, result = SessionManager.login(email, password)
                if success:
                    # Show success message with spinner
                    with st.spinner("Logging in..."):
                        success_placeholder = st.empty()
                        success_placeholder.success("Login successful! Redirecting...")
                        time.sleep(1)  # Brief pause to show message
                        st.rerun()
                else:
                    st.error(f"Login failed: {result}")
            else:
                st.error("Please enter both email and password")

def show_signup_form():
    with st.form("signup_form"):
        new_name = st.text_input("Full Name", key="signup_name")
        new_email = st.text_input("Email", key="signup_email")
        new_password = st.text_input("Password", type="password", key="signup_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="signup_password2")
        
        st.markdown("""
            Password requirements:
            - At least 8 characters
            - One uppercase letter
            - One lowercase letter
            - One number
        """)
        
        if st.form_submit_button("Sign Up", use_container_width=True, type="primary"):
            validation_result = validate_signup_fields(
                new_name, new_email, new_password, confirm_password
            )
            
            if not validation_result[0]:
                st.error(validation_result[1])
                return
            
            # Show loading spinner during signup
            with st.spinner("Creating your account..."):
                success, response = st.session_state.auth_service.sign_up(
                    new_email, new_password, new_name
                )
                
                if success:
                    st.session_state.authenticated = True
                    st.session_state.user = response
                    st.success("Account created successfully! Redirecting...")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error(f"Sign up failed: {response}")
