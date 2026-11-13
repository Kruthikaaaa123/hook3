
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\STUDENT\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Downloading source code from GitHub'
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
                echo 'Compiling Python application'
                bat '"%PYTHON%" -m py_compile app.py'
                echo 'Build completed successfully'
            }
        }

        stage('Test') {
            steps {
                echo 'Executing automated unit tests'
                bat '"%PYTHON%" -m unittest app -v'
                echo 'All tests completed successfully'
            }
        }

        stage('Run Application') {
            steps {
                echo 'Running Student Calculator Application'
                bat '"%PYTHON%" app.py'
            }
        }
    }

    post {
        success {
            echo '================================'
            echo 'CI PIPELINE COMPLETED SUCCESSFULLY!'
            echo '================================'
        }

        failure {
            echo '================================'
            echo 'CI PIPELINE FAILED!'
            echo 'Check Console Output for errors'
            echo '================================'
        }

        always {
            echo 'Jenkins Pipeline Execution Finished'
        }
    }
}




