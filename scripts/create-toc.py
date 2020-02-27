#!python3

import os
import re

import Doc

indexMdfile = os.path.normpath("./docs/index.md")

if os.path.exists(indexMdfile):
    os.remove(indexMdfile)

nameToFile = Doc.File.BuildFileDictionary("./docs")

tocOrder = []
Doc.Toc.DetermineTocOrder("./docs", tocOrder)

tocContent = Doc.Toc.GenerateToc(nameToFile, tocOrder)

with open("./docs/index.txt", "r") as indexTxt:
    indexContent = indexTxt.read()

indexContent = indexContent.replace("{TOC}", tocContent)

with open(indexMdfile, "w") as indexMd:
    indexMd.write(indexContent)

nameToFile["index.md"] = indexMdfile

Doc.Link.FixFileLinks(indexMdfile, nameToFile)
Doc.Link.FixAllFileLinks(nameToFile)
