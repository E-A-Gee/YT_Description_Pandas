# Music Publisher Youtube Description Generator Using Pandas

I created this little program after completing the **Learn Data Analysis with Pandas** on *Codecademy*.

*Background Info:*
For my job at an educational music publisher, one of my responsibilities is to post score videos of our music to our YouTube channel. Each YouTube description follows a template: 
1. A link to where they can purchase the piece.
2. The voicing or grade level/difficulty of the piece.
3. A brief description of the piece.
4. Copyright information.

Conveniently, our database can do a standard exported csv file that contains the needed information. Previously I had been formatting these YouTube descriptions manually, which, while simple on an individual basis, became tedious given the amount of titles I had to upload. Each year we release over 100 choral pieces, and about 30 orchestra and band pieces each. 

To make things easier, (and for fun!), I created this program which takes the csv file and creates a new column with each of the YouTube descriptions automatically. Sitting down to create this file I knew basics of reading and writing to csv files using basic Python, but I didn't know where to start. Upon doing some researching, I found that life could be much easier if I could learn how to use Pandas.

**A Note on the Test File:** To protect the information of the music publisher I currently work at, ALL of the data in the test file has been FABRICATED. I deleted a lot of columns that are usually in a standard csv export from our database. I also used a mix of random number generators, random name generators, and simply made stuff up. Sidenote: I have a music background and could have put thought into if a elementary school orchestra could play in  x key with x many sharps or flats, etc. ...but decided not to. lol. 

