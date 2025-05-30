Cross-Linguistic Emotional Expression

A Comparative Analysis of Emotion Scores in English and Italian Using Mistral LLM
Project Overview

This project was developed for the Cognitive Data Science Hackathon at the University of Trento. It investigates cross-linguistic emotional expression in English and Italian by analyzing eight core emotions—anger, joy, trust, sadness, disgust, fear, anticipation, and surprise—as expressed in responses from Mistral LLM.
We analyze how the same prompts, expressed in both languages, yield different emotional scores when passed through the EmoAtlas emotion analysis model.

Methodology

1. Data Collection
70 prompts were generated asking for opinions, translated into both English and Italian.
Each prompt was submitted separately in each language to the Mistral LLM, generating distinct responses.
The final dataset includes 550 samples, each containing an English and Italian prompt/response pair.
2. Emotion Analysis
Responses were scored using EmoAtlas, a tool for extracting standardized z-scores for emotional content.
3. Modeling
The Mistral LLM generated responses using identical prompts in English and Italian.
Responses were processed independently for each language, and emotion scores were extracted.
4. Statistical Comparison
Scores were compared emotion-by-emotion between English and Italian.
Paired t-tests were used to assess whether emotion scores differed significantly between the two languages.

Results and Insights

Key Statistical Results:
Emotion	p-value	Significant?
Anger	0.234	No
Joy	0.0029	✅ Yes
Trust	2.08e-13	✅✅✅ Extremely significant
Sadness	6.66e-11	✅ Yes
Disgust	1.31e-07	✅ Yes
Fear	0.916	No
Anticipation	0.016	✅ Yes
Surprise	2.25e-06	✅ Yes
🔍 Deeper Findings
Low cross-linguistic correlation (r ≈ 0.2) and a mean absolute error (MAE) of 0.9_ reveal substantial differences in emotional expression across the two languages.
A heatmap of standardized z-scores (see heat_maps.png) highlights trust and anticipation as dimensions with the strongest divergences.
“These findings suggest that linguistic structure and cultural norms play critical roles in shaping how emotions are verbalized.”

Theoretical Insight
Recent work by Moroni et al. (2025) on Semantic Alignment Vocabulary Adaptation (SAVA) shows how token optimization can significantly impact LLM performance in Italian. Although their method focuses on vocabulary redundancy reduction (25% in Mistral-7B-v0.1), it underscores how finetuning for Italian affects emotion expression, shedding light on why Mistral might produce emotionally divergent content depending on language.


Technologies Used

Python
Mistral LLM
EmoAtlas (emotion scoring)


# Clone the repository
git clone https://github.com/tercasaskova311/Comparing-Emotional-Scores-of-Mistral-LLM-Responses-via-EmoAtlas.git

# Navigate to the project directory
cd Crosslinguistics_emotional_expression

# Install required packages
pip install -r requirements.txt

Future Work and Improvements

Expand analysis to more languages and cultural contexts.
Integrate additional emotion classifiers to validate results.
Develop an interactive dashboard to visualize and compare responses and scores in real time.


Acknowledgments

University of Trento – Cognitive Data Science Hackathon
Prof. Stella
Mistral LLM – Open LLM used for response generation
EmoAtlas – Emotion vector scoring
