import sqlite3
import pickle

mydb = sqlite3.connect(database="database.db", check_same_thread=False)
mycursor = mydb.cursor()

mycursor.execute("DROP TABLE IF EXISTS question_paper")
mycursor.execute("CREATE TABLE question_paper(u_id VARCHAR(5), name VARCHAR(20), username VARCHAR(10), dept VARCHAR(10), year int(1), phoneno CHAR(10), instagram VARCHAR(30), facebook VARCHAR(30))")
# u_id, name, username, dept, year, phoneno, instagram, facebook
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("1", "name 1", "username 1", "CSE", 2, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("2", "name 2", "username 2", "MECH", 1, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("3", "name 3", "username 3", "CSE", 3, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("4", "name 4", "username 4", "MECH", 4, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("5", "name 5", "username 5", "CSE", 2, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("6", "name 6", "username 6", "MECH", 1, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("7", "name 7", "username 7", "CSE", 4, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("8", "name 8", "username 8", "MECH", 3, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("9", "name 9", "username 9", "MECH", 2, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("10", "name 10", "username 10", "CSE", 1, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("11", "name 11", "username 11", "EEE", 1, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("12", "name 12", "username 12", "EEE", 1, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("13", "name 13", "username 13", "EEE", 1, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("14", "name 14", "username 14", "CSE", 3, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("15", "name 15", "username 15", "ECE", 3, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("16", "name 16", "username 16", "ECE", 3, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("17", "name 17", "username 17", "ECE", 3, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("18", "name 18", "username 18", "ECE", 1, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("19", "name 19", "username 19", "ICE", 4, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')
mycursor.execute('''INSERT INTO question_paper (u_id, name, username, dept, year, phoneno, instagram, facebook) VALUES ("20", "name 20", "username 20", "ICE", 4, "1234567890", "https://www.instagram.com/instagram/", "https://www.facebook.com/facebookIndia")''')


f = open("interest_table.bin", "wb")
interest = {
    "1": ["coding", "watching web series"],
	"2": ["coding", "watching movies"],
	"3": ["coding", "watching movies"],
	"4": ["dancing", "watching movies"],
	"5": ["dancing", "watching web series"],
	"6": ["dancing", "watching movies"],
	"7": ["coding", "watching movies"],
	"8": ["dancing", "watching movies"],
	"9": ["coding", "watching movies"],
	"10": ["coding", "watching movies"],
	"11": ["dancing", "watching web series"],
	"12": ["coding", "watching movies"],
	"13": ["music", "watching movies"],
	"14": ["music", "watching web series"],
	"15": ["music", "watching movies"],
	"16": ["music", "watching movies"],
	"17": ["coding", "watching movies"],
	"18": ["music", "watching web series"],
	"19": ["coding", "watching movies"],
	"20": ["music", "watching web series"],
}
