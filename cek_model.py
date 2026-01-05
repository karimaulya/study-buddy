import google.generativeai as genai

# Ganti ini sama API KEY kamu yang tadi
genai.configure(api_key="AIzaSyBFv6JUriAwceCGEo-Yyc2aisjWnoVxmuQ") 

print("Mencari model yang tersedia...")
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)