import requests
import json

# Set up the API key and list ID
api_key = ''
list_id = 'a0ba715e0e'

# Set up the endpoint URLs
root_url = 'https://us18.api.mailchimp.com/3.0/'
lists_url = root_url + 'lists/'
campaigns_url = root_url + 'campaigns/'

# Define the email content
email_subject = 'Test Mail With Mailchimp'
email_body = '<html><body><h1>Hello From mailchimp</h1><p>This mail is send through mailchimp for testing</p><center><br/><br/><br/><table border="0" cellpadding="0" cellspacing="0" width="100%" id="canspamBarWrapper" style="background-color:#FFFFFF; border-top:1px solid #E5E5E5;"><tr><td align="center" valign="top" style="padding-top:20px; padding-bottom:20px;"><table border="0" cellpadding="0" cellspacing="0" id="canspamBar"><tr><td align="center" valign="top" style="color:#606060; font-family:Helvetica, Arial, sans-serif; font-size:11px; line-height:150%; padding-right:20px; padding-bottom:5px; padding-left:20px; text-align:center;">This email was sent to <a href="mailto:*|EMAIL|*" target="_blank" style="color:#404040 !important;">*|EMAIL|*</a><br/><a href="*|ABOUT_LIST|*" target="_blank" style="color:#404040 !important;"><em>why did I get this?</em></a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="*|UNSUB|*" style="color:#404040 !important;">unsubscribe from this list</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="*|UPDATE_PROFILE|*" style="color:#404040 !important;">update subscription preferences</a><br/>*|LIST:ADDRESSLINE|*<br/><br/>*|REWARDS|*</td></tr></table></td></tr></table><style type="text/css">@media only screen and (max-width: 480px){table#canspamBar td{font-size:14px !important;}table#canspamBar td a{display:block !important; margin-top:10px !important;}}</style></center></body></html>'

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


