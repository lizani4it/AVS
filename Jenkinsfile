pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "rgz-test_app:latest"
        CONTAINER_NAME = "test_app"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Deploy Application') {
            steps {
                script {
                    sh '''
                        ls -la
                    '''
                }
            }
        }
    }
}