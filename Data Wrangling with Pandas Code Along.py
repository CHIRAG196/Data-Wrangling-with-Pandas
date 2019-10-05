#!/usr/bin/env python
# coding: utf-8

# # IPL Dataset Analysis
# 
# ## Problem Statement
# We want to know as to what happens during an IPL match which raises several questions in our mind with our limited knowledge about the game called cricket on which it is based. This analysis is done to know as which factors led one of the team to win and how does it matter.

# ## About the Dataset :
# The Indian Premier League (IPL) is a professional T20 cricket league in India contested during April-May of every year by teams representing Indian cities. It is the most-attended cricket league in the world and ranks sixth among all the sports leagues. It has teams with players from around the world and is very competitive and entertaining with a lot of close matches between teams.
# 
# The IPL and other cricket related datasets are available at [cricsheet.org](https://cricsheet.org/%c2%a0(data). Feel free to visit the website and explore the data by yourself as exploring new sources of data is one of the interesting activities a data scientist gets to do.
# 
# Snapshot of the data you will be working on:<br>
# <br>
# The dataset 136522 data points and 23 features<br>
# 
# |Features|Description|
# |-----|-----|
# |match_code|Code pertaining to individual match|
# |date|Date of the match played|
# |city|City where the match was played|
# |venue|Stadium in that city where the match was played|
# |team1|team1|
# |team2|team2|
# |toss_winner|Who won the toss out of two teams|
# |toss_decision|toss decision taken by toss winner|
# |winner|Winner of that match between two teams|
# |win_type|How did the team won(by wickets or runs etc.)|
# |win_margin|difference with which the team won| 
# |inning|inning type(1st or 2nd)|
# |delivery|ball delivery|
# |batting_team|current team on batting|
# |batsman|current batsman on strike|
# |non_striker|batsman on non-strike|
# |bowler|Current bowler|
# |runs|runs scored|
# |extras|extra run scored|
# |total|total run scored on that delivery including runs and extras|
# |extras_type|extra run scored by wides or no ball or legby|
# |player_out|player that got out|
# |wicket_kind|How did the player got out|
# |wicket_fielders|Fielder who caught out the player by catch|
# 

# ### Analyzing data using pandas module

# ### Read the data using pandas module.

# In[1]:


import pandas as pd
import numpy as np
df_ipl = pd.read_csv('ipl_dataset.csv')
df_ipl.shape


# In[2]:


len(df_ipl['match_code'].unique())

# You can also use: 
#df_ipl['match_code'].nunique()


# ### There are certain fixed cities all around the world where matches are held. Find the list of unique cities where matches were played 

# In[5]:


# Corrected as Venues to Cities
fixed_venues = df_ipl['venue'].unique()
fixed_venues    


# ### Find the columns which contains null values if any ?

# In[8]:


null = df_ipl.columns[df_ipl.isnull().any()]
#null = null.isnull().sum()
null


# ### Though the match is held in different cities all around the world it may or maynot have multiple venues (stadiums where matches are held) list down top 5 most played venues 
# 

# In[19]:


#most = df_ipl.venue.value_counts().max()
#most = df_ipl.mode()
most = df_ipl['venue'].value_counts().head(5)#[df_ipl['venue'].value_counts() == df_ipl['venue'].value_counts().max()]
most


# In[ ]:





# ### Make a runs vs run-count frequency table

# In[4]:


run_counts = df_ipl['runs'].value_counts()
run_counts


# In[ ]:





# ### IPL seasons are held every year now let's look at our data and extract how many seasons were recorded.

# In[7]:


df_ipl['year'] = df_ipl['date'].apply(lambda x : x[:4])
print('Total number of seasons played:',len(df_ipl['year'].unique()))
print('IPL played in the following years:',df_ipl['year'].unique())


# ### What are the total no. of matches played per season

# In[22]:


matches_played_per_season = df_ipl.groupby('year')['match_code'].nunique()
print(matches_played_per_season)


# ### What are the total runs scored across each season 

# In[8]:


runs_scored = df_ipl.groupby('year')['total'].sum()
print(runs_scored)


# In[ ]:





# ### There are teams which are high performing and low performing. Let's look at the aspect of performance of an individual team. Filter the data and aggregate the runs scored by each team. Display top 10 results which are having runs scored over 200.

# In[43]:


high_scores = df_ipl.groupby(['match_code','inning','team1','team2','batting_team','winner'])['total'].sum().reset_index()
high_scores = high_scores[high_scores['total']>=200]
high_scores.nlargest(10,'total')


# In[55]:





# In[ ]:





# ### Chasing a 200+ target is difficulty in T-20 format. What are the chances that a team scoring runs above 200  in their 1st inning is chased by the opposition in 2nd inning.

# In[52]:


high_score1 = high_scores[high_scores['inning']==1]
high_score2 = high_scores[high_scores['inning']==2]
high_score1 = high_score1.merge(high_score2[['match_code','inning','total']], on='match_code')
high_score1.rename(columns={'inning_x':'inning_1','inning_y':'inning_2','total_x':'inning1_runs','total_y':'inning2_runs'}, inplace=True)
high_score1 = high_score1[high_score1['inning1_runs']>=200]
high_score1['is_score_chased'] = np.where(high_score1['inning1_runs']<=high_score1['inning2_runs'],'yes','no')
chances = high_score1['is_score_chased'].value_counts()
print(chances)


# In[69]:





# In[ ]:





# In[ ]:





# ### Every season has that one team which is outperforming others and is in great form. Which team has the highest win counts in their respective seasons ?

# In[15]:


best_team = df_ipl.groupby(['team1','team2','year','winner'])['total'].sum().reset_index()
best_team_final = best_team.groupby(['year','winner'])['total'].sum().reset_index()
best_team_final


# In[ ]:





# In[ ]:




