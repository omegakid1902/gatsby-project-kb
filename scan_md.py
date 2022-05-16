import os

base_docs_url = "./demo/content/"

for root, dirs, files in os.walk(base_docs_url):
    for file in files:
        if file.endswith(".md"):
            publish = False
            with open(os.path.join(root, file), encoding="utf8") as f:
                if 'publish: True' in f.read():
                    publish = True
                    
            if publish == False:
                print("Remove file:", file)
                os.remove(os.path.join(root, file))

for root, dirs, files in os.walk(base_docs_url):
    for name in files:
        abs_link_url = os.path.join(root, name)
        if abs_link_url.endswith('.md'):
            with open(abs_link_url, 'r+', encoding='utf_8') as fi:
                content = fi.readlines()
                fi.seek(0)
                for line in content:
                    if line.rstrip().startswith("# ") or line.rstrip().startswith("UID: ") or line.rstrip().startswith("birth:") or line.rstrip().startswith("death:"):
                        continue
                    fi.write(line)
                fi.truncate()


