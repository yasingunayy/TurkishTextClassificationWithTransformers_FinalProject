from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

tokenizer= AutoTokenizer.from_pretrained("dbmdz/bert-base-turkish-uncased")
model= AutoModelForSequenceClassification.from_pretrained("modelPack")

nlp=pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

code_to_label={
 'LABEL_0': 'Su ve Kanalizasyon',
 'LABEL_1': 'Ulaşım',
 'LABEL_2': 'Park ve Bahçeler',
 'LABEL_3': 'Zabıta',
 'LABEL_4': 'Temizlik İşleri' ,
 'LABEL_5': 'Veteriner İşleri',
 'LABEL_6': 'Sosyal Hizmet ve Yardımlar',
 'LABEL_7': 'Diğer' }

while True:
    inputText = input("Belediyeye İletmek İstediğiniz Şikayetinizi Giriniz: ")
    if inputText!='end':
        print(code_to_label[nlp(inputText)[0]['label']])
    else:
        break
