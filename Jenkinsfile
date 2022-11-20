pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('MariamDghaim')
	}

	stages {

		stage('Build') {

			steps {
				sh 'sudo docker build -t MariamDghaim/Docker-Final-task:latest .'
			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'sudo docker push MariamDghaim/Docker-Final-task:latest'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}
