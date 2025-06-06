# Cross-Linguistic Emotional Expression  
**A Comparative Analysis of Emotion Scores in English and Italian Using Mistral LLM**

## Project Overview

This project was developed during the Cognitive Data Science Hackathon at the University of Trento. It explores cross-linguistic differences in emotional expression by analyzing the emotion scores of responses generated by the Mistral LLM in English and Italian. The analysis focuses on eight basic emotions: anger, joy, trust, sadness, disgust, fear, anticipation, and surprise.

A total of 550 samples were generated from prompts formulated in both English and Italian. The aim was to investigate how identical opinion-seeking prompts yield emotionally distinct responses in different languages.

## Methodology

### Data Collection

- 550 opinion-seeking prompts were generated in both English and Italian.
- Each prompt was used to query the Mistral LLM separately in each language.
- Responses were collected independently, resulting in a bilingual dataset of 550 paired samples.

### Emotion Analysis

- Responses were processed using EmoAtlas, a tool for extracting standardized z-scores across eight basic emotions.
- Each response was scored individually for each emotion.

### Modeling

- The Mistral LLM was queried for each prompt using both English and Italian input.
- Emotional responses were collected and analyzed separately for each language.

### Statistical Comparison

- Paired t-tests were used to assess whether there were statistically significant differences in emotion scores between the English and Italian responses.

## Results and Insights

### Statistical Summary

| Emotion       | p-value   | Significant?             |
|---------------|-----------|--------------------------|
| Anger         | 0.234     | No                       |
| Joy           | 0.0029    | Yes                      |
| Trust         | 2.08e-13  | Yes (highly significant) |
| Sadness       | 6.66e-11  | Yes                      |
| Disgust       | 1.31e-07  | Yes                      |
| Fear          | 0.916     | No                       |
| Anticipation  | 0.016     | Yes                      |
| Surprise      | 2.25e-06  | Yes                      |

### Heat Map of Emotion Scores
![Heat map](https://github.com/tercasaskova311/Comparing-Emotional-Scores-of-Mistral-LLM-Responses-via-EmoAtlas/blob/4e7a71073212105e260bef6a5908982ae16044fb/heat_maps.png)


## Visualizations

### Principal Component Analysis (PCA)
![PCA plot](https://github.com/tercasaskova311/Comparing-Emotional-Scores-of-Mistral-LLM-Responses-via-EmoAtlas/blob/76b50c3eb49b8d49790f5c8e53f5ee83948a05e3/PCA.png)

### Radar Plot of Emotion Scores
![Radar plot](https://github.com/tercasaskova311/Comparing-Emotional-Scores-of-Mistral-LLM-Responses-via-EmoAtlas/blob/9e8c902b9f4ab1fd9e6b752d63fdded39d32653b/radarplot.png)


### Key Observations

- Emotional intensity and structure vary significantly across languages.
- The correlation between English and Italian emotion scores was low (r ≈ 0.2).
- The mean absolute error (MAE) between emotion scores in the two languages was 0.9.
- Trust and anticipation displayed the largest cross-linguistic divergences, as visualized in the heatmap of standardized z-scores (see `heat_maps.png`).

These findings suggest that linguistic structure and cultural norms can influence emotional expression. Differences in tokenization and vocabulary efficiency also play a role, especially in language models optimized for specific languages.

## Theoretical Context

The results align with prior research indicating that language influences emotional expression. Moroni et al. (2025) introduced a method called Semantic Alignment Vocabulary Adaptation (SAVA), which improves LLM performance in Italian by reducing token redundancy. While primarily aimed at boosting general performance, their findings highlight how language-specific finetuning can impact the expressiveness of large language models. This has implications for affective computing and multilingual LLM development.

## Technologies Used

- Python
- Mistral LLM
- EmoAtlas
- Pandas, NumPy
- Matplotlib, Seaborn

## Setup and Installation

To set up the project:

```bash
git clone https://github.com/tercasaskova311/Comparing-Emotional-Scores-of-Mistral-LLM-Responses-via-EmoAtlas.git
cd Crosslinguistics_emotional_expression
pip install -r requirements.txt
