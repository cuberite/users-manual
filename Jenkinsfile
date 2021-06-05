pipeline {
    agent {
        docker 'python:latest'
    }
    stages {
        stage("Prepare") {
            steps {
                sh 'pip3 install html5validator'
            }
        }
        stage("Build") {
            steps {
                sh 'python3 generate.py'
                sh 'html5validator --root out'
            }
        }
    }
}
