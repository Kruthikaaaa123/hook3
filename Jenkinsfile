
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\STUDENT\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                echo 'Checking Python installation'
                bat '"%PYTHON%" --version'
            }
        }

        stage('Build') {
            steps {
                echo 'Checking Python application'
                bat '"%PYTHON%" -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Executing automated tests'
                bat '"%PYTHON%" -m unittest app'
            }
        }

        stage('Run application') {
            steps {
                echo 'Running Python application'
                bat '"%PYTHON%" app.py'
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully!'
        }

        failure {
            echo 'CI pipeline failed!'
        }
    }
}


