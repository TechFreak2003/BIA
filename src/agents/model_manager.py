import groq
import streamlit as st
from enum import Enum
import logging
import time

logger = logging.getLogger(__name__)

class ModelTier(Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary" 
    TERTIARY = "tertiary"
    FALLBACK = "fallback"

class ModelManager:
    """
    Manages AI model selection, fallback, and rate limits.
    Implements an agent-based approach for model management.
    """
    
    MODEL_CONFIG = {
        ModelTier.PRIMARY: {
            "provider": "groq",
            "model": "meta-llama/llama-4-maverick-17b-128e-instruct",
            "max_tokens": 2000,
            "temperature": 0.7
        },
        ModelTier.SECONDARY: {
            "provider": "groq", 
            "model": "llama-3.3-70b-versatile",
            "max_tokens": 2000,
            "temperature": 0.7
        },
        ModelTier.TERTIARY: {
            "provider": "groq",
            "model": "llama-3.1-8b-instant",
            "max_tokens": 2000, 
            "temperature": 0.7
        },
        ModelTier.FALLBACK: {
            "provider": "groq",
            "model": "llama3-70b-8192",
            "max_tokens": 2000,
            "temperature": 0.7
        }
    }
    
    def __init__(self):
        self.clients = {}
        self._initialize_clients()

    def _initialize_clients(self):
        """Initialize API clients for each provider."""
        try:
            self.clients["groq"] = groq.Groq(api_key=st.secrets["GROQ_API_KEY"])
        except Exception as e:
            logger.error(f"Failed to initialize Groq client: {str(e)}")

    def generate_analysis(self, data, system_prompt, retry_count=0):
        """
        Generate analysis using the best available model with automatic fallback.
        Implements agent-based decision making for model selection.
        """
        if retry_count > 3:
            return {"success": False, "error": "All models failed after multiple retries"}

        # Determine which model tier to use based on retry count
        if retry_count == 0:
            tier = ModelTier.PRIMARY
        elif retry_count == 1:
            tier = ModelTier.SECONDARY
        elif retry_count == 2:
            tier = ModelTier.TERTIARY
        else:
            tier = ModelTier.FALLBACK
            
        model_config = self.MODEL_CONFIG[tier]
        provider = model_config["provider"]
        model = model_config["model"]
        
        # Check if we have a client for this provider
        if provider not in self.clients:
            logger.error(f"No client available for provider: {provider}")
            return self.generate_analysis(data, system_prompt, retry_count + 1)
            
        try:
            client = self.clients[provider]
            logger.info(f"Attempting generation with {provider} model: {model}")
            
            if provider == "groq":
                completion = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": str(data)}
                    ],
                    temperature=model_config["temperature"],
                    max_tokens=model_config["max_tokens"]
                )
                
                return {
                    "success": True,
                    "content": completion.choices[0].message.content,
                    "model_used": f"{provider}/{model}"
                }
                
        except Exception as e:
            error_message = str(e).lower()
            logger.warning(f"Model {model} failed: {error_message}")
            
            # Check for rate limit errors
            if "rate limit" in error_message or "quota" in error_message:
                # Wait briefly before retrying with a different model
                time.sleep(2)
            
            # Try next model in hierarchy
            return self.generate_analysis(data, system_prompt, retry_count + 1)
            
        return {"success": False, "error": "Analysis failed with all available models"}
