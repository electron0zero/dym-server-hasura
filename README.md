# dym-server-hasura

[dym Server](https://github.com/electron0zero/dym-server-hasura) as a Hasura Microservice

[Normal Docker version can be found here](https://github.com/electron0zero/dym-server)

Did you mean(dym) is simple microservice that does spelling correction and word segmentation.
If you combine both you get something similar to Google's `Did you mean` kind of service.

This API Server is using Flask(Python Microframework) & Swagger 2.0(aka Open API)

It has a deployed version(API and [API playground](https://myapp.actualize97.hasura-app.io/v1/ui/)) on hasura, check them out

If you want to learn how this works check these links.

- [How to write a spell corrector](http://norvig.com/spell-correct.html)
- [Peter Norving - How to Do Things with Words](https://github.com/norvig/pytudes/blob/master/ipynb/How%20to%20Do%20Things%20with%20Words.ipynb)

--------------------------------------------
##### Autogenerated stubs

---------------------------------------------

## Files and Directories

The project (a.k.a. project directory) has a particular directory structure and it has to be maintained strictly, else `hasura` cli would not work as expected. A representative project is shown below:

```
.
├── hasura.yaml
├── clusters.yaml
├── conf
│   ├── authorized-keys.yaml
│   ├── auth.yaml
│   ├── ci.yaml
│   ├── domains.yaml
│   ├── filestore.yaml
│   ├── gateway.yaml
│   ├── http-directives.conf
│   ├── notify.yaml
│   ├── postgres.yaml
│   ├── routes.yaml
│   └── session-store.yaml
├── migrations
│   ├── 1504788327_create_table_userprofile.down.yaml
│   ├── 1504788327_create_table_userprofile.down.sql
│   ├── 1504788327_create_table_userprofile.up.yaml
│   └── 1504788327_create_table_userprofile.up.sql
└── microservices 
    ├── adminer
    │   └── k8s.yaml
    └── flask
        ├── src/
        ├── k8s.yaml
        └── Dockerfile
```

### `hasura.yaml`

This file contains some metadata about the project, namely a name, description and some keywords. Also contains `platformVersion` which says which Hasura platform version is compatible with this project.

### `clusters.yaml`

Info about the clusters added to this project can be found in this file. Each cluster is defined by it's name allotted by Hasura. While adding the cluster to the project you are prompted to give an alias, which is just hasura by default. The `kubeContext` mentions the name of kubernetes context used to access the cluster, which is also managed by hasura. The `config` key denotes the location of cluster's metadata on the cluster itself. This information is parsed and cluster's metadata is appended while conf is rendered. `data` key is for holding custom variables that you can define.

```yaml
- name: h34-ambitious93-stg
  alias: hasura
  kubeContext: h34-ambitious93-stg
  config:
    configmap: controller-conf
    namespace: hasura
  data: null  
```
