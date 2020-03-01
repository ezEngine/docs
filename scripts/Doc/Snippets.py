import os
import re

from .File import *

def SearchSourceSnippets(srcDir: str, snippets: dict):

    def FoundFile(parentDir: str, name: str):

        if not name.endswith(".h") and not name.endswith(".cpp"):
            return True

        with open(os.path.join(parentDir, name), "r") as file:
            lines = file.readlines()

        lineIdx = 0

        while(lineIdx < len(lines)):

            line = lines[lineIdx]
            lineIdx += 1

            idx = line.find("BEGIN-DOCS-CODE-SNIPPET:")
            if idx >= 0:

                snippetName = line[idx + 24:].strip(' \r\n\t').lower()

                print(f"Found snippet: {snippetName}")

                snippetText = ""
                maxWhiteSpace = 100

                snippetLines = []

                while(lineIdx < len(lines)):
                    lineIdx += 1
                    line = lines[lineIdx - 1]
                    line = line.replace("\t", "  ")

                    if line.find("END-DOCS-CODE-SNIPPET") >= 0:
                        break

                    wsc = len(line) - len(line.lstrip(' '))
                    maxWhiteSpace = min(maxWhiteSpace, wsc)

                    snippetLines.append(line)

                for line in snippetLines:
                    line = line[maxWhiteSpace:]
                    snippetText += line

                snippets[snippetName] = snippetText

        return True

    WalkFileStructure(srcDir, FoundFile, reportFolders=False)



def ReplaceTargetSnippets(targetDir: str, snippets: dict):

    def FoundFile(parentDir: str, name: str):

        if not name.endswith(".md"):
            return True

        with open(os.path.join(parentDir, name), "r") as file:
            lines = file.readlines()

        lineIdx = 0

        newLines = []
        replacedAny = False

        while(lineIdx < len(lines)):

            line = lines[lineIdx]
            lineIdx += 1

            newLines.append(line)

            idx = line.find("BEGIN-DOCS-CODE-SNIPPET:")
            if idx >= 0:

                snippetName = line[idx + 24:].lower()
                snippetName = snippetName.replace("-->", "")
                snippetName = snippetName.strip(' \r\n\t')

                print(f"Replacing snippet: {snippetName}")
                replacedAny = True

                newLines.append("```cpp\n")
                newLines.append(snippets[snippetName])
                newLines.append("```\n")

                while(lineIdx < len(lines)):
                    if lines[lineIdx].find("END-DOCS-CODE-SNIPPET") >= 0:
                        break

                    lineIdx += 1

        if replacedAny:

            with open(os.path.join(parentDir, name), "w") as file:
                file.writelines(newLines)

        return True

    WalkFileStructure(targetDir, FoundFile, reportFolders=False)