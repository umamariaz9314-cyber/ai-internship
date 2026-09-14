\# Model Card: Customer Churn Predictor



\## Intended Use

This model predicts the probability that a telecom customer will 

churn (cancel their subscription) within the near future. It is 

intended to support the retention team in prioritising outreach 

to at-risk customers — it is a decision-support tool, not an 

automated action-taker.



\## Training Data

7,043 customer records from a telecom provider, including account 

information (tenure, contract type, payment method), services used 

(internet, phone, streaming), and billing details (monthly/total 

charges). About 27% of customers in this dataset churned.



\## Metrics

\- Test Accuracy: \[fill in from your results]

\- Test Precision: \[fill in]

\- Test Recall: \[fill in]

\- Test ROC-AUC: \[fill in]



\## Limitations

\- The model was trained on historical data and may not generalise 

&#x20; to new pricing plans or services not present in training data.

\- Performance varies across customer segments (see error analysis) 

&#x20; — accuracy is lower for certain contract types and payment methods.

\- The model does not account for external factors like competitor 

&#x20; pricing changes or economic conditions.



\## Ethical Considerations

\- Predictions should not be used to justify discriminatory pricing 

&#x20; or service denial based on protected attributes.

\- The model should be periodically re-evaluated for fairness across 

&#x20; demographic segments (see fairness check, if completed).

\- False positives (predicting churn incorrectly) could lead to 

&#x20; unnecessary retention spending; false negatives mean missed 

&#x20; intervention opportunities — the cost of each should inform the 

&#x20; chosen decision threshold in production.

