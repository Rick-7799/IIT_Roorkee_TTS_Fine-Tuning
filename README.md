
# TTS Fine-Tuning Assignment

Welcome to the TTS Fine-Tuning Assignment repository! This project focuses on enhancing Text-to-Speech (TTS) models for both English technical speech and a selected regional language[Hindi]. The aim is to fine-tune existing models to improve their performance in specialized contexts, such as technical jargon and regional dialects.

## Table of Contents

- [Project Overview](#project-overview)
- [Branches](#branches)
- [Installation](#installation)
- [Usage](#usage)

## Project Overview

Text-to-Speech technology has become increasingly important in various applications, including virtual assistants, accessibility tools, and language learning platforms. This assignment involves:

- Fine-tuning TTS models to accurately pronounce technical terms commonly used in English technical interviews.
- Adapting TTS models for a regional language to ensure naturalness and intelligibility.
- Implementing optimization techniques such as quantization to enhance model efficiency.

## Branches

This repository contains the following branches:

- **[Task 1: English Technical Speech]**: 
  - Focuses on fine-tuning a TTS model for English technical vocabulary. Includes detailed reports and code snippets.
  
- **[Task 2: Regional Language TTS]**: 
  - Covers the fine-tuning of a TTS model for a selected regional language[Hindi]. Contains comprehensive evaluation results and methodologies.
  
- **[Bonus-Task]**: 
  - Discusses optimization strategies employed to improve inference speed and model size, including code examples.

- **[Final Report]**: 
  - A comprehensive overview of the entire assignment, including methodologies for fine-tuning TTS models for both English technical speech and a regional language. This report consolidates results, challenges faced, and key takeaways from the project.

## Installation

To get started with this project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Rick-7799/IIT_Roorkee_TTS_Fine-Tuning.git
   ```

2. **Navigate into the Directory**:
   ```bash
   cd IIT_Roorkee_TTS_Fine-Tuning
   ```

3. **Install Required Packages**:
   Make sure you have Python installed (preferably version 3.6 or later). Then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the fine-tuning scripts for each task, use the following commands:

### For Task 1 (English Technical Speech):
```bash
python src/fine_tune_coqui.py
```

### For Task 2 (Regional Language):
```bash
python src/fine_tune_speecht5.py
```
