markdown
# Практическая работа: Локальный рабочий процесс

**Студент:** [Прохорович Дарья]  
**Дата:** 31.03.2026

---

## 1. Скриншот git log --graph --oneline (атомарность)

![git log](https://github.com/prohorovicdara491-art/atomic-lab/raw/main/screenshots/git-log.png)

**Результат:**
f298198 chore: add pre-commit config and Makefile

ea490f0 test: add unit tests with Given-When-Then structure

b80c06c chore: fix file endings with pre-commit

02af128 fix: remove unused variable in main function

35b36ed chore: add .gitignore

0a73434 chore: fix dependencies versions

fa41d41 fix: add error handling to auth

9c74a00 feat: add user status function

e7488e5 refactor: rename variables for clarity

cb9b070 docs: add analysis of atomicity risks

9dc9c14 Initial setup

text

**Вывод:** Все 11 коммитов атомарные — каждый содержит только одно изменение.

---

## 2. Скриншот чистого старта и запуска тестов

![чистый старт](https://github.com/prohorovicdara491-art/atomic-lab/raw/main/screenshots/clean-start.png)

**Процесс:**
deactivate
rm -rf venv
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.lock.txt
python app.py
pytest test_app.py -v

text

**Результат:**
Processing user: John (status: active)
Done

============================== 8 passed in 0.04s ==============================

text

**Вывод:** Приложение восстановилось из lock-файла, все тесты пройдены.

---

## 3. Скриншот pre-commit хука (блокировка коммита)

![pre-commit](https://github.com/prohorovicdara491-art/atomic-lab/raw/main/screenshots/pre-commit.png)

**Попытка сделать коммит с ошибкой:**
git commit -m "test"
black....................................................................Failed
flake8...................................................................Failed

text

**Вывод:** Pre-commit заблокировал коммит с плохим стилем кода.

---

## 4. Ответы на контрольные вопросы

### Вопрос 1: Как git add -p помогает при отладке через git bisect?

`git add -p` позволяет разбить изменения на атомарные коммиты (каждый коммит = одно изменение). При поиске бага через `git bisect` это помогает точно определить, какой именно коммит вызвал ошибку, вместо того чтобы разбираться в куче изменений из одного коммита.

---

### Вопрос 2: Почему requirements.lock.txt критичен для командной работы?

`requirements.lock.txt` фиксирует точные версии ВСЕХ библиотек (и тех, которые зависят от других). Это дает:
- У всех разработчиков одинаковые версии
- Приложение работает одинаково на всех компьютерах
- Можно восстановить окружение через год

Обычный `requirements.txt` без версий может установить новые версии, которые сломают код.

---

### Вопрос 3: В чем преимущество Makefile перед текстовой инструкцией?

Makefile автоматизирует команды. Вместо того чтобы вручную писать 3-4 команды, достаточно одной: `make install`. Это быстрее, исключает ошибки и все разработчики используют одинаковые команды.

---

### Вопрос 4: Как тесты реализуют «живую документацию» и почему важен seed?

Тесты в стиле Given-When-Then показывают, как пользоваться функциями и что они возвращают. Это всегда актуальная документация.

Фиксация seed (`random.seed(42)`) делает случайные числа одинаковыми при каждом запуске, поэтому тесты всегда дают одинаковый результат (не падают случайно).

---

### Вопрос 5: Что будет, если удалить venv и выполнить make install?

Будет создано новое виртуальное окружение и установлены все зависимости из `requirements.lock.txt`. Приложение запустится и будет работать так же, как и раньше. Это показано на скриншоте №2.

---

## 5. Выполненные этапы

| Этап | Что сделано | Статус |
|------|-------------|--------|
| 1 | Создан репозиторий, файлы, анализ рисков | ✅ |
| 2 | Сделаны 3 атомарных коммита через git add -p | ✅ |
| 3 | Создано venv, lock-файл, проверен чистый старт | ✅ |
| 4 | Созданы Makefile, pre-commit, тесты | ✅ |

---

**Ссылка на репозиторий:** https://github.com/prohorovicdara491-art/atomic-lab
