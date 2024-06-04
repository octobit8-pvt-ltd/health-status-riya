import requests
import json
# Function to get Jenkins health status
def get_jenkins_health_status(jenkins_url, user, api_token):
    try:
        response = requests.get(f'{jenkins_url}/api/json', auth=(user, api_token))
        response.raise_for_status()
        data = response.json()
        overall_health = data.get('overallLoad', {}).get('load', 'UNKNOWN')
        return overall_health
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Jenkins health status: {e}")
        return 'UNKNOWN'
# Function to send Slack notification
def send_slack_notification(webhook_url, message):
    payload = {
        "text": message
    }
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        print("Successfully sent Slack notification")
    except requests.exceptions.RequestException as e:
        print(f"Error sending Slack notification: {e}")
# Main function
def main():
    # Jenkins details
    jenkins_url = 'http://your-jenkins-server:8080'
    user = 'riyakochar'
    api_token = '11051296ff53ae050783bc92e27f3029b5'
    # Slack webhook URL
    slack_webhook_url = 'https://hooks.slack.com/services/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'
    # Get Jenkins health status
    health_status = get_jenkins_health_status(jenkins_url, user, api_token)
    # Prepare Slack notification message
    message = f"Jenkins Health Status: {health_status}"
    # Send Slack notification
    send_slack_notification(slack_webhook_url, message)
if __name__ == "__main__":
    main()