from googletrans import Translator

translator = Translator()
sample_text = 'Hi my name is subash'
det = translator.detect(sample_text)
print(det)
output= translator.translate(sample_text, dest="ta")
print(output)
