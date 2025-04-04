from typing import Dict, List
import os
from dotenv import load_dotenv
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Environment variables
load_dotenv()

class PoliticalAgent:
    def __init__(self, name: str, party: str, character: str, location: str):
        self.name = name
        self.party = party
        self.character = character
        self.location = location
        self.model_name = "deepseek-ai/deepseek-coder-1.3b-base"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        
    def generate_response(self, agenda: str, previous_messages: List[Dict]) -> str:
        """
        Generate a response based on the agenda and previous messages using DeepSeek model
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
        inputs = self.tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
        outputs = self.model.generate(
            inputs["input_ids"],
            max_length=200,
            num_return_sequences=1,
            temperature=0.7,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )
        
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response.split(f"{self.name} olarak cevabın:")[-1].strip()

class DenizAgent(PoliticalAgent):
    def __init__(self):
        super().__init__(
            name="Deniz",
            party="CHP",
            character="Aydın, kültürlü, entelektüel",
            location="Ankara / Çankaya"
        )
    
    def generate_response(self, agenda: str, previous_messages: List[Dict]) -> str:
        # TODO: Implement specific CHP-oriented response generation
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
        # TODO: Implement specific AKP-oriented response generation
        return super().generate_response(agenda, previous_messages) 