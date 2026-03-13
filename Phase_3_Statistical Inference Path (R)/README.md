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

### 3.3 Key Findings
The calculations revealed two main conclusions:
* **Impact of Hesitation:** The numbers clearly proved that spending more seconds hesitating in front of the payment button reduces the chance of completing the transaction.
* **Impact of Scrolling:** We noticed a very clear split in visitor behavior. People who scrolled deeply down the page completed the purchase, while those who barely scrolled abandoned the cart.

3.4 Statistical Data Visualization (DataViz)
To visually communicate the mathematical mechanics to non-technical stakeholders, a Logistic Probability Curve (Sigmoid) was plotted using ggplot2.

[Insert your English plot image here]

Visual Insight: The plot clearly illustrates the "Complete Separation" phenomenon. The sharp S-curve demonstrates how scroll depth acts as a perfect predictor in this dataset, while the expanded confidence band visually represents the algorithm's standard error calculation behavior under these deterministic conditions.





