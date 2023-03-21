import requests
import json

# Set up the API key and list ID
api_key = '02afa9ecd14cdf88099bf0ae57cdf287-us18'
list_id = 'a0ba715e0e'

# Set up the endpoint URLs
root_url = 'https://us18.api.mailchimp.com/3.0/' # Replace X with your data center ID
lists_url = root_url + 'lists/'
campaigns_url = root_url + 'campaigns/'

# Define the email content
email_subject = 'Test Mail With Mailchimp API'
email_body = '<html><body><h1>Hello World!</h1><p>This is a test email sent using Mailchimp API.</p></body></html>'

# Define the campaign details
campaign_data = {
    'recipients': {'list_id': list_id},
    'type': 'regular',
    "status": "sent",
    'settings': {
        'subject_line': email_subject,
        'reply_to': 'shadik@praavahealth.com',
        'from_name': 'Shadik Hasan',
        # 'template_id': 12345 # Replace with your template ID, if using one
    }
}

# Create the campaign
response = requests.post(campaigns_url, auth=('apikey', api_key), json=campaign_data)

# Check for errors
if response.status_code != 200:
    print('Error creating email campaign:', response.text)
else:
    # Extract the campaign ID from the response
    campaign_id = json.loads(response.text)['id']

    # Add the email content to the campaign
    email_content = {
        'html': email_body,
        'text': email_body
    }
    response = requests.put(campaigns_url + campaign_id + '/content', auth=('apikey', api_key), json=email_content)

    # Check for errors
    if response.status_code != 204:
        print('Error adding email content to campaign:', response.text)
    else:
        # Send the campaign
        response = requests.post(campaigns_url + campaign_id + '/actions/send', auth=('apikey', api_key))

        # Check for errors
        if response.status_code != 204:
            print('Error sending email campaign:', response.text)
        else:
            print('Email campaign sent successfully!')
