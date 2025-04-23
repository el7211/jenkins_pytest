# 🧪 jenkins_pytest

This project demonstrates how to use **Jenkins** with **Docker** to run a simple **Pytest** test suite inside a containerized environment.

## 🔧 Overview

The repo includes:

- A basic test script: `tests/test_addition.py`
- A `docker-compose.yml` to spin up a container that:
  - Installs dependencies
  - Runs the test using `pytest`
- Instructions to launch a **Jenkins** container that can execute the job via pipeline or freestyle project.
