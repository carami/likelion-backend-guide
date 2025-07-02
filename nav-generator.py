import os
import yaml

def generate_nav(root_dir="docs"):
    교안_nav = []

    for root, dirs, files in os.walk(root_dir):
        md_files = [f for f in files if f.endswith(".md") and f != "index.md"]
        if not md_files:
            continue

        rel_path = os.path.relpath(root, root_dir).replace("\\", "/")
        page_entries = []

        for f in sorted(md_files):
            name = os.path.splitext(f)[0].replace("_", " ").title()
            file_path = os.path.join(rel_path, f).replace("\\", "/")
            page_entries.append({name: file_path})

        if rel_path == ".":
            교안_nav.extend(page_entries)
        else:
            section_name = rel_path.replace("_", " ").title()
            교안_nav.append({section_name: page_entries})

    return 교안_nav

def update_mkdocs_yml(교안_nav):
    with open("mkdocs.yml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # 고정된 메뉴는 위/아래 배치
    fixed_nav_top = [{"홈": "index.md"}]
    fixed_nav_bottom = [
        {"체크리스트": [
            "checklist/week01.md",
            "checklist/week02.md"
        ]},
        {"FAQ": "faq.md"}
    ]

    # 전체 nav 구성
    config["nav"] = fixed_nav_top + [{"교안": 교안_nav}] + fixed_nav_bottom

    with open("mkdocs.yml", "w", encoding="utf-8") as f:
        yaml.dump(config, f, allow_unicode=True)

    print("✅ mkdocs.yml nav 항목이 '교안'으로 자동 묶여 생성되었습니다.")

if __name__ == "__main__":
    교안 = generate_nav()
    update_mkdocs_yml(교안)
