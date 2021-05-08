
import sqlite3
import matplotlib.pyplot as plt


conn = sqlite3.connect("oscar_winners.sqlite")
cursor = conn.cursor()

# გვიჩვენებს თუ რომელმა მსახიობებმა მოახერხეს მომხმარებლის მიერ შეყვანილ ასაკში ოსაკირს მოგება
age=(int(input("შეიყვანეთ ასაკი")))
cursor.execute("SELECT name FROM oscar WHERE age=:age", {'age': age})
records = cursor.fetchall()
namelist=[]
for x in records:
    namelist.append(x[0])
print(f"თქვენს მიერ მითითებულ ასაკში ოსკარი მოიგეს შემდეგმა მსახიობებმა {str(namelist)}")

# შეაქვს მომხმარებლის მიერ შეყვანილი მონაცემები შესაბამის ველებში
year = int(input('გადაცემის წელი'))
age = int(input('მსახიობის ასაკი'))
name = input('მსახიობის სახელი:')
gender=str(input('მსახიობის სქესი F-ქალი M-კაცი:'))
gender=gender.upper()
movie_name=str(input('ფილმის სახელი:'))
cursor.execute("INSERT INTO oscar (Year , age, name, gender,movie) VALUES (?,?,?,?,?)",
               (year,age,name,gender,movie_name))
conn.commit()
print('შეტანა წარმატებით დასრულდა')

# მომხმარებელს შეყავს ფილმის სახელი და შემდეგ ამ ფილმის შესაბამის ველებში ცვლის მსახიობის ასაკს მსახიობის სახელს
# მსახობის სქესს ოსკარის გადაცემის თარიღს
year = int(input('გადაცემის წელი'))
age = int(input('მსახიობის ასაკი:'))
name = str(input('მსახიობის სახელი'))
gender=str(input('მსახიობის სქესი F-ქალი M-კაცი:'))
gender=gender.upper()
movie_name=str(input('ფილმის სახელი'))
cursor.execute("UPDATE oscar SET year=?,age=?,name=?,gender=? WHERE movie=?",
        (year,age,name,gender,movie_name))
conn.commit()
print("მონაცემები წარმატებით განახლდა")


# სქესის მიხედვით გამოქავს  ოსკარის გამარჯვებულთა პროცენტული მაჩვენებელი
cursor.execute("SELECT gender From oscar")
records=cursor.fetchall()
female_count=0
male_cout=0
for x in records:
    if x[0]=="F":
        female_count+=1
    if x[0]=="M":
        male_cout+=1
sizes = [male_cout, female_count]
fig1, ax1 = plt.subplots()
labels=("ქალები","კაცები")
ax1.pie(sizes, labels=labels, autopct='%2.2f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

conn.close()
cursor.close()