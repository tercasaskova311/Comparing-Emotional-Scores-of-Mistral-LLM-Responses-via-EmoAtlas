# Cross-Linguistic Emotional Expression
A Comparative Analysis of Emotion Scores in English and Italian Using Mistral LLM

Project Overview

This project was developed as part of the Cognitive Data Science Hackathon at University of Trento. It explores the cross-linguistic differences in emotional expression in responses of Mistral LLM between English and Italian by analyzing emotion scores of these responses for eight basic emotions: anger, joy, trust, sadness, disgust, fear, anticipation, and surprise. The dataset comprises 550 samples of responses to various prompts which were generated in both languages based on the following request:

"I want to make multiple prompts to an LLM with the same phrase in English and Italian, and I want to use a JSON file. I need 70 phrases, each needs to ask for opinions. Can you make that JSON for me, with all the 70 phrases?"



## Methodology

Data Collection: Same prompts were collected in both English and Italian with asking separately for response in English and Italian, resulting in different responses, with dataset of 550 samples.

Emotion Analysis: Emotion scores were extracted using EmoAtlas, a tool for vectorization and normalization of emotional content.

Modeling: The Mistral LLM was employed to process and generate responses based on the prompts give by Mistral for opinion needed questions in both languages.

Comparison: Emotional scores for the eight emotions were compared between the two languages to identify possible patterns and discrepancies.



## Results and Insights

The analysis revealed some differences in emotional intensity and expression given two languages. Key findings include:

Anger: Higher intensity in Italian responses.

Joy and Trust: Stronger expressions in English responses.

Sadness and Disgust: Minor cross-linguistic differences.

These findings provide valuable insights into the dynamics of multilingual emotional expression, contributing to the fields of multilingual communication and affective computing.

![heat_map](https://github.com/user-attachments/assets/9f1caa1b-c3c9-4052-ae09-02f818ffcb31)


## Technologies Used

Python

Mistral LLM

EmoAtlas

Data Analysis Libraries (e.g., pandas, numpy)

Visualization Libraries (e.g., matplotlib, seaborn)



## Setup and Installation

Clone the repository:

git clone https://github.com/username/Crosslinguistics_emotional_expression.git

Navigate to the project directory:

cd Crosslinguistics_emotional_expression

Install required packages:

pip install -r requirements.txt



## Usage




## Future Work and Improvements

Expand the dataset to include more languages and samples.

Apply additional emotional analysis tools to validate the findings.

Develop a visualization dashboard for interactive exploration of results.



## Contributors

Your Name (@)

Collaborator Name (@collaborator)

Acknowledgments

Cognitive Data Science Hackathon

Mistral LLM

EmoAtlas


