import os
import pandas as pd
import numpy as np
import re
#path = 'texts_txt'
#count = 0
def read_txt_file(txt):
    reader = open(txt,'r')
    content = reader.read()
#remove '\n' may destroy the structure but for text classification in 
#this case, it does not matter
    content = re.sub('\n',' ',content)
    reader.close()
    return content

def read_dir(path):
    count = 0
    text_name = []
    recipe = []
    category = []
    for item in os.listdir(path):
        sub_dir = path + '/' + item
        for txt_file in os.listdir(sub_dir):
            count += 1
            category.append(sub_dir.split('/')[-1])
            text_name.append(txt_file.split('.')[0])
            full_file = sub_dir + '/' + txt_file    
            recipe.append(read_txt_file(full_file))
    cols = {'text_name': text_name,'recipe':recipe, 'category':category}
    upmc_food_101_df = pd.DataFrame(data = cols)
    #print upmc_food_101_df.head()
    upmc_food_101_df.to_csv('../../common/texts/texts_train.csv',header=True)
    return count, upmc_food_101_df
pt = "../../common/texts/train"
count, df = read_dir(pt)
#print(Recipe)
print("there are total %d samples in text form \n",count) 
print('finished reading\n')
#print(Category)
# print ('\n'.join(read_txt_file(full_file).split('\n')))

#print(count)
