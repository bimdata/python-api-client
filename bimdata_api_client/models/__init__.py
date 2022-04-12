# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from bimdata_api_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from bimdata_api_client.model.bcf_project import BcfProject
from bimdata_api_client.model.bcf_project_request import BcfProjectRequest
from bimdata_api_client.model.building import Building
from bimdata_api_client.model.check_plan import CheckPlan
from bimdata_api_client.model.check_plan_request import CheckPlanRequest
from bimdata_api_client.model.checker_result import CheckerResult
from bimdata_api_client.model.checker_result_request import CheckerResultRequest
from bimdata_api_client.model.checker_status_enum import CheckerStatusEnum
from bimdata_api_client.model.classification import Classification
from bimdata_api_client.model.classification_request import ClassificationRequest
from bimdata_api_client.model.clipping_plane import ClippingPlane
from bimdata_api_client.model.clipping_plane_request import ClippingPlaneRequest
from bimdata_api_client.model.cloud import Cloud
from bimdata_api_client.model.cloud_invitation import CloudInvitation
from bimdata_api_client.model.cloud_invitation_request import CloudInvitationRequest
from bimdata_api_client.model.cloud_request import CloudRequest
from bimdata_api_client.model.cloud_role import CloudRole
from bimdata_api_client.model.cloud_role_enum import CloudRoleEnum
from bimdata_api_client.model.coloring import Coloring
from bimdata_api_client.model.coloring_request import ColoringRequest
from bimdata_api_client.model.comment import Comment
from bimdata_api_client.model.comment_request import CommentRequest
from bimdata_api_client.model.component import Component
from bimdata_api_client.model.component_request import ComponentRequest
from bimdata_api_client.model.components_parent import ComponentsParent
from bimdata_api_client.model.components_parent_request import ComponentsParentRequest
from bimdata_api_client.model.create_building_by_name_request import CreateBuildingByNameRequest
from bimdata_api_client.model.create_model_request import CreateModelRequest
from bimdata_api_client.model.detailed_extensions import DetailedExtensions
from bimdata_api_client.model.direction import Direction
from bimdata_api_client.model.direction_request import DirectionRequest
from bimdata_api_client.model.document import Document
from bimdata_api_client.model.document_with_element_list import DocumentWithElementList
from bimdata_api_client.model.element import Element
from bimdata_api_client.model.element_classification_relation import ElementClassificationRelation
from bimdata_api_client.model.element_classification_relation_request import ElementClassificationRelationRequest
from bimdata_api_client.model.element_property_set_relation_request import ElementPropertySetRelationRequest
from bimdata_api_client.model.element_request import ElementRequest
from bimdata_api_client.model.export_enum import ExportEnum
from bimdata_api_client.model.extensions import Extensions
from bimdata_api_client.model.feature import Feature
from bimdata_api_client.model.feature_request import FeatureRequest
from bimdata_api_client.model.folder import Folder
from bimdata_api_client.model.folder_group_permission import FolderGroupPermission
from bimdata_api_client.model.folder_group_permission_request import FolderGroupPermissionRequest
from bimdata_api_client.model.folder_permission_enum import FolderPermissionEnum
from bimdata_api_client.model.folder_request import FolderRequest
from bimdata_api_client.model.folder_user_project import FolderUserProject
from bimdata_api_client.model.folder_without_children import FolderWithoutChildren
from bimdata_api_client.model.folder_without_children_request import FolderWithoutChildrenRequest
from bimdata_api_client.model.full_topic import FullTopic
from bimdata_api_client.model.full_topic_request import FullTopicRequest
from bimdata_api_client.model.group import Group
from bimdata_api_client.model.group_folder import GroupFolder
from bimdata_api_client.model.group_request import GroupRequest
from bimdata_api_client.model.ifc_access_token import IfcAccessToken
from bimdata_api_client.model.ifc_access_token_request import IfcAccessTokenRequest
from bimdata_api_client.model.ifc_checker import IfcChecker
from bimdata_api_client.model.ifc_checker_request import IfcCheckerRequest
from bimdata_api_client.model.ifc_export import IfcExport
from bimdata_api_client.model.ifc_export_request import IfcExportRequest
from bimdata_api_client.model.ifc_merge_request import IfcMergeRequest
from bimdata_api_client.model.ifc_optimize_request import IfcOptimizeRequest
from bimdata_api_client.model.invitation import Invitation
from bimdata_api_client.model.invitation_status_enum import InvitationStatusEnum
from bimdata_api_client.model.label import Label
from bimdata_api_client.model.label_request import LabelRequest
from bimdata_api_client.model.layer import Layer
from bimdata_api_client.model.layer_element import LayerElement
from bimdata_api_client.model.layer_element_request import LayerElementRequest
from bimdata_api_client.model.layer_request import LayerRequest
from bimdata_api_client.model.line import Line
from bimdata_api_client.model.line_request import LineRequest
from bimdata_api_client.model.managed_by_enum import ManagedByEnum
from bimdata_api_client.model.marketplace_app import MarketplaceApp
from bimdata_api_client.model.marketplace_app_image import MarketplaceAppImage
from bimdata_api_client.model.marketplace_app_image_request import MarketplaceAppImageRequest
from bimdata_api_client.model.marketplace_app_request import MarketplaceAppRequest
from bimdata_api_client.model.material import Material
from bimdata_api_client.model.material_list_component import MaterialListComponent
from bimdata_api_client.model.material_list_component_request import MaterialListComponentRequest
from bimdata_api_client.model.material_option import MaterialOption
from bimdata_api_client.model.material_request import MaterialRequest
from bimdata_api_client.model.model import Model
from bimdata_api_client.model.model_errors import ModelErrors
from bimdata_api_client.model.model_errors_request import ModelErrorsRequest
from bimdata_api_client.model.model_files import ModelFiles
from bimdata_api_client.model.model_property import ModelProperty
from bimdata_api_client.model.model_request import ModelRequest
from bimdata_api_client.model.model_source_enum import ModelSourceEnum
from bimdata_api_client.model.model_status_enum import ModelStatusEnum
from bimdata_api_client.model.model_type_enum import ModelTypeEnum
from bimdata_api_client.model.model_with_positioning_plan import ModelWithPositioningPlan
from bimdata_api_client.model.nature_enum import NatureEnum
from bimdata_api_client.model.null_enum import NullEnum
from bimdata_api_client.model.organization import Organization
from bimdata_api_client.model.organization_request import OrganizationRequest
from bimdata_api_client.model.orthogonal_camera import OrthogonalCamera
from bimdata_api_client.model.orthogonal_camera_request import OrthogonalCameraRequest
from bimdata_api_client.model.patched_bcf_project_request import PatchedBcfProjectRequest
from bimdata_api_client.model.patched_check_plan_request import PatchedCheckPlanRequest
from bimdata_api_client.model.patched_checker_result_request import PatchedCheckerResultRequest
from bimdata_api_client.model.patched_classification_request import PatchedClassificationRequest
from bimdata_api_client.model.patched_cloud_request import PatchedCloudRequest
from bimdata_api_client.model.patched_comment_request import PatchedCommentRequest
from bimdata_api_client.model.patched_document_request import PatchedDocumentRequest
from bimdata_api_client.model.patched_element_request import PatchedElementRequest
from bimdata_api_client.model.patched_folder_without_children_request import PatchedFolderWithoutChildrenRequest
from bimdata_api_client.model.patched_full_topic_request import PatchedFullTopicRequest
from bimdata_api_client.model.patched_group_folder_request import PatchedGroupFolderRequest
from bimdata_api_client.model.patched_group_request import PatchedGroupRequest
from bimdata_api_client.model.patched_ifc_access_token_request import PatchedIfcAccessTokenRequest
from bimdata_api_client.model.patched_ifc_checker_request import PatchedIfcCheckerRequest
from bimdata_api_client.model.patched_label_request import PatchedLabelRequest
from bimdata_api_client.model.patched_layer_request import PatchedLayerRequest
from bimdata_api_client.model.patched_model_request import PatchedModelRequest
from bimdata_api_client.model.patched_positioning_plan_request import PatchedPositioningPlanRequest
from bimdata_api_client.model.patched_priority_request import PatchedPriorityRequest
from bimdata_api_client.model.patched_processor_handler_request import PatchedProcessorHandlerRequest
from bimdata_api_client.model.patched_project_access_token_request import PatchedProjectAccessTokenRequest
from bimdata_api_client.model.patched_project_request import PatchedProjectRequest
from bimdata_api_client.model.patched_property_definition_request import PatchedPropertyDefinitionRequest
from bimdata_api_client.model.patched_property_request import PatchedPropertyRequest
from bimdata_api_client.model.patched_property_set_request import PatchedPropertySetRequest
from bimdata_api_client.model.patched_rule_component_request import PatchedRuleComponentRequest
from bimdata_api_client.model.patched_rule_request import PatchedRuleRequest
from bimdata_api_client.model.patched_ruleset_request import PatchedRulesetRequest
from bimdata_api_client.model.patched_space_request import PatchedSpaceRequest
from bimdata_api_client.model.patched_stage_request import PatchedStageRequest
from bimdata_api_client.model.patched_system_request import PatchedSystemRequest
from bimdata_api_client.model.patched_topic_request import PatchedTopicRequest
from bimdata_api_client.model.patched_topic_status_request import PatchedTopicStatusRequest
from bimdata_api_client.model.patched_topic_type_request import PatchedTopicTypeRequest
from bimdata_api_client.model.patched_unit_request import PatchedUnitRequest
from bimdata_api_client.model.patched_user_cloud_update_request import PatchedUserCloudUpdateRequest
from bimdata_api_client.model.patched_user_project_update_request import PatchedUserProjectUpdateRequest
from bimdata_api_client.model.patched_viewpoint_request import PatchedViewpointRequest
from bimdata_api_client.model.patched_visa_comment_request import PatchedVisaCommentRequest
from bimdata_api_client.model.patched_visa_request import PatchedVisaRequest
from bimdata_api_client.model.patched_visa_validation_request import PatchedVisaValidationRequest
from bimdata_api_client.model.patched_web_hook_request import PatchedWebHookRequest
from bimdata_api_client.model.patched_zone_request import PatchedZoneRequest
from bimdata_api_client.model.patched_zone_space_request import PatchedZoneSpaceRequest
from bimdata_api_client.model.perspective_camera import PerspectiveCamera
from bimdata_api_client.model.perspective_camera_request import PerspectiveCameraRequest
from bimdata_api_client.model.point import Point
from bimdata_api_client.model.point_request import PointRequest
from bimdata_api_client.model.positioning_plan import PositioningPlan
from bimdata_api_client.model.priority import Priority
from bimdata_api_client.model.priority_request import PriorityRequest
from bimdata_api_client.model.processor_handler import ProcessorHandler
from bimdata_api_client.model.project import Project
from bimdata_api_client.model.project_access_token import ProjectAccessToken
from bimdata_api_client.model.project_access_token_request import ProjectAccessTokenRequest
from bimdata_api_client.model.project_invitation import ProjectInvitation
from bimdata_api_client.model.project_invitation_request import ProjectInvitationRequest
from bimdata_api_client.model.project_request import ProjectRequest
from bimdata_api_client.model.project_role import ProjectRole
from bimdata_api_client.model.project_role_enum import ProjectRoleEnum
from bimdata_api_client.model.project_size import ProjectSize
from bimdata_api_client.model.project_status_enum import ProjectStatusEnum
from bimdata_api_client.model.project_with_children import ProjectWithChildren
from bimdata_api_client.model.property_definition import PropertyDefinition
from bimdata_api_client.model.property_definition_request import PropertyDefinitionRequest
from bimdata_api_client.model.property_request import PropertyRequest
from bimdata_api_client.model.property_set import PropertySet
from bimdata_api_client.model.property_set_request import PropertySetRequest
from bimdata_api_client.model.public_organization import PublicOrganization
from bimdata_api_client.model.public_organization_request import PublicOrganizationRequest
from bimdata_api_client.model.raw_classification import RawClassification
from bimdata_api_client.model.raw_classification_request import RawClassificationRequest
from bimdata_api_client.model.raw_definition import RawDefinition
from bimdata_api_client.model.raw_definition_request import RawDefinitionRequest
from bimdata_api_client.model.raw_element import RawElement
from bimdata_api_client.model.raw_element_request import RawElementRequest
from bimdata_api_client.model.raw_elements import RawElements
from bimdata_api_client.model.raw_elements_request import RawElementsRequest
from bimdata_api_client.model.raw_layer import RawLayer
from bimdata_api_client.model.raw_layer_request import RawLayerRequest
from bimdata_api_client.model.raw_material import RawMaterial
from bimdata_api_client.model.raw_material_list import RawMaterialList
from bimdata_api_client.model.raw_material_list_components import RawMaterialListComponents
from bimdata_api_client.model.raw_material_list_components_request import RawMaterialListComponentsRequest
from bimdata_api_client.model.raw_material_list_request import RawMaterialListRequest
from bimdata_api_client.model.raw_material_options import RawMaterialOptions
from bimdata_api_client.model.raw_material_options_request import RawMaterialOptionsRequest
from bimdata_api_client.model.raw_material_request import RawMaterialRequest
from bimdata_api_client.model.raw_property import RawProperty
from bimdata_api_client.model.raw_property_request import RawPropertyRequest
from bimdata_api_client.model.raw_property_set import RawPropertySet
from bimdata_api_client.model.raw_property_set_request import RawPropertySetRequest
from bimdata_api_client.model.raw_system import RawSystem
from bimdata_api_client.model.raw_system_request import RawSystemRequest
from bimdata_api_client.model.raw_unit import RawUnit
from bimdata_api_client.model.raw_unit_request import RawUnitRequest
from bimdata_api_client.model.recursive_folder_children import RecursiveFolderChildren
from bimdata_api_client.model.recursive_folder_children_request import RecursiveFolderChildrenRequest
from bimdata_api_client.model.recursive_folder_children_type_enum import RecursiveFolderChildrenTypeEnum
from bimdata_api_client.model.rule import Rule
from bimdata_api_client.model.rule_component import RuleComponent
from bimdata_api_client.model.rule_component_request import RuleComponentRequest
from bimdata_api_client.model.rule_request import RuleRequest
from bimdata_api_client.model.ruleset import Ruleset
from bimdata_api_client.model.ruleset_request import RulesetRequest
from bimdata_api_client.model.self_bcf_user import SelfBcfUser
from bimdata_api_client.model.self_user import SelfUser
from bimdata_api_client.model.simple_element import SimpleElement
from bimdata_api_client.model.size import Size
from bimdata_api_client.model.snapshot import Snapshot
from bimdata_api_client.model.snapshot_request import SnapshotRequest
from bimdata_api_client.model.space import Space
from bimdata_api_client.model.space_request import SpaceRequest
from bimdata_api_client.model.stage import Stage
from bimdata_api_client.model.stage_request import StageRequest
from bimdata_api_client.model.storey import Storey
from bimdata_api_client.model.system import System
from bimdata_api_client.model.system_request import SystemRequest
from bimdata_api_client.model.topic import Topic
from bimdata_api_client.model.topic_request import TopicRequest
from bimdata_api_client.model.topic_status import TopicStatus
from bimdata_api_client.model.topic_status_request import TopicStatusRequest
from bimdata_api_client.model.topic_type import TopicType
from bimdata_api_client.model.topic_type_request import TopicTypeRequest
from bimdata_api_client.model.unit import Unit
from bimdata_api_client.model.unit_request import UnitRequest
from bimdata_api_client.model.user import User
from bimdata_api_client.model.user_project import UserProject
from bimdata_api_client.model.user_project_id_request import UserProjectIdRequest
from bimdata_api_client.model.view_setup_hints import ViewSetupHints
from bimdata_api_client.model.view_setup_hints_request import ViewSetupHintsRequest
from bimdata_api_client.model.viewpoint import Viewpoint
from bimdata_api_client.model.viewpoint_request import ViewpointRequest
from bimdata_api_client.model.visa import Visa
from bimdata_api_client.model.visa_comment import VisaComment
from bimdata_api_client.model.visa_comment_request import VisaCommentRequest
from bimdata_api_client.model.visa_request import VisaRequest
from bimdata_api_client.model.visa_status_enum import VisaStatusEnum
from bimdata_api_client.model.visa_validation import VisaValidation
from bimdata_api_client.model.visa_validation_request import VisaValidationRequest
from bimdata_api_client.model.visa_validation_status_enum import VisaValidationStatusEnum
from bimdata_api_client.model.visibility import Visibility
from bimdata_api_client.model.visibility_request import VisibilityRequest
from bimdata_api_client.model.web_hook import WebHook
from bimdata_api_client.model.web_hook_request import WebHookRequest
from bimdata_api_client.model.zone import Zone
from bimdata_api_client.model.zone_request import ZoneRequest
from bimdata_api_client.model.zone_space import ZoneSpace
from bimdata_api_client.model.zone_space_request import ZoneSpaceRequest
