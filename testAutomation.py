import requests

testcases = [
    {"url": "http://127.0.0.1:8000/add/2/2", "expected": 4, "description": "Addition of 2 and 2"},
    {"url": "http://127.0.0.1:8000/subtract/2/2", "expected": 0, "description": "Subtraction of 2 from 2"},
    {"url": "http://127.0.0.1:8000/multiply/2/2", "expected": 4, "description": "Multiplication of 2 and 2"}
]

def test():
    for case in testcases:
        response = requests.get(case["url"])
        result = response.json()["result"]
        assert result == case["expected"], f"Test failed: {case['description']}"
        print(f"Test passed: {case['description']}")

test()
