def extract_skills(tokens, skill_list):
    """
    Extracts skills from tokenized resume text.
    """
    extracted_skills = set()

    for token in tokens:
        if token in skill_list:
            extracted_skills.add(token)

    return list(extracted_skills)


def calculate_match_score(resume_skills, jd_skills):
    """
    Calculates percentage match between resume skills and job description skills.
    """
    if not jd_skills:
        return 0

    matched = set(resume_skills).intersection(set(jd_skills))
    score = (len(matched) / len(jd_skills)) * 100

    return round(score, 2), list(matched)
