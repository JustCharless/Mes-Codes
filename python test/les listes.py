notesCompta = [10, 10, 20, 16, 9, 8, 2, 11, 12, 14, 18]
élèves = ['clément', 'mathilde', 'éloise', 'mathieu', 'kaito', "cole", 'camille', 'lou', 'chloe', 'roy', 'blake', 'jordan']

print(notesCompta[-3])
lenght = len(notesCompta)
print("la liste comporte ",lenght, "éléments mais on a oublié la note de camille")
notesCompta.append(13)
print(notesCompta)
lenght = len(notesCompta)
print("maintenant on a ",lenght, "copies")
