# openshift-demo-app

Demo Python applicatie om te deployen in OpenShift met S2I

## Uitrollen in OpenShift

Ga naar de "Developer" interface van OpenShift 4 en klik op "+Add" en kies voor "From Git" en vul de onderstaande informatie in.

Je kan er natuurlijk ook voor kiezen om je eigen Java, Go, Node.js of Python applicatie uit te rollen.
Hiervoor heb je een publieke Git repo nodig, met optioneel een Dockerfile.

* Git url: <https://github.com/rvanbutselaar/openshift-demo-app.git>
* Git Reference: "main" voor nieuwe git repositories en "master" voor oudere
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

## ConfigMap



Ga naar de "Developer" interface van OpenShift 4 en klik op "+Add" en kies voor "YAML".
Plak onderstaande YAML en klik op Create om een ConfigMap aan te maken.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: config
data:
  app.properties: |-
    property1=value1
    property2=value2
    property3=value3
```

Pas vervolgens de DeploymentConfig (DC) aan, plak onderstaande net boven `restartPolicy` (let op de indent)!

```yaml
      volumeMounts:
      - name: config-volume
        mountPath: /etc/config
  volumes:
    - name: config-volume
      configMap:
        name: config
```

Meer info: <https://docs.openshift.com/container-platform/4.6/builds/builds-configmaps.html>

## Secret

Maak de secret aan op basis van de onderstaande YAML.

```yaml
kind: Secret
apiVersion: v1
metadata:
  name: secret
data:
  password: V2Vsa29tMDE=
type: Opaque
```

En pas de DeploymentConfig (DC) aan, onder de bestaande `volumeMounts` en `volumes`.

```yaml
      volumeMounts:
      - name: secret-volume
        mountPath: /etc/secret
  volumes:
    - name: secret-volume
      secret:
        secretName: secret
```

Meer info: <https://docs.openshift.com/container-platform/4.6/nodes/pods/nodes-pods-secrets.html>

## https

Https via Let's encrypt.

Open de Route en voeg de volgende annotatie toe:

* KEY: kubernetes.io/tls-acme:
* VALUE: true

Vervolgens maakt de Let's Encrypt controller op het Apollo platform automatisch een certificaat aan op de route.

## Environment vars

Open de DeploymentConfig en ga naar Environment.
Hier kan je environment vars toevoegen op basis van key/value, maar ook op basis van een ConfigMap of Secret.

## Memory request / limit

Zorgt ervoor dat OpenShift weet wat je applicatie minimaal nodig heeft om goed te functioneren, op basis van deze info komt een Pod wel of niet op een bepaalde node terecht.
En zorgt er ook voor dat je applicatie niet teveel geheugen gaat gebruiken.

Open de DeploymentConfig en ga naar YAML om dit te bekijken en aan ta passen.

## CPU request / limit

Zorgt ervoor dat OpenShift weet wat je applicatie minimaal nodig heeft om goed te functioneren, op basis van deze info komt een Pod wel of niet op een bepaalde node terecht.
En zorgt er ook voor dat je applicatie niet teveel CPU gaat gebruiken.

Open de DeploymentConfig en ga naar YAML om dit te bekijken en aan ta passen.

## Health Checks

Hiermee kan OpenShift monitoren of je applicatie nog werkt en of die klaar is om gebruikers/verkeer te ontvangen.

Open de DeploymentConfig en klik op Actions -> Edit Health Checks.

Meer info: <https://docs.openshift.com/container-platform/4.6/applications/application-health.html>

## Replicas

Standaard draait er maar een Pod, waardoor je applicatie tijdelijk onbereikbaar is als er problemen zijn met de onderliggende node.
Draai daarom je DeploymentConfig in productie altijd met minimaal 2 replica's om dit te voorkomen.

Ga naar de DeploymentConfig en klik op Actions -> Edit Pod Count.
