import random
import Cookie
import cookielib
class UserInfo(object):
    def setUserInfo(self, first, last, email):
         cookie = Cookie.SimpleCookie();
         sessionID = random.randint(1,100000);
         cookie["session_id"] = sessionID;
         cookie["firstName"] = first;
         cookie["lastName"] = last;
    def setUserInterests(self, interestsInput):
         interests = interestsInput.split(",");
         sessionID = random.randint(1,100000);
         cookie = Cookie.SimpleCookie();
         for key,value in enumerate(interests):
           cookie["interest{0}".format(key)]="{0}".format(interests[key]);
         cookie["session_id"] = sessionID;
    def getUserInfo(self):
	cj = cookielib.CookieJar();
	cookielib.Cookie(cookie);
userInfo = UserInfo();
userInfo.setUserInterests("test, test, testing, tester");
