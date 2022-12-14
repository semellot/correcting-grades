
# scripts.py

Содержит функции для изменения данных в [электронном дневнике школы](https://github.com/devmanorg/e-diary).

## Использование

Чтобы запустить скрипт скопируйте содержимое файла в `shell` или положите файл с кодом рядом с manage.py и подключите через import:
```
from scripts import *
```

Второй путь удобнее и надёжнее.

### find_schoolkid

Принимает строку с именем ученика.
Для точного поиска вводите полное имя.
Возвращает объект с учеником из модели Schoolkid.
```
>>> find_schoolkid('Фролов Иван')
<Schoolkid: Фролов Иван Григорьевич 6А>
```

### fix_marks

Исправляет плохие оценки (2 и 3) для ученика.
```
>>> fix_marks('Фролов Иван')
Все плохие оценки изменены на 5.

>>> fix_marks('Фролов Иван')
У этого ученика нет плохих оценок.
```

### remove_chastisements

Удаляет все наказания для ученика.
```
>>> remove_chastisements('Фролов Иван')
Все наказания ученика удалены.

>>> remove_chastisements('Фролов Иван')
У этого ученика нет наказаний.
```

### create_commendation

Добавляет похвалу ученику для выбранного предмета.
```
>>> create_commendation('Фролов Иван', 'Музыка')
Похвала добавлена ученику для указанного предмета.
```
