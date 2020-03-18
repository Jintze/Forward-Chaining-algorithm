# Lab Assignment #6
# Forward Chaining Algorithm
# 
# AUCSC 460
# Author: Jinzhe Li
# Instructor: Mi-Young Kim
# 
# This Python program uses forward chaining algorithm to find the solution
# based on user's input of knowledge base.

inferred = []
agenda = []
####################################################################################
# Get the input of knowledge base from user.
def inputKB():
    userInput = ""
    i = 0   # KB's number
    k = 0   # Agenda's number
    knowledgeBase = [] 
    while userInput != "exit":
        print("Please input knowledge base:(type 'exit' if you want to stop)")
        userInput = input()

        if userInput != "exit":
            # Agenda if user's input is one single letter.
            if len(userInput) == 1:
                print("Agenda[" + str(k) + "]:" + userInput[0])
                agenda.insert(0,userInput)
                k+=1
            # Get the premise and conclusion and put them into KB.
            else:
                userConclusion = userInput.split("=>")
                conclusion = (userConclusion[-1])
                userPremise = userConclusion[0].split("^")
                premise = userPremise
                count = len(premise)
                newKB = [premise, conclusion, count]
                knowledgeBase.append(newKB)
                # Print KB if the input is not agenda.
                for j in range(0, len(premise)):
                    print("KB[" + str(i) + "]." + "premise[" + str(j) + "]:" + premise[j] + ", ", end = '')
                print("KB[" + str(i) + "]." + "conclusion:" + conclusion + ", count:" + str(count))
                i+=1

        else:
            print("stopped")    # Stop if input is exit.
    return knowledgeBase

####################################################################################
# After creating the KB, this function deals with Forward Chaining Algorithm
# and the print of each step.
def forwardChaining(knowledgeBase):
    print("What is your query?")
    q = input()
    print("=============")
    print("Forward chaining algorithm starts")
    print("=============")
    while agenda:   # while agenda is not empty
        p = agenda.pop(0)   # p←POP(agenda)
        print("***** Current agenda:" + p + " *****")
        #if p = q then return true
        if p == q:
            print("Goal Achieved")
            print("The query " + p + " is true based on the knowledge.")
            print("---- The End -----")
            return True
        # if inferred[p] = false
        if p not in inferred:
            inferred.append(p)  # nferred[p]←true
            # for each clause c in KB where p is in c.PREMISE
            for clauseNum in range(0, len(knowledgeBase)):
                for premiseNum in range (0, len(knowledgeBase[clauseNum][0])):
                    if p == knowledgeBase[clauseNum][0][premiseNum]:

                        for j in range(0, len(knowledgeBase[clauseNum][0])):
                            if j != len(knowledgeBase[clauseNum][0]) - 1:
                                print(knowledgeBase[clauseNum][0][j] + "^", end = '')
                            else:
                                print(knowledgeBase[clauseNum][0][j], end = '')
                        print("=>" + knowledgeBase[clauseNum][1] + ", count:" + str(knowledgeBase[clauseNum][2]))
                        print("Primise " + p + " matched agenda")
                        knowledgeBase[clauseNum][2] -= 1    # # decrement count [c]
                        # if count [c] = 0 then add c.CONCLUSION to agenda
                        if knowledgeBase[clauseNum][2] == 0:
                            print("Count is reduced to 0 ==> Agenda " + knowledgeBase[clauseNum][1] + " is created")
                            agenda.append(knowledgeBase[clauseNum][1])
                        else:
                            print("Count is reduced to " + str(knowledgeBase[clauseNum][2]))
                        print("=============")
    else:
        print("Goal can not be achieved")
        return False

####################################################################################

def main():
    forwardChaining(inputKB())

# Call main() to run it
if __name__ == "__main__":
    main()