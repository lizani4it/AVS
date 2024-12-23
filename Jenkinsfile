pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/lizani4it/AVS.git'  // Укажите ваш репозиторий
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'docker build -t avs-image .'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh 'docker stop avs-container || true'
                    sh 'docker rm avs-container || true'
                    sh 'docker run -d --name avs-container -p 8080:8080 avs-image'
                }
            }
        }
    }
}
