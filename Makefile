PYTHON = python
VENV = venv
VENV_SCRIPTS = $(VENV)/Scripts
PYTHON_VENV = $(VENV_SCRIPTS)/python
PIP_VENV = $(VENV_SCRIPTS)/pip

.PHONY: help install lint test run clean

help:
	@echo "Доступные команды:"
	@echo "  make install   - Создать venv и установить зависимости"
	@echo "  make lint      - Проверить стиль кода"
	@echo "  make test      - Запустить тесты"
	@echo "  make run       - Запустить приложение"
	@echo "  make clean     - Очистить временные файлы"

install:
	$(PYTHON) -m venv $(VENV)
	$(PIP_VENV) install -r requirements.lock.txt
	$(PIP_VENV) install black flake8 pytest

lint:
	$(PYTHON_VENV) black --check app.py
	$(PYTHON_VENV) flake8 app.py

test:
	$(PYTHON_VENV) pytest test_app.py -v

run:
	$(PYTHON_VENV) python app.py

clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
