\# EDA Summary — Titanic Dataset



\## Dataset Overview

891 rows, 12 columns. Target: Survived (binary classification).



\## Data Quality Issues Found

\- Age: \~20% missing, imputed with median

\- Cabin: \~77% missing, dropped entirely

\- Embarked: 2 rows missing, imputed with mode



\## Key Findings

1\. Survival rate is imbalanced (\~38% survived)

2\. Sex is the strongest predictor — women survived at 74.2%, men at 18.9%

3\. Passenger class strongly correlates with survival (1st: \~63%, 3rd: \~24%)

4\. Age shows a mild relationship — survivors skew slightly younger

5\. Embarked correlates with survival, likely as a proxy for Pclass 

&#x20;  (Cherbourg had more 1st class passengers)



\## Modelling Implications

\- Sex and Pclass are likely the strongest features

\- Consider handling class imbalance in the target

\- Watch for multicollinearity between Embarked and Pclass

