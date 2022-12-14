# Working with passwords

Запуск и работа с API:

Перед работой с двумя файлами для генерации файла с хешами и поиска паролей в файле (blackhole) необходимо установить через консоль 'pycryptodome', 'pathib'. Для этого необходимо выполнить в командной строке:

```
pip install pycryptodome  
pip install  pathib
``` 

## Утилита gen
Данная утилита генерирует файл с заданным количество хешей, часть из них - захешированные пароли, переданные с помощью йвходного файла как параметр командной строки утилиты. Остальные хеши - это хеши для рандомно-сгенерированных строк.
- для того, чтобы сгенерировать файл хешей, заданной величины, необходимо обратиться к api gen.py через командную строку с параметрами:
 
     python main.py [FUNCTION_NAME] [PASSWORDS_FILE] [CODING] [HASH_ALGO] [OUTPUT_FILE_SIZE] [OUTPUT_FILE]
    
      
     данная утилита не выводит ответа в консоль, она вычисляет заданное количество (OUTPUT_FILE_SIZE) хешей, создает(или перезаписывает) их в выходной          файл (OUTPUT_FILE), обработка паролей из файла паролей (PASSWORDS_FILE) происходит по заданной кодировке (CODING).
      
     пример возможного вызова:
      
     python main.py --func=gen --passwords=input.txt --hashlist=out.txt --code=utf-8 --hash_func=sha256 --words_val=1000 
      
        - main.py - имя исполняемого файла
        - gen - имя исполняемой функции - генерация хешей для паролей
        - input.txt - путь до файла с паролями, которые необходимо перевести в хеши
        - utf-8 - кодировка
        - sha256 - алгоритм хеширования
        - out.txt - путь к выходному файлу, в который будут сохраняться хеши
        - words_val - кол-во хешей, которое должно быть в выходном файле
  
     порядок указанных переменных окружения неважен. обработка аргументов командной строки происходит с помощью модуля, реализованного в файле work_args.py. 
     
Утилита crack.py выводит в консоль сформированный словарь пароль-его хеш-значение, например:
```
mtksnzgmqzppyjc : 7107b0550e126018d1fea26bb41b9b1ffca80f2e
lqqrvlnmhmmyvqcljhy : 591ba587e2501fac6426c21db1124a9804e58490
fwlnevrtebvvvxeemef : 16d5d12f5390173ababd01458deb6a9520c20e54
aomospslodtemxd : c056645f0d26f83144915d13236cd5acf219c89b
jhgnffhhsxj : b242842bade2f1c965e53d2186bf0e24ffcda965
ffzjnfkddnbw : deb5e25bd22e0117309c968662411c9e03501961
xqxuenobesgqfyvve : fe63594c18f725da4192ac0117e0d780ed72c34e
ludhaaizkrmyvnmwmhv : 8914617d56c5cb34f748ff5305bd16a4215746f8
eqxezzammvdusqumy : 6adc0958d7e71fd73de285a9f0ec5f3eba377662
zlmuwykrcxuyiciax : 7a0b692fa3eb4a45a8402784719242d9c93b3612
hexvjxaynk : c840ac597b4bd732bdca622a84aaa7c0cdf85508
ybhdrectxrphhp : 4c83d1e06ea9f4e4adfe830bb183c013b7cb8062

====== System description =====
Darwin MacBook-Air-Angelina.local 21.1.0 
Darwin Kernel Version 21.1.0: Wed Oct 13 17:33:24 PDT 2021; 
root:xnu-8019.41.5~1/RELEASE_ARM64_T8101 x86_64
====== ------------------ =====
```

  
  
## Утилита crack

Утилита ищет заданные пароли, переданные файлом в виде аргумента в входном файле с захешированными паролями.   

```bash
python main.py [FUNCTION_NAME] [PASSWORDS_FILE] [CODING] [HASH_ALGO] [HASHLIST_FILE]
```
Пример запуска API через консоль: 

```
python main.py --func=crack --passwords=input.txt --hashlist=out.txt --code=utf-8 --hash_func=sha256
```
  
- main.py - имя исполняемого файла
- crack - исполняемая функция - составление словаря из паролей и их хешей
- input.txt - путь до файла с паролями, поиск которых будет исполняться
- utf-8 - кодировка хешей
- sha256 - алгоритм хеширования
- out.txt - путь к файлу, в который будет проводиться поиск 

Утилита выводит найденные пароли в формате, привиденном в пункте - Возможный вывод утилит и также небольшую информацию о статистике проведенного поиска. 

## Пример работы утилит

В программе test.py приведен алгоритм проведения тестирования, в результате которого было получено, что в среднем скорость обработки кандидатов = 60,5 кандидатов/секунду.

Тестирование проводилось следующим образом: 20 раз повторялся алгоритм - сгенерировать от 500 до 1000 паролей в файл input.txt, задать от 1000 до 2500 кол-во выходных хешей для файла output.txt - применить алгоритм gen с заданными параметрами, далее для каждой такой пары файлов запускалась утилита crack.py, до начала работы которой и после ставились временные метки, чтобы замерить длительность выполнения работы программы. Далее кол-во паролей из файла input делилось на полученное время и информация по каждой итерации записывалась в result.txt.



