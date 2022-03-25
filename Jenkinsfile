pipeline {
    agent any
    environment {
        DOCKER_REGISTRY_NAME = 'artifactory-demo.io:8082'
        DOCKER_REPO_NAME = 'docker-local'
        APP_NAME = 'simple-flask-app'
    }
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
                    docker.build("${env.DOCKER_REGISTRY_NAME}/${env.DOCKER_REPO_NAME}/${env.APP_NAME}:${env.BUILD_ID}", "--label io.demo.app=${env.APP_NAME} .")
                } 
                println "Checking if the new image is in place.."
                bat "docker image ls -f label=io.demo.app=${env.APP_NAME}"
            }
        }
        stage('Test Application') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Push Docker Image') {
            steps {
                println "Pushing image to jfrog registry.."
                script {
                    docker.withRegistry("http://${env.DOCKER_REGISTRY_NAME}", "jfrog-container-registry-auth") {                        
                        dockerImage.push("${env.DOCKER_REGISTRY_NAME}/${env.DOCKER_REPO_NAME}/${env.APP_NAME}:${env.BUILD_ID}")                     
                    }
                }
            }
        }
        stage('Deploy to K8s') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}