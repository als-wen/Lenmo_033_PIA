pipeline {
    agent any

    environment {
        FLASK_APP = 'app.py'
        DOCKER_IMAGE = 'team-crud'
    }

    parameters {
        booleanParam(name: 'STOP_CONTAINER', defaultValue: false, description: 'Check this to stop the Docker container.')
    }

    stages {
        stage('Pull Repository') {
            steps {
                git credentialsId: 'github-credentials', url: 'https://github.com/alan-vglez/Lenmo_033_PIA', branch: 'main'
            }
        }

        stage('Build and Run Docker Container') {
            steps {
                script {
                    sh 'docker-compose up -d --build'
                }
            }
        }

        stage('Stop Docker Container') {
            when {
                expression { params.STOP_CONTAINER } 
            }
            steps {
                script {
                    sh 'docker-compose down' 
                }
            }
        }
    }

    post {
        success {
            echo 'The pipeline executed successfully!'
        }
        failure {
            echo 'An error occurred. Check logs for details.'
        }
    }
}
