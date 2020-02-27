import os
import re
from typing import List, Tuple

def DetermineTocOrder(curDir, order: list):

    tocTxt = os.path.join(curDir, "toc.txt")
    folders = []
    subItems = []

    if os.path.exists(tocTxt):
        
        with open(tocTxt, "r") as tocFile:
            subItems = tocFile.readlines()

    else:

        for item in os.listdir(curDir):
            subItems.append(item)

    for item in subItems:

        itemName = item.strip()

        if itemName == "":
            continue
        if itemName == "media":
            continue

        folderName = itemName
        displayName = itemName

        if folderName == "---":

            order.append("---")

        else:

            displayName = displayName.replace("-", " ")
            displayName = displayName.title()

            sep = itemName.find("|")
            
            if sep >= 0:
                folderName = itemName[0:sep]
                displayName = itemName[sep+1:]

            folderName = folderName.strip()
            displayName = displayName.strip()

            subPath = os.path.join(curDir, folderName)

            if os.path.isdir(subPath):

                order.append(">>>" + displayName)
                DetermineTocOrder(subPath, order)
                order.append("<<<")

            else:
                order.append(subPath)

    return

def GenerateToc(nameToFile: dict, order: list):

    tocContent = ""

    topLevel = True
    indentation = ""

    for item in order:

        line:str = item

        if item == "<<<":

            if indentation == "":
                topLevel = True
            else:
                indentation = indentation[0:-2]
            
            continue

        if line.startswith(">>>"):

            headline = line[3:]

            if topLevel:
                tocContent += f"\n### {headline}\n\n"

                topLevel = False
                indentation = ""
            else:
                tocContent += f"{indentation}* __{headline}__\n"

                indentation = indentation + "  "

        elif line.startswith("---"):

            tocContent += f"\n{indentation}---\n"

        else:

            tocContent += f"{indentation}* []({item})\n"

    return tocContent