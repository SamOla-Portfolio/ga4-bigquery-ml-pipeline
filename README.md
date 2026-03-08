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

## 5. Expected Results and Deliverables
The expected outcome is a practical business solution:
* **Statistical Proof:** A mathematical model that calculates exactly how much sales are lost due to user hesitation.
* **System Design:** Documentation showing how to balance smart data predictions with a fast, delay-free website.
* **Business Scorecard:** A visual dashboard that translates user behaviour into clear financial numbers, focusing on "Revenue at Risk" and "Saved Sales" rather than basic page views.
  
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
