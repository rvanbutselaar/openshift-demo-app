# openshift-demo-app

Demo Python applicatie om te deployen in OpenShift met S2I

Ga naar de "Developer" interface van OpenShift 4 en klik op "+Add" en kies voor "From Git" en vul de onderstaande informatie in.

Je kan er ook voor kiezen om je eigen demo applicatie uit te rollen.

* Git url: <https://github.com/rvanbutselaar/openshift-demo-app.git>
* Git Reference: "main" voor nieuwe git repositories en "master" voor oude
* Builder image: python
* Application name: openshift-demo-app
* Name: openshift-demo-app
* Resources: DeploymentConfig
* Advanced: create route
* Readiness & Liveness probe: /health
* Resource Limit:
  * cpu request: 10
  * cpu limit: 500
  * memory request: 30
  * memory limit: 250
* Deployment:
  * Auto deploy when new image is available
  * Auto deploy when deployment configuration changes
* Build configuration:
  * Configure a webhook build trigger
  * Automatically build a new image when the builder image changes
  * Launch the first build when the build configuration is created


## https

kubernetes.io/tls-acme: true als annotatie toevoegen aan de route

## env vars

Open DeploymentConfig en maak een env var aan met key NAAM

## memory limit

## cpu limit

## github webhook laten zien?