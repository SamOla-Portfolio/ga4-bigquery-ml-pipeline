# Datapipeline för prediktiv analys av användarbeteende
**En komplett datapipeline för att analysera användartvekan och köpsannolikhet med hjälp av GA4, BigQuery och R.**

### **Projektstatus: Konceptbevis (Proof of Concept)**
Detta projekt är utvecklat som ett **Konceptbevis (PoC)** för att demonstrera en modern och skalbar **Dataarkitektur**. Syftet är att visa hur man praktiskt kan integrera avancerad statistik och **Artificiell intelligens** för att lösa affärskritiska utmaningar, såsom digital användarfriktion.

Genom att använda en kombination av **BigQuery**, **SQL**, **R** och **Python**, illustrerar projektet hela kedjan från datainsamling till prediktiva insikter. Även om data som används är syntetiska, är den tekniska infrastrukturen designad för att kunna implementeras direkt i en verklig produktionsmiljö för att skapa mätbar **Kundnytta** och optimera affärsresultat.
---

# Fallstudie: Psykologisk friktionspoäng inom e-handel
## 1. Projektets syfte
Traditionell webbanalys fokuserar vanligtvis på om en användare genomförde ett köp eller lämnade sidan. Detta projekt undersöker istället den ”gråzon” som finns däremellan genom att mäta tyst användartvekan (psykologisk friktion) under utcheckningsprocessen. 

Målet är att bygga ett pålitligt system som identifierar var användare stöter på problem och omedelbart visar hjälpsamma meddelanden för att rädda försäljningen innan de lämnar sin varukorg. Detta är ett testprojekt som använder 500 simulerade besök för att demonstrera ett praktiskt och affärsfokuserat tillvägagångssätt.

## 2. Forskningsfrågor
Projektet syftar till att besvara följande kärnfråga:
* ”Hur kan vi mäta osynliga användarbeteenden (som tvekan) på ett pricksäkert sätt för att förutse övergivna varukorgar, och omedelbart ingripa med förgenererad AI-hjälp utan att kompromissa med webbplatsens prestanda?”

## 3. Underliggande teorier och principer
Projektet vilar på två beteendeteorier och en praktisk regel för systemdesign:

* **Teorin om kognitiv belastning (Cognitive Load Theory):** Det mänskliga arbetsminnet har en begränsad kapacitet. Komplexa gränssnitt eller stressiga ekonomiska beslut ökar den mentala ansträngningen. Eftersom vi inte kan mäta tankar direkt, använder vi **tvekan (i sekunder)** som ett mätbart substitut. Mer tvekan tyder på högre mental ansträngning och förvirring.
* **Foggs beteendemodell (Fogg Behavior Model):** Ett beteende uppstår endast när motivation, förmåga och en trigger (prompt) sammanfaller. När en användare når betalknappen finns triggern tydligt där. Om de tvekar antar vi att det finns problem med antingen deras förmåga (formuläret är förvirrande) eller deras motivation (brist på förtroende).
* **Praktiskt systemdesign:** Verktyg för djupgående dataanalys är ofta för långsamma för att köras i realtid medan en användare väntar på en webbsida. För att hålla webbplatsen snabb beräknar systemet risknivåer i förväg och genererar hjälpinformation i bakgrunden. Detta gör att webbplatsen kan visa rätt meddelande direkt när en användare fastnar.

## 4. Hypoteser
* **H1:** Användare som uppvisar hög tvekan (t.ex. >15 sekunder) under utcheckningen har en statistiskt signifikant högre sannolikhet för övergiven varukorg jämfört med baslinjen.
* **H2:** Genom att generera AI-hjälpmeddelanden i bakgrunden möjliggörs omedelbara ingripanden när en användare tvekar, vilket minskar antalet övergivna varukorgar utan att sänka webbplatsens hastighet.

## 5. Dataset-översikt (Data Dictionary)
Datasetet som används i detta konceptbevis (PoC) är syntetiskt genererat via en Python-simulering. Det är utformat för att efterlikna anpassad beteendespårning (t.ex. via Google Tag Manager och GA4) som fångar mikrointeraktioner som ofta missas i standardkonfigurationer. Datasetet består av 538 användarsessioner.

