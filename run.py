#
#
#
#
import autopy
import time
#user config
username = "vual1z"
username2 = "hotmail.com"
password = "after76n"

#declaired varibles

raw_input("Press enter...")


def login_random():
    """Look for the login screen. Tell me if you found it."""
    runescape = autopy.bitmap.capture_screen()
    loginform = autopy.bitmap.Bitmap.open('loginform.png')
    wronglogin = autopy.bitmap.Bitmap.open('wronglogin.png')
    
    pos2 = runescape.find_bitmap(loginform)

    while pos2:
        print "Login screen encounted"
	print "Attempting to login now"
	print "moving mouse to, x: " + str(pos2[0]) 
	print " and, y: " + str(pos2[1])
	autopy.mouse.smooth_move(pos2[0], pos2[1])
	autopy.mouse.click(autopy.mouse.LEFT_BUTTON)
	autopy.key.type_string(username, 20)
	print "entering username..."
	autopy.key.type_string(username2, 40)
	autopy.key.tap(autopy.key.K_RETURN)
	print "entering password..."
	autopy.key.type_string(password, 45)
	autopy.key.tap(autopy.key.K_RETURN)
	print "login in..."
	time.sleep(5)
	runescape = autopy.bitmap.capture_screen()
	wronglog = runescape.find_bitmap(wronglogin)
        if wronglog:
            print "oppps wrong login 0_o"
            print "lets try again, shall we..."
            autopy.mouse.smooth_move(wronglog[0], wronglog[1])
            autopy.mouse.click(autopy.mouse.LEFT_BUTTON)
	    login_random()
        else:
            print "are you are the website, i cant find login screen"

login_random()







raw_input("Press enter...")

#http://www.runescape.com/game.ws?j=1
#
#
#




