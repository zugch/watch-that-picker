# watch-that-picker
## create image
```
docker build -t watch-that-picker .
```
## run container (example)
```
docker run --rm -e SCRAPE_URL="https://example.com" -e ELEMENT_SELECTOR="h1" -e CRON_EXPRESSION="*/1 * * * *" watch-that-picker
```
### run container (detached mode and naming)
Flag ```-d``` for detached mode

Name the container with ```--name```
```
docker run --rm -d --name watch-that-picker-example -e SCRAPE_URL="https://example.com" -e ELEMENT_SELECTOR="h1" -e CRON_EXPRESSION="*/1 * * * *" watch-that-picker
docker run --rm -d --name watch-that-picker-watch -e SCRAPE_URL="https://www.uhrzeit.org/atomuhr" -e ELEMENT_SELECTOR=".anzeige" -e CRON_EXPRESSION="*/1 * * * *" watch-that-picker
```
Check your running containers with ```ps```
```
docker ps
```
Bring your container back to the front
```
docker attach watch-that-picker-watch
```
## credits and documentation
Python library for data pulling: https://www.crummy.com/software/BeautifulSoup/bs4/doc/