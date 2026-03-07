**Phase 1: Setting Up the Tracking (GTM & GA4)**
This phase is the foundation of the project. Instead of just tracking basic clicks, I designed a system to capture how users behave before they decide to buy or leave.

**1. Smart Event Triggers**
- Tracking "Idle" Time: I created a custom JavaScript listener that detects when a user stops moving their mouse on important parts of the page (like the "Checkout" button). This helps us measure true Hesitation.

- Scroll Milestones: I set up triggers to fire at specific points (25%, 50%, 75%, and 100% of the page). This shows us how much of the content a user actually reads.

**2. Capturing the Right Numbers**
- Using the DataLayer: I configured GTM to "grab" specific numbers from the browser, such as exactly how many seconds a user hesitated.

- Clean Data: I ensured that these numbers are saved as clean, mathematical values —such as hesitation_time and scroll_depth— so they can be easily analyzed later by R and BigQuery.

**3. Custom Labels for GA4**
- Beyond Basic Clicks: I mapped these behavioral signals to custom parameters in Google Analytics 4.

- Rich Data Profiles: Instead of just seeing "User visited page," we now see "User visited page, scrolled 75%, and hesitated for 12 seconds." This creates a much more detailed picture for our analysis.

**4. Testing and Quality Check**
- Debug Mode: I used GTM Preview mode to double-check that every trigger fires at the exact right moment.

- Removing Noise: I added filters to make sure we don't track "fake" hesitation (like when someone just leaves a tab open in the background), keeping our final dataset accurate.
