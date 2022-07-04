"""
Automated blogpost builder for static website

Used by my GitHub pages site, you can use a modified version for your site if you wish

Maxim Hoxha 2022
"""

import glob

excludeList = ["blog\\examplepost.html", "blog\\test98.html"] #These are testing files
blogMainPath = "blogtop.html" #The following constants are very specific to my site, so uh... modify them before reusing them.
blogIndent = "\t\t\t\t"
vertBreak = blogIndent + '<div class="vertbreak"></div>\n'
dateNoteOpen = blogIndent + '<p class="dateNote">'
dateHeadOpen = blogIndent + '<p class="dateHead">'
paraClose = '</p>\n'
expanderOpen = blogIndent + '<div class="postexpand">\n\
					<a href="'
expanderClose = '">See more...</a>\n\
				</div>\n'
navWrapperOpen = blogIndent + '<div id="blognav" class="postnav">\n\
					<ul>\n'
navWrapperClose = '					</ul>\n\
				</div>\n'
navPrevOpen = blogIndent + '\t\t<li><a href="'
navNextOpen = blogIndent + '\t\t<li><a href="'
standardBlogHtml = '<!DOCTYPE html>\n\
<html>\n\
	<head>\n\
		<title>Stuff by Max - Blog</title>\n\
		<link rel="stylesheet" href="../stdstyle.css" />\n\
		<link rel="shortcut icon" href="../assets/icon.png" />\n\
	</head>\n\
	<body>\n\
		<div id="commonHeader" class="masterhead">\n\
			<img src="../assets/banner.png" id="banner" title="Welcome to my website!"/>\n\
		</div>\n\
		<div id="belowHead">\n\
			<div id="topnavbar" class="topnav">\n\
				<ul>\n\
					<li><a href="../index.html">Home</a></li>\n\
					<li><a href="../blogtop.html">Blog</a></li>\n\
					<li><a href="../projectstop.html">Projects</a></li>\n\
					<li><a href="../links.html">Links</a></li>\n\
					<li><a href="../about.html">About</a></li>\n\
				</ul>\n\
			</div>\n\
			<div id="topnavbarmobile" class="topnavmobile">\n\
				<p id="menuButton" class="closed">Menu</p>\n\
				<ul id="menu" class="closed">\n\
					<li><a href="../index.html">Home</a></li>\n\
					<li><a href="../blogtop.html">Blog</a></li>\n\
					<li><a href="../projectstop.html">Projects</a></li>\n\
					<li><a href="../links.html">Links</a></li>\n\
					<li><a href="../about.html">About</a></li>\n\
				<ul>\n\
			</div>\n\
			<div id="mainBody" class="main">\n\
				<div id="bodyHeader" class="pagehead">\n\
					<h1>Blog maxBlog = new Blog();</h1>\n\
					<h2>My blog</h2>\n\
				</div>\n\
				<!--HINT:nav-->\n\
				<!--HINTEND:nav-->\n\
				<div class="vertbreak"></div>\n\
				<!--HINT:blogpost-->\n\
				<!--HINTEND:blogpost-->\n\
			</div>\n\
			<footer id="commonFooter">\n\
				<p>2022 Maxim Hoxha</p>\n\
			</footer>\n\
		</div>\n\
		<script src="../scripts/menuopen.js"></script>\n\
	</body>\n\
</html>'
standardBlogTopHtml = '<!DOCTYPE html>\n\
<html>\n\
	<head>\n\
		<title>Stuff by Max - Blog</title>\n\
		<link rel="stylesheet" href="stdstyle.css" />\n\
		<link rel="shortcut icon" href="assets/icon.png" />\n\
	</head>\n\
	<body>\n\
		<div id="commonHeader" class="masterhead">\n\
			<img src="assets/banner.png" id="banner" title="Welcome to my website!"/>\n\
		</div>\n\
		<div id="belowHead">\n\
			<div id="topnavbar" class="topnav">\n\
				<ul>\n\
					<li><a href="index.html">Home</a></li>\n\
					<li><a href="blogtop.html">Blog</a></li>\n\
					<li><a href="projectstop.html">Projects</a></li>\n\
					<li><a href="links.html">Links</a></li>\n\
					<li><a href="about.html">About</a></li>\n\
				</ul>\n\
			</div>\n\
			<div id="topnavbarmobile" class="topnavmobile">\n\
				<p id="menuButton" class="closed">Menu</p>\n\
				<ul id="menu" class="closed">\n\
					<li><a href="index.html">Home</a></li>\n\
					<li><a href="blogtop.html">Blog</a></li>\n\
					<li><a href="projectstop.html">Projects</a></li>\n\
					<li><a href="links.html">Links</a></li>\n\
					<li><a href="about.html">About</a></li>\n\
				<ul>\n\
			</div>\n\
			<div id="mainBody" class="main">\n\
				<div id="bodyHeader" class="pagehead">\n\
					<h1>Blog maxBlog = new Blog();</h1>\n\
					<h2>My blog</h2>\n\
				</div>\n\
				<h3>Latest Posts</h3>\n\
				<!--HINT:bloglist-->\n\
				<!--HINTEND:bloglist-->\n\
			</div>\n\
			<footer id="commonFooter">\n\
				<p>2022 Maxim Hoxha</p>\n\
			</footer>\n\
		</div>\n\
		<script src="scripts/menuopen.js"></script>\n\
	</body>\n\
</html>'
newBlogPostTemplate = '<!DOCTYPE html>\n\
<html>\n\
	<head>\n\
		<title>Stuff by Max - Blog</title>\n\
		<link rel="stylesheet" href="../stdstyle.css" />\n\
		<link rel="shortcut icon" href="../assets/icon.png" />\n\
	</head>\n\
	<body>\n\
		<div id="commonHeader" class="masterhead">\n\
			<img src="../assets/banner.png" id="banner" title="Welcome to my website!"/>\n\
		</div>\n\
		<div id="belowHead">\n\
			<div id="topnavbar" class="topnav">\n\
				<ul>\n\
					<li><a href="../index.html">Home</a></li>\n\
					<li><a href="../blogtop.html">Blog</a></li>\n\
					<li><a href="../projectstop.html">Projects</a></li>\n\
					<li><a href="../links.html">Links</a></li>\n\
					<li><a href="../about.html">About</a></li>\n\
				</ul>\n\
			</div>\n\
			<div id="topnavbarmobile" class="topnavmobile">\n\
				<p id="menuButton" class="closed">Menu</p>\n\
				<ul id="menu" class="closed">\n\
					<li><a href="../index.html">Home</a></li>\n\
					<li><a href="../blogtop.html">Blog</a></li>\n\
					<li><a href="../projectstop.html">Projects</a></li>\n\
					<li><a href="../links.html">Links</a></li>\n\
					<li><a href="../about.html">About</a></li>\n\
				<ul>\n\
			</div>\n\
			<div id="mainBody" class="main">\n\
				<div id="bodyHeader" class="pagehead">\n\
					<h1>Blog maxBlog = new Blog();</h1>\n\
					<h2>My blog</h2>\n\
				</div>\n\
				<!--HINT:nav-->\n\
				<div id="blognav" class="postnav">\n\
					<ul>\n\
						<li><a href="test98.html">Previous post</a></li>\n\
						<li><a href="">Next post</a></li>\n\
					</ul>\n\
				</div>\n\
				<!--HINTEND:nav-->\n\
				<div class="vertbreak"></div>\n\
				<!--DATE:1900-01-01-->\n\
				<!--HINT:blogpost-->\n\
				<p class="dateHead">1 January 1900</p>\n\
				<article id="postExample">\n\
					<div id="bodyHeader" class="pagehead">\n\
						<h1>Example post</h1>\n\
					</div>\n\
					<p>This post serves as a template for further posts. With support for <span class="bold">boldface</span>, <span class="italic">italics</span>, <span class="underline">underlining</span>, <span class="strikethrough">strikethrough</span> and <span class="spoiler">spoiler hiding</span>. Do not actually post this, as it doesn\'t include any useful information.</p>\n\
					<h2>A useless heading</h2>\n\
					<p>I really don\'t think extra stuff like this will help</p>\n\
				</article>\n\
				<!--HINTEND:blogpost-->\n\
			</div>\n\
			<footer id="commonFooter">\n\
				<p>2022 Maxim Hoxha</p>\n\
			</footer>\n\
		</div>\n\
		<script src="../scripts/menuopen.js"></script>\n\
	</body>\n\
</html>'

