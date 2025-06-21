#!/usr/bin/env python
# coding: utf-8

# # Project Goal: To analyze and visualize the performance of attacking players in a top European league for a recent season.

# In[3]:


import pandas as pd
import time
import os
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df = pd.read_excel("C:/Users/LENOVO/Downloads/attacking_players_filtered.xlsx")


# In[6]:


df


# In[8]:


print("Top teams by Goals (Gls):")
display(df.sort_values(by='Gls', ascending=False).head())


# In[9]:


print("\nTop teams by Shots on Target (SoT):")
display(df.sort_values(by='SoT', ascending=False).head())


# In[10]:


print("\nTop teams by Expected Goals (xG):")
display(df.sort_values(by='xG', ascending=False).head())


# In[11]:


print("Top teams by Goals per Shot (G/Sh):")
display(df.sort_values(by='G/Sh', ascending=False).head())


# In[12]:


print("\nTop teams by Goals per Shot on Target (G/SoT):")
display(df.sort_values(by='G/SoT', ascending=False).head())


# In[13]:


print("Teams overperforming Expected Goals (G-xG):")
display(df.sort_values(by='G-xG', ascending=False).head())


# In[14]:


print("\nTeams underperforming Expected Goals (G-xG):")
display(df.sort_values(by='G-xG', ascending=True).head())


# In[15]:


print("\nTeams overperforming Non-Penalty Expected Goals (np:G-xG):")
display(df.sort_values(by='np:G-xG', ascending=False).head())


# In[16]:


print("\nTeams underperforming Non-Penalty Expected Goals (np:G-xG):")
display(df.sort_values(by='np:G-xG', ascending=True).head())


# In[18]:


plt.figure(figsize=(12, 6))
sns.barplot(x='Squad', y='Gls', data=df)
plt.title('Total Goals Scored by Attacking Teams')
plt.xlabel('Team')
plt.ylabel('Goals Scored')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
""


# In[20]:


plt.figure(figsize=(10, 6))
plt.scatter(x='Sh', y='Gls', data=df)
plt.title('Relationship between Shots and Goals Scored')
plt.xlabel('Total Shots')
plt.ylabel('Total Goals Scored')
plt.grid(True)
plt.show()


# In[21]:


df_melted = df.melt(id_vars='Squad', value_vars=['Gls', 'xG'], var_name='Metric', value_name='Value')

plt.figure(figsize=(14, 7))
sns.barplot(x='Squad', y='Value', hue='Metric', data=df_melted, palette='viridis')
plt.title('Actual Goals vs. Expected Goals (xG) by Team')
plt.xlabel('Team')
plt.ylabel('Total Value')
plt.xticks(rotation=90)
plt.legend(title='Metric')
plt.tight_layout()
plt.show()


# In[24]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='G/Sh', y='Gls', data=df, hue='Squad', s=100)
plt.title('Goals per Shot vs. Total Goals')
plt.xlabel('Goals per Shot (G/Sh)')
plt.ylabel('Total Goals Scored')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='G/SoT', y='Gls', data=df, hue='Squad', s=100)
plt.title('Goals per Shot on Target vs. Total Goals')
plt.xlabel('Goals per Shot on Target (G/SoT)')
plt.ylabel('Total Goals Scored')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.grid(True)
plt.show()


# In[ ]:




