import re
import twitter
import auth

twitter_api=auth.oauth_login()

hat=r'[<>]?'
eyes=r'[:;=8]'
optional_nose=r'[\-o\*\']?'
mouth=r'[\)\]\(\[dDpP/\:\}\{@\|\\]'


text=input()

if re.match(hat,text):
    print "the text contains hats and brows"
if re.match(eyes,text):
    print "the text contains eyes"
if re.match(optional_nose,text):
    print "the text has optional nose"

if re.match(mouth,text):
    print "the text has mouth"
