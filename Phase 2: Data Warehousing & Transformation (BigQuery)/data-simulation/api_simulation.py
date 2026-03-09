"""
Data Simulation Module for 'Psychological Friction Score' Project.

This script generates synthetic user sessions to populate the BigQuery warehouse
via the Google Analytics 4 Measurement Protocol. It simulates user behavior
(hesitation time and scroll depth) and calculates purchase probability based 
on the Fogg Behavior Model and Cognitive Load Theory.
"""
import requests
import json
import random
import time
import uuid

# --- Configuration Settings ---
# API details
api_secret = "API_SECRET"
measurement_id = "G-YOUR_MEASUREMENT_ID"
url = f"https://www.google-analytics.com/mp/collect?measurement_id={measurement_id}&api_secret={api_secret}"

# Function to make a session
def make_session(index):
    client_id = str(uuid.uuid4())
    session_id = int(time.time()) + index

    # Get random numbers for scroll and hesitation
    scroll = random.choice([25, 50, 75, 90, 100])
    hesitation = round(random.uniform(1.0, 18.0), 2)

    # Check if they buy based on variables
    buy_prob = 0.2
    if hesitation < 6.0:
        buy_prob += 0.4
    if scroll >= 75:
        buy_prob += 0.2

    did_buy = random.random() < buy_prob

    # Make the events list
    events = [
        {"name": "first_visit", "params": {"session_id": session_id, "engagement_time_msec": 10}},
        {"name": "session_start", "params": {"session_id": session_id, "engagement_time_msec": 10}},
        {"name": "page_view", "params": {"session_id": session_id, "page_location": "https://samola-portfolio.github.io/gtm-test-site/checkout.html", "engagement_time_msec": 1000}},
        {"name": "scroll_tracking", "params": {"session_id": session_id, "percent_scrolled": scroll, "engagement_time_msec": 2000}},
        {"name": "hesitation_complete", "params": {"session_id": session_id, "hesitation_time": hesitation, "engagement_time_msec": int(hesitation * 1000)}}
    ]

    if did_buy:
        events.append({"name": "purchase_success", "params": {"session_id": session_id, "engagement_time_msec": 500}})

    data = {
        "client_id": client_id,
        "events": events
    }

    return data, hesitation, scroll, did_buy

# Run the script 500 times
if __name__ == "__main__":
    print("Starting script...")
    success = 0
    
    for i in range(1, 501):
        data, hes, scr, bought = make_session(i)
        
        try:
            res = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            
            if res.status_code == 200 or res.status_code == 204:
                success += 1
                print(f"Session {i} sent. Hesitation: {hes}, Scroll: {scr}, Bought: {bought}")
            else:
                print(f"Error {res.status_code} on session {i}")
                
        except Exception as e:
            print(f"Failed to connect: {e}")

        # Sleep to avoid rate limits
        time.sleep(random.uniform(0.5, 1.5))

    print(f"Done. Sent {success} out of 500.")
