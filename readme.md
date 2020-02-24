# WhatToEatNow

## WhatToEatNow has two functions.
### 1. Line bot to recommend what to eat now.

### 2. Webapp for users to save their preferences.

## Usage

```bash
docker-compose up
```
Delete existing volume to refresh static data(restframework)
```bash
docker-compose down -v
```
Do this again to start container
```bash
docker-compose up
```

Access to the link below to see api

```
localhost:80/api
```

For testing webhook

```
`ngrok http 80`
```

if you have not installed `ngrok`, install wby the command below

```
brew cask install ngrok
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

