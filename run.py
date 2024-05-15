from GameField import GameField
from task import Optimizer
import json
import time

FIELD_FILENAME = "field.csv"


def main():
    field = GameField()
    field.fill(FIELD_FILENAME)
    TIMEOUT_SECONDS = 100

    try:
        # start_time = time.time()
        best_chromosome = Optimizer.optimize(field)
        result = field.testAnt(best_chromosome)
        print(f"Your result is {result}")
        print("Max is 89")
        # end_time = time.time()
        # elapsed_time = end_time - start_time
        # if elapsed_time > TIMEOUT_SECONDS:
        #     raise Exception("Test exceeded time limit.")

        grade = 0

        if 50 <= result < 60:
            grade = 1
        elif 70 > result >= 60:
            grade = 2
        elif 75 > result >= 70:
            grade = 3
        elif 80 > result >= 75:
            grade = 4
        elif result >= 80:
            grade = 5

    except Exception as e:
        print(f"Error during optimization: {e}")
        grade = "exeption"

    with open('grade.json') as fp:
        dictObj = json.load(fp)

    with open('grade.json', 'r+') as file:
        dictObj['grade'].append(grade)
        file.write(json.dumps(dictObj))
        file.close()


if __name__ == "__main__":
    main()
