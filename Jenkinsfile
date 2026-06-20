pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ai-devops-agent .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f ai-devops-agent-container || true'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker run -d \
                --name ai-devops-agent-container \
                -p 5001:5000 \
                ai-devops-agent
                '''
            }
        }
    }
}
