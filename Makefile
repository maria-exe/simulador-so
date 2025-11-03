PYTHON = python3
PIP = pip3

.PHONY: all
all: run

.PHONY: run
run:
	@echo "--- Executando o SimuladorOS (Usando Python do Sistema) ---"
	$(PYTHON) main.py

.PHONY: install
install: requirements.txt
	@echo "--- Instalando dependências para o usuário atual (flag --user) ---"
	$(PIP) install --upgrade pip
	$(PIP) install --user -r requirements.txt
	@echo "Instalação concluída."
	@echo "AVISO: Certifique-se que o diretório de pacotes do usuário está no seu PATH."

.PHONY: clean
clean:
	@echo "--- Limpando arquivos de cache e gráficos (.png) ---"
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.png" -delete
	@echo "Limpeza concluída."