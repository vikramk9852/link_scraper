from bs4 import BeautifulSoup
import urllib.request
 
 
def visit(site):
	try:
		page = urllib.request.urlopen(site)
		soup = BeautifulSoup(page, "lxml")
		return soup
	except:	
		print(site)
 
site = "https://www.codechef.com"
temp = site.split(':')
depth = 2
sites = set()
visited = set()
sites.add(site)


for i in range(depth):
	next = set()
	for links in sites:
		soup = visit(links)
		if soup is not None:
			for link in soup.find_all('a', href = True):
				found = link['href']
				if temp[1] in found or found.startswith('/'):
					if found.startswith('/'):
						if len(found) > 1 and found[1] == '/':
							found = 'https:'+found
						else:
							found = site+found
					if temp[0] not in found:
						http = found.split(':')
						found = 'https:'+http[1]
					if found not in visited:
						print(found)
						visited.add(found)
						next.add(found)	
	sites = next
