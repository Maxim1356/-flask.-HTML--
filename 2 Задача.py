from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def title():
    return "Missiya"

def return_sample_page(n):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">

                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="../static/css/style.css"/>
  </head>
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
           alt="терпи">
                    <div class="alert alert-primary" role="alert">
                      На ней много необходимых ресурсов;
                    </div>
                    <div class="alert alert-primary" role="uio">
                      На ней много необходимых ресурсов;
                    </div>
                    <div class="alert alert-primary" role="uio">
                      На ней много необходимых ресурсов;
                    </div>
                    <div class="alert alert-primary" role="uio">
                      На ней много необходимых ресурсов;
                    </div>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" 
                    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" 
                    crossorigin="anonymous"></script>
                  </body>
                </html>'''


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return return_sample_page(planet_name)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
