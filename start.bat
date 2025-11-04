@echo off
echo =====================================
echo Iniciando sistema de Cotações
echo =====================================

:: Ativa o ambiente virtual do Django (se existir)
echo Ativando ambiente virtual...
cd backend
if exist venv (
    call venv\Scripts\activate
)

:: Inicia o backend Django em uma nova janela
echo Iniciando o servidor Django...
start "Django Server" cmd /k "python manage.py runserver"

:: Volta para a raiz e inicia o frontend
cd ..
cd frontend

echo Iniciando o frontend Vue.js...
start "Vue Frontend" cmd /k "npm run dev"

echo =====================================
echo Sistema iniciado! 
echo Backend: http://localhost:8000
echo Frontend: http://localhost:5173 (ou porta indicada)
echo =====================================

pause
