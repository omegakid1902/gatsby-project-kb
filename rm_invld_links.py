import os
import re
from shutil import *

base_docs_url = "./demo/content"


# For Regex, match groups are:
#       0: Whole roamlike link e.g. [[filename#title|alias]]
#       1: Whole roamlike link e.g. filename#title|alias
#       2: filename
#       3: #title
#       4: |alias
ROAMLINK_RE = r'\[\[(([^\]#\|]*)(#[^\|\]]+)*(\|[^\]]*)*)\]\]'

class RoamLinkDetect:
    def __init__(self, base_docs_url, page_url):
        self.base_docs_url = base_docs_url
        self.page_url = page_url.replace("./docs/", "").replace("\\", "/")
        self.file_name = os.path.basename(page_url).replace(".md", "")

    def simplify(self, filename):
        """ ignore - _ and space different, replace .md to '' so it will match .md file,
        if you want to link to png, make sure you filename contain suffix .png, same for other files
        but if you want to link to markdown, you don't need suffix .md """
        return re.sub(r"[\-_ ]", "", filename.lower()).replace(".md", "")

    def gfm_anchor(self, title):
        """Convert to gfw title / anchor 
        see: https://gist.github.com/asabaylus/3071099#gistcomment-1593627"""
        if title:
            title = title.strip().lower()
            title = re.sub(r'[^\w\u4e00-\u9fff\- ]', "", title)
            title = re.sub(r' +', "-", title)
            return title
        else:
            return ""

    def __call__(self, match):
        # Name of the markdown file
        whole_link = match.group(0)
        filename = match.group(2).strip() if match.group(2) else ""
        title = match.group(3).strip() if match.group(3) else ""
        format_title = self.gfm_anchor(title)
        alias = match.group(4).strip('|') if match.group(4) else ""
        #print(f'    --debug: link: {whole_link}, filename:{filename}, title: {title}, format_title: {format_title} alias:{alias}  ')
        
        # Absolute URL of the linker
        abs_linker_url = os.path.dirname(
            os.path.join(self.base_docs_url, self.page_url))

        # Find directory URL to target link
        rel_link_url = ''
        # Walk through all files in docs directory to find a matching file
        if filename:
            for root, dirs, files in os.walk(self.base_docs_url):
                for name in files:
                    # If we have a match, create the relative path from linker to the link
                    if self.simplify(name) == self.simplify(filename):
                        return whole_link

            print('WARNING: unable to find ' + filename + ' in directory ' + self.base_docs_url)
            
            # Replace roamlink by italic style
            return "__" + match.group(2) + "__"

        return whole_link

for root, dirs, files in os.walk(base_docs_url):
    for file in files:
        if file.endswith(".md"):
            page_url = os.path.join(root, file)
            #print(f'--debug: Scan File: {page_url}')
            with open(os.path.join(root, file), encoding="utf-8") as f:
                markdown = f.read()
                markdown = re.sub(ROAMLINK_RE,
                          RoamLinkDetect(base_docs_url, page_url), markdown)

            with open(os.path.join(root, file), 'w', encoding="utf-8") as f:
                f.write(markdown)
