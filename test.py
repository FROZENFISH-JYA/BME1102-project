import read_write_csv as rw
import search as s
import ordering as o

df=rw.ReadCsv("./CSVtest.csv")
print("original:")
print(df)
print("search by:")
a=s.search_Date(df,'2023.1.2','2023.1.3')
a=s.search_Name(a,'cat1')
print(a)