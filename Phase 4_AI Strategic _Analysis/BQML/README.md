### 4.1 Predictive Scoring via BigQuery ML (BQML)
Instead of moving data to external machine learning servers, a Logistic Regression model was trained directly inside the data warehouse using BigQuery ML. This approach reduces architectural complexity and operational costs.

**The Process:** The model was trained on the historical simulated dataset to learn the relationship between behavioral friction (hesitation, scroll depth) and the final purchase.

**The Output:** Using the `ML.PREDICT` function, the model assigns a precise conversion probability score to each session. 

**Business Logic Applied:** A SQL `CASE` statement routes these probabilities into actionable business segments:
  
    **High Risk (<30% probability):** Users likely to abandon the cart due to high friction.
   
    **Medium Risk (30% - 70% probability):** Undecided users requiring subtle nudges.
    
    **Low Risk (>70% probability):** Highly engaged users likely to convert without intervention.
