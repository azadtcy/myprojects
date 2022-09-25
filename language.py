pip install langedetect
from langdetect import detect
text = input("Enter text in any language")
print(detect(text))