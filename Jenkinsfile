pipeline{
	
	//run the job on any of the available nodes
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
       // only triggered when blue or green sign
       success {
           slackSend color: "good", message: "Image has been built and sent!"
       }
       
       failure {
          slackSend color: "danger", message: "Failed"
       }
       // trigger every-works
       always {
           slackSend color: "normal", message: "Job done"
	       sh 'docker logout'
       }
    }

}
