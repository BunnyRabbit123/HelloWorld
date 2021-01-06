pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Unit Testing') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy to Dev Integration Server') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('Dev Integration Test') {
            steps {
                echo 'Testing....'
            }
        }
    }
    post {
    success {
      googleStorageBuildLogUpload bucket: 'gs://artifacts.optical-forest-295616.appspot.com/JenkinsArtifacts', credentialsId: 'Release Orchestration', logName: "'build-log-${BRANCH}-${BUILD_NUMBER}.txt'"
    }
  }
}
