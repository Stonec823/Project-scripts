{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5c3cc901",
   "metadata": {},
   "outputs": [],
   "source": [
    "## importing libraries ##\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "from os import path\n",
    "\n",
    "DATA_DIR = '/Users/cstone/Downloads'\n",
    "\n",
    "df = pd.read_csv(path.join(DATA_DIR, 'AgeDataset-V1.csv'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "63caa9ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Id', 'Name', 'Short description', 'Gender', 'Country', 'Occupation',\n",
      "       'Birth year', 'Death year', 'Manner of death', 'Age of death'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(df.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "33ba649d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                Id                                  Name  \\\n",
      "471187    Q5496068                           Fred Peters   \n",
      "221572    Q1883763                     Cornelius Nozeman   \n",
      "1048161  Q29344828  Arthur Heinrich Sprecher von Bernegg   \n",
      "530366    Q6131303                         James Chilton   \n",
      "613255    Q7411270                          Samuel Dixon   \n",
      "\n",
      "                                         Short description Gender  \\\n",
      "471187                                         illustrator   Male   \n",
      "221572                               Remonstrant ministers   Male   \n",
      "1048161                                        (1852-1912)   Male   \n",
      "530366   Mayflower passenger and New World colonist (15...   Male   \n",
      "613255                                American businessman   Male   \n",
      "\n",
      "                              Country                Occupation  Birth year  \\\n",
      "471187       United States of America       Animator; penciller        1923   \n",
      "221572                    Netherlands  Ornithologist; predikant        1720   \n",
      "1048161  Switzerland; Austria-Hungary                       NaN        1852   \n",
      "530366                            NaN                       NaN        1556   \n",
      "613255       United States of America                Politician        1856   \n",
      "\n",
      "         Death year Manner of death  Age of death  \n",
      "471187       2018.0             NaN          95.0  \n",
      "221572       1786.0             NaN          66.0  \n",
      "1048161      1912.0             NaN          60.0  \n",
      "530366       1620.0             NaN          64.0  \n",
      "613255       1934.0             NaN          78.0  \n"
     ]
    }
   ],
   "source": [
    "print(df.sample(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4ba7b802",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Id - 0%\n",
      "Name - 0%\n",
      "Short description - 6%\n",
      "Gender - 11%\n",
      "Country - 27%\n",
      "Occupation - 17%\n",
      "Birth year - 0%\n",
      "Death year - 0%\n",
      "Manner of death - 96%\n",
      "Age of death - 0%\n"
     ]
    }
   ],
   "source": [
    "\n",
    "for col in df.columns:\n",
    "    pct_missing = np.mean(df[col].isnull())\n",
    "    print('{} - {}%'.format(col, round(pct_missing*100)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "22224330",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Gender\n",
      "Eunuch                                            51.333333\n",
      "Eunuch; Male                                      63.611111\n",
      "Female                                            71.307846\n",
      "Female; Female                                    75.000000\n",
      "Female; Male                                      71.428571\n",
      "Intersex                                          59.000000\n",
      "Intersex; Female                                  64.000000\n",
      "Intersex; Male                                    55.500000\n",
      "Intersex; Transgender Male                        79.000000\n",
      "Male                                              69.185657\n",
      "Non-Binary                                        61.000000\n",
      "Non-Binary; Intersex                              22.000000\n",
      "Transgender Female                                49.810127\n",
      "Transgender Female; Female                        65.000000\n",
      "Transgender Female; Intersex                      61.000000\n",
      "Transgender Female; Male                          37.000000\n",
      "Transgender Male                                  57.111111\n",
      "Transgender Male; Female                          62.000000\n",
      "Transgender Male; Male                            67.000000\n",
      "Transgender Person; Intersex; Transgender Male    71.000000\n",
      "Name: Age of death, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "df1 = df.groupby('Gender')['Age of death'].mean()\n",
    "print(df1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "574ec716",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function matplotlib.pyplot.show(close=None, block=None)>"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    " ## females seem to live longer than males, let's see their age distribution ##\n",
    "\n",
    "df.loc[df['Gender'] == 'Female'].hist(column=['Age of death'], bins = 20)\n",
    "plt.xlabel('Age of Death')\n",
    "plt.ylabel('# of Females')\n",
    "plt.show"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "4b922ce9",
   "metadata": {},
   "outputs": [],
   "source": [
    "df2 = (df.groupby('Death year')['Age of death'].mean().reset_index())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "f204209b",
   "metadata": {},
   "outputs": [],
   "source": [
    "## Look at average age od death for the last 250 years \n",
    "\n",
    "df250 = (df2.tail(250))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "aecbf323",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Death year\n",
      "1772.0    61.210169\n",
      "1773.0    61.806159\n",
      "1774.0    61.861404\n",
      "1775.0    63.267692\n",
      "1776.0    62.331190\n",
      "            ...    \n",
      "2017.0    79.089162\n",
      "2018.0    79.060775\n",
      "2019.0    79.450289\n",
      "2020.0    80.231658\n",
      "2021.0    79.904859\n",
      "Name: Age of death, Length: 250, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "print(df250)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "1a20a62c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.frame.DataFrame"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(df250)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "114469e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot('Death year', 'Age of death', data=df250)\n",
    "plt.xlabel('Year')\n",
    "plt.ylabel('Age of Death')\n",
    "plt.title('Average Lifespan')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "ed349d71",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Occupation\n",
      "Artist                281512\n",
      "Politician            195390\n",
      "Athlete               110943\n",
      "Researcher             90709\n",
      "Military personnel     52911\n",
      "Religious figure       37086\n",
      "Businessperson         19529\n",
      "Architect              17865\n",
      "Journalist             16002\n",
      "Teacher                15693\n",
      "Name: Occupation, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "## Top 10 Occupations\n",
    "\n",
    "df3 = df.groupby('Occupation')['Occupation'].count().sort_values(ascending=False).head(10)\n",
    "print(df3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1183daf6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
