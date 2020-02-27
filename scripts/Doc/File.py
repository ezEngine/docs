import os

def WalkFileStructure(curDir, callback, reportFiles = True, reportFolders = True):

    for name in os.listdir(curDir):

        if name.startswith("."):
            continue

        fullPath = os.path.join(curDir, name)

        if (reportFiles and os.path.isfile(fullPath)) or (reportFolders and os.path.isdir(fullPath)):

            if not callback(curDir, name):
                return False

        if os.path.isdir(fullPath):
            if not WalkFileStructure(fullPath, callback, reportFiles, reportFolders):
                return False

    return True


def BuildFileDictionary(dir):

    nameToPath = {}

    def foundPath(parentDir: str, name: str):

        if not name.endswith(".md") and not name.endswith(".jpg") and not name.endswith(".png"):
            return True

        fullPath = os.path.join(parentDir, name)

        if name in nameToPath:
            print(f"Error: File name is not unique: '{name}' - {fullPath}")
            #return False

        nameToPath[name] = fullPath
        return True

    WalkFileStructure(dir, foundPath, reportFolders=False)
    return nameToPath