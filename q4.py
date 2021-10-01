# Assumptions
#  - Each question is in new line and starts with `Q` has a number after it and then a `)`
#  - Bonus Question is a part of Q5
#  - Subquestions will be below the parent question
import re
from functools import cmp_to_key

# Define a comparator for our questions
def comparator(q1, q2):
    q_number1 = int(re.search(r'^(\d+)(\))', q1).group(1))
    q_number2 = int(re.search(r'^(\d+)(\))', q2).group(1))
    return q_number1 - q_number2


with open('assignment.txt') as assignment:
    with open('assignmentNew.txt', 'w+') as assignmentNew:
        
        # Extract blocks that start with `Q`
        partitions = assignment.read().split("\nQ")
        questions = []
        
        # Squeeeze the blocks that start with `Q` but aren't a question
        # This doesn't apply to header (partition[0])
        for block in partitions[1:]:
            if not re.match("^\d+\)", block):
                questions[-1] = questions[-1] + "\nQ" + block
            else:
                questions.append(block)

        # Write the header + sorted questions in new file
        assignmentNew.write("\nQ".join(partitions[0:1] + sorted(questions, key=cmp_to_key(comparator))))