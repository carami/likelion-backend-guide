@echo off
echo ---------------------------------------
echo ?  MkDocs NAV �ڵ� ���� ���� ��...
echo ---------------------------------------

REM Python ��ũ��Ʈ ����
python nav-generator.py

IF %ERRORLEVEL% NEQ 0 (
    echo ? ���� �߻�: Python ��ũ��Ʈ ���� ����
    pause
    exit /b 1
)

echo ? nav �׸��� mkdocs.yml�� ���������� �ݿ��Ǿ����ϴ�.
echo ? mkdocs serve �� ���� Ȯ�� ����
pause
