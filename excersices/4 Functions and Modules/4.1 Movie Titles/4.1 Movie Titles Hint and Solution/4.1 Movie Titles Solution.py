

def valid_title(movie_title):
    '''

    Returns a boolean (True/False)
    True if the title is valid, False otherwise.

    '''

    acp_words = set(['a' , 'an', 'the','and', 'but', 'or','in', 'on', 'at', 'with', 'from', 'of'])
    status = True
    words = movie_title.split()

    final_title = []

    
    if not words[0].istitle():
        status = False
    
    final_title.append(words[0].title())



    for word in words[1:-1]:
        if word.lower() in acp_words:
            if not word.islower():
                status = False
                final_title.append(word.lower())
            else:
                final_title.append(word)
        elif not word.istitle():
            status = False
            final_title.append(word.title())
        else:
            final_title.append(word)

    
    if len(words) >= 2:
        if not words[-1].istitle():
            status = False
        
        final_title.append(words[-1].title())


    return status, " ".join(final_title)


# movie_title = input("Enter The Movie Title: ")

# print(movie_title)



"""
Uncomment this code below for checks
"""

movie_titles = [
    "The KnifeSaw Comeback",
    "Orange Story",
    "The ZeusDad",
    "Brawl bat",
    "gone with the wind",
    "A Horrible Story",
    "Insertion",
    "The Light Kday",
    "GreatFriends",
    "The System",
    "In an Open Room",
    "Forrest Guy",
    "Interstellarrs",
    "The Lord of the RoundTable",
    "The avengers",
    "Gladiator of Persia",
    "jurassic park",
    "titanic",
    "the"
]

for movie in movie_titles:
    print(valid_title(movie))

"""
Expected Output

False, 'The Knifesaw Comeback'
True, 'Orange Story'
False, 'The Zeusdad'
False, 'Brawl Bat'
False, 'Gone with the Wind'
True, 'A Horrible Story'
True, 'Insertion'
True, 'The Light Kday'
False, 'Greatfriends'
True, 'The System'
True, 'In an Open Room'
True, 'Forrest Guy'
True, 'Interstellarrs'
False, 'The Lord of the Roundtable'
False, 'The Avengers'
True, 'Gladiator of Persia'
False, 'Jurassic Park'
False, 'Titanic'
False, 'The'

False means the original movie title is not valid


"""


