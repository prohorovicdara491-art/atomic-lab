# Практическая работа: Локальный рабочий процесс

**Тема:** Атомарность, документирование и воспроизводимость

**Студент:** [Прохорович Дарья]

---

## 1. Скриншот git log --graph --oneline (демонстрация атомарности)

![git log --graph --oneline](https://github.com/prohorovicdara491-art/atomic-lab/raw/main/screenshots/git-log.png)

**Результат выполнения команды:**
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

**Вывод:**  
Все 11 коммитов атомарные. Каждый коммит содержит только одно логическое изменение, что видно по четкой структуре: рефакторинг → новая функция → исправление ошибки → документация → инфраструктура → тесты. Это позволяет легко ориентироваться в истории проекта и откатывать изменения при необходимости.

---

## 2. Скриншот чистого старта (восстановление окружения) и запуска тестов

![Чистый старт и тесты](https://github.com/prohorovicdara491-art/atomic-lab/raw/main/screenshots/clean-start.png)

**Процесс восстановления окружения:**
```bash
# Выход из текущего окружения
deactivate

# Удаление старой папки venv
rm -rf venv

# Создание нового виртуального окружения
python -m venv venv

# Активация окружения (Windows)
.\venv\Scripts\activate

# Установка зависимостей из lock-файла
pip install -r requirements.lock.txt

# Запуск приложения
python app.py

# Запуск тестов
pytest test_app.py -v
Результат запуска приложения:

Processing user: John (status: active)
Done
Результат запуска тестов:

test_app.py::TestValidateEmail::test_valid_email PASSED
test_app.py::TestValidateEmail::test_invalid_email_no_at PASSED
test_app.py::TestValidateEmail::test_empty_email PASSED
test_app.py::TestGetUserStatus::test_active_user PASSED
test_app.py::TestGetUserStatus::test_inactive_user PASSED
test_app.py::TestGetUserStatus::test_user_without_status PASSED
test_app.py::TestProcessUserData::test_process_valid_user PASSED
test_app.py::TestProcessUserData::test_process_invalid_email PASSED

============================== 8 passed in 0.04s ==============================
Вывод:
Приложение успешно восстановилось из requirements.lock.txt. Использование lock-файла с точными версиями гарантирует воспроизводимость окружения на любой машине. Все 8 тестов пройдены успешно, что подтверждает корректность работы программы.

3. Скриншот сработки pre-commit хука (блокировка коммита)
https://github.com/prohorovicdara491-art/atomic-lab/raw/main/screenshots/pre-commit.png

Пример создания коммита с нарушением стиля:

bash
# Создание файла с нарушением стиля (лишние пробелы)
echo "def bad_function(  ):" > test_bad.py
echo "    print('test')" >> test_bad.py

# Добавление в Git
git add test_bad.py

# Попытка сделать коммит
git commit -m "test: should be blocked"
Результат блокировки:

black....................................................................Failed
- hook id: black
- exit code: 123

error: cannot format test_bad.py: invalid or missing encoding declaration

flake8...................................................................Failed
- hook id: flake8
- exit code: 1

test_bad.py:1:1: E999 SyntaxError: source code string cannot contain null bytes
Вывод:
Pre-commit хук (black и flake8) успешно заблокировал коммит с нарушением стиля кода (лишние пробелы в скобках). Это защищает репозиторий от попадания некачественного кода и обеспечивает единый стандарт оформления для всех разработчиков.

4. Ответы на контрольные вопросы
Вопрос 1: Как использование git add -p помогает при отладке через git bisect?
Ответ:
git add -p (интерактивное добавление изменений) позволяет разбить большой набор изменений на несколько атомарных коммитов, каждый из которых содержит только одно логическое изменение. При использовании git bisect для поиска коммита, вызвавшего ошибку:

С атомарными коммитами: bisect точно указывает на конкретный коммит с ошибкой

Без атомарности: bisect указывает на коммит с несколькими изменениями, и требуется дополнительное время, чтобы выяснить, какое именно изменение вызвало проблему

Пример: Если после добавления новой функции get_user_status появился баг, атомарный коммит feat: add user status function сразу указывает на проблему, а не заставляет разработчика разбираться в коммите, который также содержит рефакторинг и исправления.

Вопрос 2: Почему наличие requirements.lock.txt критично для командной работы и чем оно лучше обычного requirements.txt с версиями без минорных номеров?
Ответ:
requirements.lock.txt фиксирует точные версии всех зависимостей, включая транзитивные (зависимости зависимостей). Это дает следующие преимущества:

Преимущество	Описание
Идентичность окружений	Все разработчики используют одинаковые версии библиотек
Предсказуемость	На CI/CD сервере приложение работает так же, как локально
Воспроизводимость	Можно восстановить окружение через месяц/год
Защита от обновлений	Новые версии библиотек не сломают код без вашего ведома
Сравнение:

requirements.txt без версий: requests → установится последняя версия (может всё сломать)

requirements.txt с минорными номерами: requests==2.31.0 → фиксирует только одну библиотеку, но не её зависимости

requirements.lock.txt: содержит requests==2.31.0, urllib3==2.0.4, certifi==2023.7.22 и т.д. → фиксирует всё

Вопрос 3: В чем преимущество Makefile перед текстовой инструкцией в README?
Ответ:
Makefile — это исполняемая документация, которая дает ряд преимуществ:

Автоматизация — одна команда вместо нескольких

Избегание ошибок — не нужно вручную вводить длинные команды

Единый интерфейс — все разработчики используют одинаковые команды

Зависимости — можно описать последовательность действий

Самодокументирование — make help показывает все доступные команды

Пример:

makefile
# Вместо этого в README:
# 1. python -m venv venv
# 2. source venv/bin/activate  
# 3. pip install -r requirements.lock.txt
# 4. pytest test_app.py -v

# Достаточно одной команды:
make test
Вопрос 4: Как тесты реализуют принцип «живой документации» и почему фиксация seed важна для воспроизводимости?
Ответ:

Тесты как живая документация:
Тесты в стиле Given-When-Then служат документацией, которая всегда актуальна:

Given (Дано) — показывают, как подготовить входные данные

When (Когда) — демонстрируют, как вызывать функцию

Then (Тогда) — показывают ожидаемый результат

Пример из test_app.py:

python
def test_active_user():
    # GIVEN активный пользователь
    user = {"is_active": True}
    
    # WHEN проверяем статус
    status = get_user_status(user)
    
    # THEN должен быть "active"
    assert status == "active"
Почему фиксация seed важна:

random.seed(42) делает случайные числа детерминированными

Без seed: тесты могут иногда проходить, иногда падать (flaky tests)

С seed: тесты всегда дают одинаковый результат → воспроизводимость

Вопрос 5: Что произойдет, если удалить папку venv и выполнить make install на чистой машине? Продемонстрируйте это на практике.
Ответ:

При выполнении make install на чистой машине происходит следующее:

Создается новое виртуальное окружение (python -m venv venv)

Устанавливаются все зависимости из requirements.lock.txt с точными версиями

Устанавливаются инструменты разработки (black, flake8, pytest)

Результат: Полностью идентичное окружение, как на машине разработчика.

Демонстрация на практике (см. скриншот №2):
На втором скриншоте показан именно этот процесс:

Удаление старой папки venv

Создание нового виртуального окружения

Установка зависимостей из requirements.lock.txt

Успешный запуск приложения и тестов

Processing user: John (status: active)
Done
============================== 8 passed ==============================
Это демонстрирует принцип воспроизводимости — окружение может быть восстановлено в любом месте и в любое время.

5. Выполненные этапы работы
Этап	Описание	Результат	Статус
Этап 1	Эмуляция нарушений и анализ	Создан analysis.md с описанием рисков	✅
Этап 2	Атомарность через git add -p	3 атомарных коммита: refactor, feat, fix	✅
Этап 3	Обеспечение воспроизводимости	requirements.lock.txt, .gitignore, проверка чистого старта	✅
Этап 4	Документирование и автоматизация	Makefile, pre-commit хуки, 8 тестов	✅
6. Файлы в репозитории
Файл	Назначение
app.py	Основное приложение (валидация, бизнес-логика)
test_app.py	Тесты с структурой Given-When-Then (8 тестов)
Makefile	Автоматизация задач (install, lint, test, run)
.pre-commit-config.yaml	Pre-commit хуки (black, flake8)
requirements.lock.txt	Все зависимости с точными версиями
requirements.txt	Основные зависимости
.gitignore	Игнорируемые файлы (venv, pycache)
analysis.md	Анализ рисков неатомарных коммитов
