# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


#set your executable path--SPLINTER 
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Assign the url and instruct the browser to visit it.
# Visit the Mars news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Set up the HTML parser & Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

#Earlier, we identified the parent element and created a variable to hold it. 
#With this new code, we’re searching within that element for the title. We’re 
#also stripping the additional HTML attributes and tags with the use of 
#.get_text().


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Images

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# #### MARS FACTS

# Create DataFrame using Panda to scrape/rip table from site for our own use
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# Use the below "function" to have the Html of the DF table we created above
# to use whe we produce table into our own website
df.to_html()

# ALWAYS REMEMBER TO EXIT THE AUTOMATED BROWSER
browser.quit()

# ### D1: Scrape High-Resolution Mars' Hemisphere Images and Titles

### Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

for x in range (4):
    hemispheres = {}
    
    #Parse the resulting html with soup
    html = browser.html
    hem_soup = soup(html, 'html.parser')
    
    # Find & Click Hemisphere Link
    hem_link = browser.find_by_tag('h3')[x]
    hem_link.click()    
     
    # Parse the resulting html with soup (initially had this before the find & click but was experiencing and No object error so added 2 instances)
    html = browser.html
    hem_soup = soup(html, 'html.parser')
    
    browser.is_element_present_by_css('div.list_text', wait_time=1)
    
    
    # Retrieve the title
    hem_title = hem_soup.find('h2').get_text() 
        
    # Find the relative image url
        
    hemi_img_url_rel = hem_soup.find('img', class_='wide-image').get('src') 
    
    # Use the base url to create an absolute url
    img_url = f'https://marshemispheres.com/{hemi_img_url_rel}'
    
    #storing results in the dictionary
    hemispheres = {
        'FullRes_image_url': img_url,
        'Title': hem_title
        
    }
    
    #appending to dict
    hemisphere_image_urls.append(hemispheres)
    
    browser.back()

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()
