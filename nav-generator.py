import os
import yaml

# 제외할 단일 파일
EXCLUDE_FILES = ["index.md", "faq.md"]

# 교안 자동 포함에서 제외할 디렉토리
EXCLUDE_DIRS = ["checklist"]

def generate_curriculum_nav(root_dir="docs"):
    교안_nav = []

    for root, dirs, files in os.walk(root_dir):
        rel_dir = os.path.relpath(root, root_dir).replace("\\", "/")
        if rel_dir in EXCLUDE_DIRS:
            continue

        md_files = [f for f in files if f.endswith(".md") and f not in EXCLUDE_FILES]
        if not md_files:
            continue

        page_entries = []
        for f in sorted(md_files):
            name = os.path.splitext(f)[0].replace("_", " ").title()
            file_path = os.path.join(rel_dir, f).replace("\\", "/")
            page_entries.append({name: file_path})

        if rel_dir == ".":
            교안_nav.extend(page_entries)
        else:
            section_name = rel_dir.replace("_", " ").title()
            교안_nav.append({section_name: page_entries})

    return 교안_nav

def generate_checklist_nav(checklist_dir="docs/checklist"):
    checklist_nav = []
    for f in sorted(os.listdir(checklist_dir)):
        if f.endswith(".md"):
            file_path = f"checklist/{f}"
            checklist_nav.append(file_path)
    return checklist_nav

def update_mkdocs_yml():
    교안_nav = generate_curriculum_nav()
    checklist_nav = generate_checklist_nav()

    with open("mkdocs.yml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    fixed_nav_top = [{"홈": "index.md"}]
    fixed_nav_bottom = [
        {"체크리스트": checklist_nav},
        {"FAQ": "faq.md"}
    ]

    config["nav"] = fixed_nav_top + [{"교안": 교안_nav}] + fixed_nav_bottom

    with open("mkdocs.yml", "w", encoding="utf-8") as f:
        yaml.dump(config, f, allow_unicode=True)

    print("✅ mkdocs.yml nav 항목이 완성되었습니다.")

if __name__ == "__main__":
    update_mkdocs_yml()
