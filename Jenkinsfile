

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Checking Python application'
                bat 'py -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Executing automated test'
                bat 'py -m unittest app'
            }
        }

        stage('Run application') {
            steps {
                bat 'py app.py'
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully'
        }

        failure {
            echo 'CI pipeline failed'
        }
    }
}
