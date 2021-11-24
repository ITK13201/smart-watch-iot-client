import infrastructure
from config.config import PORT, DEBUG


if __name__ == "__main__":
    infrastructure.Engine.run(port=PORT)
