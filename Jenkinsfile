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
        stage('Deploy to Dev Server') {
            steps {
                echo 'Deploying....'
            }
        }
    }
    post {
    success {
      googleStorageBuildLogUpload bucket: 'gs://artifacts.optical-forest-295616.appspot.com/JenkinsArtifacts', credentialsId: 'Release Orchestration', logName: 'build-log.txt'
    }
  }
}
