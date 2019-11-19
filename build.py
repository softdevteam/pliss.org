#!/usr/bin/env python3

import codecs, os, shutil, re, sys
from mako.template import Template
from mako.lookup import TemplateLookup

SITE_NAME = "https://pliss.org"

def preprocessor(template):
    template = template.replace("\\", '&#92;')
    return template

class Build:
    def __init__(self):
        self.htdocs_dir = os.environ.get("HTDOCS_DIR", "htdocs")
        self._abs_htdocs_dir = os.path.abspath(self.htdocs_dir)

    def build(self):
        lookup = TemplateLookup(directories=["."])

        assert SITE_NAME[-1] != "/"

        for root, _, leafs in os.walk("templates", followlinks=True):
            if root == "templates":
                dest_root = self.htdocs_dir
            else:
                assert root.startswith("templates")
                dest_root = self.htdocs_dir + root[len("templates"):]
            if not os.path.exists(dest_root):
                os.makedirs(dest_root)

            for l in leafs:
                if l == ".gitignore" or os.path.splitext(l)[1] in [".inc", ".out"]:
                    continue

                source = os.path.join(root, l)
                dest = os.path.abspath(os.path.join(dest_root, l))

                if os.path.splitext(source)[1] in (".html", ".rss") and not os.path.basename(source).startswith('google'):
                    print("Process", dest)
                    # render HTML files
                    content = Template(filename=source, lookup=lookup, default_filters=['decode.utf8'], input_encoding='utf-8', output_encoding="utf8", encoding_errors='replace', preprocessor=preprocessor)

                    # get current page name
                    assert dest.startswith(self._abs_htdocs_dir)
                    page = dest[len(self._abs_htdocs_dir)+1:]
                    m = re.match("([^\.]*\/)*(([^\.]+).html)", page)
                    if m:
                        page = m.group(3)
                    else:
                        page = ""

                    # get path to root
                    rootpath = ("../" * root.count("/"))[:-1]

                    f = codecs.open(dest, "w", encoding="utf-8")
                    f.write(content.render_unicode(host=SITE_NAME, rootpath=rootpath, leaf=l, page=page))
                    f.close()
                else:
                    sys.stdout.write("Copy %s" % dest)
                    if os.path.exists(dest) and os.stat(source).st_mtime <= os.stat(dest).st_mtime:
                        sys.stdout.write(" (cached)\n")
                        continue
                    sys.stdout.write("\n")
                    shutil.copy(source, dest)
                    shutil.copystat(source, dest)


if __name__ == "__main__":
    Build().build()
