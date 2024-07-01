from datasets import load_dataset

from transformers import AutoTokenizer,AutoModelForSequenceClassification
from transformers import TrainingArguments, Trainer

import numpy as np
import evaluate

train_dataset = load_dataset("csv", data_files={"train": "train.csv"})
val_dataset = load_dataset("csv", data_files={"validation": "validation.csv"})


tokenizer= AutoTokenizer.from_pretrained("dbmdz/bert-base-turkish-uncased")
model= AutoModelForSequenceClassification.from_pretrained("dbmdz/bert-base-turkish-uncased", num_labels=8)

def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

tokenized_train_dataset = train_dataset.map(tokenize_function, batched=True)
tokenized_validation_dataset =  val_dataset.map(tokenize_function, batched=True)

tuned_train_dataset = tokenized_train_dataset["train"].shuffle(seed=42)
tuned_eval_dataset = tokenized_validation_dataset["validation"].shuffle(seed=42)

metric = evaluate.load("accuracy")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)

training_args = TrainingArguments(
    output_dir="test_trainer", 
    evaluation_strategy="epoch", 
    num_train_epochs=3,
    learning_rate=0.0001
    )

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tuned_train_dataset,
    eval_dataset=tuned_eval_dataset,
    compute_metrics=compute_metrics,
)

trainer.train()
fine_tuned_model = trainer.model
fine_tuned_model.save_pretrained("./modelPack")
