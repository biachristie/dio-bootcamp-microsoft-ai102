import requests, os
from bs4 import BeautifulSoup
from langchain_openai.chat_models.azure import AzureChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def extract_text_from_url(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        for script_or_style in soup([ "script", "style" ]):
            script_or_style.decompose()

        text = soup.get_text(" ", strip=True)
        return text.encode("ASCII", "ignore").decode("ASCII")

    else:
        print(f"Failed to fetch the URL. Status code: { response.status_code }")
        return None


client = AzureChatOpenAI(
    azure_endpoint = os.getenv("AZURE_OAI_ENDPOINT"),
    api_key = os.getenv("AZURE_OAI_KEY"),
    api_version = os.getenv("AZURE_OAI_VERSION"),
    deployment_name = "gpt-4o-mini",
    max_retries = 0
)


def translate_article(text, lang):
    messages = [
        ( "system", "Você atua como tradutor de textos" ),
        ( "user", f"Traduza o { text } para o idioma { lang } e responda em markdown" )
    ]

    response = client.invoke(messages)
    print(response.content)
    return (response.content)


url = os.getenv("ARTICLE_URL")

text = extract_text_from_url(url)
article = translate_article(text.encode("utf-8").decode("utf-8"), "pt-br")


print(article)