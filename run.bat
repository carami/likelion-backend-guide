@echo off
echo ---------------------------------------
echo 🛠  MkDocs NAV 자동 생성 실행 중...
echo ---------------------------------------

REM Python 스크립트 실행
python nav-generator.py

IF %ERRORLEVEL% NEQ 0 (
    echo ❌ 오류 발생: Python 스크립트 실행 실패
    pause
    exit /b 1
)

echo ✅ nav 항목이 mkdocs.yml에 성공적으로 반영되었습니다.
echo 🔄 mkdocs serve 로 로컬 확인 가능
pause
