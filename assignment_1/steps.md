First let's set up the database. I will be using PostgreSQL, in particular psql:
<img width="1473" height="896" alt="{FBDEE11E-7CCF-4F59-AB46-65050A0B2C3E}" src="https://github.com/user-attachments/assets/24422105-fe95-48a1-8ca2-87d7d04f4eec" />

As you see we created a database. Now we can choose it and see what's inside it:
<img width="1469" height="442" alt="{79C43A10-19FD-4115-8D06-7E4E683CA47E}" src="https://github.com/user-attachments/assets/fdb03276-300a-4727-ae1e-80d777e8ef0d" />

That's right, absolutely nothing - 'Did not find any relations' means the database is empty. Let's create tables first before importing. Let's start with districts table:
<img width="1255" height="849" alt="{6CB6EC14-A7EB-476B-804E-8CC8B5A2874D}" src="https://github.com/user-attachments/assets/f9724612-cdf2-46d3-a350-9e584247eed8" />

Now, that the districts table is intact, we can import data from our csv file to it:
<img width="1349" height="846" alt="{92938822-ADA3-46F1-9145-8A3255BBBEBC}" src="https://github.com/user-attachments/assets/eae2e975-5ce4-4c94-8139-cc4924278516" />

Soon enough, we can do the same with all other tables:
