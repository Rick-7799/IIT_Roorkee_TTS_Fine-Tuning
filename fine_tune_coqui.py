from TTS.api import TTS
import json
model_name = 'tts_models/en/ljspeech/tacotron2-DDC'
tts = TTS(model_name=model_name)
with open('dataset.json', 'r') as f:
    config = json.load(f)
config['datasets'] = 'dataset.json'
config['output_path'] = 'fine_tuned_model/' 
tts.train(config)
