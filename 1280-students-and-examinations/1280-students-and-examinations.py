import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    all_combo = students.merge(subjects, how="cross")

    exam_copy = examinations.copy()
    exam_copy['attended'] = 1

    df = all_combo.merge(exam_copy, how="left", on=['student_id', 'subject_name'])
    result = df.groupby(['student_id', 'student_name', 'subject_name'], as_index=False, dropna=False).agg(attended_exams=('attended', 'count'))
    return result.sort_values(by=['student_id', 'subject_name'])
    