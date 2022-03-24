pipeline {
    agent any
    options {
        disableConcurrentBuilds()
        timestampts()
    }

    stages {
        stage('SonarQube Code Analysis') {
            def scannerHome = tool 'sonar-scanner';
            steps {
                withSonarQubeEnv('sonaqube-local', credentialsId: 'sonarqube-auth-token') {
                    bat 'sonar-scanner'
                }
            }
        }
        stage("Quality Gate") {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    // Parameter indicates whether to set pipeline to UNSTABLE if Quality Gate fails
                    // true = set pipeline to UNSTABLE, false = don't
                    waitForQualityGate abortPipeline: false
                }
            }
        }
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
}