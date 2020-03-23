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
        sh 'behave --tags=regression --junit --junit-directory /var/lib/jenkins/workspace/pysel_master'
      }
    }

    stage('Reporting') {
      steps {
        junit 'TESTS-home_page.xml'
      }
    }

  }
}
