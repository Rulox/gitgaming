Git Gaming (GG)
=========
##http://www.gitgaming.com

![alt tag](http://upload.wikimedia.org/wikipedia/commons/thumb/0/06/AGPLv3_Logo.svg/200px-AGPLv3_Logo.svg.png)

If you want to receive news about the progress of this proyect (in Spanish), visit  

### http://www.gitgaming.com/weblog

-
Made for the **IX Free Software Contest** in http://www.concursosoftwarelibre.org/ will be continued after the contest. We want to create a big community of Developers/Game lovers in order to create stats and analyze data in a *"gamer"* and funny way.

Open Source Gamified System for GitHub Developers. Track your work in GitHub repositories with us. Use our system in order to improve your production or analyze your team work in a funny way.

With GitGaming, you will live the Gaming experience while you are developing as usual. Make tests, follow good practises and document your code to get more experience and achievements in order to be first in our Rankings. Earn badges or titles and compare your progression with your dev friends.

We recommend you to use our system at http://www.gitgaming.com

Of course you can download and deploy GG in your system, add new badges and achievements, etc.

# Dependencies
    See requirements.txt
-
# Usage

    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

* You need to register your app in GitHub and follow steps to make Login with GitHub possible.

* After that, you have to copy both secret and public keys from GitHub App to your settings.py

* You can use our settings.py in Dev with sqlite3. Do **not** use that version in Production!

* Go to localhost:8000

**Note:** Our custom basic badges are implemented and provided with the code. We have developed an easy way to create new badges. If you are using GG and you want us to code new badges, feel free to contact via website or create a new issue in GitHub.


-
# Models

### Developers
### Badges
### Achievements
### Stats



