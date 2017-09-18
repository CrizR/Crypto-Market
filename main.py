import os
os.chdir("/tmp")
from coinmarketcap import Market
from Util import Util

def lambda_handler(event, context):
    APPID = 'amzn1.ask.skill.f39dd9e4-776b-4ed3-9db3-bd7e40fe10ff'
    # Checks if program is called from a valid APPID
    if event['session']['application']['applicationId'] != APPID:
        raise ValueError("Invalid Application ID")
    # If it's an Intent Request...
    if event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    # If it's a Launch Request...
    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])
    # If it's a Session Ended Request...
    if event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])

    return ''


def on_session_ended(request, session):
    # Say out goodbye to the user of the Alexa Skill
    util = Util()
    return Util.build_response(util, "",
                               Util.build_speechlet_response(
                                   util, '', "Goodbye", "", False))


def on_launch(request_id, session):
    # Welcome the User to the App
    util = Util()
    return Util.build_response(util, "",
                           Util.build_speechlet_response(
                               util, '', "Welcome to CryptoMarket", "", False))


def on_intent(intent_request, session):
    coinmarketcap = Market()
    # Determines what intent has been called and what to do.
    intent_name = intent_request["intent"]["name"]
    util = Util()
    if intent_name == "EthStatus":
        data = coinmarketcap.ticker('Ethereum', limit=3, convert='USD')
        ethprice = data[0]['price_usd']
        return Util.build_response(util, "", Util.build_speechlet_response(
            util, '', "Ethereum is currently valued at " + ethprice + " dollars",
            "", False))
    if intent_name == "BtcStatus":
        data = coinmarketcap.ticker('Bitcoin', limit=3, convert='USD')
        btcprice = data[0]['price_usd']
        return Util.build_response(util, "", Util.build_speechlet_response(
            util, '', "Bitcoin is currently valued at " + btcprice + " dollars",
            "", False))
    if intent_name == "RplStatus":
        data = coinmarketcap.ticker('Ripple', limit=3, convert='USD')
        rplprice = data[0]['price_usd']
        return Util.build_response(util, "", Util.build_speechlet_response(
            util, '', "Ripple is currently valued at " + rplprice + " dollars",
            "", False))