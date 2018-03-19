

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import bs4
import requests
import pandas as pd

#question1
driver = webdriver.Firefox(executable_path=r'C:\Users\yuxia\Documents\geckodriver.exe')
driver.get('http://www.mlb.com')

wait = WebDriverWait(driver, 10)
stats = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#_pagebuilder_index > div.megamenu > div > div.megamenu-navbar > div > nav.megamenu-navbar-overflow > ul > li.megamenu-navbar-overflow__menu-item.megamenu-navbar-overflow__menu-item--stats > a')))
stats.click()
stats.click()

year=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#sp_hitting_season')))
menu = driver.find_element_by_css_selector('#sp_hitting_season')
ActionChains(driver).move_to_element(menu).click(menu).perform()
year2015=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#sp_hitting_season > option:nth-child(4)')))
year2015.click()

headline=driver.find_element_by_css_selector('#headline')
headline.click()

team_selection=driver.find_element_by_css_selector('#st_parent')
team_selection.click()

season_selection=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#st_hitting_game_type > option:nth-child(1)')))
season_selection.click()

headline=driver.find_element_by_css_selector('#headline')
headline.click()

data_div=driver.find_element_by_id('datagrid')
data_html=data_div.get_attribute('innerHTML')
soup=bs4.BeautifulSoup(data_html,'html5lib')

data_head=[x.text.replace('▼','') for x in soup.thead.find_all('th')]

df=pd.DataFrame(columns=data_head)

data_body=[]
for a in soup.tbody.find_all('td'):
    data_body.append(a.text)

fix_data_body=[]
for b in range(int(len(data_body)/len(data_head))):
    c=data_body[b*len(data_head):(b+1)*len(data_head)]
    fix_data_body.append(c)

for i in range(30):
    df.loc[i]=fix_data_body[i]

a_df=df[["Team","HR"]]
result_df=a_df.sort_values(by='HR',ascending = False)
print(result_df)
result_df.to_csv('question1')
print(result_df.at[1,'Team'])
print('had the most homeruns in the regular season of 2015')


# In[2]:


#question1 end


# In[3]:


#question2_a start
AL_df=df[df['League']=='AL']


# In[4]:


AL_df.to_csv('q2AL.csv')


# In[5]:


df2_1A=pd.read_csv('q2AL.csv')


# In[6]:


AL_avg=df2_1A['HR'].mean()


# In[7]:


NL_df=df[df['League']=='NL']


# In[8]:


NL_df.to_csv('q2NL.csv')


# In[9]:


df2_1N=pd.read_csv('q2NL.csv')


# In[10]:


NL_avg=df2_1N['HR'].mean()


# In[11]:


more_AVG=max(AL_avg,NL_avg)


# In[12]:


if AL_avg>NL_avg:
    print('In the regular season of 2015, AL had the most homeruns, which is: ')
    print(more_AVG)
else:
    print('In the regular season of 2015, NL had the most homeruns, which is: ')
    print(more_AVG)
#question2_a end        


# In[13]:


#question2_b start
inner_selection=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#st_hitting_hitting_splits > optgroup:nth-child(13) > option:nth-child(1)')))
inner_selection.click()


# In[14]:


data_div=driver.find_element_by_id('datagrid')
data_html=data_div.get_attribute('innerHTML')
soup=bs4.BeautifulSoup(data_html,'html5lib')

data_head=[x.text.replace('▼','') for x in soup.thead.find_all('th')]

df2_b=pd.DataFrame(columns=data_head)

data_body=[]
for a in soup.tbody.find_all('td'):
    data_body.append(a.text)

fix_data_body=[]
for b in range(int(len(data_body)/len(data_head))):
    c=data_body[b*len(data_head):(b+1)*len(data_head)]
    fix_data_body.append(c)

for i in range(30):
    df2_b.loc[i]=fix_data_body[i]


# In[15]:


AL_df2_b=df2_b[df2_b['League']=='AL']
AL_df2_b.to_csv('q2_bAL.csv')
df2_bA=pd.read_csv('q2_bAL.csv')
in1AL_avg=df2_bA['HR'].mean()
NL_df2_b=df2_b[df2_b['League']=='NL']
NL_df2_b.to_csv('q2_bNL.csv')
df2_bN=pd.read_csv('q2_bNL.csv')
in1NL_avg=df2_bN['HR'].mean()
in1more_AVG=max(in1AL_avg,in1NL_avg)
if in1AL_avg>in1NL_avg:
    print('In the regular season of 2015 in the first inning, AL had the most homeruns, which is: ')
    print(in1more_AVG)
else:
    print('In the regular season of 2015 in the first inning, NL had the most homeruns, which is: ')
    print(in1more_AVG)
#question2_b end


# In[22]:


#question3_a start
year2017=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#st_hitting_season > option:nth-child(2)')))
year2017.click()


# In[23]:


Player_selection=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#sp_parent')))
Player_selection.click()


# In[24]:


NYY_select=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#sp_hitting_team_id > option:nth-child(20)')))
NYY_select.click()


# In[25]:


default_split=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#sp_hitting_hitting_splits > option:nth-child(1)')))
default_split.click()


# In[26]:


data_div=driver.find_element_by_id('datagrid')
data_html=data_div.get_attribute('innerHTML')
soup=bs4.BeautifulSoup(data_html,'html5lib')

data_head=[x.text.replace('▼','') for x in soup.thead.find_all('th')]

df3_a=pd.DataFrame(columns=data_head)

data_body=[]
for a in soup.tbody.find_all('td'):
    data_body.append(a.text)

fix_data_body=[]
for b in range(int(len(data_body)/len(data_head))):
    c=data_body[b*len(data_head):(b+1)*len(data_head)]
    fix_data_body.append(c)

