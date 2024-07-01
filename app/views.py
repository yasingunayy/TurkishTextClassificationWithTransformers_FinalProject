from flask import Flask, render_template , request

from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)

tokenizer= AutoTokenizer.from_pretrained("dbmdz/bert-base-turkish-uncased")
model= AutoModelForSequenceClassification.from_pretrained(r"C:\Users\yguna\Desktop\FinalProject\app\model")

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


@app.route("/")

def home():
    return render_template("index.html")


@app.route("/predict" ,  methods=['POST'])
def result():
    inputText = request.form['text'] 
    prediction = code_to_label[nlp(inputText)[0]['label']] 
    contactNum = ""
    if prediction == 'Su ve Kanalizasyon':
        contactNum = "0324 332 11 11"
    elif prediction == 'Ulaşım':
        contactNum = "0324 336 22 22"
    elif prediction == 'Park ve Bahçeler':
        contactNum = "0324 336 33 33"
    elif prediction == 'Zabıta':
        contactNum = "0324 336 44 44"
    elif prediction == 'Temizlik İşleri':
        contactNum = "0324 336 55 55"
    elif prediction == 'Veteriner İşleri':
        contactNum = "0324 336 66 66"
    elif prediction == 'Sosyal Hizmet ve Yardımlar':
        contactNum = "0324 336 77 77"           
    else:
        contactNum = "0324 336 65 83"

    return render_template('result.html', prediction=prediction , contactNum=contactNum) 

if __name__ == '__main__':
    app.run(debug=True)    