import requests

BASE_URL = 'http://localhost:5000'


def test_edit_job_correct():
    url = f"{BASE_URL}/api/jobs/2"
    data = {
        "user_id": 2,
        "job": "Updated Job",
        "work_size": 15,
        "collaborators": "John, Jane",
        "start_date": "2024-07-16T10:00:00",
        "end_date": "2024-07-16T18:00:00",
        "is_finished": True
    }
    response = requests.put(url, json=data)
    print(response)


def test_edit_job_incorrect():
    url = f"{BASE_URL}/api/jobs/q"
    data = {
        "user_id": 1,
        "job": "Updated Job"
    }
    response = requests.put(url, json=data)
    print(response)

    url = f"{BASE_URL}/api/jobs/9999"
    data = {
        "user_id": 2,
        "job": "Updated Job",
        "work_size": 15,
        "collaborators": "John, Jane",
        "start_date": "2024-07-16 10:00:00",
        "end_date": "2024-07-16 18:00:00",
        "is_finished": True
    }
    response = requests.put(url, json=data)
    print(response)


def test_get_all_jobs():
    url = f"{BASE_URL}/api/jobs"
    response = requests.get(url)
    print(response.json())


if __name__ == "__main__":
    test_edit_job_correct()
    test_edit_job_incorrect()
    test_get_all_jobs()
