#!/bin/bash
echo "🛠️ MkDocs NAV 자동 생성 중..."
python3 nav-generator.py

if [ $? -ne 0 ]; then
  echo "❌ 오류 발생: Python 스크립트 실패"
  exit 1
fi

echo "✅ nav 자동 갱신 완료!"
