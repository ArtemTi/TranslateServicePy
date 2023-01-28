from googletrans import Translator
from fastapi import FastAPI
from pydantic import BaseModel


class TextModel(BaseModel):
    text: str


app = FastAPI()
translator = Translator()


@app.post('/api/translate')
async def translate_text(text: TextModel):
    translatedText = translator.translate(text.text)
    return {'translatedText': translatedText.text, 'lang': translatedText.src}
