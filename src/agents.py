from typing import Dict, List
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key='AIzaSyBzH19H_iU5LHwGyfnVh3cYmF-zXjUeuCw')

class PoliticalAgent:
    def __init__(self, name: str, party: str, character: str, location: str):
        self.name = name
        self.party = party
        self.character = character
        self.location = location
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        
    def generate_response(self, agenda: str, previous_messages: List[Dict]) -> str:
        """
        Generate a response based on the agenda and previous messages using Gemini
        """
        # Construct the prompt
        prompt = f"""
        Sen {self.name} adlı bir siyasetçisin.
        Parti: {self.party}
        Karakter: {self.character}
        Konum: {self.location}
        
        Gündem: {agenda}
        
        Önceki mesajlar:
        """
        
        for msg in previous_messages:
            prompt += f"\n{msg['role']}: {msg['content']}"
            
        prompt += f"\n\n{self.name} olarak cevabın:"
        
        # Generate response
        response = self.model.generate_content(prompt)
        return response.text.strip()

class DenizAgent(PoliticalAgent):
    def __init__(self):
        super().__init__(
            name="Deniz",
            party="CHP",
            character="Aydın, kültürlü, entelektüel",
            location="Ankara / Çankaya"
        )
    
    def generate_response(self, agenda: str, previous_messages: List[Dict]) -> str:
        # CHP-oriented response generation
        return super().generate_response(agenda, previous_messages)

class PolatAgent(PoliticalAgent):
    def __init__(self):
        super().__init__(
            name="Polat",
            party="AKP",
            character="Muhafazakar, taşralı, halkçı",
            location="Konya / Merkez"
        )
    
    def generate_response(self, agenda: str, previous_messages: List[Dict]) -> str:
        # AKP-oriented response generation
        return super().generate_response(agenda, previous_messages) 