from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
x="12345"
with open("123.txt","w") as fo:
    fo.write(x)
y="67890"
if __name__ == '__main__':
    app.run()

