#######################################
## BOT Messages
#######################################


# Message in response to someone asking us to verify them
bot_msg_verify='''
 Hello there! I believe you requested verification?

 If so please reply back to THIS PRIVATE MESSAGE with your Account Name (name with numbers) and API key.

 Ex.
      <Account Name> <API Key>
      TCWarrior.5463 7895D172-4991-9546-CB5B-78B015B0D8A72BC0E007-4FAF-48C3-9BF1-DA1OAD241266


   NOTE: Guild Wars 2 API keys can be created/deleted via [url=https://account.arena.net/login?redirect_uri=%2Fapplications]ArenaNet site[/url].

'''

#Message sent for sucesful verification
bot_msg_success='''
  Authentication was succesful! Thank you fellow Adventurer. Have fun \(^.^)/
'''

#Message sent for failed verification
bot_msg_fail='''
  Unfortantely your authentication failed. Ask the Teamspeak admin to review the logs.
     ~ Likely a bad API key or incorrect API settings. ( API Key needs access to 'account' and 'character' )

NOTE: Guild Wars 2 API keys permission can be viewed via [url=https://account.arena.net/login?redirect_uri=%2Fapplications]ArenaNet site[/url].
'''

#Message sent for client TS ID limit reached (trying to access Teamspeack from a second computer after having authenticated on a prior machine
bot_msg_limit_Hit='''
   The TeamSpeak Admins have set a limit to how many computers can authenticate with your Guild Wars 2 account. You are already authenticated
   from a different computer (or you reinstalled Teamspeak client which reset your TeamSpeak ID with this server).

'''

#Message sent to someone who is already verified but asks to be verified
bot_msg_alrdy_verified='''
  It looks like you are already verified! Why do you torture me sooo /cry
'''

#Message sent to someone who is not verified but asks to set guild tags via channel text.
bot_msg_sguild_nv='''
  I'm sorry, I can't help you set guild tags unless you are authenticated. Please verify first by replying to me with your Account Name (name with numbers) and API key.

   Ex.
      <Account Name> <API Key>
      TCWarrior.5463 7895D172-4991-9546-CB5B-78B015B0D8A72BC0E007-4FAF-48C3-9BF1-DA1OAD241266

'''

#Message sent to someone who is verified and asks to set guild tags.
bot_msg_sguild='''
        Let's get to work! First, I need your API key (we don't store your API key in the backend). Reply back with your API key:

           Ex.
               7895D172-4991-9546-CB5B-78B015B0D8A72BC0E007-4FAF-48C3-9BF1-DA1OAD241266

'''

#Message sent to someone who is not verified and asks to set guild tags via private message.
bot_msg_gld_needs_auth='''

        Where you trying to change your guild tags? If so, please be aware you have not been verified yet! Read below to verify:

        Otherwise, It appears you were attempting to verify but only sent me your API key. If veryfing remember to reply with your Account Name and API key.

   Ex.
      <Account Name> <API Key>
      TCWarrior.5463 7895D172-4991-9546-CB5B-78B015B0D8A72BC0E007-4FAF-48C3-9BF1-DA1OAD241266
'''

#Base Message sent to someone who gave us the API key to pull guild tags.
bot_msg_gld_list='''
  API Authentication succedded. Session built. Here are your guild TAGS your can choose to assign:
'''

#Default message we send to Private messages that didn't match a command
bot_msg_rcv_default='''
  Hrm...So I get that your saying something but I don't understand what. Are you trying to get verified? If so please provide your
    account name with API key in the format: <Account Name> <API Key>

    Example:

      TCWarrior.5463 7895D172-4991-9546-CB5B-78B015B0D8A72BC0E007-4FAF-48C3-9BF1-DA1OAD241266

'''


#######################################
