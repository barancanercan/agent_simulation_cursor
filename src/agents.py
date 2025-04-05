from typing import Dict, List
import os
from dotenv import load_dotenv
import google.generativeai as genai
import time

# Environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

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
        # Add delay before API call
        time.sleep(5)
        
        # Construct the prompt
        prompt = f"""
        Sen {self.name} adlı bir seçmensin.
        Parti: {self.party}
        Karakter: {self.character}
        Konum: {self.location}
        
        Gündem: {agenda}
        
        Önceki mesajlar:
        """
        
        for msg in previous_messages:
            prompt += f"\n{msg['role']}: {msg['content']}"
            
        prompt += f"\n\n{self.name} olarak cevabın:"
        prompt += "\n\nÖnemli: Cevabını kısa ve öz tut, en fazla 5-10 cümle olsun."
        
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

class KararsizAgent:
    def __init__(self):
        self.name = "Miraç"
        self.character = "Küskün ve kararsız bir seçmen. Siyasi kutuplaşmadan bunalmış, her iki tarafın da haklı olduğu noktaları görebilen ama hiçbir tarafa tam olarak güvenemeyen. Yolsuzluk iddialarından rahatsız olan, aynı zamanda bunların siyasi malzeme yapılmasından da bıkmış. 'Türkiye Yüzyılı' gibi hamasi söylemlere inanmayan, farklı fikirlere tahammülün azaldığından yakınan"
        self.model = genai.GenerativeModel('gemini-2.0-flash')
    
    def analyze_debate(self, agenda: str, messages: List[Dict]) -> str:
        """
        Analyze the debate and provide a comment as a disillusioned voter
        """
        # Add delay before API call
        time.sleep(5)
        
        # Construct the prompt
        prompt = f"""
        Sen "Miraç" adında bir vatandaşsın.
        Karakter: {self.character}
        
        Aşağıdaki siyasi tartışmayı dinledin ve şimdi yorum yapacaksın. 
        Her iki tarafın da haklı olduğu noktaları görebilirsin, ama genel olarak siyasi kutuplaşmadan ve hamasi söylemlerden bunalmış durumdasın.
        Yolsuzluk iddialarından rahatsız olursun, ama bunların siyasi malzeme yapılmasından da bıkmışsındır.
        
        Gündem: {agenda}
        
        Tartışma:
        """
        
        for msg in messages:
            prompt += f"\n{msg['role']}: {msg['content']}"
            
        prompt += f"\n\nSen bir kararsız ve küskün seçmen olarak bu tartışmaya yorumun:"
        prompt += "\n\nÖnemli: Tüm fikirlerini detaylı bir şekilde açıkla. Her iki tarafın da söylediklerini değerlendir, kendi görüşlerini paylaş ve siyasi kutuplaşma hakkındaki düşüncelerini belirt. Cümle sınırlaması yok, istediğin kadar uzun konuşabilirsin."
        
        # Generate response
        response = self.model.generate_content(prompt)
        return response.text.strip() 