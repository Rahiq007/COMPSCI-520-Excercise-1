import os
from anthropic import Anthropic
import google.generativeai as genai
from dotenv import load_dotenv
import time

load_dotenv()

class LLMInterface:
    def __init__(self):
        # Initialize Claude
        anthropic_key = os.getenv("ANTHROPIC_API_KEY")
        if not anthropic_key:
            raise ValueError("ANTHROPIC_API_KEY not found in .env file")
        self.claude_client = Anthropic(api_key=anthropic_key)
        
        # Initialize Gemini
        google_key = os.getenv("GOOGLE_API_KEY")
        if not google_key:
            raise ValueError("GOOGLE_API_KEY not found in .env file")
        genai.configure(api_key=google_key)
        self.gemini_model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    def call_claude(self, prompt, max_tokens=2000):
        """Call Claude API"""
        try:
            message = self.claude_client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=max_tokens,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return message.content[0].text
        except Exception as e:
            print(f"Claude API Error: {e}")
            return None
    
    def call_gemini(self, prompt):
        """Call Gemini API"""
        try:
            response = self.gemini_model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Gemini API Error: {e}")
            return None
    
    def generate_code(self, llm_name, prompt):
        """Generate code using specified LLM"""
        print(f"  Calling {llm_name}...")
        
        if llm_name.lower() == "claude":
            response = self.call_claude(prompt)
        elif llm_name.lower() == "gemini":
            response = self.call_gemini(prompt)
        else:
            raise ValueError(f"Unknown LLM: {llm_name}")
        
        time.sleep(1)  # Rate limiting
        return response