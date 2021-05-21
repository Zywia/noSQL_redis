# Instrukcja ćwiczenia

Aplikacja to prosto lista zadań napisana w Django:
- Podpięta jest do bazy dany psql.
- udostępnia rest'owy interfejs do obsługi zadań w dwóch wersjach:
   - z cache'em
   - bez cache'u

### konfiguracja
1. docker-compose up -d
2. docker-compose exec web bash
3. python manage.py migrate 
4. python populate.py
5. exit

### monitorowanie redis
1. docker-compose exec redis redis-cli
2. monitor 

tutaj będą wyświetlane wszelkie operacje na redis.

### Zadanie 

W nowym terminalu

1. sprawdzenie czasu odpowiedzi na endpoint'cie z ustawionym cache'em dwu krotnie. Porównanie obu wyników. 
   W terminalu gdzie działa redis monitor powinny być wyświetlane operacje:
    - curl -w "@curl-format.txt" -o /dev/null -s "http://0.0.0.0:8000/cache_task/"
   
2. sprawdzenie czasu odpowiedzi na endpoint'cie bez ustawionego cache'u:
    - curl -w "@curl-format.txt" -o /dev/null -s "http://0.0.0.0:8000/task/"
3. sprawdzenie zawartości bazy danych redis:
    1. docker-compose exec redis redis-cli - pozwa połaczyć się z Redis
    2. keys * - w ten sposób możemy sprawdzić wszystkie klucze w bazie
    3. z pomocą komendy get <key> sprawdzić zawartość
    
4. persistance
   1. ustawienie zapisu snapshot'u bazy:
        1. wpisująć komęndę "config get *" możemy zobaczyć wszystkie możliwe ustawienia
        2. wpisująć komęndę "config set \<ustawienie>" możemy daną opcję skonfigurawać
        3. należy wpisać komęde :config set save "2 1". Oznacza ona że snapshot bazy zostanie zapisany raz na 2s jeżeli co najmniej jedna wartość w bazie uległa zmianie
        4. w przeglądarce poprać jeden element z bazy: http://0.0.0.0:8000/cache_task/2/
        5. po krutkim czasie w folderze redis-volume powinien pokazać się plik dump.rdb z snapshot'em
        

