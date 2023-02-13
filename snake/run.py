from game import Game


if __name__ == "__main__":
    run = Game()

    try:
        # Starting the application.
        run.start_game()
    except KeyboardInterrupt:
        # Stopping the application.
        quit("\n\nProgram Terminated")
