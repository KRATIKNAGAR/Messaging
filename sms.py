from twilio.rest import Client

account_sid = 'ACc0d2e2e0a860f912a689a37043d825fc'
auth_token = '7f4715eab96a26013b1a27d6ae7f7a7a'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MGd7ccaac3084e82804e96f00095fe2546',
    body='hiiii broo',
    to='+919834770216'
)

print(message.sid)