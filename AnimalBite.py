# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 12:43:33 2020

@author: Taha
"""
 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset=pd.read_csv('data.csv')


dataset.isnull().sum()

dataset.bite_date[(dataset.bite_date>('2018-01-01'))]
to_replace={"5013-07-15 00:00:00":"2013-07-15 00:00:00","2020-08-08 00:00:00":"2002-08-08 00:00:00"}
dataset.bite_date.replace(to_replace,inplace=True)

species=dataset.SpeciesIDDesc
species.isnull().sum()
species=species.dropna()
speciesofAnimals=species.unique()

#Animal Bites per month according to each species
k=[]
for i in speciesofAnimals:
    k.append(len(species[species==i]))
    
import seaborn as sns    
ax=sns.barplot(x=speciesofAnimals,y=k)

month_list= ['01','02','03','04','05','06','07','08','09','10','11','12']
numberOfAnimal=[]
for i in month_list:
    x = dataset.loc[(dataset['SpeciesIDDesc']=='BAT')&(dataset['bite_date'].str.split('-').str[1]==i)]
    numberOfAnimal.append(len(x))
ax = sns.barplot(x=month_list,y=numberOfAnimal,palette  = "Blues")

count=dataset.BreedIDDesc.value_counts()
ax=sns.barplot(x=count[0:10].index,y=count[0:10])
bitePlaces=dataset.WhereBittenIDDesc.unique()
dataset.WhereBittenIDDesc.value_counts()
head=dataset.loc[(dataset.SpeciesIDDesc=='DOG')&(dataset.WhereBittenIDDesc=='HEAD')]
body=dataset.loc[(dataset.SpeciesIDDesc=='DOG')&(dataset.WhereBittenIDDesc=='BODY')]
#head=dataset.loc[(dataset.SpeciesIDDesc=='CAT')&(dataset.WhereBittenIDDesc=='HEAD')]
#head=dataset.loc[(dataset.SpeciesIDDesc=='CAT')&(dataset.WhereBittenIDDesc=='BODY')]

#Probabilities of getting bitten on head and body
ax=sns.barplot()
for i in count.index:
    s=np.sum(head.shape[0]+body.shape[0])
    head.shape[0]/s
    body.shape[0]/s
    
    


#Testing Rabidity
def rabid_prob(animal,data):
    labels = ['POSITIVE','NEGATIVE']
    colors = ['red','green']
    explode = [0.1,0]
    p = data.loc[(data['SpeciesIDDesc']==animal)&(data['ResultsIDDesc']=='POSITIVE')]
    n = data.loc[(data['SpeciesIDDesc']==animal)&(data['ResultsIDDesc']=='NEGATIVE')]
    sizes = [len(p),len(n)]
    print(sizes)
    if len(p)==0:
        labels = ['','NEGATIVE']
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct ='%1.1f&&')
    plt.axis('equal')
    plt.title(animal + ' Rabid Probability')
    plt.show()
    
    rabid_prob('DOG',dataset)


    
    
    
