print("Type in 4 adjectives: ")
adjectives = input()
adjectives = adjectives.split()

print("Type in 3 nouns: ")
nouns = input()
nouns = nouns.split()

print("Type in 2 adverbs: ")
adverbs = input()
adverbs = adverbs.split()

print("Type in 3 verbs: ")
verbs = input()
verbs = verbs.split()

print(f"Today I went to the zoo. I saw a(n) {adjectives[0]} {nouns[0]} jumping up and down in its tree. He {verbs[0]} {adverbs[0]} through the large tunnel that led to its {adjectives[1]} {nouns[1]}. I got some peanuts and passed them through the cage to a gigantic gray {nouns[2]} towering above my head. Feeding that animal made me hungry. I went to get a {adjectives[2]} scoop of ice cream. It filled my stomach. Afterwards I had to {verbs[1]} {adverbs[1]} to catch our bus. When I got home I {verbs[2]} my mom for a {adjectives[3]} day at the zoo.")
