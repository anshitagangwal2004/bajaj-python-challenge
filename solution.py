import requests

# Step 1: Register to get webhook and token
payload = {
    "name": "John Doe",
    "regNo": "REG12347",  # Use your own reg no
    "email": "john@example.com"
}

register_url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
response = requests.post(register_url, json=payload)

if response.status_code == 200:
    res_json = response.json()
    webhook_url = res_json.get("webhook")
    access_token = res_json.get("accessToken")
    print("✅ Webhook and token received!")
    print("Webhook URL:", webhook_url)
    print("Access Token:", access_token)
else:
    print("❌ Error:", response.text)
    exit()

# Step 2: Final SQL query (you will fill this after solving the problem)
sql_query = """
YOUR_SQL_QUERY_HERE
"""

# Step 3: Submit the solution
headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

submit_payload = {
    "finalQuery": sql_query.strip()
}

submit_response = requests.post(webhook_url, headers=headers, json=submit_payload)

if submit_response.status_code == 200:
    print("✅ Successfully submitted your SQL query!")
else:
    print("❌ Submission failed:", submit_response.text)
