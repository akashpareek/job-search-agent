def format_jobs(data):

    jobs = data.get("data", [])

    if not jobs:
        return "No jobs found"

    result = ""

    for job in jobs[:5]:

        result += f'''
Company: {job.get("employer_name")}

Role: {job.get("job_title")}

Location: {job.get("job_city")}

Apply:
{job.get("job_apply_link")}

-----------------------------------
'''

    return result