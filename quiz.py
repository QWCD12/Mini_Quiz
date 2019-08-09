#title
print ("The Something Quiz\n")

#counter variable
correct = 0
incorrect = 0

#Answer Input function
def answer(answer, a, b, c, d):
    global correct
    global incorrect
    while answer != a or answer != b or answer != c or answer != d:
        if answer == a:
            print ("correct")
            correct += 1
            break
        elif answer == b or answer == c or answer == d:
            print ("incorrect")
            incorrect += 1
            break
        else:
            answer = input()

#Instructions
print ("Answer questions by typing the letter assigned.\n")
#first question
print ("1.What is the cricumference of the earth?")
print ("a)4,070km \nb)35,981km \nc)40,070km \nd)58,374km")
first_answer = input()
answer(first_answer, "c", "a", "b", "d")

#second question
print ("\n2.What is the country south of Spain?")
print ("a)Moroco \nb)Africa \nc)Portugal \nd)France")
second_answer = input()
answer(second_answer, "a", "b", "c", "d")

#third question
print ("\n3.What computer runs linux default?")
print ("a)Dell \nb)Macbook \nc)Chromebook \nd)None")
third_answer = input()
answer(third_answer, "d", "a", "b", "c")

#forth question error
print ("\n4.What genre involves aliens and alternative universes?")
print ("a)sci-fi \nb)romcom \nc)non-fiction")
forth_answer = input()
answer(forth_answer, "a", "b", "c", "c")

#fifth question
print ("\n5.How many electrons are contained in a hydrogen atom?")
print ("a)17 \nb)25 \nc)8 \nd)1")
fifth_answer = input()
answer(fifth_answer, "d", "a", "b", "c")

#sixth question
print ("\n6.The clear gel inside your eye is called?")
print ("a)Water \nb)Vitreous \nc)Sodium-Water mix \nd)Lubricant")
sixth_answer = input()
answer(sixth_answer, "b", "a", "c", "d")

#seventh question
print ("\n7.Fill in the blank:Earth is one big _____.")
print ("a)Organism \nb)Tree \nc)Land water Hybrid \nd)Magnet")
seventh_answer = input()
answer(seventh_answer, "d", "a", "b", "c")

#eigth question
print ("\n8.What is the reverse of evaporation?")
print ("a)Condensation \nb)Condsenation \nc)Evapotranspiration \nd)Precipitation")
eigth_answer = input()
answer(eigth_answer, "a", "b", "c", "d")

#ninth question
print ("\n9.Heat moves in three ways: radiation, conduction, convection.")
print ("a)True \nb)False")
ninth_answer = input()
answer(ninth_answer, "a", "b", "b", "b")

#final question
print ("\n10.What does a telescope do?")
print ("a)Helps heat items \nb)Long tube with mirrors & lenses \nc)Makes distant objects look near")
final_answer = input()
answer(final_answer, "c", "a", "b", "b")

# Result
print ("\n\nFinal Result")
print ("Correct: " + str(correct))
print ("Incorrect: " + str(incorrect))
correct = correct * 10
print  ("Precentage: " + str(correct) + "%")
