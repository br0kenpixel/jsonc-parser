import json

__author__ = "br0kenpixel"

def loads(string):
    assert isinstance(string, str), "Argument must be a string"
    content = string
    del string
    content = content.split("\n")
    content = list(map(lambda line: line.strip(), content))
    content = list(filter(lambda line: not line.startswith("//"), content)) #Delete single line comments
    content = list(filter(lambda line: not line.startswith("#"), content)) #Delete single line comments
    content = list(filter(lambda line: line != "", content)) #Delete empty lines
    #Delete single line comments using /* and */
    for index, line in enumerate(content):
        if "/*" in line and "*/" in line:
            start = line.index("/*")
            content[index] = line[:start]
        if "//" in line:
            start = line.index("//")
            content[index] = line[:start]
    #Delete multi-line comments
    multilineComment = False
    filteredContent = []
    for index, line in enumerate(content):
        if "/*" in line:
            multilineComment = True
            continue
        if "*/" in line:
            multilineComment = False
            continue
        if multilineComment:
            continue
        filteredContent.append(line)
    content = filteredContent
    content = "\n".join(content)
    return json.loads(content)

def load(stream):
    content = stream.read()
    assert "\n" in content, "Stream must contain a multi-line string"
    if not isinstance(content, str):
        content = content.decode()
    return loads(content)

if __name__ == "__main__":
    print("Running test...")
    f = open("example.jsonc")
    json = load(f)
    print("Use \"json\" variable to evaluate results")