from Cli.app import App

import asyncio

if __name__=="__main__":
  app=App()
  asyncio.run(app.start_app())