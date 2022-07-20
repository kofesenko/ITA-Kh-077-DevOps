from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
"https://media0.giphy.com/media/ICOgUNjpvO0PC/giphy.gif",
"https://media2.giphy.com/media/ilqOZH5iI98vxx3nt6/200.gif",
"https://thumbs.gfycat.com/ScentedGiantDolphin-size_restricted.gif",
"https://thumbs.gfycat.com/TanPeacefulImperatorangel-size_restricted.gif",
"https://media0.giphy.com/media/GeimqsH0TLDt4tScGw/giphy.gif",
"https://www.gatewaytheatre.com/sites/default/files/giphy_34.gif",
"https://s18670.pcdn.co/wp-content/uploads/cat-happy.gif",
"http://thelistlove.com/wp-content/uploads/2015/07/lion-cat.gif",
"http://www.cutecatgifs.com/wp-content/uploads/2021/02/wow.gif",
"https://blog.alleninteractions.com/hs-fs/hubfs/4_carrying.gif?width=389&name=4_carrying.gif",
"http://i.imgur.com/tCcR0UX.gif",
"https://c.tenor.com/e_afIeyI4pIAAAAM/cat-nail-file.gif"
]
@app.route('/')
def index():
url = random.choice(images)
return render_template('index.html', url=url)
if __name__ == "__main__":
app.run(host="0.0.0.0")