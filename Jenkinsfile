pipeline {
    agent any

    environment {
        FLASK_APP = 'app.py'
        DOCKER_IMAGE = 'team-crud'  
    }

    stages {
        stage('Pull Repository') {
            steps {
                git credentialsId: 'github-credentials', url: 'https://github.com/alan-vglez/Lenmo_033_PIA', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker compose down'  
                    sh 'docker compose up -d --build'  
                }
            }
        }
    }
    
    post {
        success {
            echo 'The Flask application is now running!'
        }
        failure {
            echo 'The build or deployment failed. Check logs for details.'
        }
    }
}
