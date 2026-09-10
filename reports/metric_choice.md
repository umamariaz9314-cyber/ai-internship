\# Metric Choice — Classification



\## Why Not Just Accuracy?

Accuracy is misleading on imbalanced data — a model that always 

predicts the majority class can score high accuracy while being 

completely useless.



\## My Approach

\- For balanced problems, I use precision, recall, and F1 alongside 

&#x20; accuracy for a fuller picture.

\- For imbalanced problems, I prioritise PR-AUC over ROC-AUC, since 

&#x20; ROC-AUC can look optimistic when negatives dominate.

\- I choose the decision threshold based on business cost: lower 

&#x20; threshold when missing positives is costly, higher threshold 

&#x20; when false alarms are costly.

\- I check calibration when predicted probabilities themselves need 

&#x20; to be trusted (e.g., "there's a 90% chance"), not just the 

&#x20; ranking of predictions.



\## Key Takeaway

The "right" metric depends on the cost of each error type in the 

specific business context — there's no universal best metric.

