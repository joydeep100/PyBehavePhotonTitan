pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'pip3.8 install -r requirements.txt'
      }
    }

    stage('Test') {
      steps {
        sh 'behave --tags=regression --junit'
      }
    }

    stage('Reporting') {
      steps {
        junit '/home/joydeep/pysel/reports/TESTS-home_page.xml'
      }
    }

  }
}
