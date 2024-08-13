import csv
from collections import Counter


with open('user_data/main_diary.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    trainings = [row for row in reader]

month = trainings[0]['DATE'].split('.')[1]
days_with_trainings = len([training for training in trainings if training['DATE'].split('.')[1] == month])

exercise_counts = Counter(training['EXERSICE'] for training in trainings)
most_frequent_exercise = exercise_counts.most_common(1)[0][0]

highest_level_exercise = max(trainings, key=lambda x: int(x['LEVEL']))

print(f"Количество дней, когда были тренировки в этом месяце: {days_with_trainings}")
print(f"Самое частое упражнение: {most_frequent_exercise}")
print(f"Упражнение с самым высоким уровнем: {highest_level_exercise['EXERSICE']} (уровень {highest_level_exercise['LEVEL']})")
