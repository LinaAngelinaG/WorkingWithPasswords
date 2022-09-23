# Find-Passwords-By-Hash

Перед работой с двумя файлами для генерации файла с хешами и поиска паролей в файле (blackhole) необходимо установить через консоль `pycryptodome`. Для этого выполните следующий код в командной строке:

```python
pip install pycryptodome  
```

## Возможный вывод утилит: 

Утилита generate.py в консоль выводит ничего. Утилита cracking.py выводит в консоль следующий пример вывода:
```
[OK] :  9ny438yt8vq  ::  fd8ad08e30bdc2d95366f275b69cd3a2

[OK] :  tu8n954t8n  ::  e5af06c1354b81bda8a289959bf75fee

[OK] :  ry4[tuyty4  ::  45b1cefc2f6d4e3df8b9f3647f4ce8b9

[OK] :  ddfhsjkdfh  ::  a5e4cb6143327fc0c42946e0afb0b915

[OK] :  ntu498yt  ::  3b13eddf1bc8a8186ed00605a51846fe

[OK] :  huf984895ty  ::  8048dd65a7a549dbc3776fc97179c176

[OK] :  hughfhg  ::  190daff9933330138e98b40fff1ee69a

[OK] :  oooo  ::  8200ed3b76e52f89f7972ca7a4de7998

[OK] :  ty8459t59  ::  051e6af375246917783d6178758aff03

[OK] :  y598y89y  ::  474cbf5d008a9fc1147bd2aa76c0785a

====== System description =====
macOS-12.0.1-arm64-arm-64bit arm
====== Data description =====
passwords ::  10  blackhole ::  50
====== Time scale =====
time ::  0.9597290803834977  cand/ms
```


## Утилита generate

Данная утилита генерирует файл с хешами заданного размера (параметром), где часть хешей - захешированные пароли, переданные в аргументе утилите. Хеши паролей распределены по файлу выхода.

```bash
python3 generate.py [PASSWORDS_FILE] [CODING] [HASH_ALGO] [OUTPUT_FILE_SIZE] [OUTPUT_FILE]
```

Чтобы запустить утилиту по генерации файла с хешами необходимо выполнить следующий код в консоли (Пример): 

```bash  
python3 generate.py pass UTF-8 SHA1 200 out2.txt
```

Где,
+ generate.py - имя исполняемого файла
+ pass - путь до файла с паролями, которые необходимо перевести в хеши
+ UTF-8 - кодировка
+ SHA1 - алгоритм хеширования
+ out2.txt - путь к файлу, в который будут сохраняться хеши

## Утилита cracking

Утилита ищет заданные пароли, переданные файлом в виде аргумента в входном файле с захешированными паролями (blackhole).   

```bash
python3 cracking.py [PASSWORDS_FILE] [CODING] [HASH_ALGO] [BLACKHOLE_FILE]
```
Чтобы запустить утилиту по поиску паролей в файле необходимо выполнить следующий код в консоли (Пример): 

```bash  
python3 cracking.py pass UTF-8 SHA1 200 out2.txt
```

Где,
+ cracking.py - имя исполняемого файла
+ pass - путь до файла с паролями, поиск которых будет исполняться
+ UTF-8 - кодировка хешей
+ SHA1 - алгоритм хеширования
+ out2.txt - путь к файлу, в который будет проводиться поиск (blackhole in code)

Утилита выводит найденные пароли в формате, привиденном в пункте - Возможный вывод утилит и также небольшую информацию о статистике проведенного поиска. 

```
python3 cracking.py pass UTF-8 MD4 out1.txt
====== System description =====
macOS-12.0.1-arm64-arm-64bit arm
===== Data description =====
passwords ::  10  blackhole ::  200
====== Time scale =====
time ::  1.0710246772348424  cand/ms
```


## Пример работы утилит

Будем использовать файл с паролями - `./test_files/test.txt`. 

Выполним утилиту generate с параметрами: 

```bash
python3 generate.py ./test_files/test.txt UTF-8 MD5 100 out.txt
```
Выполним утилиту cracking с параметрами, удалив 1 пароль из списка `./test_files/test_out.txt`.

```bash
python3 cracking.py ./test_files/test.txt UTF-8 MD5 ./test_files/test_out.txt
```

Получим вывод: 

```bash
[OK] :  hughfhg  ::  4cfccd210542b9204bc0e9a84423d36e

[OK] :  ddfhsjkdfh  ::  cef6f25e65b3f14fc34b8f57271e5491

[OK] :  ty8459t59  ::  3628fb484a0501cb6d36ab6696702876

[OK] :  ntu498yt  ::  c2dd2c4a5b1647ab32328341fcbcca62

[OK] :  y598y89y  ::  f4e784b371eafed9c6c20097551ccab5

[OK] :  ry4[tuyty4  ::  eef0f9f783218ccd61b9db4cf05ade6f

[OK] :  tu8n954t8n  ::  519808899315c2af742d0f305065382a

[OK] :  huf984895ty  ::  08ac9bf621822c9eb8716c0491177125

====== System description =====
macOS-12.0.1-arm64-arm-64bit arm
====== Data description =====
passwords ::  9  blackhole ::  100
====== Time scale =====
time ::  0.9566360963682851  cand/ms

```
> Использованные файлы также приложены в проекте. 



