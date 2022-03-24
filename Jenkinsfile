pipeline {
    agent any
    options {
        disableConcurrentBuilds()
        timestamps()
    }

    stages {
        // stage('Git') {
        //     steps {
        //         git branch: 'main', credentialsId: 'github-jenkins-key', url: 'git@github.com:RomanGoryainov/simple-flask-app.git'
        //     }
        // }
        stage('SonarQube Code Analysis') {           
            steps {
                script {
                    scannerHome = tool 'sonar-scanner';
                }
                    withSonarQubeEnv('sonaqube-local') {                
                        bat "${scannerHome}/bin/sonar-scanner.bat"
                    }
            }
        }
        stage("Quality Gate") {
            steps {
                timeout(time: 10, unit: 'MINUTES') {
                    // Parameter indicates whether to set pipeline to UNSTABLE if Quality Gate fails
                    // true = set pipeline to UNSTABLE, false = don't
                    waitForQualityGate abortPipeline: false, credentialsId: 'sonabe-webhook-token'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                 docker.build("test:${env.BUILD_ID}", '--label io.demo.app=simple-flask-app .')
                } 
                bat 'docker image ls -f "label=io.demo.app=simple-flask-app"'
            }
        }
        stage('Test Application') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy to K8s') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}