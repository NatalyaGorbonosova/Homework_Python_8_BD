Выполнила: Горбоносова Наталья

Схема взаимодействия модулей: scema.jpg

# База данных учеников

Имеет графический интерфейс, а также БД Sqlite.

## Главное меню

Содержит три кнопки:
1. Список

При нажатии показывает список всех учеников

2. Найти

Переходит в окно поиска ученика по выбранным критериям

3. Добавить

Переходит в окно добавления ученика

## Окно Списка ученико

Представляет собой список учеников в текстовом поле, что позволяет копировать данные ученика. 

## Окно поиска ученика

Сначала необходимо выбрать критерий поиска из выпадающего списка. После нажатия кнопки "Выбрать" появляется поле ввода данных, затем при нажатии кнопки "Ввести значение" появляется список учеников, подходящих под введенные критерии. Также появляются кнопки для удаления и изменения данных ученика по id. 

При нажатии на удаление появляется новое окно с полем для ввода id ученика, которого нужно удалить из списка.

При нажатии кнопки "Изменить данные ученика" появляется окно для внесения изменений. В данном окне есть поле ввода для фамилии, имени, класса, родителей и телефона, в которых уже есть исходные данные ученика и которые можно редактировать. Индекс ученика нельзя менять.

## Окно добавления ученика

В окне находится уже назначенный индекс и пять полей для ввода данных (фамилия, имя, класс, имена родителей, телефон). После нажатия на кнопку "Добавить" данные добавляются в БД.