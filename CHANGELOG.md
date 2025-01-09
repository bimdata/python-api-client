# CHANGELOG


## v10.10.1 (2025-01-09)

### Fix

- Patch: PEP 625
  ([`cdb0b31`](https://github.com/bimdata/python-api-client/commit/cdb0b31e6db22066d2921790366c22b8f900131d))


## v10.10.0 (2025-01-08)

### Feature

- Minor: remove some document fields in model.document serialization
  ([`feb0558`](https://github.com/bimdata/python-api-client/commit/feb05588959dc9ee5c3468019c8681673841fc82))

* improve storey performances

* add comments


## v10.9.3 (2024-11-19)

### Fix

- Patch: remove deprecation warning on semantic-release
  ([`c80f047`](https://github.com/bimdata/python-api-client/commit/c80f0478600802578da09c7ec6ec687a5af84b68))


## v10.9.2 (2024-11-19)

### Fix

- Patch: fix(storey): allow to add photosphere as storey plan + fix process_hint on createDocument
  (#790)
  ([`556b744`](https://github.com/bimdata/python-api-client/commit/556b74415c6ab771fb6a09bc314a5f3764d6b9de))

* fix(storey): allow to add photosphere as storey plan

* fix(storey): create STOREY_CHILD_TYPES list + add 'process_hint' to Docuemnt serializer fields


## v10.9.1 (2024-10-24)

### Fix

- Patch: fix swagger with project children
  ([`f6ec7a8`](https://github.com/bimdata/python-api-client/commit/f6ec7a8583be703eb018ed22686b2da69bd88a8c))


## v10.9.0 (2024-10-24)

### Feature

- Minor: remove sub projects (#782)
  ([`640445c`](https://github.com/bimdata/python-api-client/commit/640445c300a0cb1823c3378191645bbb1ad852e6))


## v10.8.0 (2024-10-23)

### Feature

- Minor: add model layout_name for DWG models (#780)
  ([`e2b806e`](https://github.com/bimdata/python-api-client/commit/e2b806e68bcc0c1d6b9bcbf565e3988057981ff2))


## v10.7.0 (2024-09-16)

### Feature

- Minor: Bcf odata (#772)
  ([`34ee7c9`](https://github.com/bimdata/python-api-client/commit/34ee7c9d3104f9f3a0a6363b40f38b778f900666))

* implement odata filters

* add orderby

* factorize

* replace test domains with bimdata.test


## v10.6.0 (2024-09-16)

### Feature

- Minor: remove smart_data from get_size routes
  ([`250dc2c`](https://github.com/bimdata/python-api-client/commit/250dc2c6409f9bc59cddf88b121cb7c8946e333a))


## v10.5.0 (2024-09-11)

### Feature

- Minor: Feature: Photosphere Model (#758)
  ([`3add6a0`](https://github.com/bimdata/python-api-client/commit/3add6a0633832dcab2db9d9a33baadb7d29945dd))

* MINOR: feat(photosphere): add PHOTOSPHERE model type

* MINOR: feat(photosphere): add create-photosphere route

* MINOR: feat: add create-photospĥere-building route

* fix: IsMetaBuilding perm classes + little opti in create-photosphere route

* fix(ifc): merge 2 migrations into 1


## v10.4.3 (2024-09-09)

### Fix

- Patch: fix storey name open api
  ([`1ec7339`](https://github.com/bimdata/python-api-client/commit/1ec733927e2e879c678c7e24b609c7ec19f0368c))


## v10.4.2 (2024-09-09)

### Fix

- Patch: bimdata_elevation response can be null
  ([`a367be3`](https://github.com/bimdata/python-api-client/commit/a367be3cc9df3248b5ef631872c4d37a8a285f03))


## v10.4.1 (2024-09-09)

### Fix

- Patch: fix bimdata_elevation open api field type
  ([`8ee2be6`](https://github.com/bimdata/python-api-client/commit/8ee2be67d59b7ed18c83da89c02a0d4b2801fb8d))


## v10.4.0 (2024-09-09)

### Feature

- Minor: Bimdata elevation (#770)
  ([`2f61155`](https://github.com/bimdata/python-api-client/commit/2f61155c2c71ceda62ace5b83979fec3c806521d))

* add BIMData Elevation to storey

* add update storey elevation

* fix typo in comment


## v10.3.0 (2024-09-04)

### Feature

- Minor: serialize basic document data in /me/visa responses (#769)
  ([`d145d94`](https://github.com/bimdata/python-api-client/commit/d145d9441ac934aaccb5163bfbf0a63f6218f7f9))

* MINOR: serialize basic document data in /me/visa responses

* fix minor mistakes

* fix parent_id in doc

* fix prefetch


## v10.2.2 (2024-07-30)

### Fix

- Patch: Update ci-requirements.txt
  ([`83e0968`](https://github.com/bimdata/python-api-client/commit/83e0968df4a62af918209ac628a5fd2f3c8028f2))


## v10.2.1 (2024-07-30)

### Fix

- Patch: fix project-access-token nullable fields
  ([`7277533`](https://github.com/bimdata/python-api-client/commit/7277533e82734d36c02bf1f043c66a1cc9f1d427))


## v10.2.0 (2024-07-04)

### Feature

- Minor: Add bcf bimdata_viewer_layout (#759)
  ([`e6e043b`](https://github.com/bimdata/python-api-client/commit/e6e043ba5e7e82aaacd5c77ceb1bbdb524ec8d65))

* Add bcf bimdata_layout

* Rename into bimdata_viewer_layout

* Fix test...


## v10.1.0 (2024-06-20)

### Feature

- Minor: remove bcf project id in response
  ([`0d32ce4`](https://github.com/bimdata/python-api-client/commit/0d32ce4f80873c50d8a1d4125a4770fb8eefd3b7))


## v10.0.0 (2024-05-30)

### Breaking

- Major: chore: remove deprecated ifc routes from doc (#725)
  ([`6556cb8`](https://github.com/bimdata/python-api-client/commit/6556cb84ce89f6ed9f483df48dcd20d253c24ae6))

### Feature

- Minor: Add log for cloud invitations (#746)
  ([`d35212c`](https://github.com/bimdata/python-api-client/commit/d35212c15a9d26e6348f827776cd79b3e75ce526))

* Add cloud invitation logs.

* Add log for canceled invitations.

* Add migration to delete unwanted UserProject.

* Fix typo.

* Better log action naming.

* Fix migration.

* Rename log decorators.

- Minor: Add missing attachment in visa validation serializer. (#726)
  ([`157b488`](https://github.com/bimdata/python-api-client/commit/157b488573349452828fefd97c2b3071a75a1e4d))

- Minor: Feat/add link between zone and storey (#723)
  ([`abe503b`](https://github.com/bimdata/python-api-client/commit/abe503bc8934c2108a389f82057730922148b5a5))

* Add a link between zone and storey.

* Zone-storey, use uuid instead of pk.

* Rename storey as storey_uuid in zone serializer.

* Split update/remove storey from zone test.

- Minor: add logging for documents, folder and user invitations (#712)
  ([`d68b901`](https://github.com/bimdata/python-api-client/commit/d68b90147f5ce18b32b2fe4d80e30e36eeae6aae))

* first implementation with documents

* implement and test documents and folders

* aborted try to test folder permission propagation

* fix test get_path

* add project invitation logs

* improve admin

* typo

* add log view test and scope

* fix check_access test

* commit app migrations

- Minor: Add filters and document and some utility routes (#710)
  ([`1c43bba`](https://github.com/bimdata/python-api-client/commit/1c43bbac2d36f8db99acdb3b320e528c3d43194a))

* add folder:id/document route and visa validation attachment

* add filter on first level

* add document advanced filters and folder-tree route

* remove uselesss unpacking operator

- Minor: add model drawings (#709)
  ([`81c1d8e`](https://github.com/bimdata/python-api-client/commit/81c1d8ee19e118ddb478f92fc36c7803df734acb))

* MINOR: add model drawings

* fix tests

* add admin

- Minor: add user deail to check-access response (#707)
  ([`368656e`](https://github.com/bimdata/python-api-client/commit/368656ed2a9c47df2f232ba3a1a152845c698d28))

### Fix

- Patch: fix openAPI definition of getProjectFolderTree
  ([`ed5e2d5`](https://github.com/bimdata/python-api-client/commit/ed5e2d5c43c24fb2020e7523fe22389ad83cca8e))

- Patch: fix openAPI definition of getProjectFolderTree
  ([`c88cf8e`](https://github.com/bimdata/python-api-client/commit/c88cf8ed9c36093d5879b5d82e4e276c4a6e97df))

- Patch: fix project/folder-tree path
  ([`4ba4d60`](https://github.com/bimdata/python-api-client/commit/4ba4d60c3a8aabce89ff8afeae0508c68b3b579f))

- Patch: test CI
  ([`adc39fc`](https://github.com/bimdata/python-api-client/commit/adc39fc781cdd9a9ed918275b4bff629cb761483))


## v9.22.2 (2023-11-27)

### Fix

- Patch: restore viewpoint patch (#706)
  ([`c2d241f`](https://github.com/bimdata/python-api-client/commit/c2d241f23c68d4ea0e534d3cc5aca6fb990690a2))

* restore viewpoint patch

* use ModelViewSet


## v9.22.1 (2023-11-27)

### Fix

- Patch: forbid to non admin to create topic properties (#705)
  ([`792e47f`](https://github.com/bimdata/python-api-client/commit/792e47f4406fc1c1008f5fe6f44dae5b9bd88f6e))

* forbid to non admin to create topic properties

* remvoe prints

* users and guests can only edit their own BCFs

* remove PUT viewpoint route

* fix import

* code optimization

* remove dead code


## v9.22.0 (2023-10-27)

### Feature

- Minor: add viewpoint models field (#702)
  ([`6f3768c`](https://github.com/bimdata/python-api-client/commit/6f3768c3c8512cb0c4ebd5836220a6e59f1adb65))

* MINOR: add viewpoint models field

* fix typos


## v9.21.1 (2023-10-19)

### Fix

- Patch: add geometry to ZoneSpace
  ([`4832e71`](https://github.com/bimdata/python-api-client/commit/4832e7169cae8ec549053fb17a58a6866c69ca98))


## v9.21.0 (2023-09-25)

### Feature

- Minor: add routes to manage zone_space relations (#690)
  ([`68bc812`](https://github.com/bimdata/python-api-client/commit/68bc81277d1ba297a771ca9fcc2eae6c078c6f34))


## v9.20.2 (2023-09-25)

### Fix

- Patch: zone: parent_id field may be null
  ([`3aec51b`](https://github.com/bimdata/python-api-client/commit/3aec51b2eac56ab36976e05211e1b13ea09ef96a))


## v9.20.1 (2023-09-21)

### Fix

- Patch: add id project to serializer getProjectFolderTreeSerializers
  ([`fbe126b`](https://github.com/bimdata/python-api-client/commit/fbe126ba7320faa09ead023384a7e8b41c5e7a0b))


## v9.20.0 (2023-09-14)

### Feature

- Minor: order in zones and spacezones
  ([`2b6e416`](https://github.com/bimdata/python-api-client/commit/2b6e4160fb3010d6cb2aed943172483e2e551118))


## v9.19.1 (2023-09-07)

### Fix

- Patch: add history_count to document serialization and prefetch stuff
  ([`261a2e6`](https://github.com/bimdata/python-api-client/commit/261a2e6cf557e73cfd2d3f993fbff37866f396e5))


## v9.19.0 (2023-09-07)

### Feature

- Minor: Add SSO create user route(#674)
  ([`93f86a5`](https://github.com/bimdata/python-api-client/commit/93f86a5d04193e0c6361d9cfee461f4091d59416))

* create-user route

* email_impersonation in project access token


## v9.18.2 (2023-09-06)

### Fix

- Patch: Add document history count (#681)
  ([`a2f63e3`](https://github.com/bimdata/python-api-client/commit/a2f63e3ce5f5f74e4424ed7f8d33540a322ac5e3))

* add document history count

* typo fixe


## v9.18.1 (2023-09-01)

### Fix

- Patch: fix bcf excel export documentation
  ([`4054f7c`](https://github.com/bimdata/python-api-client/commit/4054f7c0aba4a707528736a9dee98c2c14933727))


## v9.18.0 (2023-08-30)

### Feature

- Minor: Add xlsx export (#676)
  ([`953ab41`](https://github.com/bimdata/python-api-client/commit/953ab414de0dcec8e23237bb0da99251b4041aa9))

* action xlsx export

* black

* add documentation

* add BIMData logo

* poetry update

---------

Co-authored-by: Amoki <hugo@bimdata.io>


## v9.17.0 (2023-08-30)

### Feature

- Minor: feat(organization): add main_model field to Project model
  ([`391aa88`](https://github.com/bimdata/python-api-client/commit/391aa888082ac451c6fd742b167a58eb567dfaad))


## v9.16.1 (2023-08-24)

### Fix

- Patch: add z field to geometryPoint
  ([`0fc0507`](https://github.com/bimdata/python-api-client/commit/0fc05073daec5f8d22a2a237a5ddf79856f3118c))


## v9.16.0 (2023-08-09)

### Feature

- Minor: add space geometry (#672)
  ([`0670d25`](https://github.com/bimdata/python-api-client/commit/0670d25901e4923b1d65fdbca2249a8a5bf11597))

* add space geometry

* restor deleted code line


## v9.15.1 (2023-07-07)

### Fix

- Patch: add head_id field to Document serializer (#669)
  ([`02c7125`](https://github.com/bimdata/python-api-client/commit/02c71259431aa17f56c50fafe8ecef2e61702860))


## v9.15.0 (2023-06-22)

### Feature

- Minor: import from project route (#664)
  ([`7e45889`](https://github.com/bimdata/python-api-client/commit/7e4588908ae01e5763e65058eccdf7852a2180da))

* feat: clone project route

* renaming route, reverse pk and project_id

* renaming

* simpler help text


## v9.14.0 (2023-06-20)

### Feature

- Minor: Add pins routes (#663)
  ([`8ad8d81`](https://github.com/bimdata/python-api-client/commit/8ad8d81e62fd9c2f9083a4bc6c4908fed4f4aac3))

* WIP: add pins detail views

* fix view and add tests


## v9.13.1 (2023-06-15)

### Fix

- Patch: add parent_id field in model
  ([`7ec69f0`](https://github.com/bimdata/python-api-client/commit/7ec69f034ceaa5620ef3a68b254375d832be3ee7))


## v9.13.0 (2023-06-05)

### Feature

- Minor: add project description (#659)
  ([`7d29aa4`](https://github.com/bimdata/python-api-client/commit/7d29aa46f1839229a97cb06c517d9a40315b965c))


## v9.12.0 (2023-05-17)

### Feature

- Minor: add xkt_files fields to support many xtk versions (#647)
  ([`1b3009c`](https://github.com/bimdata/python-api-client/commit/1b3009c81b2e5e3a189ed61e34345885803a83f2))

* add xkt_files fields to support many xtk versions

* fix xkt_file serialization, add admin, migrate data to XktFile

* add unique xkt version constraint


## v9.11.3 (2023-05-16)

### Fix

- Patch: add filters to getRawElements and getSimpleElements
  ([`1bf3b71`](https://github.com/bimdata/python-api-client/commit/1bf3b7188e48b5697cbd008bbbd41ac198fcbd16))


## v9.11.2 (2023-04-26)

### Fix

- Patch: allow null cloud serializer + add sub field to userproject (#643)
  ([`8d8ad1c`](https://github.com/bimdata/python-api-client/commit/8d8ad1c438519e2a63f5d8cef203f9ecd27042a0))


## v9.11.1 (2023-04-26)

### Fix

- Patch: add office_preview to dms-tree serializer
  ([`4afbee7`](https://github.com/bimdata/python-api-client/commit/4afbee7f7205b8fd767aab0abf376b60b8e515cc))


## v9.11.0 (2023-04-25)

### Feature

- Minor: add document-preview (#642)
  ([`ce78abd`](https://github.com/bimdata/python-api-client/commit/ce78abdfe55727155d5c94ce9b73ea9d1db56023))

* add document-preview

* add admin reprocess

* rename field


## v9.10.7 (2023-04-20)

### Fix

- Patch: Feat/permission explicit propagate (#636)
  ([`5eca95a`](https://github.com/bimdata/python-api-client/commit/5eca95ae72a16146fd80159b081749529464f728))

* add delete permission route, remove signals implicit propagation

* explicit propagation for permissions

* remove useless tests

* fix nested group folder serializer

* include delete groupFolder in update route


## v9.10.6 (2023-04-18)

### Fix

- Patch: fix ordering pdf pages (#638)
  ([`1f9ffe8`](https://github.com/bimdata/python-api-client/commit/1f9ffe8da45895f1262475ea73d3ddee52a75eaa))


## v9.10.5 (2023-04-17)

### Fix

- Patch: add id field to Pin
  ([`395d86c`](https://github.com/bimdata/python-api-client/commit/395d86c06bef50cc68b9e5f440f059addd8c5678))


## v9.10.4 (2023-03-09)

### Fix

- Patch: fix requestBody on simple delete route
  ([`ece7509`](https://github.com/bimdata/python-api-client/commit/ece7509ed7e31a24ef3347245bfd7f9331f1f8fe))


## v9.10.3 (2023-03-02)

### Fix

- Patch: add model.binary_2d_file field
  ([`4bd519d`](https://github.com/bimdata/python-api-client/commit/4bd519d8a800557f2ba434d5a43a0a4f6c6273a9))


## v9.10.2 (2023-02-06)

### Fix

- Patch: remove some useless field on dms-tree
  ([`035c4e4`](https://github.com/bimdata/python-api-client/commit/035c4e4e7f63f75ffd9acc69478ba4265133a096))


## v9.10.1 (2023-01-27)

### Fix

- Patch: force request body on delete method with drf-spectacular (#615)
  ([`206ee31`](https://github.com/bimdata/python-api-client/commit/206ee31fdd0ade562478a39ba5f7d1caa2ae0991))


## v9.10.0 (2023-01-16)

### Feature

- Minor: add marketplace app links (#609)
  ([`c28d8c1`](https://github.com/bimdata/python-api-client/commit/c28d8c161d7341866d8bf3ed6afba861bba0c0e2))


## v9.9.0 (2023-01-05)

### Feature

- Minor: Remove folder groups and history fields form DMS-Tree(#599)
  ([`9edfcb5`](https://github.com/bimdata/python-api-client/commit/9edfcb5c93767b5d10776adeb3047a0013b1707e))

* optimize some routes and remove group_permissions from dms-tree

* add more tests

* remove history from dms-tree

* typo

* fix documentation

* restore features prefetch

* remove useless prefetch

* fix prefetch

* remove useless prefetch


## v9.8.1 (2022-12-20)

### Fix

- Patch: Feat/multipage pdf (#596)
  ([`0eaaff0`](https://github.com/bimdata/python-api-client/commit/0eaaff0c974a843dc80316c30af6059a4870737e))

* create multipage-pdf

* fix create_model tests

* fix tests

* add explicit comment to signal function

* update help_text for parent and children


## v9.8.0 (2022-12-20)

### Feature

- Minor: create import group from ids (#595)
  ([`b0459fd`](https://github.com/bimdata/python-api-client/commit/b0459fdd1f71ee919cc1963f0c82b5a51b145451))

* feat: create import group from id

* remove UserProject property, add select_related to userprojects queryset

* import several groups from a project instead of one


## v9.7.0 (2022-12-06)

### Feature

- Minor: add project check access route(#561)
  ([`bfb2c05`](https://github.com/bimdata/python-api-client/commit/bfb2c05b2e5ac3247f359ad45006f95b54b43037))

* Add projcte check-access route

* add route description

* update tests with new invitation routes


## v9.6.12 (2022-11-30)

### Fix

- Patch: fix model export doc response
  ([`aa8fbfd`](https://github.com/bimdata/python-api-client/commit/aa8fbfd7a717ba3a5d1c2074effd81ea07b43d18))


## v9.6.11 (2022-11-16)

### Fix

- Patch: added missing value (client name) to User Invitation Serializer (#590)
  ([`19b7898`](https://github.com/bimdata/python-api-client/commit/19b78982253fe658aa0008866a6fab0bbc58d448))


## v9.6.10 (2022-11-09)

### Fix

- Patch: create DMS Tree return same datas as the get route (#587)
  ([`8ec4ab1`](https://github.com/bimdata/python-api-client/commit/8ec4ab1be66e53ff4d49c782867b8bed5d557058))


## v9.6.9 (2022-11-09)

### Fix

- Patch: create DMS Tree return same datas as the get route (#587)
  ([`5bd84de`](https://github.com/bimdata/python-api-client/commit/5bd84de4148c2c19adcff8a8f5acc9d4ff55a2d8))


## v9.6.8 (2022-11-07)

### Fix

- Patch: fix model deserialization
  ([`623b8f6`](https://github.com/bimdata/python-api-client/commit/623b8f6234b83b65e312e609d6513f13a5c15171))


## v9.6.7 (2022-10-21)

### Fix

- Patch: rename model 360 field (#576)
  ([`8de9eae`](https://github.com/bimdata/python-api-client/commit/8de9eaebf5e2991649ccd08332b37ce6db8fac8c))

* rename model 360 field

* keep viewer_360_file field

* remove useless field in write only serializer


## v9.6.6 (2022-10-18)

### Fix

- Patch: rename request param in patch user cloud (#572)
  ([`2907dd6`](https://github.com/bimdata/python-api-client/commit/2907dd671f669f95d72ae0bb34e3d611ebdeacb4))


## v9.6.5 (2022-10-11)

### Fix

- Patch: fix bad body serializer linkDocumentsOfElement
  ([`81cff13`](https://github.com/bimdata/python-api-client/commit/81cff13e6c4e8b35db22a022735e269d828b749c))


## v9.6.4 (2022-10-10)

### Fix

- Patch: fix #536 body in linkDocumentsOfElement
  ([`01b3da8`](https://github.com/bimdata/python-api-client/commit/01b3da8507448e88b30946aaf5911475aabffad9))


## v9.6.3 (2022-10-07)

### Fix

- Patch: created_at and responded_at in Invitation model (#570)
  ([`dc7063d`](https://github.com/bimdata/python-api-client/commit/dc7063dac2b4d3f6839d12248b708eb4d0b54a06))

* created_at and updated_at in Invitation model

* invitation: manual responded_at field


## v9.6.2 (2022-10-07)

### Fix

- Patch: cloud_id and project_id in Invitation serializer
  ([`d7315c0`](https://github.com/bimdata/python-api-client/commit/d7315c0b017a7f475bc79b960feb5d31b73a14e0))


## v9.6.1 (2022-10-06)

### Fix

- Patch: Update fields of userInvitation serializer
  ([`88f7294`](https://github.com/bimdata/python-api-client/commit/88f7294512206fef11de7cce399d3c6e56344fa6))


## v9.6.0 (2022-10-06)

### Feature

- Minor: user invitation routes (#569)
  ([`2f7d1d4`](https://github.com/bimdata/python-api-client/commit/2f7d1d45f528616b5b5921d06fec8cd36be2ca83))

* make invitation api updatable

* add user:write scope

* use many to many scopes in views and tests

* set scopes in MarketplaceAppAuthorization view


## v9.5.0 (2022-09-14)

### Feature

- Minor: Point cloud
  ([`5f4bd06`](https://github.com/bimdata/python-api-client/commit/5f4bd06b2a5603b59130f8fc4037a9960c7287ac))


## v9.4.9 (2022-09-09)

### Fix

- Patch: allow empty file on document upload
  ([`32585b1`](https://github.com/bimdata/python-api-client/commit/32585b1ed8aeef00f45cae6efa8fae0ad51e5c54))


## v9.4.8 (2022-09-07)

### Fix

- Patch: allow empty files
  ([`c191c95`](https://github.com/bimdata/python-api-client/commit/c191c958362b0f2cf4d66232e592f683f6378c55))


## v9.4.7 (2022-08-29)

### Fix

- Patch: Fix/inline serializer fields (#560)
  ([`6b706ce`](https://github.com/bimdata/python-api-client/commit/6b706ce71d28225513dd83a52e9f9e232f8fa00f))

Fix CreateStoreyPlan and BuildingStoreyPlan


## v9.4.6 (2022-08-09)

### Fix

- Patch: fix project access token enum (#555)
  ([`1005bc4`](https://github.com/bimdata/python-api-client/commit/1005bc47ee0d8369a8ffbc0b98a532aff4c2b812))


## v9.4.5 (2022-08-03)

### Fix

- Patch: add response data to create DMSTree
  ([`66c3969`](https://github.com/bimdata/python-api-client/commit/66c3969287fe9de08f80a5d60cb9b4bef702ae3d))


## v9.4.4 (2022-06-24)

### Fix

- Patch: Add authoring viewpoint fields (#547)
  ([`5d0a18b`](https://github.com/bimdata/python-api-client/commit/5d0a18b4752fb192b0d8023677099794cc4c77e7))


## v9.4.3 (2022-06-22)

### Fix

- Patch: fix get-dms-tree serializer
  ([`ce53acf`](https://github.com/bimdata/python-api-client/commit/ce53acff6a0c3977f1c71c2e73c25b054b60dde1))


## v9.4.2 (2022-06-22)

### Fix

- Patch: fix create-dsm-tree serializer
  ([`9f58aae`](https://github.com/bimdata/python-api-client/commit/9f58aae36e98cd7aa7cf5f5538c0645af99f4c50))


## v9.4.1 (2022-06-16)

### Fix

- Patch: improve viewpoint pins (#543)
  ([`7a42412`](https://github.com/bimdata/python-api-client/commit/7a424129ec9ec62252018a17476afcffe01c1acb))


## v9.4.0 (2022-06-09)

### Feature

- Minor: Add BCF authoring tool (#540)
  ([`f8da5ba`](https://github.com/bimdata/python-api-client/commit/f8da5ba89f43f67cba93336c5031849ba0acdcd5))


## v9.3.10 (2022-05-13)

### Fix

- Patch: fix create dms tree doc, children was missing in serializer request (#531)
  ([`f734b1b`](https://github.com/bimdata/python-api-client/commit/f734b1b19270e293610b98951ebe44d098718001))

* fix create dms tree doc, children was missing in serializer request

* rename serializer


## v9.3.9 (2022-05-12)

### Fix

- Patch: add tag to document in dms-tree (#533)
  ([`4ffe2ea`](https://github.com/bimdata/python-api-client/commit/4ffe2ea7d309477ebf5305b4b80ae6d3f47ea3fd))


## v9.3.8 (2022-05-10)

### Fix

- Patch: versioning: more permissive archi (#528)
  ([`4cb18fd`](https://github.com/bimdata/python-api-client/commit/4cb18fdbc2ebf3de4de3e82c183ff5f43c80a929))


## v9.3.7 (2022-05-05)

### Fix

- Patch: rename operation_id
  ([`e04c180`](https://github.com/bimdata/python-api-client/commit/e04c180145e8ab619657a38b6c3a59c4eb13b1eb))


## v9.3.6 (2022-05-05)

### Fix

- Patch: delete all document version on delete (#525)
  ([`9aa819b`](https://github.com/bimdata/python-api-client/commit/9aa819bd370259e21f61686a2903f34069bcaada))

* delete all document version on delete

* versioning: add delete history route


## v9.3.5 (2022-05-04)

### Fix

- Patch: add document_id to visa serializer
  ([`2ec598a`](https://github.com/bimdata/python-api-client/commit/2ec598a2b1bdc0ebdf270e7c74df463327a2db28))


## v9.3.4 (2022-05-04)

### Fix

- Patch: visa serialization in document (#522)
  ([`213c4d7`](https://github.com/bimdata/python-api-client/commit/213c4d7141e9c5c8fc00d80e21739d1dfa2f8bf8))

* visa serialization in document

* no prefetch tag


## v9.3.3 (2022-05-03)

### Fix

- Patch: reorder document history
  ([`c1afe9e`](https://github.com/bimdata/python-api-client/commit/c1afe9ea010a61da0ed2d0c0c7e43437e56bd311))


## v9.3.2 (2022-05-02)

### Fix

- Patch: serialize document creator
  ([`cb1f35c`](https://github.com/bimdata/python-api-client/commit/cb1f35c2348a89acb7f8f0b3d47ff5d86e4eb80b))


## v9.3.1 (2022-04-29)

### Fix

- Patch: remove parent from document serialization (#521)
  ([`fbc5445`](https://github.com/bimdata/python-api-client/commit/fbc544512b74cc852b2b6f155cb2b62b79122289))


## v9.3.0 (2022-04-29)

### Feature

- Minor: Feat/versionning (#517)
  ([`d562d95`](https://github.com/bimdata/python-api-client/commit/d562d9583f76b61f0f6ddf97ec80150a6fd6b902))

* add model, migrations, views, serializers

* test DocumentHistory view

* fix last tests

* filter list model

* fix migration and add reverse_code

* renaming old_version_id


## v9.2.0 (2022-04-21)

### Feature

- Minor: add bcf pins (#515)
  ([`8948499`](https://github.com/bimdata/python-api-client/commit/8948499b4f427735081404a23b9c68fe2f1b12d4))

* add bcf pins

* add view tests


## v9.1.1 (2022-04-20)

### Fix

- Patch: fix createDocument response missing
  ([`a7a4208`](https://github.com/bimdata/python-api-client/commit/a7a4208fa4163eb55e82628a570e743e217b85c3))


## v9.1.0 (2022-04-15)

### Feature

- Minor: create document tag views (#513)
  ([`3c00f75`](https://github.com/bimdata/python-api-client/commit/3c00f752a14f58a4fc38ed9a3ff03ba54e005580))

* create document tag views

* fix: serializer readOnly

* add admin tags

* add inline Tag Project


## v9.0.0 (2022-04-12)

### Breaking

- Major: Feat/openapi3 (#508)
  ([`57074b7`](https://github.com/bimdata/python-api-client/commit/57074b73f37e92e1ee0b37cdfde59b3ccd7bdd80))

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

Co-authored-by: Amoki <hugo@bimdata.io>

### Fix

- Patch: fix swagger generation
  ([`3952685`](https://github.com/bimdata/python-api-client/commit/3952685f9c92059b94605b178693de95cd670f1d))


## v8.0.0 (2022-04-12)

### Breaking

- Major: Feat/openapi3 (#508)
  ([`18591ec`](https://github.com/bimdata/python-api-client/commit/18591ec7c8156e00549d7d604500a0773b79463a))

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

Co-authored-by: Amoki <hugo@bimdata.io>


## v7.4.2 (2022-03-17)

### Fix

- Patch: remove comment visa nested (#502)
  ([`a516af8`](https://github.com/bimdata/python-api-client/commit/a516af86ac3aa3ef6858f1b75c7f36e182bf7c45))


## v7.4.1 (2022-02-25)

### Fix

- Patch: fix create building and storey doc serializer
  ([`03903e7`](https://github.com/bimdata/python-api-client/commit/03903e7c077a08434ad587401dc691c5e2c8b646))


## v7.4.0 (2022-02-25)

### Feature

- Minor: order plans in storey (#495)
  ([`ea3cf1d`](https://github.com/bimdata/python-api-client/commit/ea3cf1d3fc82b9baa09a5536cde76e1f2cfcfc9c))

* init refacto storey

* add building test

* fix serializers

* replace Counter

* init refacto storey

* order plans in storey

* merge migration ifc/88_

* fix bad merge

* fix bad merge


## v7.3.0 (2022-02-25)

### Feature

- Minor: refacto storeys and add buildings (#494)
  ([`06a735c`](https://github.com/bimdata/python-api-client/commit/06a735c75412fdfb301f7e10ecb29a5e4275afe7))

* init refacto storey

* add building test

* fix serializers

* replace Counter


## v7.2.0 (2022-02-24)

### Feature

- Minor: add size_ratio fields
  ([`2a5d90c`](https://github.com/bimdata/python-api-client/commit/2a5d90c51c5de429d10d6cf1f4d5da9da5448093))


## v7.1.2 (2022-02-24)

### Fix

- Patch: bcf detailed extensions labels
  ([`7d5ade7`](https://github.com/bimdata/python-api-client/commit/7d5ade750437b1e5007c4434fdaabfd1c54d9dc9))


## v7.1.1 (2022-02-23)

### Fix

- Patch: add creadted_at and upated_at to Propertie et PropertySet
  ([`9218cd7`](https://github.com/bimdata/python-api-client/commit/9218cd7ae22192003e0e09017565940604bff67c))


## v7.1.0 (2022-02-15)

### Feature

- Minor: Feature/bcf colors (#485)
  ([`64b5792`](https://github.com/bimdata/python-api-client/commit/64b579260b41558e0c959ba65dcbfe159d57fcf0))

* wip

* update project extensions GET method

* cleanup

* fix project extensions

* implement extension update

* add color to all existing topics

* respond with 400 if duplicated name

* remove useless config


## v7.0.1 (2022-02-15)

### Fix

- Patch: rename last ifc operations (#489)
  ([`6a0bce1`](https://github.com/bimdata/python-api-client/commit/6a0bce138e8adad44c462cec339d523fc33cc346))


## v7.0.0 (2022-02-04)

### Breaking

- Major: rename ifc to model (#477)
  ([`6d48496`](https://github.com/bimdata/python-api-client/commit/6d48496db3d7b9f80e1ffcfe407873046383e516))

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

* fix bad rebase


## v6.0.0 (2022-02-04)

### Breaking

- Major: sync with js libs
  ([`eb430f5`](https://github.com/bimdata/python-api-client/commit/eb430f5f2a77313a510db067276c7fe520c28adc))


## v5.22.0 (2022-01-31)

### Feature

- Minor: 2d positioning (#471)
  ([`f8bf0c8`](https://github.com/bimdata/python-api-client/commit/f8bf0c8b641cb613d99d7a116ecd8377fab46245))

* filter storey models with permissions

* rework storey serializer

* add positioning plan to m2m (storey-plan)

* add route with params id and positioning route renaming

* include positioning in storey serializer

* fix tests


## v5.21.1 (2022-01-31)

### Fix

- Patch: filter storey models with permissions and add models_unreachable_count field (#470)
  ([`b68c55a`](https://github.com/bimdata/python-api-client/commit/b68c55a4665fda225fd205dac533f64d9dca9ee8))

* filter storey models with permissions

* fix test add model to storey

* rework storey serializer


## v5.21.0 (2022-01-31)

### Feature

- Minor: add img_format=url in BCF routes (#472)
  ([`9cef689`](https://github.com/bimdata/python-api-client/commit/9cef6891bd435d25098035e413489bb6735515c2))


## v5.20.1 (2022-01-28)

### Fix

- Patch: one storey site by building (#469)
  ([`7c907c8`](https://github.com/bimdata/python-api-client/commit/7c907c80cb76328f174e414efb73850ca81dc188))

* one storey site by building

* add db unique constraint

* Update ifc/v1/views.py

Co-authored-by: Hugo Duroux <hugo@bimdata.io>

* Update ifc/v1/views.py

Co-authored-by: Hugo Duroux <hugo@bimdata.io>

Co-authored-by: Hugo Duroux <hugo@bimdata.io>


## v5.20.0 (2022-01-27)

### Feature

- Minor: plans and storeys (#468)
  ([`6a125d1`](https://github.com/bimdata/python-api-client/commit/6a125d1eebe97eacd063a6ef2001c9057ac57cb2))

* create storey

* add migrations and route manage model children

* create metabuilding and relation between storey and model-plans

* fix signal test

* PR review

* models can update name


## v5.19.1 (2022-01-18)

### Fix

- Patch: Add non automatic models (#464)
  ([`b224801`](https://github.com/bimdata/python-api-client/commit/b2248010f7890245d90e9b4f067e4ca96ea00a63))

* Add non automatic models

* improve tests

* rename route and add permissions

* add model delete with doc


## v5.19.0 (2022-01-14)

### Feature

- Minor: Feature/smart files (#463)
  ([`a5ba918`](https://github.com/bimdata/python-api-client/commit/a5ba9187333e0a1b754b49755322102085adacc3))

* allow many model types

* add tests

* fix document name

* more cleanup

* update ci poetry version

* do not reprocess on file update

* fix export,merge and optimize queues

* add types.py

* more contants


## v5.18.3 (2022-01-11)

### Fix

- Patch: (visa) add validations_in_error to serializer
  ([`e4df33f`](https://github.com/bimdata/python-api-client/commit/e4df33ffcaf01b3f60f7e214a2a64809d2befcf3))


## v5.18.2 (2022-01-04)

### Fix

- Patch: fix document elements list uuids
  ([`39de959`](https://github.com/bimdata/python-api-client/commit/39de959c2a58e9ab3b5949542efe76456cd8cad9))


## v5.18.1 (2021-12-22)

### Fix

- Patch: rename element_ids to element_uuids
  ([`461e3db`](https://github.com/bimdata/python-api-client/commit/461e3db667d2edba71b1596d694185f61d3233b5))


## v5.18.0 (2021-12-22)

### Feature

- Minor: add element/documents route
  ([`68a02e7`](https://github.com/bimdata/python-api-client/commit/68a02e7d227d78ef2e4efd9bdfbe82b1b686cf89))


## v5.17.1 (2021-12-13)

### Fix

- Patch: add document to visa serializer (#458)
  ([`7504aee`](https://github.com/bimdata/python-api-client/commit/7504aee678ed033bcbe517ab9fcfe7c54776bfcf))


## v5.17.0 (2021-12-09)

### Feature

- Minor: Feature/link element document (#457)
  ([`92814d1`](https://github.com/bimdata/python-api-client/commit/92814d193cd97e2feddbed979806ed702db7301d))

* add documents to elements

* add test for filterred ifc and document list

* typo

* add some query optimizations


## v5.16.0 (2021-12-06)

### Feature

- Minor: Feature/visa (#451)
  ([`a963e5f`](https://github.com/bimdata/python-api-client/commit/a963e5f94af8f3e4d098856adc9253a0cb473252))

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

* add userproject to serializers context


## v5.15.2 (2021-12-02)

### Fix

- Patch: add id to Public Organization Serializer
  ([`5ac3574`](https://github.com/bimdata/python-api-client/commit/5ac357430084e206b40537112334d8de4075f805))


## v5.15.1 (2021-12-02)

### Fix

- Patch: add organization serializer in App and MPApp serializers (#452)
  ([`b1f0958`](https://github.com/bimdata/python-api-client/commit/b1f0958e511655ca19ddbf52ab35fbb1d1fd1fc2))

* add organization serializer in App and MPApp serializers

* fix test and add select related

* use Public Organization Serializer


## v5.15.0 (2021-11-24)

### Feature

- Minor: Remove deprecated and put (#450)
  ([`5769df5`](https://github.com/bimdata/python-api-client/commit/5769df5195f22e65696b4c46ed1a8ee925634526))

* remove deprecated route and PUT route without BCF routes

* fix some tests

* fix last tests and restore project tree route

* restore BCF tests change

* rename fullUpdate operation

- Minor: Add leave project route (#449)
  ([`4d52c51`](https://github.com/bimdata/python-api-client/commit/4d52c51628bf3e977074dfec3d8af51615a13c2d))

* Add leave project route

* fix roles

### Fix

- Patch: fix semantic release
  ([`aca3560`](https://github.com/bimdata/python-api-client/commit/aca3560c5d69a91d32be6992c0d8aea1153110b4))

- Patch: fix serializer user project (#448)
  ([`8b5446a`](https://github.com/bimdata/python-api-client/commit/8b5446a58252f767665f6cd3fff59af93baddfbd))

Breaking Change: - key to for GroupUser create view - Route pk for userProject views is now
  UserProject pk and not FosUser pk

Some other change: - fix serializer of userProject for swagger and libs - add missing invitation
  user project from project and group - fix some test

- Patch: add invitation key in UserProject
  ([`30a8fb5`](https://github.com/bimdata/python-api-client/commit/30a8fb5ad88a6aed47de4bcb69a34cd37702e5ff))

- Patch: get cloud size operation id in openapi
  ([`d508862`](https://github.com/bimdata/python-api-client/commit/d5088627492eec9d1ea02a8915cfb1d7ed4ce09c))

- Patch: fix list/create methods openAPI
  ([`7519d93`](https://github.com/bimdata/python-api-client/commit/7519d931205caffc57f964e92e0547714d916304))


## v5.14.0 (2021-09-13)

### Feature

- Minor: serialize user-permissions on documents
  ([`8597421`](https://github.com/bimdata/python-api-client/commit/859742176f6e0827c170dd8d30c95c254d502fcc))

- Minor: Add profile_picture field in user serialization
  ([`45bd37c`](https://github.com/bimdata/python-api-client/commit/45bd37ce3e9ead5bb4050fa2a26a609a64e8ac26))

* add user picture field

* fix user.company, add comment about an edge case

- Minor: add GED permissions
  ([`00b987a`](https://github.com/bimdata/python-api-client/commit/00b987af3d7f310c07beb9d30c7354b9e5830d26))

- Minor: allow bigger guids (#420)
  ([`54b2b09`](https://github.com/bimdata/python-api-client/commit/54b2b090cbbf127cf8ac0f17c3492e6d0e1c7f29))

### Fix

- Patch: allow empty name in raw layers and raw materials
  ([`b96d9a7`](https://github.com/bimdata/python-api-client/commit/b96d9a7eb1e3828fd2b3f7e9edb558b296d38f0b))

- Patch: allow empty name in raw layers and raw materials
  ([`c0d6bb6`](https://github.com/bimdata/python-api-client/commit/c0d6bb6f662d3289915da48580553bb2277c7ee7))

- Patch: allow empty name in raw layers and raw materials
  ([`22e450d`](https://github.com/bimdata/python-api-client/commit/22e450d38322621610ca85750524c94dd197f33c))

- Patch: fix dms-tree group permissions
  ([`38f8ce5`](https://github.com/bimdata/python-api-client/commit/38f8ce5608ad11f8dd1518a9a901da5ef8779bdd))

- Patch: fix field name and add field to children dms-tree (#426)
  ([`2881af8`](https://github.com/bimdata/python-api-client/commit/2881af81fb7ae5fe2718f8187ffc5ae350aa4ebd))


## v5.13.3 (2021-06-02)

### Fix

- Patch: fix raw element serializer
  ([`e71a065`](https://github.com/bimdata/python-api-client/commit/e71a0653503541b72f556149e3108134cbbd89f2))


## v5.13.2 (2021-05-24)

### Fix

- Patch: (raw element) key named material_list instead of materials
  ([`b2e94e0`](https://github.com/bimdata/python-api-client/commit/b2e94e03dc847ffbe507799810f8ec9167f3bcad))


## v5.13.1 (2021-05-24)

### Fix

- Patch: fix(raw element): material_ids is integer and add id properties
  ([`c5f3ac4`](https://github.com/bimdata/python-api-client/commit/c5f3ac456cc5ff143d25231e9c745fca6aa15f6c))


## v5.13.0 (2021-05-21)

### Feature

- Minor: add recommanded_2d_angle (#403)
  ([`60bb446`](https://github.com/bimdata/python-api-client/commit/60bb446730a3a8636de676dc0baa15b47d7ea347))


## v5.12.1 (2021-05-19)

### Fix

- Patch: fix some open api fields (#401)
  ([`a0757ca`](https://github.com/bimdata/python-api-client/commit/a0757ca1683cbaab1691fd083943ab69a5cb3168))


## v5.12.0 (2021-05-05)

### Feature

- Minor: serialization mpApp.organization_id
  ([`86dd09b`](https://github.com/bimdata/python-api-client/commit/86dd09b03bdade1f22f5d7742a09782935086bc8))


## v5.11.0 (2021-04-16)

### Feature

- Minor: add ifc north vector (#394)
  ([`58ef3ac`](https://github.com/bimdata/python-api-client/commit/58ef3aca21afa401496830d7b5384b04c844eca3))


## v5.10.0 (2021-04-13)

### Feature

- Minor: add ifc version (#392)
  ([`266ac60`](https://github.com/bimdata/python-api-client/commit/266ac6032648ad0d5d0a72f8af058969071d913a))


## v5.9.0 (2021-04-07)

### Feature

- Minor: add ifc.archived field
  ([`f3d2eee`](https://github.com/bimdata/python-api-client/commit/f3d2eeeccbaf6ac76636f15d90f65c9e3a8d25e2))


## v5.8.1 (2021-01-26)

### Fix

- Patch: fix BCF projects serialization
  ([`5fa5f0b`](https://github.com/bimdata/python-api-client/commit/5fa5f0b7eaaa6fcd4ac7990892ae63eb5d620723))


## v5.8.0 (2020-11-23)

### Feature

- Minor: add delete all pset route
  ([`f08cb86`](https://github.com/bimdata/python-api-client/commit/f08cb8676eb700237f00d959ae9b084daeeb5f1a))


## v5.7.0 (2020-08-01)

### Feature

- Minor: add project access token
  ([`142080f`](https://github.com/bimdata/python-api-client/commit/142080f499348df876d6c31bb35afbe00fbb07a7))


## v5.6.1 (2020-03-30)

### Fix

- Patch: fix document type enum
  ([`eb0d75d`](https://github.com/bimdata/python-api-client/commit/eb0d75df86e8a0a48ca758e429000d5c8fc7913f))


## v5.6.0 (2020-03-27)

### Feature

- Minor: add merge and optimize routes
  ([`07bb292`](https://github.com/bimdata/python-api-client/commit/07bb292f1d14991506c08a2bf7b903e0259bb9a6))


## v5.5.0 (2020-03-04)

### Feature

- Minor: filtering by email for list cloud user and project user
  ([`fbd3b8b`](https://github.com/bimdata/python-api-client/commit/fbd3b8b20e7408a922f3dd4b3ea501a039fe0217))


## v5.4.0 (2020-03-02)

### Feature

- Minor: Add IFC export route. Fix users deserialization when firstname and lastname are empty
  ([`f8766ce`](https://github.com/bimdata/python-api-client/commit/f8766ce37a659722c69d841c553a2a87f669f2dd))


## v5.3.1 (2020-02-25)

### Fix

- Patch: add property_set_id to property serialization
  ([`7945a13`](https://github.com/bimdata/python-api-client/commit/7945a13402fd3d847674a6a0cac8d8908bdfc70f))


## v5.3.0 (2020-02-24)

### Feature

- Minor: add property update route
  ([`b5425e4`](https://github.com/bimdata/python-api-client/commit/b5425e4c8cd7e050e537b569e471926ee8d65c7f))


## v5.2.0 (2020-02-20)

### Feature

- Minor: add BCF import route
  ([`b2330e9`](https://github.com/bimdata/python-api-client/commit/b2330e93b02a91f9ee51b1f9778e8a6ee8b23202))


## v5.1.2 (2020-02-14)

### Fix

- Patch: fix typo in BCF.Line object. From LineSeriaizer to Line
  ([`d72a96d`](https://github.com/bimdata/python-api-client/commit/d72a96de3a152814944093d5f33af9e80413db68))


## v5.1.1 (2020-02-10)

### Fix

- Patch: methods can't be in many apis at the same times. Too many tools don't support it.
  ([`56c9283`](https://github.com/bimdata/python-api-client/commit/56c928326717f177a3462a31045559e2a39c50d7))


## v5.1.0 (2020-01-22)

### Feature

- Minor: add optionnal document.ifc_source (default: UPLOAD) to specify the source of the IFC
  ([`41a16fc`](https://github.com/bimdata/python-api-client/commit/41a16fc6d7f9ac33cd1a2114c1e3c257bd88bffb))


## v5.0.2 (2020-01-21)

### Fix

- Patch: project field of createDocument is no more mandatory
  ([`08788d0`](https://github.com/bimdata/python-api-client/commit/08788d05a66bee238b6c43e72745e2a9ba7cfbcb))


## v5.0.1 (2020-01-21)

### Fix

- Patch: Fix System and Layers serialization in RawElements
  ([`611068c`](https://github.com/bimdata/python-api-client/commit/611068c14b772fd4aeb8e5495f22b12b099688de))


## v5.0.0 (2020-01-13)

### Breaking

- Major: rename apis. See release for more info
  ([`7444421`](https://github.com/bimdata/python-api-client/commit/74444219b062643fceefb0dd7455b3377c19388b))


## v4.6.0 (2020-01-10)

### Feature

- Minor: add params to ifc/export route
  ([`71dfe01`](https://github.com/bimdata/python-api-client/commit/71dfe01ce7ae809cae8dd2462a665dbbf12e90c4))


## v4.5.0 (2020-01-08)

### Feature

- Minor: Add IFC warnings
  ([`8fab6fc`](https://github.com/bimdata/python-api-client/commit/8fab6fc9f13fcdcc722800faaa07ff750bddef1e))


## v4.4.0 (2019-12-18)

### Feature

- Minor: add user deletion route, add IFC layers routes, add element/simple representation, add IFC
  Systems routes, add IFC errors route, fix some malformed operationId
  ([`4b899c9`](https://github.com/bimdata/python-api-client/commit/4b899c9cb149996025c5cbed572a5353cf92125b))


## v4.3.0 (2019-11-19)

### Feature

- Minor: add provider field in user serilization
  ([`510c0ba`](https://github.com/bimdata/python-api-client/commit/510c0ba88511fe393156289ee5e71f380752d695))


## v4.2.2 (2019-11-08)

### Fix

- Patch: Feature/description pypi (#1)
  ([`997f1e1`](https://github.com/bimdata/python-api-client/commit/997f1e11fcceaa63f42c39d3c1d44d5f92c882a2))

* add long description in setup; check readme syntax in circleci

* fix open import for py2

* fix command missing circleci


## v4.2.1 (2019-10-08)

### Fix

- Patch: zone name is no more required
  ([`16c9b09`](https://github.com/bimdata/python-api-client/commit/16c9b09f30ee873568a64d26d728807ccd1e29b8))


## v4.2.0 (2019-10-07)

### Feature

- Minor: Add cloud image
  ([`1efca02`](https://github.com/bimdata/python-api-client/commit/1efca02eace97a68ed6faa94e75e953a35e31a10))


## v4.1.0 (2019-09-18)

### Feature

- Minor: Add IfcAccessToken. It is usefull to create read_only tokens to share a viewer or when
  you're using an app without users
  ([`3503c35`](https://github.com/bimdata/python-api-client/commit/3503c35c9b5693ab70dbc74e56fa282659bce0cd))


## v4.0.7 (2019-09-04)

### Fix

- Patch: fix RecursiveFolderChildren model to allow an empty children field
  ([`c92e9da`](https://github.com/bimdata/python-api-client/commit/c92e9dae3d70c0c1d430952309fd8473c2e63592))


## v4.0.6 (2019-09-04)

### Fix

- Patch: fix FolderChildren serialization: creator is not mandatory
  ([`c140634`](https://github.com/bimdata/python-api-client/commit/c14063410f1fe16ad11e37d513f46e9e5b3e5040))


## v4.0.5 (2019-09-03)

### Fix

- Patch: add missing ifc.xkt_file
  ([`f7520fa`](https://github.com/bimdata/python-api-client/commit/f7520faeaeedf31b2239157c0bb76ea6b8140138))


## v4.0.4 (2019-09-03)

### Fix

- Patch: fix bulk create route. Regression removed the declaration and bulk route were only
  accessible with a single objects instead of an array
  ([`ad13dd0`](https://github.com/bimdata/python-api-client/commit/ad13dd0a272dd6e64d44d3d4e7acf4bda519a0f3))


## v4.0.3 (2019-09-03)

### Fix

- Patch: fix viewpoint guid read_only instead of read/write
  ([`31896f6`](https://github.com/bimdata/python-api-client/commit/31896f68f2174a92c68abd697ba1c252991e80ae))


## v4.0.2 (2019-09-03)

### Fix

- Patch: fix python openapi-generator parameters
  ([`8b94f57`](https://github.com/bimdata/python-api-client/commit/8b94f57a6ae24cec76a83d23c344acea6f989a63))


## v4.0.1 (2019-09-02)

### Fix

- Patch: fix Folder model named. Last version renamed it RecursiveFolder by error
  ([`c2f57be`](https://github.com/bimdata/python-api-client/commit/c2f57be499134f44aa174ad5585d4216ba390fae))


## v4.0.0 (2019-09-02)

### Breaking

- Major: change BCF topics_pk route name to topics_guid
  ([`f88346d`](https://github.com/bimdata/python-api-client/commit/f88346dad95068caecb74ff4cf8df3904124c08d))


## v3.1.1 (2019-07-24)

### Fix

- Patch: revert project serialization
  ([`5384c5f`](https://github.com/bimdata/python-api-client/commit/5384c5fc56e6f46c6ee47e7ec253554af837e86b))


## v3.1.0 (2019-07-23)

### Feature

- Minor: update project serialization
  ([`5843ad6`](https://github.com/bimdata/python-api-client/commit/5843ad6a22d8c3af4fb06f556cc6a53c961b2f01))


## v3.0.3 (2019-07-11)

### Fix

- Patch: remove unexinsting method from swagger
  ([`fe605b1`](https://github.com/bimdata/python-api-client/commit/fe605b19b27f30b3cadef0877e98ea0c5d50f59f))


## v3.0.2 (2019-07-08)

### Fix

- Patch: fix FolderChildren OpenAPI Definition
  ([`2fd6775`](https://github.com/bimdata/python-api-client/commit/2fd6775fcdd57456ed1c9d2aa97a8b34182a568c))


## v3.0.1 (2019-07-05)

### Fix

- Patch: fix folder swagger definition (#150)
  ([`165f240`](https://github.com/bimdata/python-api-client/commit/165f24048731482b6885d0d5ac298100f6d9cff4))


## v3.0.0 (2019-07-01)

### Breaking

- Major: upgrade openapi-generator to 4.0.2. JS Lib is now ES6
  ([`c4c3aa0`](https://github.com/bimdata/python-api-client/commit/c4c3aa0a1131becddab9dbd6c503ee96d798fc6a))


## v2.13.0 (2019-05-23)

### Feature

- Minor: add processors
  ([`2f8746f`](https://github.com/bimdata/python-api-client/commit/2f8746ff305159fe3cbafa18cc41d986edd8c7e2))


## v2.12.7 (2019-05-09)

### Fix

- Patch: fix documents methods names
  ([`1689c2f`](https://github.com/bimdata/python-api-client/commit/1689c2f5be4f37988e63eace0e7b895340e5f432))


## v2.12.6 (2019-05-07)

### Fix

- Patch: fix webhook ping method name
  ([`a48e7b5`](https://github.com/bimdata/python-api-client/commit/a48e7b5f7de673d8249e1b9fd0b2327396dcd292))


## v2.12.5 (2019-04-11)

### Fix

- Patch: add id in invitation serialization
  ([`b2f7bf0`](https://github.com/bimdata/python-api-client/commit/b2f7bf04e8463e54ab45d3e615384b9b03cf7973))


## v2.12.4 (2019-04-01)

### Fix

- Patch: add bimdata_camera_direction
  ([`edc7f4b`](https://github.com/bimdata/python-api-client/commit/edc7f4b051207103210784cc85699dc8414d8094))


## v2.12.3 (2019-03-25)

### Fix

- Patch: add missing ifc serialization in checker
  ([`c54755e`](https://github.com/bimdata/python-api-client/commit/c54755e9f7a661d4cf7bf9410b2cb838bf5aa6f8))


## v2.12.2 (2019-03-19)

### Fix

- Patch: fix wrong role invitation type
  ([`7e87bef`](https://github.com/bimdata/python-api-client/commit/7e87beff080ccd64605966184f36f29f55366309))


## v2.12.1 (2019-03-19)

### Fix

- Patch: add missing cloud_role invitation in serialization
  ([`02e8f07`](https://github.com/bimdata/python-api-client/commit/02e8f073b95d12126ac187dbc7c5237ddeaf1562))


## v2.12.0 (2019-03-18)

### Feature

- Minor: add invitation cancellation and renew
  ([`3fc7e12`](https://github.com/bimdata/python-api-client/commit/3fc7e123dc29f876be399e7b0ba11b949b674dcc))


## v2.11.1 (2019-03-12)

### Fix

- Patch: fix bcf extension schema
  ([`d54bef0`](https://github.com/bimdata/python-api-client/commit/d54bef03adb7ef4ace39aa597c4ce6bcdb853e4d))


## v2.11.0 (2019-03-06)

### Feature

- Minor: allow cloud deletion
  ([`623938b`](https://github.com/bimdata/python-api-client/commit/623938b61167fa04ef331f950569b36680da70b0))


## v2.10.0 (2019-02-18)

### Feature

- Minor: Add un change role routes
  ([`fcbdeda`](https://github.com/bimdata/python-api-client/commit/fcbdeda68ff5527f6af5f935f0961e364e93fb26))


## v2.9.1 (2019-02-18)

### Fix

- Patch: fix invitation method name
  ([`cf81e99`](https://github.com/bimdata/python-api-client/commit/cf81e99aa9c2ce798929056a7ef491d7fb74f060))


## v2.9.0 (2019-02-08)

### Feature

- Minor: add bcf export
  ([`526eb7f`](https://github.com/bimdata/python-api-client/commit/526eb7f4906705f73918db80b2c6ccf0c8442cd3))


## v2.8.3 (2019-01-18)

### Fix

- Patch: fix selfUser serialization
  ([`956f362`](https://github.com/bimdata/python-api-client/commit/956f362fe89a4c4e9d122981978a7a6f0af29d99))


## v2.8.2 (2019-01-16)

### Fix

- Patch: fix full-topic swagger
  ([`48baaf6`](https://github.com/bimdata/python-api-client/commit/48baaf650f881eb004a2c760a734bc661e39da1f))


## v2.8.1 (2019-01-16)

### Fix

- Patch: fix swagger.json
  ([`22143d4`](https://github.com/bimdata/python-api-client/commit/22143d4a947e22627ed349c4105918e6dea301d4))


## v2.8.0 (2019-01-10)

### Feature

- Minor: add 360_viewer_file
  ([`e1ac708`](https://github.com/bimdata/python-api-client/commit/e1ac708d33882c63015853e40dbef5f6a95b253f))


## v2.7.0 (2018-12-10)

### Feature

- Minor: add patch extension endpoint
  ([`76df76e`](https://github.com/bimdata/python-api-client/commit/76df76e7c9e53790c842860d1ab9a83f1927c2e6))


## v2.6.0 (2018-12-05)

### Feature

- Minor: add bcf route
  ([`041f073`](https://github.com/bimdata/python-api-client/commit/041f0731f8e02faee991cb20767c2870df37c212))


## v2.5.4 (2018-11-20)

### Fix

- Patch: update openapi-generator
  ([`81ca880`](https://github.com/bimdata/python-api-client/commit/81ca8809d3e076690e28a8b8b74c107c96128a11))


## v2.5.3 (2018-11-12)

### Fix

- Patch: rename bcf getExtension into getExtentions
  ([`6700f53`](https://github.com/bimdata/python-api-client/commit/6700f537d7a7d7e138954582d5b4466b4782741b))


## v2.5.2 (2018-11-09)

### Fix

- Patch: fix swagger syntax
  ([`a6e9726`](https://github.com/bimdata/python-api-client/commit/a6e9726eae7a0b87933776d75c644eaf7ed32a84))


## v2.5.1 (2018-11-08)

### Fix

- Patch: add due_date to singleSjonTopic
  ([`592a006`](https://github.com/bimdata/python-api-client/commit/592a00627b7504494c6ada9ff4c9d75925aa4d08))


## v2.5.0 (2018-11-08)

### Feature

- Minor: Add bcf topic format filter
  ([`e66d412`](https://github.com/bimdata/python-api-client/commit/e66d412d7346a48a90239d40d05e7154569ec523))


## v2.4.0 (2018-11-07)

### Feature

- Minor: fix swagger.json
  ([`97369dc`](https://github.com/bimdata/python-api-client/commit/97369dc0e23a0b31e09b4dd7560ad1a606b1f849))


## v2.3.1 (2018-09-20)

### Fix

- Patch: fix create-demo swagger
  ([`cbe46ae`](https://github.com/bimdata/python-api-client/commit/cbe46ae8302c671088ef120f20c2e18e49622e43))


## v2.3.0 (2018-09-17)

### Feature

- Minor: add createDemo route
  ([`e1a9a3c`](https://github.com/bimdata/python-api-client/commit/e1a9a3c0af1e1ec73f43699e30518e75d341fe4d))


## v2.2.0 (2018-09-13)

### Feature

- Minor: add webhooks routes
  ([`b07120e`](https://github.com/bimdata/python-api-client/commit/b07120e419469abd65055614453e2630515deeb9))


## v2.1.0 (2018-08-28)

### Feature

- Minor: update generator to version 3.2.2
  ([`700b0b0`](https://github.com/bimdata/python-api-client/commit/700b0b0c447f24b26ec968aeef20d283fb41f5cf))


## v2.0.1 (2018-07-27)

### Fix

- Patch: remove fos_user password field
  ([`843da44`](https://github.com/bimdata/python-api-client/commit/843da443aaf60458044e24de63fd645cf5ad97c9))


## v2.0.0 (2018-07-27)

### Breaking

- Major: user openapi-codegen instead of swagger-codegen
  ([`a812b96`](https://github.com/bimdata/python-api-client/commit/a812b9686052b133703b41b36a81eeb1ad497263))

- Major: set default api url to beta.bimdata.io, change auth behavior to use headers instead of
  querystring
  ([`18e4efe`](https://github.com/bimdata/python-api-client/commit/18e4efeea41cfa43eda671c6a8ff097fd9f46350))


## v1.3.3 (2018-07-06)

### Fix

- Patch: fix User and SelfUser doc generation
  ([`5b71abf`](https://github.com/bimdata/python-api-client/commit/5b71abf9b3dfddfa920b5da545f11dbdc7cbcec3))


## v1.3.2 (2018-07-04)

### Fix

- Patch: fix raw element serialization
  ([`f31e616`](https://github.com/bimdata/python-api-client/commit/f31e6168592a1a14cb011a7489c53e113821bbbb))


## v1.3.1 (2018-07-04)

### Fix

- Patch: fix element model/serialization
  ([`47c1b7a`](https://github.com/bimdata/python-api-client/commit/47c1b7a29e2bbf672013738492d3ad553146a4b9))


## v1.3.0 (2018-07-03)

### Feature

- Minor: back to swagger-codegen 2.4.0
  ([`be799ab`](https://github.com/bimdata/python-api-client/commit/be799abcdd51dfef726c9af6576d2df1e05b2862))

### Fix

- Patch: manually fix lib generation circular import
  ([`26d4705`](https://github.com/bimdata/python-api-client/commit/26d4705662375746873cdf7a2f48019d33c9384f))


## v1.2.0 (2018-07-02)

### Feature

- Minor: allow empty name in spaces
  ([`a3ef30b`](https://github.com/bimdata/python-api-client/commit/a3ef30b86e8e02deaf37f8c2903e4d6bdd5401f0))


## v1.1.1 (2018-06-26)

### Fix

- Patch: fix version management
  ([`7a73046`](https://github.com/bimdata/python-api-client/commit/7a730466de9ff1766f8075fb4e65153b4e12ca80))


## v1.1.0 (2018-06-26)

### Feature

- Minor: add default_cloud and default_project to /user
  ([`ee2071b`](https://github.com/bimdata/python-api-client/commit/ee2071be065bcdc7c23a983cb00d67427d7eeba1))


## v1.0.27 (2018-06-25)

### Fix

- Patch: update-swagger-codegen
  ([`c47c676`](https://github.com/bimdata/python-api-client/commit/c47c67664cd4c4ab5084ba7dd774dc38201f3b2a))

- Patch:: test
  ([`3f95811`](https://github.com/bimdata/python-api-client/commit/3f958119eb9f430d415150886616e6b7985fa0cc))

- Patch: add semantic-release
  ([`5cf5cd7`](https://github.com/bimdata/python-api-client/commit/5cf5cd78e397316c9166a4099ced0fd80beae7d7))
