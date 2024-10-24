# CHANGELOG



## v10.9.0 (2024-10-24)

### Feature

* MINOR: remove sub projects (#782) ([`640445c`](https://github.com/bimdata/python-api-client/commit/640445c300a0cb1823c3378191645bbb1ad852e6))


## v10.8.0 (2024-10-23)

### Feature

* MINOR: add model layout_name for DWG models (#780) ([`e2b806e`](https://github.com/bimdata/python-api-client/commit/e2b806e68bcc0c1d6b9bcbf565e3988057981ff2))


## v10.7.0 (2024-09-16)

### Feature

* MINOR: Bcf odata (#772)

* implement odata filters

* add orderby

* factorize

* replace test domains with bimdata.test ([`34ee7c9`](https://github.com/bimdata/python-api-client/commit/34ee7c9d3104f9f3a0a6363b40f38b778f900666))


## v10.6.0 (2024-09-16)

### Feature

* MINOR: remove smart_data from get_size routes ([`250dc2c`](https://github.com/bimdata/python-api-client/commit/250dc2c6409f9bc59cddf88b121cb7c8946e333a))


## v10.5.0 (2024-09-11)

### Feature

* MINOR: Feature: Photosphere Model (#758)

* MINOR: feat(photosphere): add PHOTOSPHERE model type

* MINOR: feat(photosphere): add create-photosphere route

* MINOR: feat: add create-photospĥere-building route

* fix: IsMetaBuilding perm classes + little opti in create-photosphere route

* fix(ifc): merge 2 migrations into 1 ([`3add6a0`](https://github.com/bimdata/python-api-client/commit/3add6a0633832dcab2db9d9a33baadb7d29945dd))


## v10.4.3 (2024-09-09)

### Fix

* PATCH: fix storey name open api ([`1ec7339`](https://github.com/bimdata/python-api-client/commit/1ec733927e2e879c678c7e24b609c7ec19f0368c))


## v10.4.2 (2024-09-09)

### Fix

* PATCH: bimdata_elevation response can be null ([`a367be3`](https://github.com/bimdata/python-api-client/commit/a367be3cc9df3248b5ef631872c4d37a8a285f03))


## v10.4.1 (2024-09-09)

### Fix

* PATCH: fix bimdata_elevation open api field type ([`8ee2be6`](https://github.com/bimdata/python-api-client/commit/8ee2be67d59b7ed18c83da89c02a0d4b2801fb8d))


## v10.4.0 (2024-09-09)

### Feature

* MINOR: Bimdata elevation (#770)

* add BIMData Elevation to storey

* add update storey elevation

* fix typo in comment ([`2f61155`](https://github.com/bimdata/python-api-client/commit/2f61155c2c71ceda62ace5b83979fec3c806521d))


## v10.3.0 (2024-09-04)

### Feature

* MINOR: serialize basic document data in /me/visa responses (#769)

* MINOR: serialize basic document data in /me/visa responses

* fix minor mistakes

* fix parent_id in doc

* fix prefetch ([`d145d94`](https://github.com/bimdata/python-api-client/commit/d145d9441ac934aaccb5163bfbf0a63f6218f7f9))


## v10.2.2 (2024-07-30)

### Fix

* PATCH: Update ci-requirements.txt ([`83e0968`](https://github.com/bimdata/python-api-client/commit/83e0968df4a62af918209ac628a5fd2f3c8028f2))


## v10.2.1 (2024-07-30)

### Fix

* PATCH: fix project-access-token nullable fields ([`7277533`](https://github.com/bimdata/python-api-client/commit/7277533e82734d36c02bf1f043c66a1cc9f1d427))


## v10.2.0 (2024-07-04)

### Feature

* MINOR: Add bcf bimdata_viewer_layout (#759)

* Add bcf bimdata_layout

* Rename into bimdata_viewer_layout

* Fix test... ([`e6e043b`](https://github.com/bimdata/python-api-client/commit/e6e043ba5e7e82aaacd5c77ceb1bbdb524ec8d65))


## v10.1.0 (2024-06-20)

### Feature

* MINOR: remove bcf project id in response ([`0d32ce4`](https://github.com/bimdata/python-api-client/commit/0d32ce4f80873c50d8a1d4125a4770fb8eefd3b7))


## v10.0.0 (2024-05-30)

### Breaking

* MAJOR: chore: remove deprecated ifc routes from doc (#725) ([`6556cb8`](https://github.com/bimdata/python-api-client/commit/6556cb84ce89f6ed9f483df48dcd20d253c24ae6))

### Feature

* MINOR: Add log for cloud invitations (#746)

* Add cloud invitation logs.

* Add log for canceled invitations.

* Add migration to delete unwanted UserProject.

* Fix typo.

* Better log action naming.

* Fix migration.

* Rename log decorators. ([`d35212c`](https://github.com/bimdata/python-api-client/commit/d35212c15a9d26e6348f827776cd79b3e75ce526))

* MINOR: Add missing attachment in visa validation serializer. (#726) ([`157b488`](https://github.com/bimdata/python-api-client/commit/157b488573349452828fefd97c2b3071a75a1e4d))

* MINOR: Feat/add link between zone and storey (#723)

* Add a link between zone and storey.

* Zone-storey, use uuid instead of pk.

* Rename storey as storey_uuid in zone serializer.

* Split update/remove storey from zone test. ([`abe503b`](https://github.com/bimdata/python-api-client/commit/abe503bc8934c2108a389f82057730922148b5a5))

* MINOR: add logging for documents, folder and user invitations (#712)

* first implementation with documents

* implement and test documents and folders

* aborted try to test folder permission propagation

* fix test get_path

* add project invitation logs

* improve admin

* typo

* add log view test and scope

* fix check_access test

* commit app migrations ([`d68b901`](https://github.com/bimdata/python-api-client/commit/d68b90147f5ce18b32b2fe4d80e30e36eeae6aae))

* MINOR: Add filters and document and some utility routes (#710)

* add folder:id/document route and visa validation attachment

* add filter on first level

* add document advanced filters and folder-tree route

* remove uselesss unpacking operator ([`1c43bba`](https://github.com/bimdata/python-api-client/commit/1c43bbac2d36f8db99acdb3b320e528c3d43194a))

* MINOR: add model drawings (#709)

* MINOR: add model drawings

* fix tests

* add admin ([`81c1d8e`](https://github.com/bimdata/python-api-client/commit/81c1d8ee19e118ddb478f92fc36c7803df734acb))

* MINOR: add user deail to check-access response (#707) ([`368656e`](https://github.com/bimdata/python-api-client/commit/368656ed2a9c47df2f232ba3a1a152845c698d28))

### Fix

* PATCH: fix openAPI definition of getProjectFolderTree ([`ed5e2d5`](https://github.com/bimdata/python-api-client/commit/ed5e2d5c43c24fb2020e7523fe22389ad83cca8e))

* PATCH: fix openAPI definition of getProjectFolderTree ([`c88cf8e`](https://github.com/bimdata/python-api-client/commit/c88cf8ed9c36093d5879b5d82e4e276c4a6e97df))

* PATCH: fix project/folder-tree path ([`4ba4d60`](https://github.com/bimdata/python-api-client/commit/4ba4d60c3a8aabce89ff8afeae0508c68b3b579f))

* PATCH: test CI ([`adc39fc`](https://github.com/bimdata/python-api-client/commit/adc39fc781cdd9a9ed918275b4bff629cb761483))

### Unknown

* CI: fix python-semantic release build env. ([`040ba18`](https://github.com/bimdata/python-api-client/commit/040ba18185d1c246a83dd0a744ff383e7155b9e9))

* CI: Chores/fix semantic release (#7)

* MINOR: test

* Fix the semantic release

* fix build command. ([`0699c41`](https://github.com/bimdata/python-api-client/commit/0699c41778f403a5b89b86ad40b7cff2b233e07b))

* debug-ci ([`17a3396`](https://github.com/bimdata/python-api-client/commit/17a3396d169d935d829b691bc86011c3fb4a76b0))

* TEST-CI: Fix typo. ([`5c04e87`](https://github.com/bimdata/python-api-client/commit/5c04e8750d726d0785be8fbae19500584797f66f))

* Merge pull request #5 from bimdata/chores/new-ci-publish-workflow

Trying to rework the ci for pypi upload. ([`77d82aa`](https://github.com/bimdata/python-api-client/commit/77d82aaf6e6ecda0f1d5b1878a2d53c9cc119ca7))

* Trying to rework the ci for pypi upload. ([`b8d0ce5`](https://github.com/bimdata/python-api-client/commit/b8d0ce5cb2901e2402bcc1d41d083ed9cd1f5d07))

* Merge pull request #4 from bimdata/fix/fix-ci-twine-error

Upgrade twine. ([`983d34b`](https://github.com/bimdata/python-api-client/commit/983d34b5f1f4e09c0a8404913eecf11e5c646d7f))

* Upgrade twine. ([`a9fdc9d`](https://github.com/bimdata/python-api-client/commit/a9fdc9d0f7c0e571ee4bb009189bc5ff36178278))

* Minor: Add ability to invite user in cloud &amp; all projects (#744)

* Minor: Add ability to invite user in cloud &amp; all projects

* Improve performance &amp; fixes

* Fix cloud invite when project invite already exists

* Fix more bugs in invitation process.

* Fix bug where last admin can leave if an admin invit exists.

* Remove useless sql query. ([`5f6f792`](https://github.com/bimdata/python-api-client/commit/5f6f792c345a63ca3bf924103f98db820a9f31b0))

* Test CI. ([`bd00ba2`](https://github.com/bimdata/python-api-client/commit/bd00ba2fd8f0aa76a5b2ccebad14d366524e929d))

* test CI ([`2b2db82`](https://github.com/bimdata/python-api-client/commit/2b2db826c3e729faf92d76ddc8f1b46723ba2a91))


## v9.22.2 (2023-11-27)

### Fix

* PATCH: restore viewpoint patch (#706)

* restore viewpoint patch

* use ModelViewSet ([`c2d241f`](https://github.com/bimdata/python-api-client/commit/c2d241f23c68d4ea0e534d3cc5aca6fb990690a2))


## v9.22.1 (2023-11-27)

### Fix

* PATCH: forbid to non admin to create topic properties (#705)

* forbid to non admin to create topic properties

* remvoe prints

* users and guests can only edit their own BCFs

* remove PUT viewpoint route

* fix import

* code optimization

* remove dead code ([`792e47f`](https://github.com/bimdata/python-api-client/commit/792e47f4406fc1c1008f5fe6f44dae5b9bd88f6e))


## v9.22.0 (2023-10-27)

### Feature

* MINOR: add viewpoint models field (#702)

* MINOR: add viewpoint models field

* fix typos ([`6f3768c`](https://github.com/bimdata/python-api-client/commit/6f3768c3c8512cb0c4ebd5836220a6e59f1adb65))


## v9.21.1 (2023-10-19)

### Fix

* PATCH: add geometry to ZoneSpace ([`4832e71`](https://github.com/bimdata/python-api-client/commit/4832e7169cae8ec549053fb17a58a6866c69ca98))


## v9.21.0 (2023-09-25)

### Feature

* MINOR: add routes to manage zone_space relations (#690) ([`68bc812`](https://github.com/bimdata/python-api-client/commit/68bc81277d1ba297a771ca9fcc2eae6c078c6f34))


## v9.20.2 (2023-09-25)

### Fix

* PATCH: zone: parent_id field may be null ([`3aec51b`](https://github.com/bimdata/python-api-client/commit/3aec51b2eac56ab36976e05211e1b13ea09ef96a))


## v9.20.1 (2023-09-21)

### Fix

* PATCH: add id project to serializer getProjectFolderTreeSerializers ([`fbe126b`](https://github.com/bimdata/python-api-client/commit/fbe126ba7320faa09ead023384a7e8b41c5e7a0b))


## v9.20.0 (2023-09-14)

### Feature

* MINOR: order in zones and spacezones ([`2b6e416`](https://github.com/bimdata/python-api-client/commit/2b6e4160fb3010d6cb2aed943172483e2e551118))


## v9.19.1 (2023-09-07)

### Fix

* PATCH: add history_count to document serialization and prefetch stuff ([`261a2e6`](https://github.com/bimdata/python-api-client/commit/261a2e6cf557e73cfd2d3f993fbff37866f396e5))


## v9.19.0 (2023-09-07)

### Feature

* MINOR: Add SSO create user route(#674)

* create-user route

* email_impersonation in project access token ([`93f86a5`](https://github.com/bimdata/python-api-client/commit/93f86a5d04193e0c6361d9cfee461f4091d59416))


## v9.18.2 (2023-09-06)

### Fix

* PATCH: Add document history count (#681)

* add document history count

* typo fixe ([`a2f63e3`](https://github.com/bimdata/python-api-client/commit/a2f63e3ce5f5f74e4424ed7f8d33540a322ac5e3))


## v9.18.1 (2023-09-01)

### Fix

* PATCH: fix bcf excel export documentation ([`4054f7c`](https://github.com/bimdata/python-api-client/commit/4054f7c0aba4a707528736a9dee98c2c14933727))


## v9.18.0 (2023-08-30)

### Feature

* MINOR: Add xlsx export (#676)

* action xlsx export

* black

* add documentation

* add BIMData logo

* poetry update

---------

Co-authored-by: Amoki &lt;hugo@bimdata.io&gt; ([`953ab41`](https://github.com/bimdata/python-api-client/commit/953ab414de0dcec8e23237bb0da99251b4041aa9))


## v9.17.0 (2023-08-30)

### Feature

* MINOR: feat(organization): add main_model field to Project model ([`391aa88`](https://github.com/bimdata/python-api-client/commit/391aa888082ac451c6fd742b167a58eb567dfaad))


## v9.16.1 (2023-08-24)

### Fix

* PATCH: add z field to geometryPoint ([`0fc0507`](https://github.com/bimdata/python-api-client/commit/0fc05073daec5f8d22a2a237a5ddf79856f3118c))


## v9.16.0 (2023-08-09)

### Feature

* MINOR: add space geometry (#672)

* add space geometry

* restor deleted code line ([`0670d25`](https://github.com/bimdata/python-api-client/commit/0670d25901e4923b1d65fdbca2249a8a5bf11597))


## v9.15.1 (2023-07-07)

### Fix

* PATCH: add head_id field to Document serializer (#669) ([`02c7125`](https://github.com/bimdata/python-api-client/commit/02c71259431aa17f56c50fafe8ecef2e61702860))


## v9.15.0 (2023-06-22)

### Feature

* MINOR: import from project route (#664)

* feat: clone project route

* renaming route, reverse pk and project_id

* renaming

* simpler help text ([`7e45889`](https://github.com/bimdata/python-api-client/commit/7e4588908ae01e5763e65058eccdf7852a2180da))


## v9.14.0 (2023-06-20)

### Feature

* MINOR: Add pins routes (#663)

* WIP: add pins detail views

* fix view and add tests ([`8ad8d81`](https://github.com/bimdata/python-api-client/commit/8ad8d81e62fd9c2f9083a4bc6c4908fed4f4aac3))


## v9.13.1 (2023-06-15)

### Fix

* PATCH: add parent_id field in model ([`7ec69f0`](https://github.com/bimdata/python-api-client/commit/7ec69f034ceaa5620ef3a68b254375d832be3ee7))


## v9.13.0 (2023-06-05)

### Feature

* MINOR: add project description (#659) ([`7d29aa4`](https://github.com/bimdata/python-api-client/commit/7d29aa46f1839229a97cb06c517d9a40315b965c))

### Unknown

* ci: update GA versions ([`c7e492e`](https://github.com/bimdata/python-api-client/commit/c7e492e6eff278541d7ac866ad384088bc51bd71))


## v9.12.0 (2023-05-17)

### Feature

* MINOR: add xkt_files fields to support many xtk versions (#647)

* add xkt_files fields to support many xtk versions

* fix xkt_file serialization, add admin, migrate data to XktFile

* add unique xkt version constraint ([`1b3009c`](https://github.com/bimdata/python-api-client/commit/1b3009c81b2e5e3a189ed61e34345885803a83f2))


## v9.11.3 (2023-05-16)

### Fix

* PATCH: add filters to getRawElements and getSimpleElements ([`1bf3b71`](https://github.com/bimdata/python-api-client/commit/1bf3b7188e48b5697cbd008bbbd41ac198fcbd16))


## v9.11.2 (2023-04-26)

### Fix

* PATCH: allow null cloud serializer + add sub field to userproject (#643) ([`8d8ad1c`](https://github.com/bimdata/python-api-client/commit/8d8ad1c438519e2a63f5d8cef203f9ecd27042a0))


## v9.11.1 (2023-04-26)

### Fix

* PATCH: add office_preview to dms-tree serializer ([`4afbee7`](https://github.com/bimdata/python-api-client/commit/4afbee7f7205b8fd767aab0abf376b60b8e515cc))


## v9.11.0 (2023-04-25)

### Feature

* MINOR: add document-preview (#642)

* add document-preview

* add admin reprocess

* rename field ([`ce78abd`](https://github.com/bimdata/python-api-client/commit/ce78abdfe55727155d5c94ce9b73ea9d1db56023))


## v9.10.7 (2023-04-20)

### Fix

* PATCH: Feat/permission explicit propagate (#636)

* add delete permission route, remove signals implicit propagation

* explicit propagation for permissions

* remove useless tests

* fix nested group folder serializer

* include delete groupFolder in update route ([`5eca95a`](https://github.com/bimdata/python-api-client/commit/5eca95ae72a16146fd80159b081749529464f728))


## v9.10.6 (2023-04-18)

### Fix

* PATCH: fix ordering pdf pages (#638) ([`1f9ffe8`](https://github.com/bimdata/python-api-client/commit/1f9ffe8da45895f1262475ea73d3ddee52a75eaa))


## v9.10.5 (2023-04-17)

### Fix

* PATCH: add id field to Pin ([`395d86c`](https://github.com/bimdata/python-api-client/commit/395d86c06bef50cc68b9e5f440f059addd8c5678))


## v9.10.4 (2023-03-09)

### Fix

* PATCH: fix requestBody on simple delete route ([`ece7509`](https://github.com/bimdata/python-api-client/commit/ece7509ed7e31a24ef3347245bfd7f9331f1f8fe))


## v9.10.3 (2023-03-02)

### Fix

* PATCH: add model.binary_2d_file field ([`4bd519d`](https://github.com/bimdata/python-api-client/commit/4bd519d8a800557f2ba434d5a43a0a4f6c6273a9))


## v9.10.2 (2023-02-06)

### Fix

* PATCH: remove some useless field on dms-tree ([`035c4e4`](https://github.com/bimdata/python-api-client/commit/035c4e4e7f63f75ffd9acc69478ba4265133a096))


## v9.10.1 (2023-01-27)

### Fix

* PATCH: force request body on delete method with drf-spectacular (#615) ([`206ee31`](https://github.com/bimdata/python-api-client/commit/206ee31fdd0ade562478a39ba5f7d1caa2ae0991))


## v9.10.0 (2023-01-16)

### Feature

* MINOR: add marketplace app links (#609) ([`c28d8c1`](https://github.com/bimdata/python-api-client/commit/c28d8c161d7341866d8bf3ed6afba861bba0c0e2))


## v9.9.0 (2023-01-05)

### Feature

* MINOR: Remove folder groups and history fields form DMS-Tree(#599)

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

* PATCH: Feat/multipage pdf (#596)

* create multipage-pdf

* fix create_model tests

* fix tests

* add explicit comment to signal function

* update help_text for parent and children ([`0eaaff0`](https://github.com/bimdata/python-api-client/commit/0eaaff0c974a843dc80316c30af6059a4870737e))


## v9.8.0 (2022-12-20)

### Feature

* MINOR: create import group from ids (#595)

* feat: create import group from id

* remove UserProject property, add select_related to userprojects queryset

* import several groups from a project instead of one ([`b0459fd`](https://github.com/bimdata/python-api-client/commit/b0459fdd1f71ee919cc1963f0c82b5a51b145451))


## v9.7.0 (2022-12-06)

### Feature

* MINOR: add project check access route(#561)

* Add projcte check-access route

* add route description

* update tests with new invitation routes ([`bfb2c05`](https://github.com/bimdata/python-api-client/commit/bfb2c05b2e5ac3247f359ad45006f95b54b43037))


## v9.6.12 (2022-11-30)

### Fix

* PATCH: fix model export doc response ([`aa8fbfd`](https://github.com/bimdata/python-api-client/commit/aa8fbfd7a717ba3a5d1c2074effd81ea07b43d18))


## v9.6.11 (2022-11-16)

### Fix

* PATCH: added missing value (client name) to User Invitation Serializer (#590) ([`19b7898`](https://github.com/bimdata/python-api-client/commit/19b78982253fe658aa0008866a6fab0bbc58d448))


## v9.6.10 (2022-11-09)

### Fix

* PATCH: create DMS Tree return same datas as the get route (#587) ([`8ec4ab1`](https://github.com/bimdata/python-api-client/commit/8ec4ab1be66e53ff4d49c782867b8bed5d557058))


## v9.6.9 (2022-11-09)

### Fix

* PATCH: create DMS Tree return same datas as the get route (#587) ([`5bd84de`](https://github.com/bimdata/python-api-client/commit/5bd84de4148c2c19adcff8a8f5acc9d4ff55a2d8))


## v9.6.8 (2022-11-07)

### Fix

* PATCH: fix model deserialization ([`623b8f6`](https://github.com/bimdata/python-api-client/commit/623b8f6234b83b65e312e609d6513f13a5c15171))


## v9.6.7 (2022-10-21)

### Fix

* PATCH: rename model 360 field (#576)

* rename model 360 field

* keep viewer_360_file field

* remove useless field in write only serializer ([`8de9eae`](https://github.com/bimdata/python-api-client/commit/8de9eaebf5e2991649ccd08332b37ce6db8fac8c))


## v9.6.6 (2022-10-18)

### Fix

* PATCH: rename request param in patch user cloud (#572) ([`2907dd6`](https://github.com/bimdata/python-api-client/commit/2907dd671f669f95d72ae0bb34e3d611ebdeacb4))


## v9.6.5 (2022-10-11)

### Fix

* PATCH: fix bad body serializer linkDocumentsOfElement ([`81cff13`](https://github.com/bimdata/python-api-client/commit/81cff13e6c4e8b35db22a022735e269d828b749c))

### Unknown

* Merge pull request #3 from mdonkorka/patch-1

Adding Improvements ([`90e08ad`](https://github.com/bimdata/python-api-client/commit/90e08add9dafd4542726cb72e91f32260041b5bf))

* Updating setup.py

Adding improvements to setup.py file ([`ea98780`](https://github.com/bimdata/python-api-client/commit/ea98780ffa789029fbb4100f8d58bf3361441334))

* Adding improvements ([`445acff`](https://github.com/bimdata/python-api-client/commit/445acffab82cf29598de5ad2f27ddb32cdd0f7f1))


## v9.6.4 (2022-10-10)

### Fix

* PATCH: fix #536 body in linkDocumentsOfElement ([`01b3da8`](https://github.com/bimdata/python-api-client/commit/01b3da8507448e88b30946aaf5911475aabffad9))


## v9.6.3 (2022-10-07)

### Fix

* PATCH: created_at and responded_at in Invitation model (#570)

* created_at and updated_at in Invitation model

* invitation: manual responded_at field ([`dc7063d`](https://github.com/bimdata/python-api-client/commit/dc7063dac2b4d3f6839d12248b708eb4d0b54a06))


## v9.6.2 (2022-10-07)

### Fix

* PATCH: cloud_id and project_id in Invitation serializer ([`d7315c0`](https://github.com/bimdata/python-api-client/commit/d7315c0b017a7f475bc79b960feb5d31b73a14e0))


## v9.6.1 (2022-10-06)

### Fix

* PATCH: Update fields of userInvitation serializer ([`88f7294`](https://github.com/bimdata/python-api-client/commit/88f7294512206fef11de7cce399d3c6e56344fa6))


## v9.6.0 (2022-10-06)

### Feature

* MINOR: user invitation routes  (#569)

* make invitation api updatable

* add user:write scope

* use many to many scopes in views and tests

* set scopes in MarketplaceAppAuthorization view ([`2f7d1d4`](https://github.com/bimdata/python-api-client/commit/2f7d1d45f528616b5b5921d06fec8cd36be2ca83))


## v9.5.0 (2022-09-14)

### Feature

* MINOR: Point cloud ([`5f4bd06`](https://github.com/bimdata/python-api-client/commit/5f4bd06b2a5603b59130f8fc4037a9960c7287ac))


## v9.4.9 (2022-09-09)

### Fix

* PATCH: allow empty file on document upload ([`32585b1`](https://github.com/bimdata/python-api-client/commit/32585b1ed8aeef00f45cae6efa8fae0ad51e5c54))


## v9.4.8 (2022-09-07)

### Fix

* PATCH: allow empty files ([`c191c95`](https://github.com/bimdata/python-api-client/commit/c191c958362b0f2cf4d66232e592f683f6378c55))


## v9.4.7 (2022-08-29)

### Fix

* PATCH: Fix/inline serializer fields (#560)

Fix CreateStoreyPlan and BuildingStoreyPlan ([`6b706ce`](https://github.com/bimdata/python-api-client/commit/6b706ce71d28225513dd83a52e9f9e232f8fa00f))


## v9.4.6 (2022-08-09)

### Fix

* PATCH: fix project access token enum (#555) ([`1005bc4`](https://github.com/bimdata/python-api-client/commit/1005bc47ee0d8369a8ffbc0b98a532aff4c2b812))


## v9.4.5 (2022-08-03)

### Fix

* PATCH: add response data to create DMSTree ([`66c3969`](https://github.com/bimdata/python-api-client/commit/66c3969287fe9de08f80a5d60cb9b4bef702ae3d))


## v9.4.4 (2022-06-24)

### Fix

* PATCH: Add authoring viewpoint fields (#547) ([`5d0a18b`](https://github.com/bimdata/python-api-client/commit/5d0a18b4752fb192b0d8023677099794cc4c77e7))


## v9.4.3 (2022-06-22)

### Fix

* PATCH: fix get-dms-tree serializer ([`ce53acf`](https://github.com/bimdata/python-api-client/commit/ce53acff6a0c3977f1c71c2e73c25b054b60dde1))


## v9.4.2 (2022-06-22)

### Fix

* PATCH: fix create-dsm-tree serializer ([`9f58aae`](https://github.com/bimdata/python-api-client/commit/9f58aae36e98cd7aa7cf5f5538c0645af99f4c50))


## v9.4.1 (2022-06-16)

### Fix

* PATCH: improve viewpoint pins (#543) ([`7a42412`](https://github.com/bimdata/python-api-client/commit/7a424129ec9ec62252018a17476afcffe01c1acb))


## v9.4.0 (2022-06-09)

### Feature

* MINOR: Add BCF authoring tool (#540) ([`f8da5ba`](https://github.com/bimdata/python-api-client/commit/f8da5ba89f43f67cba93336c5031849ba0acdcd5))


## v9.3.10 (2022-05-13)

### Fix

* PATCH: fix create dms tree doc, children was missing in serializer request (#531)

* fix create dms tree doc, children was missing in serializer request

* rename serializer ([`f734b1b`](https://github.com/bimdata/python-api-client/commit/f734b1b19270e293610b98951ebe44d098718001))


## v9.3.9 (2022-05-12)

### Fix

* PATCH: add tag to document in dms-tree (#533) ([`4ffe2ea`](https://github.com/bimdata/python-api-client/commit/4ffe2ea7d309477ebf5305b4b80ae6d3f47ea3fd))


## v9.3.8 (2022-05-10)

### Fix

* PATCH: versioning: more permissive archi (#528) ([`4cb18fd`](https://github.com/bimdata/python-api-client/commit/4cb18fdbc2ebf3de4de3e82c183ff5f43c80a929))


## v9.3.7 (2022-05-05)

### Fix

* PATCH: rename operation_id ([`e04c180`](https://github.com/bimdata/python-api-client/commit/e04c180145e8ab619657a38b6c3a59c4eb13b1eb))


## v9.3.6 (2022-05-05)

### Fix

* PATCH: delete all document version on delete (#525)

* delete all document version on delete

* versioning: add delete history route ([`9aa819b`](https://github.com/bimdata/python-api-client/commit/9aa819bd370259e21f61686a2903f34069bcaada))


## v9.3.5 (2022-05-04)

### Fix

* PATCH: add document_id to visa serializer ([`2ec598a`](https://github.com/bimdata/python-api-client/commit/2ec598a2b1bdc0ebdf270e7c74df463327a2db28))


## v9.3.4 (2022-05-04)

### Fix

* PATCH: visa serialization in document (#522)

* visa serialization in document

* no prefetch tag ([`213c4d7`](https://github.com/bimdata/python-api-client/commit/213c4d7141e9c5c8fc00d80e21739d1dfa2f8bf8))


## v9.3.3 (2022-05-03)

### Fix

* PATCH: reorder document history ([`c1afe9e`](https://github.com/bimdata/python-api-client/commit/c1afe9ea010a61da0ed2d0c0c7e43437e56bd311))


## v9.3.2 (2022-05-02)

### Fix

* PATCH: serialize document creator ([`cb1f35c`](https://github.com/bimdata/python-api-client/commit/cb1f35c2348a89acb7f8f0b3d47ff5d86e4eb80b))


## v9.3.1 (2022-04-29)

### Fix

* PATCH: remove parent from document serialization (#521) ([`fbc5445`](https://github.com/bimdata/python-api-client/commit/fbc544512b74cc852b2b6f155cb2b62b79122289))


## v9.3.0 (2022-04-29)

### Feature

* MINOR: Feat/versionning (#517)

* add model, migrations, views, serializers

* test DocumentHistory view

* fix last tests

* filter list model

* fix migration and add reverse_code

* renaming old_version_id ([`d562d95`](https://github.com/bimdata/python-api-client/commit/d562d9583f76b61f0f6ddf97ec80150a6fd6b902))


## v9.2.0 (2022-04-21)

### Feature

* MINOR: add bcf pins (#515)

* add bcf pins

* add view tests ([`8948499`](https://github.com/bimdata/python-api-client/commit/8948499b4f427735081404a23b9c68fe2f1b12d4))


## v9.1.1 (2022-04-20)

### Fix

* PATCH: fix createDocument response missing ([`a7a4208`](https://github.com/bimdata/python-api-client/commit/a7a4208fa4163eb55e82628a570e743e217b85c3))


## v9.1.0 (2022-04-15)

### Feature

* MINOR: create document tag views (#513)

* create document tag views

* fix: serializer readOnly

* add admin tags

* add inline Tag Project ([`3c00f75`](https://github.com/bimdata/python-api-client/commit/3c00f752a14f58a4fc38ed9a3ff03ba54e005580))


## v9.0.0 (2022-04-12)

### Breaking

* MAJOR: Feat/openapi3 (#508)

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

Co-authored-by: Amoki &lt;hugo@bimdata.io&gt; ([`57074b7`](https://github.com/bimdata/python-api-client/commit/57074b73f37e92e1ee0b37cdfde59b3ccd7bdd80))

### Fix

* PATCH: fix swagger generation ([`3952685`](https://github.com/bimdata/python-api-client/commit/3952685f9c92059b94605b178693de95cd670f1d))


## v8.0.0 (2022-04-12)

### Breaking

* MAJOR: Feat/openapi3 (#508)

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

Co-authored-by: Amoki &lt;hugo@bimdata.io&gt; ([`18591ec`](https://github.com/bimdata/python-api-client/commit/18591ec7c8156e00549d7d604500a0773b79463a))


## v7.4.2 (2022-03-17)

### Fix

* PATCH: remove comment visa nested (#502) ([`a516af8`](https://github.com/bimdata/python-api-client/commit/a516af86ac3aa3ef6858f1b75c7f36e182bf7c45))


## v7.4.1 (2022-02-25)

### Fix

* PATCH: fix create building and storey doc serializer ([`03903e7`](https://github.com/bimdata/python-api-client/commit/03903e7c077a08434ad587401dc691c5e2c8b646))


## v7.4.0 (2022-02-25)

### Feature

* MINOR: order plans in storey (#495)

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

* MINOR: refacto storeys and add buildings (#494)

* init refacto storey

* add building test

* fix serializers

* replace Counter ([`06a735c`](https://github.com/bimdata/python-api-client/commit/06a735c75412fdfb301f7e10ecb29a5e4275afe7))


## v7.2.0 (2022-02-24)

### Feature

* MINOR: add size_ratio fields ([`2a5d90c`](https://github.com/bimdata/python-api-client/commit/2a5d90c51c5de429d10d6cf1f4d5da9da5448093))


## v7.1.2 (2022-02-24)

### Fix

* PATCH: bcf detailed extensions labels ([`7d5ade7`](https://github.com/bimdata/python-api-client/commit/7d5ade750437b1e5007c4434fdaabfd1c54d9dc9))


## v7.1.1 (2022-02-23)

### Fix

* PATCH: add creadted_at and upated_at to Propertie et PropertySet ([`9218cd7`](https://github.com/bimdata/python-api-client/commit/9218cd7ae22192003e0e09017565940604bff67c))


## v7.1.0 (2022-02-15)

### Feature

* MINOR: Feature/bcf colors (#485)

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

* PATCH: rename last ifc operations (#489) ([`6a0bce1`](https://github.com/bimdata/python-api-client/commit/6a0bce138e8adad44c462cec339d523fc33cc346))


## v7.0.0 (2022-02-04)

### Breaking

* MAJOR: rename ifc to model (#477)

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

* don&#39;t unzip unzipped structure files

* fix bad rebase ([`6d48496`](https://github.com/bimdata/python-api-client/commit/6d48496db3d7b9f80e1ffcfe407873046383e516))


## v6.0.0 (2022-02-04)

### Breaking

* MAJOR: sync with js libs ([`eb430f5`](https://github.com/bimdata/python-api-client/commit/eb430f5f2a77313a510db067276c7fe520c28adc))


## v5.22.0 (2022-01-31)

### Feature

* MINOR: 2d positioning (#471)

* filter storey models with permissions

* rework storey serializer

* add positioning plan to m2m (storey-plan)

* add route with params id and positioning route renaming

* include positioning in storey serializer

* fix tests ([`f8bf0c8`](https://github.com/bimdata/python-api-client/commit/f8bf0c8b641cb613d99d7a116ecd8377fab46245))


## v5.21.1 (2022-01-31)

### Fix

* PATCH: filter storey models with permissions and add models_unreachable_count field (#470)

* filter storey models with permissions

* fix test add model to storey

* rework storey serializer ([`b68c55a`](https://github.com/bimdata/python-api-client/commit/b68c55a4665fda225fd205dac533f64d9dca9ee8))


## v5.21.0 (2022-01-31)

### Feature

* MINOR: add img_format=url in BCF routes (#472) ([`9cef689`](https://github.com/bimdata/python-api-client/commit/9cef6891bd435d25098035e413489bb6735515c2))


## v5.20.1 (2022-01-28)

### Fix

* PATCH: one storey site by building (#469)

* one storey site by building

* add db unique constraint

* Update ifc/v1/views.py

Co-authored-by: Hugo Duroux &lt;hugo@bimdata.io&gt;

* Update ifc/v1/views.py

Co-authored-by: Hugo Duroux &lt;hugo@bimdata.io&gt;

Co-authored-by: Hugo Duroux &lt;hugo@bimdata.io&gt; ([`7c907c8`](https://github.com/bimdata/python-api-client/commit/7c907c80cb76328f174e414efb73850ca81dc188))


## v5.20.0 (2022-01-27)

### Feature

* MINOR: plans and storeys (#468)

* create storey

* add migrations and route manage model children

* create metabuilding and relation between storey and model-plans

* fix signal test

* PR review

* models can update name ([`6a125d1`](https://github.com/bimdata/python-api-client/commit/6a125d1eebe97eacd063a6ef2001c9057ac57cb2))


## v5.19.1 (2022-01-18)

### Fix

* PATCH: Add non automatic models (#464)

* Add non automatic models

* improve tests

* rename route and add permissions

* add model delete with doc ([`b224801`](https://github.com/bimdata/python-api-client/commit/b2248010f7890245d90e9b4f067e4ca96ea00a63))


## v5.19.0 (2022-01-14)

### Feature

* MINOR: Feature/smart files (#463)

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

* PATCH: (visa) add validations_in_error to serializer ([`e4df33f`](https://github.com/bimdata/python-api-client/commit/e4df33ffcaf01b3f60f7e214a2a64809d2befcf3))


## v5.18.2 (2022-01-04)

### Fix

* PATCH: fix document elements list uuids ([`39de959`](https://github.com/bimdata/python-api-client/commit/39de959c2a58e9ab3b5949542efe76456cd8cad9))


## v5.18.1 (2021-12-22)

### Fix

* PATCH: rename element_ids to element_uuids ([`461e3db`](https://github.com/bimdata/python-api-client/commit/461e3db667d2edba71b1596d694185f61d3233b5))


## v5.18.0 (2021-12-22)

### Feature

* MINOR: add element/documents route ([`68a02e7`](https://github.com/bimdata/python-api-client/commit/68a02e7d227d78ef2e4efd9bdfbe82b1b686cf89))


## v5.17.1 (2021-12-13)

### Fix

* PATCH: add document to visa serializer (#458) ([`7504aee`](https://github.com/bimdata/python-api-client/commit/7504aee678ed033bcbe517ab9fcfe7c54776bfcf))


## v5.17.0 (2021-12-09)

### Feature

* MINOR: Feature/link element document (#457)

* add documents to elements

* add test for filterred ifc and document list

* typo

* add some query optimizations ([`92814d1`](https://github.com/bimdata/python-api-client/commit/92814d193cd97e2feddbed979806ed702db7301d))


## v5.16.0 (2021-12-06)

### Feature

* MINOR: Feature/visa (#451)

* add invitation to userProject

* PR changes requests

* init visa

* fix: boolean swagger bad import

* fix: git conflict migrations, replace tests &#39;put&#39;

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

* PATCH: add id to Public Organization Serializer ([`5ac3574`](https://github.com/bimdata/python-api-client/commit/5ac357430084e206b40537112334d8de4075f805))


## v5.15.1 (2021-12-02)

### Fix

* PATCH: add organization serializer in App and MPApp serializers (#452)

* add organization serializer in App and MPApp serializers

* fix test and add select related

* use Public Organization Serializer ([`b1f0958`](https://github.com/bimdata/python-api-client/commit/b1f0958e511655ca19ddbf52ab35fbb1d1fd1fc2))


## v5.15.0 (2021-11-24)

### Feature

* MINOR: Remove deprecated and put (#450)

* remove deprecated route and PUT route without BCF routes

* fix some tests

* fix last tests and restore project tree route

* restore BCF tests change

* rename fullUpdate operation ([`5769df5`](https://github.com/bimdata/python-api-client/commit/5769df5195f22e65696b4c46ed1a8ee925634526))

* MINOR: Add leave project route (#449)

* Add leave project route

* fix roles ([`4d52c51`](https://github.com/bimdata/python-api-client/commit/4d52c51628bf3e977074dfec3d8af51615a13c2d))

### Fix

* PATCH: fix semantic release ([`aca3560`](https://github.com/bimdata/python-api-client/commit/aca3560c5d69a91d32be6992c0d8aea1153110b4))

* PATCH: fix serializer user project (#448)

Breaking Change:
 -  key to  for GroupUser create view
 - Route pk for userProject views is now UserProject pk and not FosUser pk

Some other change:
- fix serializer of userProject for swagger and libs
- add missing invitation user project from project and group
- fix some test ([`8b5446a`](https://github.com/bimdata/python-api-client/commit/8b5446a58252f767665f6cd3fff59af93baddfbd))

* PATCH: add invitation key in UserProject ([`30a8fb5`](https://github.com/bimdata/python-api-client/commit/30a8fb5ad88a6aed47de4bcb69a34cd37702e5ff))

* PATCH: get cloud size operation id in openapi ([`d508862`](https://github.com/bimdata/python-api-client/commit/d5088627492eec9d1ea02a8915cfb1d7ed4ce09c))

* PATCH: fix list/create methods openAPI ([`7519d93`](https://github.com/bimdata/python-api-client/commit/7519d931205caffc57f964e92e0547714d916304))


## v5.14.0 (2021-09-13)

### Feature

* MINOR: serialize user-permissions on documents ([`8597421`](https://github.com/bimdata/python-api-client/commit/859742176f6e0827c170dd8d30c95c254d502fcc))

* MINOR: Add profile_picture field in user serialization

* add user picture field

* fix user.company, add comment about an edge case ([`45bd37c`](https://github.com/bimdata/python-api-client/commit/45bd37ce3e9ead5bb4050fa2a26a609a64e8ac26))

* MINOR: add GED permissions ([`00b987a`](https://github.com/bimdata/python-api-client/commit/00b987af3d7f310c07beb9d30c7354b9e5830d26))

* MINOR: allow bigger guids (#420) ([`54b2b09`](https://github.com/bimdata/python-api-client/commit/54b2b090cbbf127cf8ac0f17c3492e6d0e1c7f29))

### Fix

* PATCH: allow empty name in raw layers and raw materials ([`b96d9a7`](https://github.com/bimdata/python-api-client/commit/b96d9a7eb1e3828fd2b3f7e9edb558b296d38f0b))

* PATCH: allow empty name in raw layers and raw materials ([`c0d6bb6`](https://github.com/bimdata/python-api-client/commit/c0d6bb6f662d3289915da48580553bb2277c7ee7))

* PATCH: allow empty name in raw layers and raw materials ([`22e450d`](https://github.com/bimdata/python-api-client/commit/22e450d38322621610ca85750524c94dd197f33c))

* PATCH: fix dms-tree group permissions ([`38f8ce5`](https://github.com/bimdata/python-api-client/commit/38f8ce5608ad11f8dd1518a9a901da5ef8779bdd))

* PATCH: fix field name and add field to children dms-tree (#426) ([`2881af8`](https://github.com/bimdata/python-api-client/commit/2881af81fb7ae5fe2718f8187ffc5ae350aa4ebd))

### Unknown

* PATH: fix pypi publish ([`600789d`](https://github.com/bimdata/python-api-client/commit/600789ddce7ada2d43ab5cf50b574ad21525d4ae))

* ci: fix demantic ([`6807364`](https://github.com/bimdata/python-api-client/commit/68073648242cbc9505d2f6830f21559ef6808995))

* ci: temp fix ([`2a0abec`](https://github.com/bimdata/python-api-client/commit/2a0abec9441482be64ad58085d582a91fe843e34))

* ci: setup GA ([`f75f8d6`](https://github.com/bimdata/python-api-client/commit/f75f8d6493763abd7d4e339be26bca8930e0716e))

* init github action ([`f68e183`](https://github.com/bimdata/python-api-client/commit/f68e183162ca83c5fec818753e71fab688d2e59c))


## v5.13.3 (2021-06-02)

### Fix

* PATCH: fix raw element serializer ([`e71a065`](https://github.com/bimdata/python-api-client/commit/e71a0653503541b72f556149e3108134cbbd89f2))

### Unknown

* add generate swagger script ([`70f974b`](https://github.com/bimdata/python-api-client/commit/70f974b6c1cbbac32814c916d583e5c264076ab0))


## v5.13.2 (2021-05-24)

### Fix

* PATCH: (raw element) key named material_list instead of materials ([`b2e94e0`](https://github.com/bimdata/python-api-client/commit/b2e94e03dc847ffbe507799810f8ec9167f3bcad))


## v5.13.1 (2021-05-24)

### Fix

* PATCH: fix(raw element): material_ids is integer and add id properties ([`c5f3ac4`](https://github.com/bimdata/python-api-client/commit/c5f3ac456cc5ff143d25231e9c745fca6aa15f6c))


## v5.13.0 (2021-05-21)

### Feature

* MINOR: add recommanded_2d_angle (#403) ([`60bb446`](https://github.com/bimdata/python-api-client/commit/60bb446730a3a8636de676dc0baa15b47d7ea347))


## v5.12.1 (2021-05-19)

### Fix

* PATCH: fix some open api fields (#401) ([`a0757ca`](https://github.com/bimdata/python-api-client/commit/a0757ca1683cbaab1691fd083943ab69a5cb3168))


## v5.12.0 (2021-05-05)

### Feature

* MINOR: serialization mpApp.organization_id ([`86dd09b`](https://github.com/bimdata/python-api-client/commit/86dd09b03bdade1f22f5d7742a09782935086bc8))


## v5.11.0 (2021-04-16)

### Feature

* MINOR: add ifc north vector (#394) ([`58ef3ac`](https://github.com/bimdata/python-api-client/commit/58ef3aca21afa401496830d7b5384b04c844eca3))


## v5.10.0 (2021-04-13)

### Feature

* MINOR: add ifc version (#392) ([`266ac60`](https://github.com/bimdata/python-api-client/commit/266ac6032648ad0d5d0a72f8af058969071d913a))


## v5.9.0 (2021-04-07)

### Feature

* MINOR: add ifc.archived field ([`f3d2eee`](https://github.com/bimdata/python-api-client/commit/f3d2eeeccbaf6ac76636f15d90f65c9e3a8d25e2))


## v5.8.1 (2021-01-26)

### Fix

* PATCH: fix BCF projects serialization ([`5fa5f0b`](https://github.com/bimdata/python-api-client/commit/5fa5f0b7eaaa6fcd4ac7990892ae63eb5d620723))


## v5.8.0 (2020-11-23)

### Feature

* MINOR: add delete all pset route ([`f08cb86`](https://github.com/bimdata/python-api-client/commit/f08cb8676eb700237f00d959ae9b084daeeb5f1a))


## v5.7.0 (2020-08-01)

### Feature

* MINOR: add project access token ([`142080f`](https://github.com/bimdata/python-api-client/commit/142080f499348df876d6c31bb35afbe00fbb07a7))


## v5.6.1 (2020-03-30)

### Fix

* PATCH: fix document type enum ([`eb0d75d`](https://github.com/bimdata/python-api-client/commit/eb0d75df86e8a0a48ca758e429000d5c8fc7913f))


## v5.6.0 (2020-03-27)

### Feature

* MINOR: add merge and optimize routes ([`07bb292`](https://github.com/bimdata/python-api-client/commit/07bb292f1d14991506c08a2bf7b903e0259bb9a6))

### Unknown

* Merge pull request #2 from bimdata/feature/remove-circle-checkout-code

Feature/remove circle checkout code ([`49dbabf`](https://github.com/bimdata/python-api-client/commit/49dbabfddb576d3b816c84d86f5c1f080f553704))

* update tox config ([`e7db3e0`](https://github.com/bimdata/python-api-client/commit/e7db3e0c10551872fbcfb48c678fc3c29f053c16))

* remove circle checkout step ([`89edfd4`](https://github.com/bimdata/python-api-client/commit/89edfd4ade249122be4323666816cd10239f6264))


## v5.5.0 (2020-03-04)

### Feature

* MINOR: filtering by email for list cloud user and project user ([`fbd3b8b`](https://github.com/bimdata/python-api-client/commit/fbd3b8b20e7408a922f3dd4b3ea501a039fe0217))


## v5.4.0 (2020-03-02)

### Feature

* MINOR: Add IFC export route. Fix users deserialization when firstname and lastname are empty ([`f8766ce`](https://github.com/bimdata/python-api-client/commit/f8766ce37a659722c69d841c553a2a87f669f2dd))


## v5.3.1 (2020-02-25)

### Fix

* PATCH: add property_set_id to property serialization ([`7945a13`](https://github.com/bimdata/python-api-client/commit/7945a13402fd3d847674a6a0cac8d8908bdfc70f))


## v5.3.0 (2020-02-24)

### Feature

* MINOR: add property update route ([`b5425e4`](https://github.com/bimdata/python-api-client/commit/b5425e4c8cd7e050e537b569e471926ee8d65c7f))


## v5.2.0 (2020-02-20)

### Feature

* MINOR: add BCF import route ([`b2330e9`](https://github.com/bimdata/python-api-client/commit/b2330e93b02a91f9ee51b1f9778e8a6ee8b23202))


## v5.1.2 (2020-02-14)

### Fix

* PATCH: fix typo in BCF.Line object. From LineSeriaizer to Line ([`d72a96d`](https://github.com/bimdata/python-api-client/commit/d72a96de3a152814944093d5f33af9e80413db68))


## v5.1.1 (2020-02-10)

### Fix

* PATCH: methods can&#39;t be in many apis at the same times. Too many tools don&#39;t support it. ([`56c9283`](https://github.com/bimdata/python-api-client/commit/56c928326717f177a3462a31045559e2a39c50d7))


## v5.1.0 (2020-01-22)

### Feature

* MINOR: add optionnal document.ifc_source (default: UPLOAD) to specify the source of the IFC ([`41a16fc`](https://github.com/bimdata/python-api-client/commit/41a16fc6d7f9ac33cd1a2114c1e3c257bd88bffb))


## v5.0.2 (2020-01-21)

### Fix

* PATCH: project field of createDocument is no more mandatory ([`08788d0`](https://github.com/bimdata/python-api-client/commit/08788d05a66bee238b6c43e72745e2a9ba7cfbcb))


## v5.0.1 (2020-01-21)

### Fix

* PATCH: Fix System and Layers serialization in RawElements ([`611068c`](https://github.com/bimdata/python-api-client/commit/611068c14b772fd4aeb8e5495f22b12b099688de))


## v5.0.0 (2020-01-13)

### Breaking

* MAJOR: rename apis. See release for more info ([`7444421`](https://github.com/bimdata/python-api-client/commit/74444219b062643fceefb0dd7455b3377c19388b))


## v4.6.0 (2020-01-10)

### Feature

* MINOR: add params to ifc/export route ([`71dfe01`](https://github.com/bimdata/python-api-client/commit/71dfe01ce7ae809cae8dd2462a665dbbf12e90c4))


## v4.5.0 (2020-01-08)

### Feature

* MINOR: Add IFC warnings ([`8fab6fc`](https://github.com/bimdata/python-api-client/commit/8fab6fc9f13fcdcc722800faaa07ff750bddef1e))


## v4.4.0 (2019-12-18)

### Feature

* MINOR: add user deletion route, add IFC layers routes, add element/simple representation, add IFC Systems routes, add IFC errors route, fix some malformed operationId ([`4b899c9`](https://github.com/bimdata/python-api-client/commit/4b899c9cb149996025c5cbed572a5353cf92125b))


## v4.3.0 (2019-11-19)

### Feature

* MINOR: add provider field in user serilization ([`510c0ba`](https://github.com/bimdata/python-api-client/commit/510c0ba88511fe393156289ee5e71f380752d695))


## v4.2.2 (2019-11-08)

### Fix

* PATCH: Feature/description pypi (#1)

* add long description in setup; check readme syntax in circleci

* fix open import for py2

* fix command missing circleci ([`997f1e1`](https://github.com/bimdata/python-api-client/commit/997f1e11fcceaa63f42c39d3c1d44d5f92c882a2))


## v4.2.1 (2019-10-08)

### Fix

* PATCH: zone name is no more required ([`16c9b09`](https://github.com/bimdata/python-api-client/commit/16c9b09f30ee873568a64d26d728807ccd1e29b8))

### Unknown

* 4.2.1 ([`4936e74`](https://github.com/bimdata/python-api-client/commit/4936e740be5ee0b66ceccc1b6d58f6a6d2f29829))


## v4.2.0 (2019-10-07)

### Feature

* MINOR: Add cloud image ([`1efca02`](https://github.com/bimdata/python-api-client/commit/1efca02eace97a68ed6faa94e75e953a35e31a10))

### Unknown

* 4.2.0 ([`b9eaed8`](https://github.com/bimdata/python-api-client/commit/b9eaed8f50c9276defa4f22910e573c6f6dd3c52))


## v4.1.0 (2019-09-18)

### Feature

* MINOR: Add IfcAccessToken. It is usefull to create read_only tokens to share a viewer or when you&#39;re using an app without users ([`3503c35`](https://github.com/bimdata/python-api-client/commit/3503c35c9b5693ab70dbc74e56fa282659bce0cd))

### Unknown

* 4.1.0 ([`578f8fe`](https://github.com/bimdata/python-api-client/commit/578f8fe99aced10297b4fd830b4b1348e1e17442))


## v4.0.7 (2019-09-04)

### Fix

* PATCH: fix RecursiveFolderChildren model to allow an empty children field ([`c92e9da`](https://github.com/bimdata/python-api-client/commit/c92e9dae3d70c0c1d430952309fd8473c2e63592))

### Unknown

* 4.0.7 ([`c675899`](https://github.com/bimdata/python-api-client/commit/c6758991f19981da42628dfe49426b0220566783))


## v4.0.6 (2019-09-04)

### Fix

* PATCH: fix FolderChildren serialization: creator is not mandatory ([`c140634`](https://github.com/bimdata/python-api-client/commit/c14063410f1fe16ad11e37d513f46e9e5b3e5040))

### Unknown

* 4.0.6 ([`337c17e`](https://github.com/bimdata/python-api-client/commit/337c17e233cf78eab68c6362c57b30aa716b73c2))


## v4.0.5 (2019-09-03)

### Fix

* PATCH: add missing ifc.xkt_file ([`f7520fa`](https://github.com/bimdata/python-api-client/commit/f7520faeaeedf31b2239157c0bb76ea6b8140138))

### Unknown

* 4.0.5 ([`674e7c3`](https://github.com/bimdata/python-api-client/commit/674e7c3c42191c50803f51c31069eb43f340cd88))


## v4.0.4 (2019-09-03)

### Fix

* PATCH: fix bulk create route. Regression removed the declaration and bulk route were only accessible with a single objects instead of an array ([`ad13dd0`](https://github.com/bimdata/python-api-client/commit/ad13dd0a272dd6e64d44d3d4e7acf4bda519a0f3))

### Unknown

* 4.0.4 ([`10bc67e`](https://github.com/bimdata/python-api-client/commit/10bc67e68c21fc104e6f493705b5281f6bf5e7e0))


## v4.0.3 (2019-09-03)

### Fix

* PATCH: fix viewpoint guid read_only instead of read/write ([`31896f6`](https://github.com/bimdata/python-api-client/commit/31896f68f2174a92c68abd697ba1c252991e80ae))

### Unknown

* 4.0.3 ([`b21c9aa`](https://github.com/bimdata/python-api-client/commit/b21c9aac22de589d095dc8547c7cb51637c792a8))

* remove old files ([`31eb816`](https://github.com/bimdata/python-api-client/commit/31eb816f9b882326408de8a0738dec75e5df8c03))


## v4.0.2 (2019-09-03)

### Fix

* PATCH: fix python openapi-generator parameters ([`8b94f57`](https://github.com/bimdata/python-api-client/commit/8b94f57a6ae24cec76a83d23c344acea6f989a63))

### Unknown

* 4.0.2 ([`2640024`](https://github.com/bimdata/python-api-client/commit/2640024578a2054d1cea74c8a40208c9f430aef3))


## v4.0.1 (2019-09-02)

### Fix

* PATCH: fix Folder model named. Last version renamed it RecursiveFolder by error ([`c2f57be`](https://github.com/bimdata/python-api-client/commit/c2f57be499134f44aa174ad5585d4216ba390fae))

### Unknown

* 4.0.1 ([`4629128`](https://github.com/bimdata/python-api-client/commit/462912801cd27f897601f710b4e8788003aa3dcc))


## v4.0.0 (2019-09-02)

### Breaking

* MAJOR: change BCF topics_pk route name to topics_guid ([`f88346d`](https://github.com/bimdata/python-api-client/commit/f88346dad95068caecb74ff4cf8df3904124c08d))

### Unknown

* 4.0.0 ([`2ede217`](https://github.com/bimdata/python-api-client/commit/2ede2170a9e1b0362df47e3805314ec8f810e7a5))


## v3.1.1 (2019-07-24)

### Fix

* PATCH: revert project serialization ([`5384c5f`](https://github.com/bimdata/python-api-client/commit/5384c5fc56e6f46c6ee47e7ec253554af837e86b))

### Unknown

* 3.1.1 ([`7081165`](https://github.com/bimdata/python-api-client/commit/70811656f91028470a1603728a7adf9a410f9532))


## v3.1.0 (2019-07-23)

### Feature

* MINOR: update project serialization ([`5843ad6`](https://github.com/bimdata/python-api-client/commit/5843ad6a22d8c3af4fb06f556cc6a53c961b2f01))

### Unknown

* 3.1.0 ([`c6dff2e`](https://github.com/bimdata/python-api-client/commit/c6dff2e82de33c0a35bfe112d196c6374bdfaae0))


## v3.0.3 (2019-07-11)

### Fix

* PATCH: remove unexinsting method from swagger ([`fe605b1`](https://github.com/bimdata/python-api-client/commit/fe605b19b27f30b3cadef0877e98ea0c5d50f59f))

### Unknown

* 3.0.3 ([`cf5d010`](https://github.com/bimdata/python-api-client/commit/cf5d0107ee14f25289d89640b304dc357fd4e683))


## v3.0.2 (2019-07-08)

### Fix

* PATCH: fix FolderChildren OpenAPI Definition ([`2fd6775`](https://github.com/bimdata/python-api-client/commit/2fd6775fcdd57456ed1c9d2aa97a8b34182a568c))

### Unknown

* 3.0.2 ([`329ac05`](https://github.com/bimdata/python-api-client/commit/329ac050dbed10e4707dbc15012e549dfe83b83d))


## v3.0.1 (2019-07-05)

### Fix

* PATCH: fix folder swagger definition (#150) ([`165f240`](https://github.com/bimdata/python-api-client/commit/165f24048731482b6885d0d5ac298100f6d9cff4))

### Unknown

* 3.0.1 ([`f4e980d`](https://github.com/bimdata/python-api-client/commit/f4e980d1055497416daa7c9675811560701ba914))


## v3.0.0 (2019-07-01)

### Breaking

* MAJOR: upgrade openapi-generator to 4.0.2. JS Lib is now ES6 ([`c4c3aa0`](https://github.com/bimdata/python-api-client/commit/c4c3aa0a1131becddab9dbd6c503ee96d798fc6a))

### Unknown

* 3.0.0 ([`d02de24`](https://github.com/bimdata/python-api-client/commit/d02de24a9f9280f8138ce44c00735ca06b7fd381))


## v2.13.0 (2019-05-23)

### Feature

* MINOR: add processors ([`2f8746f`](https://github.com/bimdata/python-api-client/commit/2f8746ff305159fe3cbafa18cc41d986edd8c7e2))

### Unknown

* 2.13.0 ([`2943397`](https://github.com/bimdata/python-api-client/commit/2943397fa6c125299328c68187fb1ce6c80dfb67))


## v2.12.7 (2019-05-09)

### Fix

* PATCH: fix documents methods names ([`1689c2f`](https://github.com/bimdata/python-api-client/commit/1689c2f5be4f37988e63eace0e7b895340e5f432))

### Unknown

* 2.12.7 ([`c4ca9d9`](https://github.com/bimdata/python-api-client/commit/c4ca9d9266b23bc3a6140b6d418ebeb19b1c3f57))


## v2.12.6 (2019-05-07)

### Fix

* PATCH: fix webhook ping method name ([`a48e7b5`](https://github.com/bimdata/python-api-client/commit/a48e7b5f7de673d8249e1b9fd0b2327396dcd292))

### Unknown

* 2.12.6 ([`4fbc5a5`](https://github.com/bimdata/python-api-client/commit/4fbc5a596bb9dc6ff8b65356feebfb4977e03f69))


## v2.12.5 (2019-04-11)

### Fix

* PATCH: add id in invitation serialization ([`b2f7bf0`](https://github.com/bimdata/python-api-client/commit/b2f7bf04e8463e54ab45d3e615384b9b03cf7973))

### Unknown

* 2.12.5 ([`54751c6`](https://github.com/bimdata/python-api-client/commit/54751c6a485250f10e111d88fe2ff26f07f9b5a8))


## v2.12.4 (2019-04-01)

### Fix

* PATCH: add bimdata_camera_direction ([`edc7f4b`](https://github.com/bimdata/python-api-client/commit/edc7f4b051207103210784cc85699dc8414d8094))

### Unknown

* 2.12.4 ([`25603a6`](https://github.com/bimdata/python-api-client/commit/25603a62fac9e5b09b36bc2c891293c89cc8cb1c))


## v2.12.3 (2019-03-25)

### Fix

* PATCH: add missing ifc serialization in checker ([`c54755e`](https://github.com/bimdata/python-api-client/commit/c54755e9f7a661d4cf7bf9410b2cb838bf5aa6f8))

### Unknown

* 2.12.3 ([`d527916`](https://github.com/bimdata/python-api-client/commit/d5279168882313066489621ff27c56ef4683ae68))


## v2.12.2 (2019-03-19)

### Fix

* PATCH: fix wrong role invitation type ([`7e87bef`](https://github.com/bimdata/python-api-client/commit/7e87beff080ccd64605966184f36f29f55366309))

### Unknown

* 2.12.2 ([`9cd195b`](https://github.com/bimdata/python-api-client/commit/9cd195b361d6eb8b7670024fb826141538aac0ba))


## v2.12.1 (2019-03-19)

### Fix

* PATCH: add missing cloud_role invitation in serialization ([`02e8f07`](https://github.com/bimdata/python-api-client/commit/02e8f073b95d12126ac187dbc7c5237ddeaf1562))

### Unknown

* 2.12.1 ([`89f9d9d`](https://github.com/bimdata/python-api-client/commit/89f9d9d64fe194aa1829a0f134a3e8094bbf18d8))


## v2.12.0 (2019-03-18)

### Feature

* MINOR: add invitation cancellation and renew ([`3fc7e12`](https://github.com/bimdata/python-api-client/commit/3fc7e123dc29f876be399e7b0ba11b949b674dcc))

### Unknown

* 2.12.0 ([`e8c5304`](https://github.com/bimdata/python-api-client/commit/e8c5304187aee966c91b1113814d0106ae667dba))


## v2.11.1 (2019-03-12)

### Fix

* PATCH: fix bcf extension schema ([`d54bef0`](https://github.com/bimdata/python-api-client/commit/d54bef03adb7ef4ace39aa597c4ce6bcdb853e4d))

### Unknown

* 2.11.1 ([`309aad6`](https://github.com/bimdata/python-api-client/commit/309aad69078400fd347e1c4071edca2886243e9d))


## v2.11.0 (2019-03-06)

### Feature

* MINOR: allow cloud deletion ([`623938b`](https://github.com/bimdata/python-api-client/commit/623938b61167fa04ef331f950569b36680da70b0))

### Unknown

* 2.11.0 ([`6a89451`](https://github.com/bimdata/python-api-client/commit/6a8945106c08ec59821577534486b06bde4a60fd))


## v2.10.0 (2019-02-18)

### Feature

* MINOR: Add un change role routes ([`fcbdeda`](https://github.com/bimdata/python-api-client/commit/fcbdeda68ff5527f6af5f935f0961e364e93fb26))

### Unknown

* 2.10.0 ([`ec0593b`](https://github.com/bimdata/python-api-client/commit/ec0593b3579821d7d1c2e9e1e944e4166f397318))


## v2.9.1 (2019-02-18)

### Fix

* PATCH: fix invitation method name ([`cf81e99`](https://github.com/bimdata/python-api-client/commit/cf81e99aa9c2ce798929056a7ef491d7fb74f060))

### Unknown

* 2.9.1 ([`7391132`](https://github.com/bimdata/python-api-client/commit/739113214f9b7b9cc0552855726a8b7d779aa8b8))


## v2.9.0 (2019-02-08)

### Feature

* MINOR: add bcf export ([`526eb7f`](https://github.com/bimdata/python-api-client/commit/526eb7f4906705f73918db80b2c6ccf0c8442cd3))

### Unknown

* 2.9.0 ([`b91207d`](https://github.com/bimdata/python-api-client/commit/b91207dfa2a51b3b8b8e2b3258d99fec3228ebe7))


## v2.8.3 (2019-01-18)

### Fix

* PATCH: fix selfUser serialization ([`956f362`](https://github.com/bimdata/python-api-client/commit/956f362fe89a4c4e9d122981978a7a6f0af29d99))

### Unknown

* 2.8.3 ([`b21f463`](https://github.com/bimdata/python-api-client/commit/b21f463f4486670a5d1bcb2ce43b5efafce72b39))


## v2.8.2 (2019-01-16)

### Fix

* PATCH: fix full-topic swagger ([`48baaf6`](https://github.com/bimdata/python-api-client/commit/48baaf650f881eb004a2c760a734bc661e39da1f))

### Unknown

* 2.8.2 ([`238d809`](https://github.com/bimdata/python-api-client/commit/238d8097955b02fac29f6b69ce18d82b88e43795))


## v2.8.1 (2019-01-16)

### Fix

* PATCH: fix swagger.json ([`22143d4`](https://github.com/bimdata/python-api-client/commit/22143d4a947e22627ed349c4105918e6dea301d4))

### Unknown

* 2.8.1 ([`52bbe32`](https://github.com/bimdata/python-api-client/commit/52bbe326cd7948845e192efb3d48184b496195bd))


## v2.8.0 (2019-01-10)

### Feature

* MINOR: add 360_viewer_file ([`e1ac708`](https://github.com/bimdata/python-api-client/commit/e1ac708d33882c63015853e40dbef5f6a95b253f))

### Unknown

* 2.8.0 ([`bfb747e`](https://github.com/bimdata/python-api-client/commit/bfb747e6e4c89994becb907b30288d044fb835c3))


## v2.7.0 (2018-12-10)

### Feature

* MINOR: add patch extension endpoint ([`76df76e`](https://github.com/bimdata/python-api-client/commit/76df76e7c9e53790c842860d1ab9a83f1927c2e6))

### Unknown

* 2.7.0 ([`22b73dd`](https://github.com/bimdata/python-api-client/commit/22b73dd442b4a761c29267ae99b213f5df831027))


## v2.6.0 (2018-12-05)

### Feature

* MINOR: add bcf route ([`041f073`](https://github.com/bimdata/python-api-client/commit/041f0731f8e02faee991cb20767c2870df37c212))

### Unknown

* 2.6.0 ([`52f9893`](https://github.com/bimdata/python-api-client/commit/52f9893bddea50e569bca01f2f019c86edcf2837))


## v2.5.4 (2018-11-20)

### Fix

* PATCH: update openapi-generator ([`81ca880`](https://github.com/bimdata/python-api-client/commit/81ca8809d3e076690e28a8b8b74c107c96128a11))

### Unknown

* 2.5.4 ([`1831d7b`](https://github.com/bimdata/python-api-client/commit/1831d7b2e245368a78a90221decf551950e9cdb7))


## v2.5.3 (2018-11-12)

### Fix

* PATCH: rename bcf getExtension into getExtentions ([`6700f53`](https://github.com/bimdata/python-api-client/commit/6700f537d7a7d7e138954582d5b4466b4782741b))

### Unknown

* 2.5.3 ([`c3370cc`](https://github.com/bimdata/python-api-client/commit/c3370ccc86e2b5f0e502f03c45c5c1ebf086a821))


## v2.5.2 (2018-11-09)

### Fix

* PATCH: fix swagger syntax ([`a6e9726`](https://github.com/bimdata/python-api-client/commit/a6e9726eae7a0b87933776d75c644eaf7ed32a84))

### Unknown

* 2.5.2 ([`44a6a47`](https://github.com/bimdata/python-api-client/commit/44a6a473bc8c317cfa0c0d7455052b1fdb53c7aa))


## v2.5.1 (2018-11-08)

### Fix

* PATCH: add due_date to singleSjonTopic ([`592a006`](https://github.com/bimdata/python-api-client/commit/592a00627b7504494c6ada9ff4c9d75925aa4d08))

### Unknown

* 2.5.1 ([`146b8fe`](https://github.com/bimdata/python-api-client/commit/146b8fed648ca9b7794326ae51365bbe9a22c9a0))


## v2.5.0 (2018-11-08)

### Feature

* MINOR: Add bcf topic format filter ([`e66d412`](https://github.com/bimdata/python-api-client/commit/e66d412d7346a48a90239d40d05e7154569ec523))

### Unknown

* 2.5.0 ([`fd06062`](https://github.com/bimdata/python-api-client/commit/fd06062f87149358aa6276db5c69973571a6c589))


## v2.4.0 (2018-11-07)

### Feature

* MINOR: fix swagger.json ([`97369dc`](https://github.com/bimdata/python-api-client/commit/97369dc0e23a0b31e09b4dd7560ad1a606b1f849))

### Unknown

* 2.4.0 ([`2966393`](https://github.com/bimdata/python-api-client/commit/29663933d714ef84314526d453b044c5db0453e2))


## v2.3.1 (2018-09-20)

### Fix

* PATCH: fix create-demo swagger ([`cbe46ae`](https://github.com/bimdata/python-api-client/commit/cbe46ae8302c671088ef120f20c2e18e49622e43))

### Unknown

* 2.3.1 ([`c6bac00`](https://github.com/bimdata/python-api-client/commit/c6bac006c9b9e7645a54e7afc45be582ba08db06))


## v2.3.0 (2018-09-17)

### Feature

* MINOR: add createDemo route ([`e1a9a3c`](https://github.com/bimdata/python-api-client/commit/e1a9a3c0af1e1ec73f43699e30518e75d341fe4d))

### Unknown

* 2.3.0 ([`1945374`](https://github.com/bimdata/python-api-client/commit/194537463a5e16f8f8283dd1ca01088801cf81ca))


## v2.2.0 (2018-09-13)

### Feature

* MINOR: add webhooks routes ([`b07120e`](https://github.com/bimdata/python-api-client/commit/b07120e419469abd65055614453e2630515deeb9))

### Unknown

* 2.2.0 ([`04c1fb3`](https://github.com/bimdata/python-api-client/commit/04c1fb39862de5ed0f0449e58f726c6271717c21))


## v2.1.0 (2018-08-28)

### Feature

* MINOR: update generator to version 3.2.2 ([`700b0b0`](https://github.com/bimdata/python-api-client/commit/700b0b0c447f24b26ec968aeef20d283fb41f5cf))

### Unknown

* 2.1.0 ([`afe80ae`](https://github.com/bimdata/python-api-client/commit/afe80ae0d1dda5a47235fcf2ae336e3a072545f7))


## v2.0.1 (2018-07-27)

### Fix

* PATCH: remove fos_user password field ([`843da44`](https://github.com/bimdata/python-api-client/commit/843da443aaf60458044e24de63fd645cf5ad97c9))

### Unknown

* 2.0.1 ([`87dd0cb`](https://github.com/bimdata/python-api-client/commit/87dd0cbafeae5947f4c1d6869cef36afa3740940))


## v2.0.0 (2018-07-27)

### Breaking

* MAJOR: user openapi-codegen instead of swagger-codegen ([`a812b96`](https://github.com/bimdata/python-api-client/commit/a812b9686052b133703b41b36a81eeb1ad497263))

* MAJOR: set default api url to beta.bimdata.io, change auth behavior to use headers instead of querystring ([`18e4efe`](https://github.com/bimdata/python-api-client/commit/18e4efeea41cfa43eda671c6a8ff097fd9f46350))

### Unknown

* 2.0.0 ([`4b13d9e`](https://github.com/bimdata/python-api-client/commit/4b13d9e5a3ee4b19194294c05921be8682178cc0))


## v1.3.3 (2018-07-06)

### Fix

* PATCH: fix User and SelfUser doc generation ([`5b71abf`](https://github.com/bimdata/python-api-client/commit/5b71abf9b3dfddfa920b5da545f11dbdc7cbcec3))

### Unknown

* 1.3.3 ([`e048589`](https://github.com/bimdata/python-api-client/commit/e0485893539ae057a36474bf19c933e08b789c9d))


## v1.3.2 (2018-07-04)

### Fix

* PATCH: fix raw element serialization ([`f31e616`](https://github.com/bimdata/python-api-client/commit/f31e6168592a1a14cb011a7489c53e113821bbbb))

### Unknown

* 1.3.2 ([`24ace47`](https://github.com/bimdata/python-api-client/commit/24ace47cb890c593fcf8982a0142f704dfbac7d4))

* fix circular dependencies ([`699cc41`](https://github.com/bimdata/python-api-client/commit/699cc417723b24919a79a0afab1b6e3594b665a8))


## v1.3.1 (2018-07-04)

### Fix

* PATCH: fix element model/serialization ([`47c1b7a`](https://github.com/bimdata/python-api-client/commit/47c1b7a29e2bbf672013738492d3ad553146a4b9))

### Unknown

* 1.3.1 ([`e446c64`](https://github.com/bimdata/python-api-client/commit/e446c645474ef858fbcc3461df8abed4a5818d99))

* fix circular dependencies ([`b15c7bf`](https://github.com/bimdata/python-api-client/commit/b15c7bfc813af438d0a5f9ddcfc51d66922b100b))


## v1.3.0 (2018-07-03)

### Feature

* MINOR: back to swagger-codegen 2.4.0 ([`be799ab`](https://github.com/bimdata/python-api-client/commit/be799abcdd51dfef726c9af6576d2df1e05b2862))

### Fix

* PATCH: manually fix lib generation circular import ([`26d4705`](https://github.com/bimdata/python-api-client/commit/26d4705662375746873cdf7a2f48019d33c9384f))

### Unknown

* 1.3.0 ([`66f58e2`](https://github.com/bimdata/python-api-client/commit/66f58e284b94d5ad13aca2dada1cd83f8feee726))


## v1.2.0 (2018-07-02)

### Feature

* MINOR: allow empty name in spaces ([`a3ef30b`](https://github.com/bimdata/python-api-client/commit/a3ef30b86e8e02deaf37f8c2903e4d6bdd5401f0))

### Unknown

* 1.2.0 ([`eddd6ab`](https://github.com/bimdata/python-api-client/commit/eddd6ab8bc03b418e75609435e24004ce71fa07a))


## v1.1.1 (2018-06-26)

### Fix

* PATCH: fix version management ([`7a73046`](https://github.com/bimdata/python-api-client/commit/7a730466de9ff1766f8075fb4e65153b4e12ca80))

### Unknown

* 1.1.1 ([`a4fe5fb`](https://github.com/bimdata/python-api-client/commit/a4fe5fb51a7e3ef1ceae0c1728b69e2126bad4fb))


## v1.1.0 (2018-06-26)

### Feature

* MINOR: add default_cloud and default_project to /user ([`ee2071b`](https://github.com/bimdata/python-api-client/commit/ee2071be065bcdc7c23a983cb00d67427d7eeba1))

### Unknown

* 1.1.0 ([`4ec1232`](https://github.com/bimdata/python-api-client/commit/4ec1232a04d290a6c3981ba5bd2c1f14a56b23a0))

* update circle build ([`b8825cb`](https://github.com/bimdata/python-api-client/commit/b8825cb1d86b84a6b639d70d86aa5bbbb6a84d50))

* Merge branch &#39;master&#39; of github.com:bimdata/python-api-client ([`a8bc495`](https://github.com/bimdata/python-api-client/commit/a8bc4958a89b4e615563f8c00bdbc2e86506d6b2))

* rename git user ([`22b21ac`](https://github.com/bimdata/python-api-client/commit/22b21ac9f5fdba828d5a547b808a85ab72071c25))


## v1.0.27 (2018-06-25)

### Fix

* PATCH: update-swagger-codegen ([`c47c676`](https://github.com/bimdata/python-api-client/commit/c47c67664cd4c4ab5084ba7dd774dc38201f3b2a))

* PATCH:: test ([`3f95811`](https://github.com/bimdata/python-api-client/commit/3f958119eb9f430d415150886616e6b7985fa0cc))

* PATCH: add semantic-release ([`5cf5cd7`](https://github.com/bimdata/python-api-client/commit/5cf5cd78e397316c9166a4099ced0fd80beae7d7))

### Unknown

* 1.0.27 ([`65a87c6`](https://github.com/bimdata/python-api-client/commit/65a87c61033d55762f2acf05a91072b7eeb84b1c))

* fix tag version ([`560426c`](https://github.com/bimdata/python-api-client/commit/560426cc32e3ef0ed620fabef896c1b73e2fd89c))

* fix tox config ([`3d0875a`](https://github.com/bimdata/python-api-client/commit/3d0875ae4bc9543959072a5fb997ed54093d937c))

* update to version 1.0.25 ([`9c24845`](https://github.com/bimdata/python-api-client/commit/9c24845a5fa5eb239e9f97aa41d6cedae985b6e8))

* update to version 1.0.24 ([`ca36f8c`](https://github.com/bimdata/python-api-client/commit/ca36f8c631290f0d2e251ea048046f8bf3334d28))

* update to version 1.0.23 ([`ea40195`](https://github.com/bimdata/python-api-client/commit/ea40195e5949912fd7400ac06ccfec636c596ecf))

* update to version 1.0.22 ([`8e1ad97`](https://github.com/bimdata/python-api-client/commit/8e1ad97db9ebbad576665f964fdefaa9fe953a11))

* update to version 1.0.20 ([`90954f2`](https://github.com/bimdata/python-api-client/commit/90954f2e4c2a1622d6b223622c178c60284ef9ba))

* update to version 1.0.20 ([`5ae3cc3`](https://github.com/bimdata/python-api-client/commit/5ae3cc34be29c3b02b953fe39ebd6a17a2b05ffe))

* update to version 1.0.19 ([`154737d`](https://github.com/bimdata/python-api-client/commit/154737dfb6fd1448f3437f9ed92cba423d151839))

* update to version 1.0.18 ([`9dead04`](https://github.com/bimdata/python-api-client/commit/9dead04b0b6e2b1b919a4ca5e3d122ba189aebaa))

* update to version 1.0.18 ([`3b28aa1`](https://github.com/bimdata/python-api-client/commit/3b28aa1760c8f076598dd880a793c42548255cef))

* update to version 1.0.17 ([`c0c299c`](https://github.com/bimdata/python-api-client/commit/c0c299ca9b4236e9dd4360cb88b71cab8ad9aea6))

* fix old behaviors, temp remove bcf ([`795b9dc`](https://github.com/bimdata/python-api-client/commit/795b9dcd22708654fed001001d7ac4571f66269e))

* update to version 1.0.15 ([`b5cfef2`](https://github.com/bimdata/python-api-client/commit/b5cfef296ccc2fce374547273937671b8c25f52e))

* update to version 1.0.14 ([`70539f4`](https://github.com/bimdata/python-api-client/commit/70539f46bb2693e70fad6ec8188a1e26beb97835))

* update to version 1.0.13 ([`10197d9`](https://github.com/bimdata/python-api-client/commit/10197d933b9c8509932bcb7aa7e4767d8d580499))

* update to version 1.0.12 ([`1480a40`](https://github.com/bimdata/python-api-client/commit/1480a404054bedea1eafaec4aefb25d18490911b))

* update to version 1.0.11 ([`7b6ec28`](https://github.com/bimdata/python-api-client/commit/7b6ec284492fb059d9ececfce7e5d2e9e6fc814e))

* update to version 1.0.10 ([`7659eb4`](https://github.com/bimdata/python-api-client/commit/7659eb44ba7db5e993e43b2dbee617dc59bdff04))

* update to version 1.0.9 ([`21f08c3`](https://github.com/bimdata/python-api-client/commit/21f08c3c992d0abd1d6f8a171f783dfc20212eec))

* update to version 1.0.8 ([`0a74566`](https://github.com/bimdata/python-api-client/commit/0a7456638e5ea76977417737611796a80310bbfb))

* update to version 1.0.7 ([`ab2582b`](https://github.com/bimdata/python-api-client/commit/ab2582be6bf45c6d046eea07b4fa77744d0df551))

* update to version 1.0.6 ([`d2780ba`](https://github.com/bimdata/python-api-client/commit/d2780ba7d74e0120accc53fbf89442310ec5996a))

* update to version 1.0.5 ([`71ccc34`](https://github.com/bimdata/python-api-client/commit/71ccc34267196f1ccff0a89e9b5934a184c88a51))

* update to version 1.0.4 ([`5882666`](https://github.com/bimdata/python-api-client/commit/5882666feb68da50d6c2c218ff9dfe8e4ce0625d))

* update to version 1.0.3 ([`14394d6`](https://github.com/bimdata/python-api-client/commit/14394d6f58b24b89c8287ec65aa6da8d0a5beeb5))

* update to version 1.0.2 ([`bb8fbc1`](https://github.com/bimdata/python-api-client/commit/bb8fbc1f212e195fa69bdc350552b853fbdfe7a0))

* update to version 1.0.1 ([`5191539`](https://github.com/bimdata/python-api-client/commit/5191539d7f90e6fbfdf9ab64650427efd965ddb7))

* initial commit ([`c2481e0`](https://github.com/bimdata/python-api-client/commit/c2481e0cd012a41aeceefdce289d48509540b909))
