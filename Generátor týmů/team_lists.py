import pandas as pd


#Anglie
database = pd.read_excel("tymy.xlsx", sheet_name="england")
england_list_5_star = database["5 star"].dropna().tolist()
england_list_4half_star = database["4.5 star"].dropna().tolist()
england_list_4_star = database["4 star"].dropna().tolist()
england_list_3half_star = database["3.5 star"].dropna().tolist()
england_list_3_star = database["3 star"].dropna().tolist()
#3-5
england_list_3_to_3half_star = england_list_3_star + england_list_3half_star
england_list_3_to_4_star = england_list_3_to_3half_star + england_list_4_star
england_list_3_to_4half_star = england_list_3_to_4_star + england_list_4half_star
england_list_3_to_5_star = england_list_3_to_4half_star + england_list_5_star
#3,5 - 5
england_list_3half_to_4_star = england_list_3half_star + england_list_4_star
england_list_3half_to_4half_star = england_list_3half_to_4_star + england_list_4half_star
england_list_3half_to_5_star = england_list_3half_to_4half_star + england_list_5_star
#4-5
england_list_4_to_4half_star = england_list_4_star + england_list_4half_star
england_list_4_to_5_star = england_list_4_to_4half_star + england_list_5_star
#4,5-5
england_list_4half_to_5_star = england_list_4half_star + england_list_5_star



#Německo
database = pd.read_excel("tymy.xlsx", sheet_name="germany")
germany_list_5_star = database["5 star"].dropna().tolist()
germany_list_4half_star = database["4.5 star"].dropna().tolist()
germany_list_4_star = database["4 star"].dropna().tolist()
germany_list_3half_star = database["3.5 star"].dropna().tolist()
germany_list_3_star = database["3 star"].dropna().tolist()

#3-5
germany_3_to_3half_star = germany_list_3_star + germany_list_3half_star
germany_3_to_4_star = germany_3_to_3half_star + germany_list_4_star
germany_3_to_4half_star = germany_3_to_4_star + germany_list_4half_star
germany_3_to_5_star = germany_3_to_4half_star + germany_list_5_star
#3,5-5
germany_3half_to_4_star = germany_list_3half_star + germany_list_4_star
germany_3half_to_4half_star = germany_3half_to_4_star + germany_list_4_star
germany_3half_to_5_star = germany_3half_to_4half_star + germany_list_4_star
#4-5
germany_4_to_4half_star = germany_list_4_star + germany_list_4half_star
germany_4_to_5_star = germany_4_to_4half_star + germany_list_4half_star
#4,5-5
germany_4half_to_5_star = germany_list_4half_star + germany_list_5_star


#Španělsko
database = pd.read_excel("tymy.xlsx", sheet_name="italy")
italy_list_5_star = database["5 star"].dropna().tolist()
italy_list_4half_star = database["4.5 star"].dropna().tolist()
italy_list_4_star = database["4 star"].dropna().tolist()
italy_list_3half_star = database["3.5 star"].dropna().tolist()
italy_list_3_star = database["3 star"].dropna().tolist()

#3-5
italy_3_to_3half_star = italy_list_3_star + italy_list_3half_star
italy_3_to_4_star = italy_3_to_3half_star + italy_list_4_star
italy_3_to_4half_star = italy_3_to_4_star + italy_list_4half_star
italy_3_to_5_star = italy_3_to_4half_star + italy_list_5_star
#3,5-5
italy_3half_to_4_star = italy_list_3half_star + italy_list_4_star
italy_3half_to_4half_star = italy_3half_to_4_star + italy_list_4_star
italy_3half_to_5_star = italy_3half_to_4half_star + italy_list_4_star
#4-5
italy_4_to_4half_star = italy_list_4_star + italy_list_4half_star
italy_4_to_5_star = italy_4_to_4half_star + italy_list_4half_star
#4,5-5
italy_4half_to_5_star = italy_list_4half_star + italy_list_5_star


#Francie
database = pd.read_excel("tymy.xlsx", sheet_name="france")
france_list_5_star = database["5 star"].dropna().tolist()
france_list_4half_star = database["4.5 star"].dropna().tolist()
france_list_4_star = database["4 star"].dropna().tolist()
france_list_3half_star = database["3.5 star"].dropna().tolist()
france_list_3_star = database["3 star"].dropna().tolist()

#3-5
france_3_to_3half_star = france_list_3_star + france_list_3half_star
france_3_to_4_star = france_3_to_3half_star + france_list_4_star
france_3_to_4half_star = france_3_to_4_star + france_list_4half_star
france_3_to_5_star = france_3_to_4half_star + france_list_5_star
#3,5-5
france_3half_to_4_star = france_list_3half_star + france_list_4_star
france_3half_to_4half_star = france_3half_to_4_star + france_list_4_star
france_3half_to_5_star = france_3half_to_4half_star + france_list_4_star
#4-5
france_4_to_4half_star = france_list_4_star + france_list_4half_star
france_4_to_5_star = france_4_to_4half_star + france_list_4half_star
#4,5-5
france_4half_to_5_star = france_list_4half_star + france_list_5_star

#Španělsko
database = pd.read_excel("tymy.xlsx", sheet_name="spain")
spain_list_5_star = database["5 star"].dropna().tolist()
spain_list_4half_star = database["4.5 star"].dropna().tolist()
spain_list_4_star = database["4 star"].dropna().tolist()
spain_list_3half_star = database["3.5 star"].dropna().tolist()
spain_list_3_star = database["3 star"].dropna().tolist()

#3-5
spain_3_to_3half_star = spain_list_3_star + spain_list_3half_star
spain_3_to_4_star = spain_3_to_3half_star + spain_list_4_star
spain_3_to_4half_star = spain_3_to_4_star + spain_list_4half_star
spain_3_to_5_star = spain_3_to_4half_star + spain_list_5_star
#3,5-5
spain_3half_to_4_star = spain_list_3half_star + spain_list_4_star
spain_3half_to_4half_star = spain_3half_to_4_star + spain_list_4_star
spain_3half_to_5_star = spain_3half_to_4half_star + spain_list_4_star
#4-5
spain_4_to_4half_star = spain_list_4_star + spain_list_4half_star
spain_4_to_5_star = spain_4_to_4half_star + spain_list_4half_star
#4,5-5
spain_4half_to_5_star = spain_list_4half_star + spain_list_5_star