for i in range(33):
    df3_a.loc[i]=fix_data_body[i]


# In[27]:


df3_a.to_csv('q3a.csv')


# In[28]:


df3_a=pd.read_csv('q3a.csv')


# In[29]:


df3_a_re=df3_a[df3_a['AB']>=30]


# In[30]:


df3_a_re


# In[31]:


df3_a1=df3_a_re[['Player','Pos','AVG',]]


# In[32]:


df3_a2=df3_a1.sort_values(by='AVG',ascending = False)


# In[115]:


print(df3_a2)
print('The player with the best overall batting average in the 2017 regular season that played for the New York Yankees, who had at least 30 at bats is Garrett Cooper, and his position is 1B')
#question3a end


# In[44]:


df3_brf=df3_a[df3_a['Pos']=='RF']


# In[37]:


df3_bcf=df3_a[df3_a['Pos']=='CF']


# In[36]:


df3_blf=df3_a[df3_a['Pos']=='LF']


# In[61]:


import numpy


# In[62]:


print(df3_brf[['Player','Pos','AVG']])


# In[63]:


print(df3_bcf[['Player','Pos','AVG']])


# In[64]:


print(df3_blf[['Player','Pos','AVG']])


# In[70]:





# In[51]:


print('The player with the best overall batting average in the 2017 regular season that played for the who played in the outfield is Aaron James Judge, and his position is RF.')


# In[52]:


#question3_b end


# In[54]:


year2015=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#sp_hitting_season > option:nth-child(4)')))
year2015.click()


# In[55]:


All_team=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#sp_hitting_team_id > option:nth-child(1)')))
All_team.click()


# In[56]:


AL_Button=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#sp_hitting-1 > fieldset:nth-child(1) > label:nth-child(4) > span:nth-child(1)')))
AL_Button.click()


# In[71]:


Qualifiers=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#sp_hitting-0 > fieldset:nth-child(5) > label:nth-child(4) > span:nth-child(1)')))
Qualifiers.click()


# In[74]:


data_div=driver.find_element_by_id('datagrid')
data_html=data_div.get_attribute('innerHTML')
soup=bs4.BeautifulSoup(data_html,'html5lib')

data_head=[x.text.replace('▼','') for x in soup.thead.find_all('th')]

df4_1=pd.DataFrame(columns=data_head)

data_body=[]
for a in soup.tbody.find_all('td'):
    data_body.append(a.text)

fix_data_body=[]
for b in range(int(len(data_body)/len(data_head))):
    c=data_body[b*len(data_head):(b+1)*len(data_head)]
    fix_data_body.append(c)

for i in range(50):
    df4_1.loc[i]=fix_data_body[i]


# In[76]:


df4_1


# In[77]:


Page2=driver.find_element_by_class_name('paginationWidget-next')
Page2.click()


# In[78]:


data_div=driver.find_element_by_id('datagrid')
data_html=data_div.get_attribute('innerHTML')
soup=bs4.BeautifulSoup(data_html,'html5lib')

data_head=[x.text.replace('▼','') for x in soup.thead.find_all('th')]

data_body=[]
for a in soup.tbody.find_all('td'):
    data_body.append(a.text)

fix_data_body=[]
for b in range(int(len(data_body)/len(data_head))):
    c=data_body[b*len(data_head):(b+1)*len(data_head)]
    fix_data_body.append(c)

for i in range(19):
    df4_1.loc[i+50]=fix_data_body[i]


# In[80]:


df4_1.to_csv('question4')


# In[82]:


df4=pd.read_csv('question4')


# In[110]:


print('The player in the American League had the most at bats in the 2015 regular season is:')


# In[111]:


print(df4.at[df4['AB'].idxmax(),'Player'])


# In[112]:


print('His team is:')


# In[113]:


print(df4.at[df4['AB'].idxmax(),'Team'])
#question4 end


# In[116]:


#qustion5 start
year2014=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#sp_hitting_season > option:nth-child(5)')))
year2014.click()


# In[117]:


All_star=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#sp_hitting_game_type > option:nth-child(2)')))
All_star.click()


# In[128]:


MLB=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'html.device-desktop.js.flexbox.no-touch.csscolumns body.mlb div#bodyWrap div#metaWrap div#contentWrap div#content_wrapper div#content div#widgets.onscreen div.panels div#sp_hitting.onscreen div#sp_hitting-1.grouping.onscreen fieldset.widget-radio.ui-buttonset label.ui-button.ui-widget.ui-state-default.ui-button-text-only.ui-corner-left span.ui-button-text')))
MLB.click()


# In[129]:




data_div=driver.find_element_by_id('datagrid')
data_html=data_div.get_attribute('innerHTML')
soup=bs4.BeautifulSoup(data_html,'html5lib')

data_head=[x.text.replace('▼','') for x in soup.thead.find_all('th')]

df5=pd.DataFrame(columns=data_head)

data_body=[]
for a in soup.tbody.find_all('td'):
    data_body.append(a.text)

fix_data_body=[]
for b in range(int(len(data_body)/len(data_head))):
    c=data_body[b*len(data_head):(b+1)*len(data_head)]
    fix_data_body.append(c)

for i in range(41):
    df5.loc[i]=fix_data_body[i]


# In[130]:


df5


# In[173]:


re=[]


# In[175]:


for i in range(41):
    Player=df5.at[i,'Player']
    PL=driver.find_element_by_link_text(str(Player).lstrip)
    PL.click()
    info=wait.until(EC.presence_of_element_located((By.CLASS_NAME,'player-bio')))
    info=driver.find_elements_by_class_name('player-bio')
    x=[li.text.replace('\n', ',') for li in info]
    driver.back()
    re=re.append(x)
    


# In[171]:




