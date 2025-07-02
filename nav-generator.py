import os
import yaml

def generate_nav(root_dir="docs"):
    nav = []

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
            nav.extend(page_entries)
        else:
            section_name = rel_path.replace("_", " ").title()
            nav.append({section_name: page_entries})

    return nav

def update_mkdocs_yml(nav):
    with open("mkdocs.yml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    config["nav"] = nav

    with open("mkdocs.yml", "w", encoding="utf-8") as f:
        yaml.dump(config, f, allow_unicode=True)

if __name__ == "__main__":
    nav_data = generate_nav()
    update_mkdocs_yml(nav_data)
    print("✅ mkdocs.yml nav 갱신 완료!")
