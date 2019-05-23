#######################################
## BOT Messages
#######################################
import TS3Auth

class Locale(object):
  def __init__(self, fallback = None):
    self._fallback = fallback
    self._values = {}

  def get(self, key, args = ()):
    '''
    key: the string to identify the locale-string with
    args: an optional tuple of arguments to pass to the old style formatter. If the number of arguments don't match the number of template spots in the string, no argument will be inserted at all
    returns: either the looked-up locale-string, the loooked-up locale from the fallback Locale (if any) or the key as fallback-fallback
    '''
    tpl = ""
    if key in self._values:
      tpl = self._values[key]
    elif self._fallback is not None:
      tpl = self._fallback.get(key)
    else:
      tpl = key
    try:
      tpl = tpl % args
    except TypeError:
      TS3Auth.log("Could not insert all %d arguments into the string with key '%s' of locale %d. I will not insert any arguments at all." % (len(args), key, self.__class__.__name__))
    return tpl

  def set(self, key, value):
    self._values[key] = value

class English(Locale):
  def __init__(self):
      super(English, self).__init__()
      self.set("bot_msg_example", "\n\nExample:\n\t\t7895D172-4991-9546-CB5B-78B015B0D8A72BC0E007-4FAF-48C3-9BF1-DA1OAD241266")
      self.set("bot_msg_note", "\n\nNOTE: Guild Wars 2 API keys can be created/deleted via ArenaNet site 'account.arena.net/applications'.")
      self.set("bot_msg_verify", "Hello there! I believe you requested verification?\n\nIf so please reply back to THIS PRIVATE MESSAGE with your API key."+self.get("bot_msg_example")+self.get("bot_msg_note"))
      
      # Banner that we send to all users upon initialization
      self.set("bot_msg", "%s is alive once again! Type 'verifyme' in the '%s' channel to begin verification!")

      # Broadcast message
      self.set("bot_msg_broadcast", "Hello there! You can begin verification by typing 'verifyme' in this channel.")
      
      #Message sent for sucesful verification
      self.set("bot_msg_success", "Authentication was succesful! Thank you fellow Adventurer. Have fun \(^.^)/")
      
      #Message sent for failed verification
      self.set("bot_msg_fail",  "Unfortuntely your authentication failed. Ask the Teamspeak admin to review the logs.\n~ Likely a bad API key or incorrect API settings. (API Key needs access to 'account' and 'character' )"+self.get("bot_msg_note"))

      #Message sent for client TS ID limit reached (trying to access Teamspeack from a second computer after having authenticated on a prior machine
      self.set("bot_msg_limit_Hit", "The TeamSpeak Admins have set a limit to how many computers can authenticate with your Guild Wars 2 account. You are already authenticated from a different computer (or you reinstalled Teamspeak client which reset your TeamSpeak ID with this server).")

      #Message sent to someone who is already verified but asks to be verified
      self.set("bot_msg_alrdy_verified", "It looks like you are already verified! Why do you torture me sooo /cry")

      #Message sent to someone who is not verified but asks to set guild tags via channel text.
      self.set("bot_msg_sguild_nv", "I'm sorry, I can't help you set guild tags unless you are authenticated. Please verify first by replying to me with your API key."+self.get("bot_msg_example")+self.get("bot_msg_note"))

      #Message sent to someone who is verified and asks to set guild tags.
      self.set("bot_msg_sguild", "Let's get to work! First, I need your API key (we don't store your API key in the backend). Reply back with your API key:"+self.get("bot_msg_example")+self.get("bot_msg_note"))

      #Message sent to someone who is not verified and asks to set guild tags via private message.
      self.set("bot_msg_gld_needs_auth", "Where you trying to change your guild tags? If so, please be aware you have not been verified yet! Read below to verify."+self.get("bot_msg_example"))

      #Base Message sent to someone who gave us the API key to pull guild tags.
      self.set("bot_msg_gld_lis", "API Authentication succeeded. Session built. Here are your guild TAGS your can choose to assign:")

      #Default message we send to Private messages that didn't match a command
      self.set("bot_msg_rcv_default", "Hrm...So I get that your saying something but I don't understand what. Are you trying to get verified? If so please provide your API key in the format:"+self.get("bot_msg_example")+self.get("bot_msg_note"))

