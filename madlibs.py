def user_input(prompt):
    user_input = input(prompt)
    return user_input


def get_user_input():

    name1 = user_input("Type a name ")
    adjective1 = user_input("Type an adjective ")
    adjective2 = user_input("Type an adjective ")
    verb1 = user_input("Type a verb ")
    verb_ed1 = user_input("Type a verb ending in 'ed' ")
    verb_ed2 = user_input("Type a verb ending in 'ed' ")
    silly_word = user_input("Type a silly word ")
    vehicle = user_input("Type a vehicle ")
    noun1 = user_input("Type a noun ")
    noun2 = user_input("Type a noun ")
    noun_plural = user_input("Type a plural noun ")

    story = """
    Darth {} looked at his master while his {} breathing filled the room.
    He was told to go {} everything on the planet of {}.
    He got in his {} and jumped to hyperspace.
    Shortly before reaching the planet, he dropped out of hyperspace and was attacked by Rebel {}.
    He {} them off and continued to the planet`s surface.
    He landed and confronted more opposition, slicing them down with his {}.
    He used the {} to choke another Rebel, then {} him aside.
    He finished off all life on the planet with a/an {} laugh.
    """.format(name1, adjective1, verb1, silly_word, vehicle, noun_plural, verb_ed1, noun1, noun2, verb_ed2, adjective2)

    print(story)

def test(name1, adjective1, adjective2, verb1, verb_ending_ed1, verb_ending_ed2, silly_word, vehicle, noun1, noun2, noun_plural):

    story = """
    Darth {} looked at his master while his {} breathing filled the room.
    He was told to go {} everything on the planet of {}.
    He got in his {} and jumped to hyperspace.
    Shortly before reaching the planet, he dropped out of hyperspace and was attacked by Rebel {}.
    He {} them off and continued to the planet`s surface.
    He landed and confronted more opposition, slicing them down with his {}.
    He used the {} to choke another Rebel, then {} him aside.
    He finished off all life on the planet with a/an {} laugh.
    """.format(name1, adjective1, verb1, silly_word, vehicle, noun_plural, verb_ending_ed1, noun1, noun2, verb_ending_ed2, adjective2)

    print(story)

#test("Ricardo", "Heavy", "Evil", "Run", "Smashed", "Dunked", "Bleh", "submarine", "Pirates", "Man", "Dogs")

get_user_input()
