# Flask Web App

Aby uruchomić plik Dockerfile, należy wykonać następujące polecenia:

1. Utwórz obraz z pliku Dockerfile.

docker build -t "nazwa_obrazu" .

2. Uruchom obraz jako kontener.

docker run --name nazwa_kontenera -p 8080:8080 "nazwa_obrazu"

Po uruchomieniu kontenera można przejść do przeglądarki i wpisać adres 'http://localhost:8080/', aby wyświetlić stronę Flask.
