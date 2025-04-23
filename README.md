# 🧪 jenkins_pytest

This project demonstrates how to use **Jenkins** with **Docker** to run a simple **Pytest** test suite inside a containerized environment.

## 🔧 Overview

Pre-req:
- A **Jenkins** container

The repo includes:
- A basic test script: `tests/test_addition.py`
- A `docker-compose.yml` to spin up a container that:
  - Installs dependencies
  - Runs the test using `pytest`

## 🔧 Run the pytest through Jenkins. 
- Launch the jenkins container 
- Create a freestyle project.
- Add git repo 'https://github.com/el7211/jenkins_pytest.git'
- Add a build shell script
```
echo "📦 Cloning repo and running docker-compose..."

echo "📍 Current directory inside Jenkins: $PWD"
echo "🔥 Jenkins WORKSPACE: $WORKSPACE"

cd "$WORKSPACE"

echo "📂 Listing current directory contents..."
ls -la

# Run Docker Compose
echo "🚀 Running docker-compose up..."
docker-compose up --build
docker-compose down -v --remove-orphans

```
- click Build and check the console output