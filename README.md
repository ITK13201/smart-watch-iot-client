# Smart Watch IoT Client

## Install

```shell
pip install pipenv
pipenv install --dev
```

## Usage

### Run

```shell
# development
pipenv run dev
# or
# production (run as daemon)
pipenv run start
```

### Enter the virtual environment

```shell
pipenv shell
```

### Tracking and Format "*.py" file

```shell
pipenv run watch
```

### Format changed "*.py" file

```shell
pipenv run format
```

### Download musics from YouTube Music

```shell
flask job download_musics --url <YouTube Music URL>
```

### register music informations to [AWS Server](https://github.com/ITK13201/smart-watch-iot-server)

```shell
flask job register_music_informations
```
