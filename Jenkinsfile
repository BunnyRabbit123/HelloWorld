pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
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
