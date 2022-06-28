def Replit():
  print('https://freshping.io')
  from flask import Flask; app = Flask('') 
  @app.route('/')
  def home():
    return "Hello. The bot is online!"
  def run():
    app.run(host='0.0.0.0',port=8080)
    t = Thread(target=run); t.start(); t.join()