class German(Locale):
  def __init__(self):
    super(German, self).__init__(English())
    self.set("bot_msg_example", "\n\nBeispiel:\n\t\t7895D172-4991-9546-CB5B-78B015B0D8A72BC0E007-4FAF-48C3-9BF1-DA1OAD241266")
    self.set("bot_msg_note", "\n\nINFO: Guild Wars 2 API keys können über die ArenaNet-Seite 'account.arena.net/applications' erstellt/gelöscht werden.")
    self.set("bot_msg_verify", "Hallöchen! Möchtest du dich registrieren?\n\nFalls ja, antworte bitte per PRIVATER NACHRICHT mit deinem API-Key."+self.get("bot_msg_example")+self.get("bot_msg_note"))

    # Banner that we send to all users upon initialization
    self.set("bot_msg", "%s ist wieder da! Schreibe 'verifyme' in den '%s' Kanal um die Freischaltung zu beginnen!")

    # Broadcast message
    self.set("bot_msg_broadcast", "Hallöchen! Du kannst die Freischaltung beginnen, indem du 'verifyme' in diesem Channel schreibst.")
    
    #Message sent for sucesful verification
    self.set("bot_msg_success", "Freischaltung erfolgreich! Danke dir, Abenteurer. Viel Spaß \(^.^)/")
    
    #Message sent for failed verification
    self.set("bot_msg_fail",  "Leider hat die Freischaltung nicht funktioniert. Bitte einen Teamspeak Administrator die Logs zu prüfen.\n~ Wahrscheinlich ein ungültiger API-Schlüssel oder falsche API-Einstellungen. (Der API-Schlüssel braucht die Berechtigungen 'account' und 'character')"+self.get("bot_msg_note"))

    #Message sent for client TS ID limit reached (trying to access Teamspeack from a second computer after having authenticated on a prior machine
    self.set("bot_msg_limit_Hit", "Die Teamspeak Admins haben ein Limit gesetzt, auf wie vielen Geräten du dich mit deinem Guild Wars 2 Account freischalten kannst. Du bist bereits von einem anderen Gerät aus registriert (oder du hat Teamspeak neu installiert, wodurch deine Teamspeak ID für diesen Servert zurückgesetzt wurde).")

    #Message sent to someone who is already verified but asks to be verified
    self.set("bot_msg_alrdy_verified", "Es scheint, als seist du bereits freigeschaltet! Wieso quälst du mich sooo /cry")

    #Message sent to someone who is not verified but asks to set guild tags via channel text.
    self.set("bot_msg_sguild_nv", "Tut mir leid, ich kann dir erst dabei helfen, ein Gildentag zu setzen, sobald du freigeschaltet bist. Bitte schalte dich frei, indem du mir mit einem API-Schlüssel antwortest."+self.get("bot_msg_example")+self.get("bot_msg_note"))

    #Message sent to someone who is verified and asks to set guild tags.
    self.set("bot_msg_sguild", "Lass uns anfangen! Zuerst brauche ich deinen API-Schlüssel (wir speichern keine Schlüssel). Antworte mir mit deinem API-Schlüssel:"+self.get("bot_msg_example")+self.get("bot_msg_note"))

    #Message sent to someone who is not verified and asks to set guild tags via private message.
    self.set("bot_msg_gld_needs_auth", "Wolltest du dein Gildentag ändern? Falls ja, beachte, dass du noch nicht freigeschaltet bist! Lies weiter, um dich freizuschalten."+self.get("bot_msg_example"))

    #Base Message sent to someone who gave us the API key to pull guild tags.
    self.set("bot_msg_gld_lis", "API-Freischaltung erfolgreich. Sitzung erstellt. Hier sind die Gildentags, aus denen du wählen kannst:")

    #Default message we send to Private messages that didn't match a command
    self.set("bot_msg_rcv_default", "Hm... ich merke, dass du etwas von mir willst, aber ich verstehe dich nicht. Möchtest du dich freischalten? Falls ja, bitte gib deinen API-Schlüssel in folgendem Format an:"+self.get("bot_msg_example")+self.get("bot_msg_note"))


def getLocale(locale):
  locale = locale or "" # make sure upper() doesn't fail on empty arguments
  locale = locale.upper()

  if locale == "DE":
    return German()
  elif locale == "EN":
    return English()
  else:
    return English() # catchall