daysInMonths = [31,28,31,30,31,30,31,31,30,31,30,31] #30 days hath September...
monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def LeapDaysSinceYear(targetyr, startyr=1900): #Uses the Gregorian rule (leap year every 4 years, except years divisble by 100 if they're not also divisble by 400)
    return ((targetyr//4) - (startyr//4)) - ((targetyr//100) - (startyr//100)) + ((targetyr//400) - (startyr//400))

def IsLeapYear(yr): #Uses the Gregorian rule (leap year every 4 years, except years divisble by 100 if they're not also divisble by 400)
    if yr%4 == 0:
        if yr%100 == 0:
            if yr%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def ConvertISODateStringToInteger(datestr): #String MUST be formatted as 'yyyy-mm-dd'
    dateint = 0
    epoch = 1900
    yearstr = datestr[0:4]
    monthstr = datestr[5:7]
    daystr = datestr[8:10]
    dateint += int(daystr) - 1
    monthint = int(monthstr)
    for i in range(1, monthint):
        dateint += daysInMonths[i-1]
    yearint = int(yearstr)
    if IsLeapYear(yearint) and monthint > 2:
        dateint += 1
    dateint += LeapDaysSinceYear(yearint-1,epoch)
    dateint += 365*(yearint-epoch)
    return dateint

def ConvertISODateStringToText(datestr): #String MUST be formatted as 'yyyy-mm-dd'
    yearstr = datestr[0:4]
    monthstr = datestr[5:7]
    daystr = datestr[8:10]
    monthint = int(monthstr) - 1
    daystr = str(int(daystr))
    return daystr + " " + monthNames[monthint] + " " + yearstr

def ExtractBlogText(outerHtml):
    startInd = outerHtml.index("<!--HINT:blogpost-->")
    endInd = outerHtml.index("<!--HINTEND:blogpost-->")
    intText = outerHtml[startInd:endInd]
    startInd = intText.index("<article")
    endInd = intText.index("</article>")
    return blogIndent + intText[startInd:endInd] + "</article>\n"

def ExtractBlogTitle(outerHtml):
    startInd = outerHtml.index("<!--HINT:posttitle-->")
    endInd = outerHtml.index("<!--HINTEND:posttitle-->")
    intText = outerHtml[startInd:endInd]
    startInd = intText.index("<h1>")
    endInd = intText.index("</h1>")
    return intText[startInd+4:endInd]

def ExtractBlogDate(outerHtml):
    ind = outerHtml.index("<!--DATE:")
    return outerHtml[(ind+9):(ind+19)]

def ExtractBlogDateNum(outerHtml):
    ind = outerHtml.index("<!--DATE:")
    return ConvertISODateStringToInteger(outerHtml[(ind+9):(ind+19)])

def ExtractBlogDateStr(outerHtml):
    ind = outerHtml.index("<!--DATE:")
    return ConvertISODateStringToText(outerHtml[(ind+9):(ind+19)])

class BlogPost:
    def __init__(self, fPath):
        self.filePath = fPath
        htmlFull = open(fPath, encoding="utf8").read()
        self.innerHtml = ExtractBlogText(htmlFull)
        self.isodate = ExtractBlogDate(htmlFull)
        self.title = ExtractBlogTitle(self.innerHtml)
        self.dateNum = ConvertISODateStringToInteger(self.isodate)
        self.dateStr = ConvertISODateStringToText(self.isodate)
        self.prevPost = None
        self.nextPost = None
        self.filePathRel = fPath[5:]
    def __lt__(self, other):
        return self.dateNum < other.dateNum
    def GeneratePrevText(self):
        if(self.prevPost != None):
            return '">Previous post: ' + self.prevPost.title + "</a></li>\n"
        else:
            return '">No previous post</a></li>\n'
    def GenerateNextText(self):
        if(self.nextPost != None):
            return '">Next post: ' + self.nextPost.title + "</a></li>\n"
        else:
            return '">No next post</a></li>\n'
    def SortNavLinks(postList):
        postList.sort()
        for i in range(len(postList)):
            if(i > 0):
                postList[i].prevPost = postList[i-1]
            else:
                postList[i].prevPost = None
            if(i < len(postList)-1):
                postList[i].nextPost = postList[i+1]
            else:
                postList[i].nextPost = None
    def GenerateFixedBlogPostHtml(self):
        startIndTitle = standardBlogHtml.index("<title>")
        endIndTitle = standardBlogHtml.index("</title>")
        startIndNav = standardBlogHtml.index("<!--HINT:nav-->")
        endIndNav = standardBlogHtml.index("<!--HINTEND:nav-->")
        startIndPost = standardBlogHtml.index("<!--HINT:blogpost-->")
        endIndPost = standardBlogHtml.index("<!--HINTEND:blogpost-->")
        blogHtmlOpen = standardBlogHtml[0:startIndTitle] + "<title>"
        blogHtmlOmid = standardBlogHtml[endIndTitle:startIndNav] + "<!--HINT:nav-->\n"
        blogHtmlMid = blogIndent + standardBlogHtml[endIndNav:startIndPost] + "<!--DATE:" + self.isodate + "-->\n" + blogIndent + "<!--HINT:blogpost-->\n"
        blogHtmlClose = blogIndent + standardBlogHtml[endIndPost:-1] + standardBlogTopHtml[-1]
        blogTitleText = "Stuff by Max - Blog - " + self.title
        blogPrevNav = ""
        blogNextNav = ""
        if(self.prevPost != None):
            blogPrevNav = self.prevPost.filePathRel
        if(self.nextPost != None):
            blogNextNav = self.nextPost.filePathRel
        blogHtmlNav = navWrapperOpen + navPrevOpen + blogPrevNav + self.GeneratePrevText() + navNextOpen + blogNextNav + self.GenerateNextText() + navWrapperClose
        blogHtmlPost = dateHeadOpen + self.dateStr + paraClose + self.innerHtml
        return blogHtmlOpen + blogTitleText + blogHtmlOmid + blogHtmlNav + blogHtmlMid + blogHtmlPost + blogHtmlClose

def TruncateBlogStr(blogpost, paras = 4):
    ind = 0
    reps = 0
    while(reps < paras):
        try:
            ind = blogpost.index("<p>", ind) + 1
            reps += 1
        except ValueError:
            return blogpost
    endind = blogpost.index("</p>", ind)
    return blogpost[0:endind] + paraClose + blogIndent + "\t<p>...</p>\n" + blogIndent + "</article>\n"

def GenerateBlogList(blogPosts, postsInPage = 20, parasInPostPre = 4):
    startInd = standardBlogTopHtml.index("<!--HINT:bloglist-->")
    endInd = standardBlogTopHtml.index("<!--HINTEND:bloglist-->")
    blogTopHtmlOpen = standardBlogTopHtml[0:startInd] + "<!--HINT:bloglist-->\n"
    blogTopHtmlClose = blogIndent + standardBlogTopHtml[endInd:-1] + standardBlogTopHtml[-1]
    blogTopHtmlList = vertBreak
    blogPosts.sort(reverse=True)
    for b in blogPosts:
        blogTopHtmlList += TruncateBlogStr(b.innerHtml, parasInPostPre)
        blogTopHtmlList += dateNoteOpen + "Posted " + b.dateStr + paraClose
        blogTopHtmlList += expanderOpen + b.filePath + expanderClose
        blogTopHtmlList += vertBreak
    return blogTopHtmlOpen + blogTopHtmlList + blogTopHtmlClose

doExclude = True

def BuildBlog(isTest = False): #Call to build the entire blog
    doExclude = not isTest
    fileList = glob.glob("blog/*")
    if doExclude:
        for e in excludeList:
            if fileList.count(e) > 0:
                fileList.remove(e)
    blogPostList = []
    for f in fileList:
        blogPostList.append(BlogPost(f))
    BlogPost.SortNavLinks(blogPostList)
    blogListHtml = GenerateBlogList(blogPostList)
    open(blogMainPath, "w", encoding="utf8").write(blogListHtml)
    for b in blogPostList:
        open(b.filePath, "w", encoding="utf8").write(b.GenerateFixedBlogPostHtml())
        
def GenerateNewBlogFile(filename): #Call to generate a new blog post from the template
    open("blog/" + filename + ".html", "x", encoding="utf8").write(newBlogPostTemplate)