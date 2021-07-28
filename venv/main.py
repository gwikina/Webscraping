import requests
from bs4 import BeautifulSoup as bs

# gets url requests
github_user = input('Input Github User: ')
url = 'https://github.com/' + github_user
r = requests.get(url)

# parsed through github source code
soup = bs(r.content, 'html.parser')

# found and accessed my city, then stored it
try:
    location = soup.find('li', {'class': 'vcard-detail pt-1 css-truncate css-truncate-target hide-sm hide-md'})[
        'aria-label']
    city = location.split(':')[1]
except TypeError:
    city = ''

# found profile image and stored a link
try:
    profile_image = soup.find('img', {'alt': 'Avatar'})['src']
except TypeError:
    profile_image = ''

# found number of repositories and then stored it
repositories = soup.find('meta', {'name': 'description'})['content']
number_of_repositories = repositories.split(' ')[2]

# prints all the user's information
print('User: ' + github_user)
if city == '':
    pass
else:
    print('City:' + city)
if profile_image == '':
    pass
else:
    print('Profile Picture: ' + profile_image)
print('Repositories: ' + repositories + ' ' + url)
