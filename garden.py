import spacy

gardenpathSentences = ["Visiting friends can be annoying.", "The nearby shop owner assisted the dog, bite victim.", "Mary gave the child a Band-Aid.", "That Jill is never here hurts", "The cotton clothing is made of grows in Mississippi."]

nlp = spacy.load('en_core_web_sm')

for sample in gardenpathSentences:
	doc = nlp(sample)
	tok = [token.orth_ for token in doc if not token.is_punct | token.is_space]

	# Tokenising
	nis = [(i, i.label_, i.label) for i in doc.ents]
	print(nis)
	for i in doc.ents:
		entity = i.label_
		entity_fact = spacy.explain(entity)
		print(f"{entity}: {entity_fact}")
		print("\n")


#FDD
# -- Food
# -- No because instead of the entity to be BVG it is FDD

#BLD
# -- Building
# -- No because there is a confusion, because building is also included in entity NORP