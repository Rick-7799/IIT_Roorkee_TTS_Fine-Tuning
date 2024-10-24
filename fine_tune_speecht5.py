import torch
from datasets import load_dataset
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, Trainer, TrainingArguments
processor = SpeechT5Processor.from_pretrained("microsoft/speecht5-tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5-tts")
dataset = load_dataset('json', data_files='dataset.json')
def preprocess_function(examples):
    audio = processor(examples["audio_filepath"], sampling_rate=16000)
    text = processor(examples["text"], return_tensors="pt", padding=True)
    return {"input_ids": text.input_ids, "attention_mask": text.attention_mask}
processed_dataset = dataset.map(preprocess_function)
training_args = TrainingArguments(
    output_dir='fine_tuned_speecht5',
    per_device_train_batch_size=4,
    num_train_epochs=3,
    logging_dir='./logs',
)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=processed_dataset['train'],
)
trainer.train()