## 6. Förväntade resultat och leveranser
Detta projekt levererar en komplett, heltäckande analytisk lösning:
* **Prediktiv ML-modell:** En logistisk regressionsmodell (byggd via BigQuery ML) som kvantifierar det exakta sambandet mellan användarens tvekan och sannolikheten för övergiven varukorg.
* **Automatiserad dataarkitektur:** En robust SQL-pipeline som omvandlar komplex, kapslad GA4-data till strukturerade, analysfärdiga tabeller utan dataförlust.
* **Interaktiv BI-dashboard:** En Looker Studio-dashboard som kartlägger en "beteendebaserad friktionstratt" och översätter abstrakta användarinteraktioner till konkreta ekonomiska mätetal (t.ex. intäkter i riskzonen och förväntad avhoppsfrekvens).
* **Kvalitativa GenAI-insikter:** Ett Python-baserat automatiseringsskript som bearbetar statistiska avvikelser och genererar läsbara, kvalitativa förklaringar till varför användare lämnar sidan.

## 7. Integritet och samtycke (Consent Mode v2)
Moderna dataprojekt måste balansera analys av användarbeteende med respekt för integritetslagar som GDPR och ePrivacy-direktivet. Detta projekt använder **Google Advanced Consent Mode v2** för att vara juridiskt efterlevande utan att förlora de analytiska signaler som krävs för våra AI-modeller.

## 8. Föreslagen testmetodik (A/B-testning)
Eftersom detta är ett simulerat portföljprojekt utvärderades systemet offline (modellens noggrannhet, precision och recall). I en verklig produktionsmiljö skulle hypotes 2 (H2) valideras genom ett strikt A/B-test:

* **Kontrollgrupp (A):** Användare går igenom den vanliga utcheckningsprocessen utan någon AI-intervention.
* **Variantgrupp (B):** Högriskanvändare (tvekan > 15 sek) får omedelbart ett förgenererat AI-hjälpmeddelande.
* **Viktiga mätetal att följa:**
  1. **Huvudmätetal:** Konverteringsgrad för utcheckning (förväntas öka i grupp B).
  2. **Skyddsmätetal 1 (Guardrail):** Genomsnittlig laddningstid för sidan (måste förbli lika mellan A och B för att bevisa att bakgrundsbearbetningen fungerar).
  3. **Skyddsmätetal 2 (Guardrail):** Avvisningsfrekvens för hjälpmeddelandet (för att mäta om AI-meddelandet upplevdes som störande).
 
### Vad händer när en användare klickar på "Neka"?
Om en användare nekar spårning slutar systemet inte att fungera; det ändrar istället i grunden hur det samlar in data för att skydda integriteten:
* **Inga kakor eller lagring:** Systemet undviker strikt att skriva eller läsa identifierare i kakor (cookies), Local Storage eller Session Storage.
* **Cookieless pings:** Anonyma anrop ("pings") skickas till Google Analytics. Systemet registrerar händelsen (som att tveka vid ett formulär) men rensar all data från personliga identifierare.
* **Anonym data:** I vår BigQuery-databas registreras användarens ID-kolumn (`user_pseudo_id`) strikt som `NULL`.

### Hur datapipelinen fungerar vid nekat samtycke (Event-Level Inference)
Eftersom vi enligt lag inte kan koppla ihop en användarsession med hjälp av lokala ID:n efter ett nej, förlitar sig arkitekturen på två metoder som följer gällande regler:
1. **Berikning på händelsenivå (Event-Level Enrichment):** Istället för att spåra variabler över tid, sparar frontend-skriptet beteendemått (skrolldjup och tvekan) i ett tillfälligt minne under körningen. När den sista användaråtgärden sker (t.ex. ett köp eller ett avbrott), bifogas dessa mått direkt till det specifika anropet som `event_parameters`.
2. **Beteendemodellering:** Systemet förlitar sig på Google Analytics 4:s inbyggda maskininlärning. Den använder beteendemönster från användare som gett samtycke för att modellera friktionspunkter för användare som inte gett samtycke. På så sätt fylls analysluckorna utan att spåra enskilda individer.
------------------------------------------------------------------------------------------------------

# ga4-bigquery-ml-pipeline
End-to-end data pipeline analysing user hesitation and purchase probability using GA4, BigQuery, and R.

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
