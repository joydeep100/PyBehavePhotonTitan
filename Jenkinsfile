pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'pip3.8 install -r requirements.txt'
        sh 'pwd'
      }
    }

    stage('Test') {
      steps {
        sh 'behave --tags=regression --junit --junit-directory .'
      }
    }

    stage('Reporting') {
      steps {
        junit 'TESTS-home_page.xml'
      }
    }

  }
}