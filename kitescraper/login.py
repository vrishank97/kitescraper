import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from kiteconnect import KiteConnect, KiteTicker


class KiteHelper( object ):
    def __init__(self, apikey, apisecret, username, password, pin):
        self.apikey = apikey
        self.apisecret = apisecret
        self.apikey = apikey
        self.username = username
        self.password = password
        self.pin = pin

    def GetKite( self ):
        kite = KiteConnect(self.apikey)
        kite.set_access_token(self.GetAccessToken())
        return kite

    def GetAccessToken( self ):
        kite = KiteConnect(self.apikey)
        requestToken = self.Automaton.Login()
        data = kite.generate_session(requestToken, self.apisecret)
        access_token = data["access_token"]
        return access_token

    def GetKiteTicker( self ):
        return KiteTicker(self.apikey, self.GetAccessToken())


class KiteAutomaton( object ):

   def __init__( self, apikey, apisecret, username, password, pin):
      self.timeout = 5
      self.options = Options()
      self.options.headless = True

   def getCssElement( self, cssSelector ):
      '''
      To make sure we wait till the element appears
      '''
      return WebDriverWait( self.driver, self.timeout ).until( EC.presence_of_element_located( ( By.CSS_SELECTOR, cssSelector ) ) )

   def Login( self ):
      self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.options)
      self.driver.get("https://kite.trade/connect/login?api_key={}&v=3".format(self.apikey))
      print ("Headless Chrome Initialized")
      try:
         passwordField = self.getCssElement( "input[placeholder=Password]" )
         time.sleep(.8)
         passwordField.send_keys( self.password )
         userNameField = self.getCssElement( "input[id='userid']" )
         time.sleep(.7)
         userNameField.send_keys( self.username )
         
         loginButton = self.getCssElement( "button[type=submit]" )
         time.sleep(.2)
         loginButton.click()
         
         # 2FA
         form2FA = self.getCssElement( "form.twofa-form" )
         pinField = self.getCssElement( "input[label='PIN']" )
         time.sleep(.65)
         pinField.send_keys( self.pin )
         
         buttonSubmit = self.getCssElement( "button[type=submit]" )
         buttonSubmit.click()

         time.sleep(1)
         print(self.driver.current_url.split("request_token=")[1].split("&")[0])
         return self.driver.current_url.split("request_token=")[1].split("&")[0]

      except TimeoutException:
         print( "Timeout occurred" )

      # close chrome
      time.sleep(1)
      self.driver.quit()

if __name__ == "__main__":
   obj = KiteAutomaton()
   obj.Login()
