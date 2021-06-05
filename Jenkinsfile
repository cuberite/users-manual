pipeline {
    agent {
        docker 'cuberite/docker-ci/users-manual:latest'
    }
    stages {
        stage("Build") {
            steps {
                sh 'python3 generate.py'
                sh 'html5validator --root out'
            }
        }
    }
}
