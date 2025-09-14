First let's set up the database. I will be using PostgreSQL, in particular psql:
<img width="1473" height="896" alt="{FBDEE11E-7CCF-4F59-AB46-65050A0B2C3E}" src="https://github.com/user-attachments/assets/24422105-fe95-48a1-8ca2-87d7d04f4eec" />

As you see we created a database. Now we can choose it and see what's inside it:
<img width="1469" height="442" alt="{79C43A10-19FD-4115-8D06-7E4E683CA47E}" src="https://github.com/user-attachments/assets/fdb03276-300a-4727-ae1e-80d777e8ef0d" />

That's right, absolutely nothing - 'Did not find any relations' means the database is empty. Let's create tables first before importing. Let's start with districts table:
<img width="1255" height="849" alt="{6CB6EC14-A7EB-476B-804E-8CC8B5A2874D}" src="https://github.com/user-attachments/assets/f9724612-cdf2-46d3-a350-9e584247eed8" />

Now, that the districts table is intact, we can import data from our csv file to it:
<img width="1349" height="846" alt="{92938822-ADA3-46F1-9145-8A3255BBBEBC}" src="https://github.com/user-attachments/assets/eae2e975-5ce4-4c94-8139-cc4924278516" />

Soon enough, we can do the same with all other tables:
<img width="1464" height="804" alt="{0041FB53-35DE-4BEB-83A0-02342D893A31}" src="https://github.com/user-attachments/assets/d62920ba-2c27-43d9-854c-29e8a9b3664a" />
<img width="1465" height="795" alt="{DE8A7F6E-A806-4FED-B318-6A6F5EC492FC}" src="https://github.com/user-attachments/assets/b262b4a8-f65b-4b57-aec9-b7b94f5f7b1d" />
<img width="1345" height="505" alt="{9FDB5F98-F022-4649-BD23-FD2F1FC5C57A}" src="https://github.com/user-attachments/assets/38613edb-4ad9-4d5b-a6fa-a1372edfe3f9" />
I used LIMIT here because this table has too much records, so processing it without LIMIT would have took too much time.

Now, that we have all the data loaded in our database, let's do some basic queries:
<img width="1032" height="318" alt="{D34FD79E-A88C-4AEA-A680-300326701F30}" src="https://github.com/user-attachments/assets/5289ada9-925b-4376-8e17-f60a4a5017cc" />
<img width="1296" height="774" alt="{A6E4736D-875A-435E-B61A-E76102869855}" src="https://github.com/user-attachments/assets/5b44528d-f049-4d44-8494-9cd5cbe5d660" />
<img width="1250" height="783" alt="{39240C2D-EFB3-45F5-BA37-18A46214B3C0}" src="https://github.com/user-attachments/assets/e373dc3d-af82-41e8-9935-efa9adc6ef88" />
