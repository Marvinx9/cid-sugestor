import os
from dotenv import load_dotenv

import vertexai
from vertexai.generative_models import GenerativeModel
from google.oauth2 import service_account

load_dotenv()

CREDENTIALS_PATH = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
GEMINI_CID_SUGESTOR = os.getenv("GEMINI_CID_SUGESTOR")

credentials = service_account.Credentials.from_service_account_file(
    CREDENTIALS_PATH
)

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    credentials=credentials
)

model = GenerativeModel(GEMINI_CID_SUGESTOR)

def generate_response(message: str) -> str:
    if message is not None:
        prompt = f"""Você é especialista em sugerir códigos CID-10 baseado em textos de anamnese.
        você vai receber um texto com o padrão = texto: 'anamnese' e deve retornar sempre no padrão abaixo
        
        CID provável: 'código' - 'nome do cid'
        
        MUITO IMPORTAMTE: Você não pode retornar em hipótese alguma uma mensagem diferente da exemplificada
        e também não pode sugerir mais de 1 CID-10, você só pode sugerir 1 opção.
        
        Abaixo segue alguns exemplos de textos que você vai receber e como deve retornar:
        
        EXEMPLO 1
        texto: Paciente relata início há 3 dias de febre baixa, coriza, dor de garganta e tosse seca.
        Refere mal-estar generalizado e leve dor no corpo. Nega falta de ar, nega dor torácica. Sem comorbidades relevantes.
        
        você deve responder com: 'CID provável: J06.9 - Infecção aguda das vias aéreas superiores, não especificada'
        
        Exemplo 2
        texto: Paciente refere dor em queimação na região epigástrica há 2 semanas, piora após refeições pesadas 
        e melhora com alimentação leve. Relata azia frequente e episódios de náusea. Niega vômitos com sangue ou 
        fezes escuras.
        
        você deve responder com: 'CID provável: K29.5 - Gastrite crônica não especificada'
        
        Segue abaixo o texto que você deve sugerir o CID
        
        texto: {message}
        """
        
        response = model.generate_content(prompt)
        message = None
        return response.text
