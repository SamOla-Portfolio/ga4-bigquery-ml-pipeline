# ga4-bigquery-ml-pipeline
End-to-end data pipeline analyzing user hesitation and purchase probability using GA4, BigQuery, and R.

# Case Study: The Psychological Friction Score in E-commerce

## 1. The Purpose of the Project
Traditional web analytics usually focus on whether a user bought something or left. This project looks at the "gray area" in between by measuring silent user hesitation (psychological friction) during checkout. The goal is to build a reliable system that finds where users struggle and instantly shows them helpful messages to save the sale before they abandon their cart. This is a test project using 500 simulated visits to demonstrate a practical, business-focused approach.

## 2. Research Questions
This project aims to answer three practical questions:
* **Measurement:** How can we accurately measure invisible behaviors, like hesitation time and scrolling, without slowing down the website?
* **Connection:** What is the exact relationship between a user hesitating at certain form fields and the likelihood of them leaving without buying?
* **Action:** How can we deliver AI-powered help to a struggling user instantly, without waiting for slow, live text generation while the user is trying to check out?

## 3. Underlying Theories and Principles
The project relies on two behavioural theories and one practical system design rule:
* **Cognitive Load Theory:** Human working memory has a limited capacity. Complex interfaces or stressful financial decisions increase mental effort. Since we cannot measure the mind directly, we use **Hesitation Time (in seconds)** as a measurable stand-in. More hesitation suggests higher mental effort and confusion.
* **Fogg Behaviour Model:** A behaviour only happens when Motivation, Ability, and a Prompt occur at the same time. When a user reaches the payment button, the prompt is clearly there. If they hesitate, we assume there is an issue with their Ability (the form is confusing) or Motivation (lack of trust), which our system will try to resolve.
* **Practical System Design:** Deep data analysis tools are too slow to run while a user is actively waiting on a webpage. To keep the site fast, the system calculates risk levels in advance and generates help messages in the background. This allows the website to display the right message instantly when a user gets stuck.

## 4. Hypotheses
* **H1:** An increase in hesitation time at complex checkout fields leads to a measurable drop in completed sales.
* **H2:** By preparing AI help messages in the background rather than generating them live, we can intervene during moments of frustration instantly, avoiding site delays that would otherwise ruin the shopping experience.

## Dataset Overview (Data Dictionary)

The dataset used in this Proof of Concept (PoC) is synthetically generated via a Python simulation. It is designed to mimic custom behavioral event tracking (e.g., via Google Tag Manager and GA4) that captures micro-interactions often missed by default configurations. The dataset consists of 538 user sessions.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `session_id` | String | A unique alphanumeric identifier for each user session. |
| `hesitation_seconds` | Numeric (Float) | The exact time in seconds a user spent idle or hesitating before clicking the final call-to-action (e.g., "Confirm Purchase") button. |
| `scroll_depth_percent` | Numeric (Integer) | The maximum scroll depth reached by the user on the product or checkout page, ranging from 0% to 100%. |
| `is_buyer` | Binary (Integer) | **Target Variable:** Indicates the final conversion outcome. `1` represents a completed purchase, while `0` represents cart abandonment. |

## 5. Expected Results and Deliverables
The expected outcome is a practical business solution:
* **Statistical Proof:** A mathematical model that calculates exactly how much sales are lost due to user hesitation.
* **System Design:** Documentation showing how to balance smart data predictions with a fast, delay-free website.
* **Business Scorecard:** A visual dashboard that translates user behaviour into clear financial numbers, focusing on "Revenue at Risk" and "Saved Sales" rather than basic page views.

## 6. Privacy and Consent (Consent Mode v2)

Modern data projects must balance tracking user behavior with respecting privacy laws like GDPR and the ePrivacy Directive. This project uses **Google Advanced Consent Mode v2** to stay legally compliant without losing the analytical signals needed for our AI models.

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
  
```mermaid
graph TD
    %% Phase 1
    subgraph P1 [1. Behavioral Ingestion]
        A[User Interaction] -->|GTM / Consent v2| B(Google Tag Manager)
        B -->|Hesitation & Scroll| C(GA4 Events)
    end

    %% Phase 2
    subgraph P2 [2. Data & Simulation]
        C -->|Daily Batch| D[(BigQuery Warehouse)]
        E[Python Synthetic Data] -->|500 sessions PoC| D
        D -->|SQL Flattening| F{Analyzable Data}
    end

    %% Phase 3 & 4
    subgraph P3_4 [3 & 4. Analytics & AI Storytelling]
        F --> G[R Studio: Logistic Regression]
        F --> H[BigQuery ML: Risk Models]
        
        G -->|Coefficient Data| I(Combined Feed)
        H -->|Abandonment Probability| I
        
        I -->|System Prompt| J{{GenAI / Gemini LLM}}
    end

    %% Phase 5
    subgraph P5 [5. BI & Data Storytelling]
        J -->|Automated Narrative| K[AI Executive Summary]
        F -->|Quant Metrics| L[KPI Dashboards]
        
        K & L --> M[Looker Studio: AI-Enhanced UI]
    end

    %% Final Output
    M --> N[GitHub: Business Case Study]

    %% Styles for readability
    style J fill:#f96,stroke:#333,stroke-width:2px,color:#000
    style M fill:#69f,stroke:#333,stroke-width:2px,color:#fff
    style D fill:#dfd,stroke:#333,color:#000
    style F fill:#fff4dd,stroke:#d4a017,stroke-width:2px
