pipeline {
    agent any
    options {
        disableConcurrentBuilds()
        timestamps()
    }

    stages {
        stage('SonarQube') {
            steps {
                withSonarQubeEnv(credentialsId: 'sonarqube-auth-token', envOnly: true) {
                // This expands the evironment variables SONAR_CONFIG_NAME, SONAR_HOST_URL, SONAR_AUTH_TOKEN that can be used by any script.
                println "${env.SONAR_HOST_URL}" 
                }
            }
        }
        // stage('SonarQube Code Analysis') {
        //     def scannerHome = tool 'sonar-scanner';
        //     steps {
        //         withSonarQubeEnv('sonaqube-local', credentialsId: 'sonarqube-auth-token') {
        //             bat 'sonar-scanner'
        //         }
        //     }
        // }
        // stage("Quality Gate") {
        //     steps {
        //         timeout(time: 5, unit: 'MINUTES') {
        //             // Parameter indicates whether to set pipeline to UNSTABLE if Quality Gate fails
        //             // true = set pipeline to UNSTABLE, false = don't
        //             waitForQualityGate abortPipeline: false
        //         }
        //     }
        // }
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