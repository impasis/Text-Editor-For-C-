# TE++ - Текстовый Редактор для C++

## Документация

Этот текстовый редактор - обычный проект, который ничем особо не примечателен.
Снизу от кнопок, вы можете писать свою программу.
Тема которая установлена это - Monokai.
Размер текста - 15.
Увеличивать окно - можно.
Шрифт - Consolas.

## Open File
Эта кнопка позволяет открывать файлы с вашего компьтера с помощью filedialog
(Думаю по названию кнопки понятно).
Также можно воспользоваться комбинацией Ctrl+O, она тоже откроет окно с файлами.

## Save
Эта кнопка быстро сохраняет введенный текст в ваш выбранный файл.
Также можно воспользоватся комбинацией Ctrl+S, будет тоже самое).

## Save As
Эта кнопка сохраняет ваши файлы с помощью filedialog - 
то есть вы можете поменять имя файла, тип и директорию.

## New File
Эта кнопка создает новое окно без определенного файла.
И вы можете им управлять, как в начале вашего запуска).
Еще можно воспользоватся сочетанием Ctrl+N

## Commands
Эта кнопка открывает новое окно где вы можете записывать свои команды для 
компиляции файла.
Вы также можете использовать другие команды.
Вот например я изпользую компилятор GNU, и мои команды будут выглядить так:

```c++
gnu name.cpp -o main
main 
```

Но я также могу добавить какие-то свои команды для удобства:

```c++
cls
gnu name.cpp -o main
main
```

Команда cls очищает всю консоль. Я ее добавил чтобы входные/выходные файлы не перемешивались.
Да и всё будет выводится в консоль, которая будет автоматически открыта.

### Примечание
Указывайте путь вашего файла! Я это потом исправлю, но все же.

### Пример
```c++
cls
gnu C:\Users\usr\name.cpp -o main
main
```

main будет сохраняться в вашу директорию (где будет стоять программа).
И после того как вы ввели все необходимые команды, нажмите "OK" для сохранения.

## ▶
Эта кнопка запускает ваши команды, которые вы ввели в окно Commands в консоли, 
которая автоматически открывается при запуске программы.
Также можно воспользоватся комбинацией F5.

## Help
Эта кнопка перекидывает вас на эту документацию, для некоторых вопросов.

## X
Просто обычное закрытия приложения. (Я ее сделал для заполнения)


# Ждите, или не ждите обновлений 
