from game import Game 
import asyncio
#function to start the game
async def main():
  game = Game()
  await game.run()

#if this is main, start the game
if __name__ == "__main__":
  asyncio.run(main())