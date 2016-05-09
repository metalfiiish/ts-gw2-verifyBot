import gw2api.v2
from datetime import datetime
import configparser
import ast

auth_configs = configparser.ConfigParser()
auth_configs.read('bot.conf')


# expects a pythonic list, Ex. ['Tarnished Coast','Kaineng']
required_servers = ast.literal_eval(
    auth_configs.get('auth settings', 'required_servers'))
required_level = auth_configs.get('auth settings', 'required_level')

log_file = 'TS3Auth.log'

# String handles
h_hdr = '#~ GW2 Handler:'  # Header
h_acct = '[AccountGet]'  # Account loading
h_char = '[CharacterGet]'  # Character loading
h_auth = '[AuthCheck]'
h_char_chk = '[CharacterCheck]'


#############################
# Functions

def log(msg, silent=False):
    if not silent:
        print (msg)
    with open(log_file, "a") as logger:
        new_log = "%s %s\n" % (str(datetime.now()), msg)
        logger.write(new_log)

# Class for an authentication request from user


class auth_request:

    # User ID left at None for queries that don't require authentication. If
    # left at None the 'success' will always fail due to self.authCheck().
    def __init__(self, api_key, user_id=''):
        self.key = api_key
        self.user = user_id
        self.success = False  # Used to verify if user is on our server
        self.char_check = False  # Used to verify is any character is at least 80
        self.required_level = int(required_level)
        self.required_servers = required_servers

        self.pushCharacterAuth()
        self.pushAccountAuth()

    def pushCharacterAuth(self):
        # if level is set to 0 bypass character API request (in case GW2
        # Character API breaks again like in April 2016.)
        if self.required_level == 0:
            self.char_check = True
            return
        try:
            log('%s %s Attempting to load character data for %s.' %
                (h_hdr, h_char, self.user))
            gw2api.v2.characters.set_token(self.key)
            self.char_dump = gw2api.v2.characters.page(page=0)
            log('%s %s Character data loaded for %s.' %
                (h_hdr, h_char, self.user))
            self.charCheck()

        except:
            log('%s %s Unable to load character data for %s. Bad API key or API key is not set to allow "character" queries.' % (
                h_hdr, h_char, self.user))

    def pushAccountAuth(self):
        try:
            self.getAccountDetails()
            log("%s %s Account loaded for %s" % (h_hdr, h_acct, self.user))
            self.authCheck()

        except:
            log('%s %s Possibly bad API Key. Error obtaining account details for %s. (Does the API key allow "account" queries?)' % (
                h_hdr, h_acct, self.user))

    def getAccountDetails(self):
        gw2api.v2.account.set_token(self.key)

        # All account details
        self.details_dump = gw2api.v2.account.get()

        # Players World [id,name,population]
        self.world = gw2api.v2.worlds.get_one(self.details_dump.get('world'))

        # Player Created Date -- May be useful to flag accounts created within past 30 days
        #self.created = self.details_dump.get('created')

        # Player Name
        self.name = self.details_dump.get('name')

        # Players Account ID
        self.id = self.details_dump.get('id')

        # Players Guilds (by ID)
        self.guilds = self.details_dump.get('guilds')

        # Players Guild Tags (Seems to order it by oldest guild first)
        self.guild_tags = []
        for guild_id in self.guilds:
            self.guild_tags.append(gw2api.guild_details(guild_id).get('tag'))

    def authCheck(self):
        log("%s %s Running auth check for %s" % (h_hdr, h_auth, self.name))
        users_server = self.world.get('name')

        # Check if account name given is correct AND if they are on the
        # required server
        if self.user == self.name and users_server in required_servers:

            # Check if player has met character requirements
            if self.char_check:
                self.success = True
                log("%s %s Auth Success for user %s." %
                    (h_hdr, h_auth, self.user))

            else:
                log("%s %s User %s is on the correct server but does not have any level %s characters." % (
                    h_hdr, h_auth, self.user, self.required_level))

        else:
            log("%s %s Authentication Failed with:\n\n    User Gave:\n        ~USER ID: %s\n          ~Server: %s\n\n     Expected:\n         ~USER ID: %s\n          ~Server: %s\n\n" % (
                h_hdr, h_auth, self.user, users_server, self.name, required_server))
        return self.success

    def charCheck(self):
        # Require at least 1 level 80 character (helps prevent spies)
        for char in self.char_dump:
            if char.get('level') >= self.required_level:
                self.char_check = True
                log("%s %s User %s has at least 1 level %s character." %
                    (h_hdr, h_char_chk, self.user, self.required_level))
                return
