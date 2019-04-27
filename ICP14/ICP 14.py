
import json
import urllib2 

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        #self.onStopped() #activate the output of the box
        # Make a get request to get the latest position of the international space station from the opennotify api.
    
        # Specify the url
        
        postureProxy = ALProxy("ALRobotPosture", "134.193.131.96", 9559)
        postureProxy.goToPosture("StandInit", 1.0)            
        url = 'http://api.openweathermap.org/data/2.5/weather?q=kansas%20city,us&appid=14308e97d762089fbd8e3cb1a004342b' 
        request = urllib2.Request(url)
        # Sends the request and catches the response
        response = urllib2.urlopen(request)        
        #data = response.json()   

        # Extracts the response
        html = json.loads(response.read())
        result = html['main']['temp']
        
        cel = (result - 273.5)
        tts = ALProxy("ALTextToSpeech","134.193.131.96",9559)
        tts.say("Current Temperature in Kansas city is "+str(cel) + "Celsius")
        postureProxy.goToPosture("LyingBelly", 1.0)    
        
         
    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
