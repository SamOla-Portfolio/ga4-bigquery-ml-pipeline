# ga4-bigquery-ml-pipeline
End-to-end data pipeline analyzing user hesitation and purchase probability using GA4, BigQuery, and R.

# Case Study: The Psychological Friction Score in E-commerce

## 1. The Purpose of the Project
Traditional web analytics usually focus on whether a user bought something or left. This project looks at the "gray area" in between by measuring silent user hesitation (psychological friction) during checkout. The goal is to build a reliable system that finds where users struggle and instantly shows them helpful messages to save the sale before they abandon their cart. This is a test project using 500 simulated visits to demonstrate a practical, business-focused approach.

## 2. Research Questions
This project aims to answer the following core question:
* "How can we accurately measure invisible user behaviours (like hesitation) to predict cart abandonment, and instantly intervene with pre-generated AI assistance without compromising website performance?"

## 3. Underlying Theories and Principles
The project relies on two behavioural theories and one practical system design rule:
* **Cognitive Load Theory:** Human working memory has a limited capacity. Complex interfaces or stressful financial decisions increase mental effort. Since we cannot measure the mind directly, we use **Hesitation Time (in seconds)** as a measurable stand-in. More hesitation suggests higher mental effort and confusion.
* **Fogg Behaviour Model:** A behaviour only happens when Motivation, Ability, and a Prompt occur at the same time. When a user reaches the payment button, the prompt is clearly there. If they hesitate, we assume there is an issue with their Ability (the form is confusing) or Motivation (lack of trust), which our system will try to resolve.
* **Practical System Design:** Deep data analysis tools are too slow to run while a user is actively waiting on a webpage. To keep the site fast, the system calculates risk levels in advance and generates help messages in the background. This allows the website to display the right message instantly when a user gets stuck.

## 4. Hypotheses
* **H1:** Users exhibiting high hesitation time (e.g., >15 seconds) during the checkout process have a statistically significant higher probability of cart abandonment compared to baseline users.
* **H2:** Generating AI help messages in the background allows for instant intervention when a user hesitates, reducing cart abandonment without slowing down the website.

## 5. Dataset Overview (Data Dictionary)

The dataset used in this Proof of Concept (PoC) is synthetically generated via a Python simulation. It is designed to mimic custom behavioral event tracking (e.g., via Google Tag Manager and GA4) that captures micro-interactions often missed by default configurations. The dataset consists of 538 user sessions.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `session_id` | String | A unique alphanumeric identifier for each user session. |
| `hesitation_seconds` | Numeric (Float) | The exact time in seconds a user spent idle or hesitating before clicking the final call-to-action (e.g., "Confirm Purchase") button. |
| `scroll_depth_percent` | Numeric (Integer) | The maximum scroll depth reached by the user on the product or checkout page, ranging from 0% to 100%. |
| `is_buyer` | Binary (Integer) | **Target Variable:** Indicates the final conversion outcome. `1` represents a completed purchase, while `0` represents cart abandonment. |

## 6. Expected Results and Deliverables
This project delivers a complete, end-to-end analytical solution:
* **Predictive ML Model**: A logistic regression model (built via BigQuery ML) that quantifies the exact relationship between user hesitation time and the probability of cart abandonment.
* **Automated Data Architecture**: A robust SQL pipeline that flattens complex, nested GA4 behavioral data into structured, analysis-ready tables without data loss.
* **Executive BI Dashboard**: An interactive Looker Studio dashboard that maps the "Behavioral Friction Funnel," translating abstract user interactions into concrete financial metrics (e.g., Revenue at Risk and Predicted Abandonment Rate).
* **Qualitative GenAI Insights**: A Python-based automation script that processes statistical anomalies and generates readable, qualitative narratives explaining user drop-offs.


## 7. Privacy and Consent (Consent Mode v2)
Modern data projects must balance tracking user behaviour with respecting privacy laws like GDPR and the ePrivacy Directive. This project uses **Google Advanced Consent Mode v2** to stay legally compliant without losing the analytical signals needed for our AI models.

## 8. Proposed Testing Methodology (A/B Testing)
Since this is a simulated portfolio project, the system was evaluated offline (model accuracy, precision, recall). In a real-world production environment, Hypothesis 2 (H2) would be validated using a rigorous A/B test:

* Control Group (A): Users go through the standard checkout process without any AI intervention.
* Variant Group (B): High-risk users (Hesitation > 15s) receive the pre-generated AI help message instantly.
* Key Metrics to Track:
  1. Primary Metric: Checkout Completion Rate (Expected to increase in Group B).
  2. Guardrail Metric 1: Average Page Load Latency (Must remain equal between A and B to prove background processing works).
  3. Guardrail Metric 2: Help Message Dismissal Rate (To measure if the AI message was perceived as annoying).
     
### What happens when a user clicks "Reject"?
If a user refuses tracking, the system doesn't stop working; it fundamentally changes how it collects data:
* **No Cookies or Storage:** It strictly avoids writing or reading *any* identifiers in cookies, Local Storage, or Session Storage.
* **Cookieless Pings:** It sends anonymous pings to Google Analytics. It records the action (like hesitating on a form) but strips the payload of all personal identifiers.
* **Anonymous Data:** In our BigQuery database, the user's ID column (`user_pseudo_id`) is strictly recorded as `NULL`.

### How the Analytics Pipeline Survives (Event-Level Inference)
Since we cannot legally stitch a user's session together using local storage IDs after a rejection, the architecture relies on two compliant methods:
1. **Event-Level Enrichment:** Instead of tracking variables across time, the frontend script holds behavioral metrics (scroll depth and hesitation time) in temporary execution memory. When the final user action occurs (e.g., a purchase or an abandonment), these metrics are appended directly to that single, final ping as `event_parameters`. 
2. **Behavioral Modeling:** The system relies on Google Analytics 4's backend machine learning. It uses the behavioral patterns of consenting users to accurately model the friction points of unconsenting users, filling the analytical gaps without tracking individuals.

### The Engineering Trade-Off
Here is how the user's choice impacts the data architecture:

| User Choice | Privacy Compliance | BigQuery Data Structure | System Capabilities |
| :--- | :--- | :--- | :--- |
| **Accept** | Fully Compliant | Complete (User ID + Session Data) | AI Dashboard Insights **AND** Ad Retargeting. |
| **Reject** | Strictly Compliant (No Storage) | Anonymous (Event-Level & Modeled Only) | AI Dashboard Insights **ONLY**. (Ads are completely disabled). |
  <img width="666" height="831" alt="diagram" src="https://github.com/user-attachments/assets/a9076e3e-41c7-44b4-95c2-279930acbd9b" />
