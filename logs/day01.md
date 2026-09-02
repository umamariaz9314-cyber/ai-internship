\# Day 1: ML Problem Framing Exercise



\## 1. Spam Filter

\- Is this ML? Yes

\- Type: Supervised — Classification (binary: spam/not spam)

\- Label: Whether an email is spam or not (0/1)

\- Unit of prediction: One email

\- Business metric: Precision (avoid marking real emails as spam), 

&#x20; Recall also matters (catch actual spam)



\## 2. Delivery ETA

\- Is this ML? Yes

\- Type: Supervised — Regression (predicting a time value)

\- Label: Actual delivery time (minutes/hours)

\- Unit of prediction: One delivery order

\- Business metric: MAE (Mean Absolute Error) in minutes, tied to 

&#x20; customer satisfaction



\## 3. Customer Churn

\- Is this ML? Yes

\- Type: Supervised — Classification (churn/no churn)

\- Label: Whether a customer will leave in the next 30 days

\- Unit of prediction: One customer

\- Business metric: Recall (catch likely churners) balanced with 

&#x20; precision (marketing cost control)



\## 4. Photo Tagging

\- Is this ML? Yes

\- Type: Supervised (multi-label classification) or self-supervised 

&#x20; with pretrained models

\- Label: Objects/people present in the image

\- Unit of prediction: One photo

\- Business metric: Accuracy/F1 score per tag



\## 5. Chat Support Bot

\- Is this ML? Yes (partially — simple cases can be rule-based)

\- Type: Hybrid — intent classification + response generation, or 

&#x20; LLM-based

\- Label: Correct intent/response

\- Unit of prediction: One user message/conversation

\- Business metric: Resolution rate, customer satisfaction score, 

&#x20; escalation rate

