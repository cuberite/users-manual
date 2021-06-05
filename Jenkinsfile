pipeline {
    agent {
        docker 'debian'
    }
    stages {
        stage("Prepare") {
            steps {
                sh 'apt-get install python3-pip python3'
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
