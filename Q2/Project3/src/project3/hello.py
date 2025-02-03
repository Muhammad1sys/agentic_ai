from litellm import completion
import os

os.environ['GEMINI_API_KEY'] = "AIzaSyC1radSULyU8WKvEqkEZbcFXCoUys2s1vs"


def call_gemini():
    response = completion(
    model="gemini/gemini-1.5-flash", 
    messages=[{"role": "user", "content": "write code for saying hi from LiteLLM"}]
    )

    print(response ['choices'][0]['message']['content'])
    
def call_gemini():
    response = completion(
    model="gemini/gemini-1.5-flash", 
    messages=[{"role": "user", "content": "who is the founder of piaic?"}]
    )

    print(response ['choices'][0]['message']['content'])