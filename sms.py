from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = "AC08eb0f81d17d47976103a94e78a8c44f"
AUTH_TOKEN = "ccc403ab0be2432f31f75fe56004428b"
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)


def send(body):
    for number in client.caller_ids.list():
        message = client.messages.create(
            to=number.phone_number,
            from_="+18017834819",
            body=body,
        )

    print(message.sid)


def listingResources():
    for number in client.caller_ids.list():
        print(number.friendly_name + " / " + number.phone_number)

        # def getaccountlist():
        #    acc = client.accounts.get(ACCOUNT_SID)
        # print(acc.friendly_name)
        # for number in client.accounts.get():
        #    print(number)
        # client.accounts.get(old_account)
        # {
        # 	"sid": "PN2a0747eba6abf96b7e3c3ff0b4530f6e",
        # 	"account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        # 	"friendly_name": "My Company Line",
        # 	"phone_number": "+15105647903",
        # 	"voice_url": "http://demo.twilio.com/docs/voice.xml",
        # 	"voice_method": "POST",
        # 	"voice_fallback_url": null,
        # 	"voice_fallback_method": "POST",
        # 	"voice_caller_idlookup": null,
        # 	"date_created": "Mon, 16 Aug 2010 23:00:23 +0000",
        # 	"date_updated": "Mon, 16 Aug 2010 23:00:23 +0000",
        # 	"sms_url": null,
        # 	"sms_method": "POST",
        # 	"sms_fallback_url": null,
        # 	"sms_fallback_method": "GET",
        # 	"capabilities": {
        # 		"voice": null,
        # 		"sms": null
        # 	},
        # 	"status_callback": null,
        # 	"status_callback_method": null,
        # 	"api_version": "2010-04-01",
        # 	"uri": "\/2010-04-01\/Accounts\/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\/IncomingPhoneNumbers\/PN2a0747eba6abf96b7e3c3ff0b4530f6e.json"
        # }
