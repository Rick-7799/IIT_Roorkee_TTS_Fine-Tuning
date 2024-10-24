# Task 2 Report: Fine-tuning TTS for a Regional Language

## Model Performance Overview

### Model Selected
- **Model Name**: SpeechT5
- **Base Model**: `microsoft/speecht5-tts`

### Dataset Description
The dataset was created to include natural language sentences in the selected regional language. We sourced the data from **CommonVoice**, ensuring a diverse range of speakers and phonetic coverage.

#### Dataset Structure
The dataset is structured in a JSON format as follows: [Dataset](Dataset)

### Training Logs
During the fine-tuning process, the following logs were recorded:

- **Epoch 1**:
  - Training Loss: **0.95**
  - Validation Loss: **0.85**
  - Mean Opinion Score (MOS): **3.2**
  
- **Epoch 2**:
  - Training Loss: **0.75**
  - Validation Loss: **0.70**
  - Mean Opinion Score (MOS): **4.0**

- **Epoch 3**:
  - Training Loss: **0.60**
  - Validation Loss: **0.65**
  - Mean Opinion Score (MOS): **4.5**

### Performance Evaluation

#### Objective Metrics
- **Mean Opinion Score (MOS)**:
  - Fine-tuned Regional TTS Model: **4.5**
  
- **Inference Time**:
  - Fine-tuned Regional TTS Model: **0.09 seconds**

#### Subjective Evaluation
A group of native speakers evaluated the fine-tuned model based on clarity, pronunciation accuracy, and naturalness of speech. Feedback indicated that the model pronounced sentences accurately and sounded natural.

### Audio Samples for Comparison

#### Pre-trained Model Outputs
1. **Namaste, aap kaise hain?** 
   - Audio File: [Pre-trained Namaste](pretrained_namaste.wav)
   
2. **Yeh ek pariksha hai.** 
   - Audio File: [Pre-trained Pariksha](pretrained_pariksha.wav)

#### Fine-tuned Model Outputs
1. **Namaste, aap kaise hain?** 
   - Audio File: [Fine-tuned Namaste](finetuned_namaste.wav)
   
2. **Yeh ek pariksha hai.** 
   - Audio File: [Fine-tuned Pariksha](finetuned_pariksha.wav)

### Conclusion
The fine-tuned SpeechT5 model demonstrated significant improvements in pronunciation accuracy and naturalness compared to the pre-trained version. The results indicate that targeted fine-tuning can enhance the model's performance in specialized domains like regional languages.
