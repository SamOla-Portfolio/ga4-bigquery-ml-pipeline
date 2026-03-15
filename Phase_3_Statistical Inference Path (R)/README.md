## Phase 3: Data Analysis and Behavior Understanding

The goal of this phase is to use numbers to confirm that user behavior (like hesitating before clicking) actually impacts the purchase decision, and that our findings aren't just a coincidence.

### 3.1 Data Preparation
We imported the dataset containing 538 user sessions. This file includes specific details for each visitor: hesitation time, how far they scrolled down the page, and their final decision (purchase or abandon).

### 3.2Logistic Regression Modeling
Built a generalized linear model (`glm`) to evaluate the impact of independent behavioral variables on the binary target variable (`is_buyer`):
```R
friction_model <- glm(is_buyer ~ hesitation_seconds + scroll_depth_percent, 
                      family = "binomial", 
                      data = friction_data)
```
### 3.3 Key Findings
The calculations revealed two main conclusions:
* **Impact of Hesitation:** The numbers clearly proved that spending more seconds hesitating in front of the payment button reduces the chance of completing the transaction.
* **Impact of Scrolling:** We noticed a very clear split in visitor behavior. People who scrolled deeply down the page completed the purchase, while those who barely scrolled abandoned the cart.

### 3.4 Statistical Data Visualization (DataViz)
To visually communicate the mathematical mechanics to non-technical stakeholders, a Logistic Probability Curve (Sigmoid) was plotted using ggplot2.


Visual Insight: The plot clearly illustrates the "Complete Separation" phenomenon. The sharp S-curve demonstrates how scroll depth acts as a perfect predictor in this dataset, while the expanded confidence band visually represents the algorithm's standard error calculation behavior under these deterministic conditions.

### 3.5 Project Limitations and Real-World Considerations
Since this is a Proof of Concept (PoC) using simulated data, there are a few practical limitations to keep in mind:

* **The "Too Perfect" Data:** Because our synthetic data created a strict rule (e.g., everyone who scrolled deep enough made a purchase), standard statistical tests struggle to process it. The model's math is designed for real-world uncertainty, not absolute certainty.
* **Missing Context:** We only measured hesitation and scroll depth. In a live business environment, we would need to feed the model with other factors that affect buying decisions, such as device type (mobile vs. desktop), traffic source, and time of day.
* **Unrealistic Outliers:** Some simulated sessions included unnaturally long hesitation times (representing a user who might have left the tab open and walked away). Before deploying this system in a real company, strict data cleaning rules must be applied to filter out these extreme cases so they do not confuse the predictions.




