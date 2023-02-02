import os
class Config(object):
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '5912024718:AAEH4ps9yHW3tLIf54oK8djR_3_Pg6yIUag')
    SCHEDULE = os.environ.get('SCHEDULE', False)
    USERID = os.environ.get('USERID', '1930954213')

# If you're not familiar with how to set Environment Variables you can do like this instead
# of  setting Environment Variables

# BOT_TOKEN = os.environ.get('BOT_TOKEN', 'BOT_TOKEN_HERE')
# GUSERNAME = os.environ.get('GUSER_NAME', 'Google Email')
# GPASSWORD = os.environ.get('GPASSWORD', 'Google Email Password')

#NOTE: Putting sensitive information in files is considered unsafe. Try to use ENVIRONMENT VARIABLES 
