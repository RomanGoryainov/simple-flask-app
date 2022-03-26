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
                    newImage = docker.build("${env.DOCKER_REGISTRY_NAME}/${env.DOCKER_REPO_NAME}/${env.APP_NAME}:v-${env.BUILD_ID}", "--label io.demo.app=${env.APP_NAME} .")
                }
                println "Checking if the new image is in place.."                 
                bat "docker image ls -f label=io.demo.app=${env.APP_NAME}"
            }
        }
        stage('Test Application') {
            steps {
                echo 'Testing..'
                // Test code using pytest package 
                //git branch: 'main', credentialsId: 'github-jenkins-key', url: 'git@github.com:RomanGoryainov/simple-flask-app-tests.git'
            }
        }
        stage('Push Docker Image') {
            steps {
                println "Pushing image to jfrog registry.."
                script {
                    docker.withRegistry("http://${env.DOCKER_REGISTRY_NAME}", "jfrog-container-registry-auth") {
                        // add tag like v-1.0.0 from git commit tag                       
                        newImage.push("latest")
                    }
                }
            }
        }
        stage('Remove docker image from Jenkins') {
            steps {
                echo 'Removing image..'
                // Test code using pytest package
                bat 'FOR /F "tokens=*" %a IN (\'docker image ls -q -f "label=io.demo.app=${env.APP_NAME}"\') DO docker rmi %a'
            }
        }
        stage('Deploy to K8s') {
            steps {
                // How to deploy new image? New deployment? How to add image from env?
                echo 'Deploying....'
            }
        }
    }
}