import markdown, pypandoc

BlogHeader = """<!DOCTYPE html><html><head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>yfan's personal website</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" type="text/css" href="../files/main.css"></head><body>
<h1>This is yfan's blog</h1>
"""

BlogFooter = """<a href="../index.html"><== Return to homepage</a>
<a class="kopimi" href="http://www.kopimi.com/kopimi" title="Kopimi"><img class="kopimi" src="../files/kopimi.svg" title="Kopimi Logo"></a>
<script src="../files/main.js"></script></body></html>
"""


def markdownConverter(markdownFilename):
    """
    This function converts my markdown file into a html body with a Table of contents(TOC). 
    """
    with open(markdownFilename, "r", encoding="utf-8") as f:
        text = f.read()
    return markdown.markdown(text, extensions=["markdown.extensions.toc"])


def writeToBlog(htmlFilename, markdownStr):
    """
    Combine blog header--which is definded in this file--and footer with body into a standalone html file.
    This blog page now has a TOC and its contents all in one page, I'll consider seperate them into two one day. 
    """
    with open(htmlFilename, "w+", encoding="utf-8") as f:
        f.write(BlogHeader)
        f.write(markdownStr)
        f.write(BlogFooter)


if __name__ == "__main__":
    writeToBlog("./blog/blog.html", markdownConverter("blog.md"))
    # I cheat here. I don't know howto unset auto_identifiers in markdown, so using pandoc instead, and cpy & paste later
    print(pypandoc.convert_file("main.md", "html", format="markdown-auto_identifiers"))
