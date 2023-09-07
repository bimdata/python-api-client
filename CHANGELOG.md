# Changelog

<!--next-version-placeholder-->

## v9.19.1 (2023-09-07)
### Fix
* Add history_count to document serialization and prefetch stuff ([`261a2e6`](https://github.com/bimdata/python-api-client/commit/261a2e6cf557e73cfd2d3f993fbff37866f396e5))

## v9.19.0 (2023-09-07)
### Feature
* Add SSO create user route(#674)

* create-user route

* email_impersonation in project access token ([`93f86a5`](https://github.com/bimdata/python-api-client/commit/93f86a5d04193e0c6361d9cfee461f4091d59416))

## v9.18.2 (2023-09-06)
### Fix
* Add document history count (#681)

* add document history count

* typo fixe ([`a2f63e3`](https://github.com/bimdata/python-api-client/commit/a2f63e3ce5f5f74e4424ed7f8d33540a322ac5e3))

## v9.18.1 (2023-09-01)
### Fix
* Fix bcf excel export documentation ([`4054f7c`](https://github.com/bimdata/python-api-client/commit/4054f7c0aba4a707528736a9dee98c2c14933727))

## v9.18.0 (2023-08-30)
### Feature
* Add xlsx export (#676)

* action xlsx export

* black

* add documentation

* add BIMData logo

* poetry update

---------

Co-authored-by: Amoki <hugo@bimdata.io> ([`953ab41`](https://github.com/bimdata/python-api-client/commit/953ab414de0dcec8e23237bb0da99251b4041aa9))

## v9.17.0 (2023-08-30)
### Feature
* Feat(organization): add main_model field to Project model ([`391aa88`](https://github.com/bimdata/python-api-client/commit/391aa888082ac451c6fd742b167a58eb567dfaad))

## v9.16.1 (2023-08-24)
### Fix
* Add z field to geometryPoint ([`0fc0507`](https://github.com/bimdata/python-api-client/commit/0fc05073daec5f8d22a2a237a5ddf79856f3118c))

## v9.16.0 (2023-08-09)
### Feature
* Add space geometry (#672)

* add space geometry

* restor deleted code line ([`0670d25`](https://github.com/bimdata/python-api-client/commit/0670d25901e4923b1d65fdbca2249a8a5bf11597))

## v9.15.1 (2023-07-07)
### Fix
* Add head_id field to Document serializer ([#669](https://github.com/bimdata/python-api-client/issues/669)) ([`02c7125`](https://github.com/bimdata/python-api-client/commit/02c71259431aa17f56c50fafe8ecef2e61702860))

## v9.15.0 (2023-06-22)
### Feature
* Import from project route (#664)

* feat: clone project route

* renaming route, reverse pk and project_id

* renaming

* simpler help text ([`7e45889`](https://github.com/bimdata/python-api-client/commit/7e4588908ae01e5763e65058eccdf7852a2180da))

## v9.14.0 (2023-06-20)
### Feature
* Add pins routes (#663)

* WIP: add pins detail views

* fix view and add tests ([`8ad8d81`](https://github.com/bimdata/python-api-client/commit/8ad8d81e62fd9c2f9083a4bc6c4908fed4f4aac3))

## v9.13.1 (2023-06-15)
### Fix
* Add parent_id field in model ([`7ec69f0`](https://github.com/bimdata/python-api-client/commit/7ec69f034ceaa5620ef3a68b254375d832be3ee7))

## v9.13.0 (2023-06-05)
### Feature
* Add project description ([#659](https://github.com/bimdata/python-api-client/issues/659)) ([`7d29aa4`](https://github.com/bimdata/python-api-client/commit/7d29aa46f1839229a97cb06c517d9a40315b965c))

## v9.12.0 (2023-05-17)
### Feature
* Add xkt_files fields to support many xtk versions (#647)

* add xkt_files fields to support many xtk versions

* fix xkt_file serialization, add admin, migrate data to XktFile

* add unique xkt version constraint ([`1b3009c`](https://github.com/bimdata/python-api-client/commit/1b3009c81b2e5e3a189ed61e34345885803a83f2))

## v9.11.3 (2023-05-16)
### Fix
* Add filters to getRawElements and getSimpleElements ([`1bf3b71`](https://github.com/bimdata/python-api-client/commit/1bf3b7188e48b5697cbd008bbbd41ac198fcbd16))

## v9.11.2 (2023-04-26)
### Fix
* Allow null cloud serializer + add sub field to userproject ([#643](https://github.com/bimdata/python-api-client/issues/643)) ([`8d8ad1c`](https://github.com/bimdata/python-api-client/commit/8d8ad1c438519e2a63f5d8cef203f9ecd27042a0))

## v9.11.1 (2023-04-26)
### Fix
* Add office_preview to dms-tree serializer ([`4afbee7`](https://github.com/bimdata/python-api-client/commit/4afbee7f7205b8fd767aab0abf376b60b8e515cc))

## v9.11.0 (2023-04-25)
### Feature
* Add document-preview (#642)

* add document-preview

* add admin reprocess

* rename field ([`ce78abd`](https://github.com/bimdata/python-api-client/commit/ce78abdfe55727155d5c94ce9b73ea9d1db56023))

## v9.10.7 (2023-04-20)
### Fix
* Feat/permission explicit propagate (#636)

* add delete permission route, remove signals implicit propagation

* explicit propagation for permissions

* remove useless tests

* fix nested group folder serializer

* include delete groupFolder in update route ([`5eca95a`](https://github.com/bimdata/python-api-client/commit/5eca95ae72a16146fd80159b081749529464f728))

## v9.10.6 (2023-04-18)
### Fix
* Fix ordering pdf pages ([#638](https://github.com/bimdata/python-api-client/issues/638)) ([`1f9ffe8`](https://github.com/bimdata/python-api-client/commit/1f9ffe8da45895f1262475ea73d3ddee52a75eaa))

## v9.10.5 (2023-04-17)
### Fix
* Add id field to Pin ([`395d86c`](https://github.com/bimdata/python-api-client/commit/395d86c06bef50cc68b9e5f440f059addd8c5678))

## v9.10.4 (2023-03-09)
### Fix
* Fix requestBody on simple delete route ([`ece7509`](https://github.com/bimdata/python-api-client/commit/ece7509ed7e31a24ef3347245bfd7f9331f1f8fe))

## v9.10.3 (2023-03-02)
### Fix
* Add model.binary_2d_file field ([`4bd519d`](https://github.com/bimdata/python-api-client/commit/4bd519d8a800557f2ba434d5a43a0a4f6c6273a9))

## v9.10.2 (2023-02-06)
### Fix
* Remove some useless field on dms-tree ([`035c4e4`](https://github.com/bimdata/python-api-client/commit/035c4e4e7f63f75ffd9acc69478ba4265133a096))

## v9.10.1 (2023-01-27)
### Fix
* Force request body on delete method with drf-spectacular ([#615](https://github.com/bimdata/python-api-client/issues/615)) ([`206ee31`](https://github.com/bimdata/python-api-client/commit/206ee31fdd0ade562478a39ba5f7d1caa2ae0991))

## v9.10.0 (2023-01-16)
### Feature
* Add marketplace app links ([#609](https://github.com/bimdata/python-api-client/issues/609)) ([`c28d8c1`](https://github.com/bimdata/python-api-client/commit/c28d8c161d7341866d8bf3ed6afba861bba0c0e2))

## v9.9.0 (2023-01-05)
### Feature
* Remove folder groups and history fields form DMS-Tree(#599)

* optimize some routes and remove group_permissions from dms-tree

* add more tests

* remove history from dms-tree

* typo

* fix documentation

* restore features prefetch

* remove useless prefetch

* fix prefetch

* remove useless prefetch ([`9edfcb5`](https://github.com/bimdata/python-api-client/commit/9edfcb5c93767b5d10776adeb3047a0013b1707e))

## v9.8.1 (2022-12-20)
### Fix
* Feat/multipage pdf (#596)

* create multipage-pdf

* fix create_model tests

* fix tests

* add explicit comment to signal function

* update help_text for parent and children ([`0eaaff0`](https://github.com/bimdata/python-api-client/commit/0eaaff0c974a843dc80316c30af6059a4870737e))

## v9.8.0 (2022-12-20)
### Feature
* Create import group from ids (#595)

* feat: create import group from id

* remove UserProject property, add select_related to userprojects queryset

* import several groups from a project instead of one ([`b0459fd`](https://github.com/bimdata/python-api-client/commit/b0459fdd1f71ee919cc1963f0c82b5a51b145451))

## v9.7.0 (2022-12-06)
### Feature
* Add project check access route(#561)

* Add projcte check-access route

* add route description

* update tests with new invitation routes ([`bfb2c05`](https://github.com/bimdata/python-api-client/commit/bfb2c05b2e5ac3247f359ad45006f95b54b43037))

## v9.6.12 (2022-11-30)
### Fix
* Fix model export doc response ([`aa8fbfd`](https://github.com/bimdata/python-api-client/commit/aa8fbfd7a717ba3a5d1c2074effd81ea07b43d18))

## v9.6.11 (2022-11-16)
### Fix
* Added missing value (client name) to User Invitation Serializer ([#590](https://github.com/bimdata/python-api-client/issues/590)) ([`19b7898`](https://github.com/bimdata/python-api-client/commit/19b78982253fe658aa0008866a6fab0bbc58d448))

## v9.6.10 (2022-11-09)
### Fix
* Create DMS Tree return same datas as the get route ([#587](https://github.com/bimdata/python-api-client/issues/587)) ([`8ec4ab1`](https://github.com/bimdata/python-api-client/commit/8ec4ab1be66e53ff4d49c782867b8bed5d557058))

## v9.6.9 (2022-11-09)
### Fix
* Create DMS Tree return same datas as the get route ([#587](https://github.com/bimdata/python-api-client/issues/587)) ([`5bd84de`](https://github.com/bimdata/python-api-client/commit/5bd84de4148c2c19adcff8a8f5acc9d4ff55a2d8))

## v9.6.8 (2022-11-07)
### Fix
* Fix model deserialization ([`623b8f6`](https://github.com/bimdata/python-api-client/commit/623b8f6234b83b65e312e609d6513f13a5c15171))

## v9.6.7 (2022-10-21)
### Fix
* Rename model 360 field (#576)

* rename model 360 field

* keep viewer_360_file field

* remove useless field in write only serializer ([`8de9eae`](https://github.com/bimdata/python-api-client/commit/8de9eaebf5e2991649ccd08332b37ce6db8fac8c))

## v9.6.6 (2022-10-18)
### Fix
* Rename request param in patch user cloud ([#572](https://github.com/bimdata/python-api-client/issues/572)) ([`2907dd6`](https://github.com/bimdata/python-api-client/commit/2907dd671f669f95d72ae0bb34e3d611ebdeacb4))

## v9.6.5 (2022-10-11)
### Fix
* Fix bad body serializer linkDocumentsOfElement ([`81cff13`](https://github.com/bimdata/python-api-client/commit/81cff13e6c4e8b35db22a022735e269d828b749c))

## v9.6.4 (2022-10-10)
### Fix
* Fix #536 body in linkDocumentsOfElement ([`01b3da8`](https://github.com/bimdata/python-api-client/commit/01b3da8507448e88b30946aaf5911475aabffad9))

## v9.6.3 (2022-10-07)
### Fix
* Created_at and responded_at in Invitation model (#570)

* created_at and updated_at in Invitation model

* invitation: manual responded_at field ([`dc7063d`](https://github.com/bimdata/python-api-client/commit/dc7063dac2b4d3f6839d12248b708eb4d0b54a06))

## v9.6.2 (2022-10-07)
### Fix
* Cloud_id and project_id in Invitation serializer ([`d7315c0`](https://github.com/bimdata/python-api-client/commit/d7315c0b017a7f475bc79b960feb5d31b73a14e0))

## v9.6.1 (2022-10-06)
### Fix
* Update fields of userInvitation serializer ([`88f7294`](https://github.com/bimdata/python-api-client/commit/88f7294512206fef11de7cce399d3c6e56344fa6))

## v9.6.0 (2022-10-06)
### Feature
* User invitation routes  (#569)

* make invitation api updatable

* add user:write scope

* use many to many scopes in views and tests

* set scopes in MarketplaceAppAuthorization view ([`2f7d1d4`](https://github.com/bimdata/python-api-client/commit/2f7d1d45f528616b5b5921d06fec8cd36be2ca83))

## v9.5.0 (2022-09-14)
### Feature
* Point cloud ([`5f4bd06`](https://github.com/bimdata/python-api-client/commit/5f4bd06b2a5603b59130f8fc4037a9960c7287ac))

## v9.4.9 (2022-09-09)
### Fix
* Allow empty file on document upload ([`32585b1`](https://github.com/bimdata/python-api-client/commit/32585b1ed8aeef00f45cae6efa8fae0ad51e5c54))

## v9.4.8 (2022-09-07)
### Fix
* Allow empty files ([`c191c95`](https://github.com/bimdata/python-api-client/commit/c191c958362b0f2cf4d66232e592f683f6378c55))

## v9.4.7 (2022-08-29)
### Fix
* Fix/inline serializer fields (#560)

Fix CreateStoreyPlan and BuildingStoreyPlan ([`6b706ce`](https://github.com/bimdata/python-api-client/commit/6b706ce71d28225513dd83a52e9f9e232f8fa00f))

## v9.4.6 (2022-08-09)
### Fix
* Fix project access token enum ([#555](https://github.com/bimdata/python-api-client/issues/555)) ([`1005bc4`](https://github.com/bimdata/python-api-client/commit/1005bc47ee0d8369a8ffbc0b98a532aff4c2b812))

## v9.4.5 (2022-08-03)
### Fix
* Add response data to create DMSTree ([`66c3969`](https://github.com/bimdata/python-api-client/commit/66c3969287fe9de08f80a5d60cb9b4bef702ae3d))

## v9.4.4 (2022-06-24)
### Fix
* Add authoring viewpoint fields ([#547](https://github.com/bimdata/python-api-client/issues/547)) ([`5d0a18b`](https://github.com/bimdata/python-api-client/commit/5d0a18b4752fb192b0d8023677099794cc4c77e7))

## v9.4.3 (2022-06-22)
### Fix
* Fix get-dms-tree serializer ([`ce53acf`](https://github.com/bimdata/python-api-client/commit/ce53acff6a0c3977f1c71c2e73c25b054b60dde1))

## v9.4.2 (2022-06-22)
### Fix
* Fix create-dsm-tree serializer ([`9f58aae`](https://github.com/bimdata/python-api-client/commit/9f58aae36e98cd7aa7cf5f5538c0645af99f4c50))

## v9.4.1 (2022-06-16)
### Fix
* Improve viewpoint pins ([#543](https://github.com/bimdata/python-api-client/issues/543)) ([`7a42412`](https://github.com/bimdata/python-api-client/commit/7a424129ec9ec62252018a17476afcffe01c1acb))

## v9.4.0 (2022-06-09)
### Feature
* Add BCF authoring tool ([#540](https://github.com/bimdata/python-api-client/issues/540)) ([`f8da5ba`](https://github.com/bimdata/python-api-client/commit/f8da5ba89f43f67cba93336c5031849ba0acdcd5))

## v9.3.10 (2022-05-13)
### Fix
* Fix create dms tree doc, children was missing in serializer request (#531)

* fix create dms tree doc, children was missing in serializer request

* rename serializer ([`f734b1b`](https://github.com/bimdata/python-api-client/commit/f734b1b19270e293610b98951ebe44d098718001))

## v9.3.9 (2022-05-12)
### Fix
* Add tag to document in dms-tree ([#533](https://github.com/bimdata/python-api-client/issues/533)) ([`4ffe2ea`](https://github.com/bimdata/python-api-client/commit/4ffe2ea7d309477ebf5305b4b80ae6d3f47ea3fd))

## v9.3.8 (2022-05-10)
### Fix
* Versioning: more permissive archi ([#528](https://github.com/bimdata/python-api-client/issues/528)) ([`4cb18fd`](https://github.com/bimdata/python-api-client/commit/4cb18fdbc2ebf3de4de3e82c183ff5f43c80a929))

## v9.3.7 (2022-05-05)
### Fix
* Rename operation_id ([`e04c180`](https://github.com/bimdata/python-api-client/commit/e04c180145e8ab619657a38b6c3a59c4eb13b1eb))

## v9.3.6 (2022-05-05)
### Fix
* Delete all document version on delete (#525)

* delete all document version on delete

* versioning: add delete history route ([`9aa819b`](https://github.com/bimdata/python-api-client/commit/9aa819bd370259e21f61686a2903f34069bcaada))

## v9.3.5 (2022-05-04)
### Fix
* Add document_id to visa serializer ([`2ec598a`](https://github.com/bimdata/python-api-client/commit/2ec598a2b1bdc0ebdf270e7c74df463327a2db28))

## v9.3.4 (2022-05-04)
### Fix
* Visa serialization in document (#522)

* visa serialization in document

* no prefetch tag ([`213c4d7`](https://github.com/bimdata/python-api-client/commit/213c4d7141e9c5c8fc00d80e21739d1dfa2f8bf8))

## v9.3.3 (2022-05-03)
### Fix
* Reorder document history ([`c1afe9e`](https://github.com/bimdata/python-api-client/commit/c1afe9ea010a61da0ed2d0c0c7e43437e56bd311))

## v9.3.2 (2022-05-02)
### Fix
* Serialize document creator ([`cb1f35c`](https://github.com/bimdata/python-api-client/commit/cb1f35c2348a89acb7f8f0b3d47ff5d86e4eb80b))

## v9.3.1 (2022-04-29)
### Fix
* Remove parent from document serialization ([#521](https://github.com/bimdata/python-api-client/issues/521)) ([`fbc5445`](https://github.com/bimdata/python-api-client/commit/fbc544512b74cc852b2b6f155cb2b62b79122289))

## v9.3.0 (2022-04-29)
### Feature
* Feat/versionning (#517)

* add model, migrations, views, serializers

* test DocumentHistory view

* fix last tests

* filter list model

* fix migration and add reverse_code

* renaming old_version_id ([`d562d95`](https://github.com/bimdata/python-api-client/commit/d562d9583f76b61f0f6ddf97ec80150a6fd6b902))

## v9.2.0 (2022-04-21)
### Feature
* Add bcf pins (#515)

* add bcf pins

* add view tests ([`8948499`](https://github.com/bimdata/python-api-client/commit/8948499b4f427735081404a23b9c68fe2f1b12d4))

## v9.1.1 (2022-04-20)
### Fix
* Fix createDocument response missing ([`a7a4208`](https://github.com/bimdata/python-api-client/commit/a7a4208fa4163eb55e82628a570e743e217b85c3))

## v9.1.0 (2022-04-15)
### Feature
* Create document tag views (#513)

* create document tag views

* fix: serializer readOnly

* add admin tags

* add inline Tag Project ([`3c00f75`](https://github.com/bimdata/python-api-client/commit/3c00f752a14f58a4fc38ed9a3ff03ba54e005580))

## v9.0.0 (2022-04-12)
### Fix
* Fix swagger generation ([`3952685`](https://github.com/bimdata/python-api-client/commit/3952685f9c92059b94605b178693de95cd670f1d))

### Breaking
* Feat/openapi3 (#508)

* install and pre configure drf-spectacular

* finish replace drf-yasg lib by drf-spectacular

* fix error on lib generation

* recreate data for oauth delete tests

* fix some typo

* fix null enums

* fix some serializer

* add bearer auth to swagger

* add test operationId and fix numquery MPApp test

* fix head action in test doc

Co-authored-by: Amoki <hugo@bimdata.io> ([`57074b7`](https://github.com/bimdata/python-api-client/commit/57074b73f37e92e1ee0b37cdfde59b3ccd7bdd80))
* Feat/openapi3 (#508)

* install and pre configure drf-spectacular

* finish replace drf-yasg lib by drf-spectacular

* fix error on lib generation

* recreate data for oauth delete tests

* fix some typo

* fix null enums

* fix some serializer

* add bearer auth to swagger

* add test operationId and fix numquery MPApp test

* fix head action in test doc

Co-authored-by: Amoki <hugo@bimdata.io> ([`57074b7`](https://github.com/bimdata/python-api-client/commit/57074b73f37e92e1ee0b37cdfde59b3ccd7bdd80))

## v8.0.0 (2022-04-12)
### Breaking
* Feat/openapi3 (#508)

* install and pre configure drf-spectacular

* finish replace drf-yasg lib by drf-spectacular

* fix error on lib generation

* recreate data for oauth delete tests

* fix some typo

* fix null enums

* fix some serializer

* add bearer auth to swagger

* add test operationId and fix numquery MPApp test

* fix head action in test doc

Co-authored-by: Amoki <hugo@bimdata.io> ([`18591ec`](https://github.com/bimdata/python-api-client/commit/18591ec7c8156e00549d7d604500a0773b79463a))
* Feat/openapi3 (#508)

* install and pre configure drf-spectacular

* finish replace drf-yasg lib by drf-spectacular

* fix error on lib generation

* recreate data for oauth delete tests

* fix some typo

* fix null enums

* fix some serializer

* add bearer auth to swagger

* add test operationId and fix numquery MPApp test

* fix head action in test doc

Co-authored-by: Amoki <hugo@bimdata.io> ([`18591ec`](https://github.com/bimdata/python-api-client/commit/18591ec7c8156e00549d7d604500a0773b79463a))

## v7.4.2 (2022-03-17)
### Fix
* Remove comment visa nested ([#502](https://github.com/bimdata/python-api-client/issues/502)) ([`a516af8`](https://github.com/bimdata/python-api-client/commit/a516af86ac3aa3ef6858f1b75c7f36e182bf7c45))

## v7.4.1 (2022-02-25)
### Fix
* Fix create building and storey doc serializer ([`03903e7`](https://github.com/bimdata/python-api-client/commit/03903e7c077a08434ad587401dc691c5e2c8b646))

## v7.4.0 (2022-02-25)
### Feature
* Order plans in storey (#495)

* init refacto storey

* add building test

* fix serializers

* replace Counter

* init refacto storey

* order plans in storey

* merge migration ifc/88_

* fix bad merge

* fix bad merge ([`ea3cf1d`](https://github.com/bimdata/python-api-client/commit/ea3cf1d3fc82b9baa09a5536cde76e1f2cfcfc9c))

## v7.3.0 (2022-02-25)
### Feature
* Refacto storeys and add buildings (#494)

* init refacto storey

* add building test

* fix serializers

* replace Counter ([`06a735c`](https://github.com/bimdata/python-api-client/commit/06a735c75412fdfb301f7e10ecb29a5e4275afe7))

## v7.2.0 (2022-02-24)
### Feature
* Add size_ratio fields ([`2a5d90c`](https://github.com/bimdata/python-api-client/commit/2a5d90c51c5de429d10d6cf1f4d5da9da5448093))

## v7.1.2 (2022-02-24)
### Fix
* Bcf detailed extensions labels ([`7d5ade7`](https://github.com/bimdata/python-api-client/commit/7d5ade750437b1e5007c4434fdaabfd1c54d9dc9))

## v7.1.1 (2022-02-23)
### Fix
* Add creadted_at and upated_at to Propertie et PropertySet ([`9218cd7`](https://github.com/bimdata/python-api-client/commit/9218cd7ae22192003e0e09017565940604bff67c))

## v7.1.0 (2022-02-15)
### Feature
* Feature/bcf colors (#485)

* wip

* update project extensions GET method

* cleanup

* fix project extensions

* implement extension update

* add color to all existing topics

* respond with 400 if duplicated name

* remove useless config ([`64b5792`](https://github.com/bimdata/python-api-client/commit/64b579260b41558e0c959ba65dcbfe159d57fcf0))

## v7.0.1 (2022-02-15)
### Fix
* Rename last ifc operations ([#489](https://github.com/bimdata/python-api-client/issues/489)) ([`6a0bce1`](https://github.com/bimdata/python-api-client/commit/6a0bce138e8adad44c462cec339d523fc33cc346))

## v7.0.0 (2022-02-04)
### Breaking
* Rename ifc to model (#477)

* filter storey models with permissions

* duplicate ifc routes and update tags ViewSet

* add deprecated ifc views and filter by type

* rename ifc operations

* rename Ifc table

* rename some Ifc classes

* duplicate ifc test and change reverse url name

* update foreignkeys

* rename ifc_pk in model_pk

* update route name

* update scopes

* fix swagger dupplicate

* fix test projectAccessToken

* actually send keycloak scope create

* restore ifc_guid

* don't unzip unzipped structure files

* fix bad rebase ([`6d48496`](https://github.com/bimdata/python-api-client/commit/6d48496db3d7b9f80e1ffcfe407873046383e516))
* rename ifc to model (#477)

* filter storey models with permissions

* duplicate ifc routes and update tags ViewSet

* add deprecated ifc views and filter by type

* rename ifc operations

* rename Ifc table

* rename some Ifc classes

* duplicate ifc test and change reverse url name

* update foreignkeys

* rename ifc_pk in model_pk

* update route name

* update scopes

* fix swagger dupplicate

* fix test projectAccessToken

* actually send keycloak scope create

* restore ifc_guid

* don't unzip unzipped structure files

* fix bad rebase ([`6d48496`](https://github.com/bimdata/python-api-client/commit/6d48496db3d7b9f80e1ffcfe407873046383e516))

## v6.0.0 (2022-02-04)
### Breaking
* Sync with js libs ([`eb430f5`](https://github.com/bimdata/python-api-client/commit/eb430f5f2a77313a510db067276c7fe520c28adc))
* sync with js libs ([`eb430f5`](https://github.com/bimdata/python-api-client/commit/eb430f5f2a77313a510db067276c7fe520c28adc))

## v5.22.0 (2022-01-31)
### Feature
* 2d positioning (#471)

* filter storey models with permissions

* rework storey serializer

* add positioning plan to m2m (storey-plan)

* add route with params id and positioning route renaming

* include positioning in storey serializer

* fix tests ([`f8bf0c8`](https://github.com/bimdata/python-api-client/commit/f8bf0c8b641cb613d99d7a116ecd8377fab46245))

## v5.21.1 (2022-01-31)
### Fix
* Filter storey models with permissions and add models_unreachable_count field (#470)

* filter storey models with permissions

* fix test add model to storey

* rework storey serializer ([`b68c55a`](https://github.com/bimdata/python-api-client/commit/b68c55a4665fda225fd205dac533f64d9dca9ee8))

## v5.21.0 (2022-01-31)
### Feature
* Add img_format=url in BCF routes ([#472](https://github.com/bimdata/python-api-client/issues/472)) ([`9cef689`](https://github.com/bimdata/python-api-client/commit/9cef6891bd435d25098035e413489bb6735515c2))

## v5.20.1 (2022-01-28)
### Fix
* One storey site by building (#469)

* one storey site by building

* add db unique constraint

* Update ifc/v1/views.py

Co-authored-by: Hugo Duroux <hugo@bimdata.io>

* Update ifc/v1/views.py

Co-authored-by: Hugo Duroux <hugo@bimdata.io>

Co-authored-by: Hugo Duroux <hugo@bimdata.io> ([`7c907c8`](https://github.com/bimdata/python-api-client/commit/7c907c80cb76328f174e414efb73850ca81dc188))

## v5.20.0 (2022-01-27)
### Feature
* Plans and storeys (#468)

* create storey

* add migrations and route manage model children

* create metabuilding and relation between storey and model-plans

* fix signal test

* PR review

* models can update name ([`6a125d1`](https://github.com/bimdata/python-api-client/commit/6a125d1eebe97eacd063a6ef2001c9057ac57cb2))

## v5.19.1 (2022-01-18)
### Fix
* Add non automatic models (#464)

* Add non automatic models

* improve tests

* rename route and add permissions

* add model delete with doc ([`b224801`](https://github.com/bimdata/python-api-client/commit/b2248010f7890245d90e9b4f067e4ca96ea00a63))

## v5.19.0 (2022-01-14)
### Feature
* Feature/smart files (#463)

* allow many model types

* add tests

* fix document name

* more cleanup

* update ci poetry version

* do not reprocess on file update

* fix export,merge and optimize queues

* add types.py

* more contants ([`a5ba918`](https://github.com/bimdata/python-api-client/commit/a5ba9187333e0a1b754b49755322102085adacc3))

## v5.18.3 (2022-01-11)
### Fix
* (visa) add validations_in_error to serializer ([`e4df33f`](https://github.com/bimdata/python-api-client/commit/e4df33ffcaf01b3f60f7e214a2a64809d2befcf3))

## v5.18.2 (2022-01-04)
### Fix
* Fix document elements list uuids ([`39de959`](https://github.com/bimdata/python-api-client/commit/39de959c2a58e9ab3b5949542efe76456cd8cad9))

## v5.18.1 (2021-12-22)
### Fix
* Rename element_ids to element_uuids ([`461e3db`](https://github.com/bimdata/python-api-client/commit/461e3db667d2edba71b1596d694185f61d3233b5))

## v5.18.0 (2021-12-22)
### Feature
* Add element/documents route ([`68a02e7`](https://github.com/bimdata/python-api-client/commit/68a02e7d227d78ef2e4efd9bdfbe82b1b686cf89))

## v5.17.1 (2021-12-13)
### Fix
* Add document to visa serializer ([#458](https://github.com/bimdata/python-api-client/issues/458)) ([`7504aee`](https://github.com/bimdata/python-api-client/commit/7504aee678ed033bcbe517ab9fcfe7c54776bfcf))

## v5.17.0 (2021-12-09)
### Feature
* Feature/link element document (#457)

* add documents to elements

* add test for filterred ifc and document list

* typo

* add some query optimizations ([`92814d1`](https://github.com/bimdata/python-api-client/commit/92814d193cd97e2feddbed979806ed702db7301d))

## v5.16.0 (2021-12-06)
### Feature
* Feature/visa (#451)

* add invitation to userProject

* PR changes requests

* init visa

* fix: boolean swagger bad import

* fix: git conflict migrations, replace tests 'put'

* add visa project view and change perform_created method on others views

* fix: duplicate swagger operation id on getComment*

* review PR and add permission mixin actions

* fix tests

* fix swagger

* add nested mixin to self visa project view

* fix creator filter view

* print test

* bypass schrodinger swagger pb

* clean useless db requests in permissions

* restore 404 ifc tests

* add userproject to serializers context ([`a963e5f`](https://github.com/bimdata/python-api-client/commit/a963e5f94af8f3e4d098856adc9253a0cb473252))

## v5.15.2 (2021-12-02)
### Fix
* Add id to Public Organization Serializer ([`5ac3574`](https://github.com/bimdata/python-api-client/commit/5ac357430084e206b40537112334d8de4075f805))

## v5.15.1 (2021-12-02)
### Fix
* Add organization serializer in App and MPApp serializers (#452)

* add organization serializer in App and MPApp serializers

* fix test and add select related

* use Public Organization Serializer ([`b1f0958`](https://github.com/bimdata/python-api-client/commit/b1f0958e511655ca19ddbf52ab35fbb1d1fd1fc2))

## v5.15.0 (2021-11-24)
### Feature
* Remove deprecated and put (#450)

* remove deprecated route and PUT route without BCF routes

* fix some tests

* fix last tests and restore project tree route

* restore BCF tests change

* rename fullUpdate operation ([`5769df5`](https://github.com/bimdata/python-api-client/commit/5769df5195f22e65696b4c46ed1a8ee925634526))
* Add leave project route (#449)

* Add leave project route

* fix roles ([`4d52c51`](https://github.com/bimdata/python-api-client/commit/4d52c51628bf3e977074dfec3d8af51615a13c2d))

### Fix
* Fix semantic release ([`aca3560`](https://github.com/bimdata/python-api-client/commit/aca3560c5d69a91d32be6992c0d8aea1153110b4))
* Fix serializer user project (#448)

Breaking Change:
 -  key to  for GroupUser create view
 - Route pk for userProject views is now UserProject pk and not FosUser pk

Some other change:
- fix serializer of userProject for swagger and libs
- add missing invitation user project from project and group
- fix some test ([`8b5446a`](https://github.com/bimdata/python-api-client/commit/8b5446a58252f767665f6cd3fff59af93baddfbd))
* Add invitation key in UserProject ([`30a8fb5`](https://github.com/bimdata/python-api-client/commit/30a8fb5ad88a6aed47de4bcb69a34cd37702e5ff))
* Get cloud size operation id in openapi ([`d508862`](https://github.com/bimdata/python-api-client/commit/d5088627492eec9d1ea02a8915cfb1d7ed4ce09c))
* Fix list/create methods openAPI ([`7519d93`](https://github.com/bimdata/python-api-client/commit/7519d931205caffc57f964e92e0547714d916304))

## v5.14.0 (2021-09-13)
### Feature
* Serialize user-permissions on documents ([`8597421`](https://github.com/bimdata/python-api-client/commit/859742176f6e0827c170dd8d30c95c254d502fcc))
* Add profile_picture field in user serialization

* add user picture field

* fix user.company, add comment about an edge case ([`45bd37c`](https://github.com/bimdata/python-api-client/commit/45bd37ce3e9ead5bb4050fa2a26a609a64e8ac26))
* Add GED permissions ([`00b987a`](https://github.com/bimdata/python-api-client/commit/00b987af3d7f310c07beb9d30c7354b9e5830d26))
* Allow bigger guids ([#420](https://github.com/bimdata/python-api-client/issues/420)) ([`54b2b09`](https://github.com/bimdata/python-api-client/commit/54b2b090cbbf127cf8ac0f17c3492e6d0e1c7f29))

### Fix
* Allow empty name in raw layers and raw materials ([`b96d9a7`](https://github.com/bimdata/python-api-client/commit/b96d9a7eb1e3828fd2b3f7e9edb558b296d38f0b))
* Allow empty name in raw layers and raw materials ([`c0d6bb6`](https://github.com/bimdata/python-api-client/commit/c0d6bb6f662d3289915da48580553bb2277c7ee7))
* Allow empty name in raw layers and raw materials ([`22e450d`](https://github.com/bimdata/python-api-client/commit/22e450d38322621610ca85750524c94dd197f33c))
* Fix dms-tree group permissions ([`38f8ce5`](https://github.com/bimdata/python-api-client/commit/38f8ce5608ad11f8dd1518a9a901da5ef8779bdd))
* Fix field name and add field to children dms-tree ([#426](https://github.com/bimdata/python-api-client/issues/426)) ([`2881af8`](https://github.com/bimdata/python-api-client/commit/2881af81fb7ae5fe2718f8187ffc5ae350aa4ebd))
