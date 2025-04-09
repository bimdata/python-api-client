# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from bimdata-api-client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from bimdata-api-client.model.auth import Auth
from bimdata-api-client.model.bcf_project import BcfProject
from bimdata-api-client.model.bcf_project_request import BcfProjectRequest
from bimdata-api-client.model.building import Building
from bimdata-api-client.model.building_model_plan_request import BuildingModelPlanRequest
from bimdata-api-client.model.check_project_access import CheckProjectAccess
from bimdata-api-client.model.classification import Classification
from bimdata-api-client.model.classification_request import ClassificationRequest
from bimdata-api-client.model.clipping_plane import ClippingPlane
from bimdata-api-client.model.clipping_plane_request import ClippingPlaneRequest
from bimdata-api-client.model.cloud import Cloud
from bimdata-api-client.model.cloud_invitation import CloudInvitation
from bimdata-api-client.model.cloud_invitation_request import CloudInvitationRequest
from bimdata-api-client.model.cloud_request import CloudRequest
from bimdata-api-client.model.cloud_role import CloudRole
from bimdata-api-client.model.coloring import Coloring
from bimdata-api-client.model.coloring_definition import ColoringDefinition
from bimdata-api-client.model.coloring_request import ColoringRequest
from bimdata-api-client.model.comment import Comment
from bimdata-api-client.model.comment_request import CommentRequest
from bimdata-api-client.model.component import Component
from bimdata-api-client.model.component_request import ComponentRequest
from bimdata-api-client.model.components_parent import ComponentsParent
from bimdata-api-client.model.components_parent_request import ComponentsParentRequest
from bimdata-api-client.model.create_building_by_name_request import CreateBuildingByNameRequest
from bimdata-api-client.model.create_model_request import CreateModelRequest
from bimdata-api-client.model.create_multi_page_model_request import CreateMultiPageModelRequest
from bimdata-api-client.model.create_user_request import CreateUserRequest
from bimdata-api-client.model.detailed_extensions import DetailedExtensions
from bimdata-api-client.model.direction import Direction
from bimdata-api-client.model.direction_request import DirectionRequest
from bimdata-api-client.model.document import Document
from bimdata-api-client.model.document_preview_file import DocumentPreviewFile
from bimdata-api-client.model.document_with_element_list import DocumentWithElementList
from bimdata-api-client.model.drawing import Drawing
from bimdata-api-client.model.drawing_request import DrawingRequest
from bimdata-api-client.model.element import Element
from bimdata-api-client.model.element_classification_relation import ElementClassificationRelation
from bimdata-api-client.model.element_classification_relation_request import ElementClassificationRelationRequest
from bimdata-api-client.model.element_property_set_relation_request import ElementPropertySetRelationRequest
from bimdata-api-client.model.element_request import ElementRequest
from bimdata-api-client.model.extensions import Extensions
from bimdata-api-client.model.feature import Feature
from bimdata-api-client.model.feature_request import FeatureRequest
from bimdata-api-client.model.folder import Folder
from bimdata-api-client.model.folder_tree import FolderTree
from bimdata-api-client.model.folder_user_project import FolderUserProject
from bimdata-api-client.model.folder_without_children import FolderWithoutChildren
from bimdata-api-client.model.folder_without_children_request import FolderWithoutChildrenRequest
from bimdata-api-client.model.full_topic import FullTopic
from bimdata-api-client.model.full_topic_request import FullTopicRequest
from bimdata-api-client.model.geometry_point import GeometryPoint
from bimdata-api-client.model.geometry_point_request import GeometryPointRequest
from bimdata-api-client.model.group import Group
from bimdata-api-client.model.group_folder import GroupFolder
from bimdata-api-client.model.group_folder_read import GroupFolderRead
from bimdata-api-client.model.group_request import GroupRequest
from bimdata-api-client.model.ifc_access_token import IfcAccessToken
from bimdata-api-client.model.ifc_access_token_request import IfcAccessTokenRequest
from bimdata-api-client.model.ifc_export_request import IfcExportRequest
from bimdata-api-client.model.ifc_merge_request import IfcMergeRequest
from bimdata-api-client.model.ifc_optimize_request import IfcOptimizeRequest
from bimdata-api-client.model.import_group_request import ImportGroupRequest
from bimdata-api-client.model.invitation import Invitation
from bimdata-api-client.model.label import Label
from bimdata-api-client.model.label_request import LabelRequest
from bimdata-api-client.model.layer import Layer
from bimdata-api-client.model.layer_element import LayerElement
from bimdata-api-client.model.layer_element_request import LayerElementRequest
from bimdata-api-client.model.layer_request import LayerRequest
from bimdata-api-client.model.light_document import LightDocument
from bimdata-api-client.model.line import Line
from bimdata-api-client.model.line_request import LineRequest
from bimdata-api-client.model.log_entry import LogEntry
from bimdata-api-client.model.marketplace_app_image import MarketplaceAppImage
from bimdata-api-client.model.marketplace_app_light import MarketplaceAppLight
from bimdata-api-client.model.marketplace_app_light_request import MarketplaceAppLightRequest
from bimdata-api-client.model.mask2_d import Mask2D
from bimdata-api-client.model.mask2_d_request import Mask2DRequest
from bimdata-api-client.model.material import Material
from bimdata-api-client.model.material_list_component import MaterialListComponent
from bimdata-api-client.model.material_list_component_request import MaterialListComponentRequest
from bimdata-api-client.model.material_option import MaterialOption
from bimdata-api-client.model.material_request import MaterialRequest
from bimdata-api-client.model.model import Model
from bimdata-api-client.model.model_document import ModelDocument
from bimdata-api-client.model.model_document_request import ModelDocumentRequest
from bimdata-api-client.model.model_errors import ModelErrors
from bimdata-api-client.model.model_errors_request import ModelErrorsRequest
from bimdata-api-client.model.model_files import ModelFiles
from bimdata-api-client.model.model_property import ModelProperty
from bimdata-api-client.model.model_serializer_without_children import ModelSerializerWithoutChildren
from bimdata-api-client.model.model_with_positioning_plan import ModelWithPositioningPlan
from bimdata-api-client.model.organization import Organization
from bimdata-api-client.model.organization_request import OrganizationRequest
from bimdata-api-client.model.orthogonal_camera import OrthogonalCamera
from bimdata-api-client.model.orthogonal_camera_request import OrthogonalCameraRequest
from bimdata-api-client.model.patched_bcf_project_request import PatchedBcfProjectRequest
from bimdata-api-client.model.patched_classification_request import PatchedClassificationRequest
from bimdata-api-client.model.patched_cloud_request import PatchedCloudRequest
from bimdata-api-client.model.patched_comment_request import PatchedCommentRequest
from bimdata-api-client.model.patched_document_request import PatchedDocumentRequest
from bimdata-api-client.model.patched_drawing_request import PatchedDrawingRequest
from bimdata-api-client.model.patched_element_request import PatchedElementRequest
from bimdata-api-client.model.patched_folder_without_children_request import PatchedFolderWithoutChildrenRequest
from bimdata-api-client.model.patched_full_topic_request import PatchedFullTopicRequest
from bimdata-api-client.model.patched_group_folder_request import PatchedGroupFolderRequest
from bimdata-api-client.model.patched_group_request import PatchedGroupRequest
from bimdata-api-client.model.patched_ifc_access_token_request import PatchedIfcAccessTokenRequest
from bimdata-api-client.model.patched_label_request import PatchedLabelRequest
from bimdata-api-client.model.patched_layer_request import PatchedLayerRequest
from bimdata-api-client.model.patched_model_request import PatchedModelRequest
from bimdata-api-client.model.patched_pin_request import PatchedPinRequest
from bimdata-api-client.model.patched_positioning_plan_request import PatchedPositioningPlanRequest
from bimdata-api-client.model.patched_priority_request import PatchedPriorityRequest
from bimdata-api-client.model.patched_processor_handler_request import PatchedProcessorHandlerRequest
from bimdata-api-client.model.patched_project_request import PatchedProjectRequest
from bimdata-api-client.model.patched_property_definition_request import PatchedPropertyDefinitionRequest
from bimdata-api-client.model.patched_property_request import PatchedPropertyRequest
from bimdata-api-client.model.patched_property_set_request import PatchedPropertySetRequest
from bimdata-api-client.model.patched_space_request import PatchedSpaceRequest
from bimdata-api-client.model.patched_stage_request import PatchedStageRequest
from bimdata-api-client.model.patched_storey_building_request import PatchedStoreyBuildingRequest
from bimdata-api-client.model.patched_system_request import PatchedSystemRequest
from bimdata-api-client.model.patched_tag_request import PatchedTagRequest
from bimdata-api-client.model.patched_topic_request import PatchedTopicRequest
from bimdata-api-client.model.patched_topic_status_request import PatchedTopicStatusRequest
from bimdata-api-client.model.patched_topic_type_request import PatchedTopicTypeRequest
from bimdata-api-client.model.patched_unit_request import PatchedUnitRequest
from bimdata-api-client.model.patched_user_cloud_update_request import PatchedUserCloudUpdateRequest
from bimdata-api-client.model.patched_user_project_update_request import PatchedUserProjectUpdateRequest
from bimdata-api-client.model.patched_viewpoint_request import PatchedViewpointRequest
from bimdata-api-client.model.patched_visa_comment_request import PatchedVisaCommentRequest
from bimdata-api-client.model.patched_visa_request import PatchedVisaRequest
from bimdata-api-client.model.patched_visa_validation_request import PatchedVisaValidationRequest
from bimdata-api-client.model.patched_web_hook_request import PatchedWebHookRequest
from bimdata-api-client.model.patched_zone_request import PatchedZoneRequest
from bimdata-api-client.model.patched_zone_space_request import PatchedZoneSpaceRequest
from bimdata-api-client.model.perspective_camera import PerspectiveCamera
from bimdata-api-client.model.perspective_camera_request import PerspectiveCameraRequest
from bimdata-api-client.model.pin import Pin
from bimdata-api-client.model.pin_request import PinRequest
from bimdata-api-client.model.point import Point
from bimdata-api-client.model.point_request import PointRequest
from bimdata-api-client.model.positioning_plan import PositioningPlan
from bimdata-api-client.model.priority import Priority
from bimdata-api-client.model.priority_request import PriorityRequest
from bimdata-api-client.model.processor_handler import ProcessorHandler
from bimdata-api-client.model.project import Project
from bimdata-api-client.model.project_access_token import ProjectAccessToken
from bimdata-api-client.model.project_access_token_request import ProjectAccessTokenRequest
from bimdata-api-client.model.project_import_request import ProjectImportRequest
from bimdata-api-client.model.project_invitation import ProjectInvitation
from bimdata-api-client.model.project_invitation_request import ProjectInvitationRequest
from bimdata-api-client.model.project_request import ProjectRequest
from bimdata-api-client.model.project_role import ProjectRole
from bimdata-api-client.model.project_size import ProjectSize
from bimdata-api-client.model.property_definition import PropertyDefinition
from bimdata-api-client.model.property_definition_request import PropertyDefinitionRequest
from bimdata-api-client.model.property_request import PropertyRequest
from bimdata-api-client.model.property_set import PropertySet
from bimdata-api-client.model.property_set_request import PropertySetRequest
from bimdata-api-client.model.public_organization import PublicOrganization
from bimdata-api-client.model.public_organization_request import PublicOrganizationRequest
from bimdata-api-client.model.raw_classification import RawClassification
from bimdata-api-client.model.raw_classification_request import RawClassificationRequest
from bimdata-api-client.model.raw_definition import RawDefinition
from bimdata-api-client.model.raw_definition_request import RawDefinitionRequest
from bimdata-api-client.model.raw_element import RawElement
from bimdata-api-client.model.raw_element_request import RawElementRequest
from bimdata-api-client.model.raw_elements import RawElements
from bimdata-api-client.model.raw_elements_request import RawElementsRequest
from bimdata-api-client.model.raw_layer import RawLayer
from bimdata-api-client.model.raw_layer_request import RawLayerRequest
from bimdata-api-client.model.raw_material import RawMaterial
from bimdata-api-client.model.raw_material_list import RawMaterialList
from bimdata-api-client.model.raw_material_list_components import RawMaterialListComponents
from bimdata-api-client.model.raw_material_list_components_request import RawMaterialListComponentsRequest
from bimdata-api-client.model.raw_material_list_request import RawMaterialListRequest
from bimdata-api-client.model.raw_material_options import RawMaterialOptions
from bimdata-api-client.model.raw_material_options_request import RawMaterialOptionsRequest
from bimdata-api-client.model.raw_material_request import RawMaterialRequest
from bimdata-api-client.model.raw_property import RawProperty
from bimdata-api-client.model.raw_property_request import RawPropertyRequest
from bimdata-api-client.model.raw_property_set import RawPropertySet
from bimdata-api-client.model.raw_property_set_request import RawPropertySetRequest
from bimdata-api-client.model.raw_system import RawSystem
from bimdata-api-client.model.raw_system_request import RawSystemRequest
from bimdata-api-client.model.raw_unit import RawUnit
from bimdata-api-client.model.raw_unit_request import RawUnitRequest
from bimdata-api-client.model.recursive_folder_children import RecursiveFolderChildren
from bimdata-api-client.model.select_user_request import SelectUserRequest
from bimdata-api-client.model.selection_definition import SelectionDefinition
from bimdata-api-client.model.self_bcf_user import SelfBcfUser
from bimdata-api-client.model.self_user import SelfUser
from bimdata-api-client.model.short_user import ShortUser
from bimdata-api-client.model.simple_element import SimpleElement
from bimdata-api-client.model.size import Size
from bimdata-api-client.model.snapshot import Snapshot
from bimdata-api-client.model.snapshot_request import SnapshotRequest
from bimdata-api-client.model.space import Space
from bimdata-api-client.model.space_request import SpaceRequest
from bimdata-api-client.model.stage import Stage
from bimdata-api-client.model.stage_request import StageRequest
from bimdata-api-client.model.storey import Storey
from bimdata-api-client.model.storey_building_request import StoreyBuildingRequest
from bimdata-api-client.model.storey_model_plan_request import StoreyModelPlanRequest
from bimdata-api-client.model.system import System
from bimdata-api-client.model.system_request import SystemRequest
from bimdata-api-client.model.tag import Tag
from bimdata-api-client.model.tag_id_request import TagIdRequest
from bimdata-api-client.model.tag_request import TagRequest
from bimdata-api-client.model.topic import Topic
from bimdata-api-client.model.topic_request import TopicRequest
from bimdata-api-client.model.topic_status import TopicStatus
from bimdata-api-client.model.topic_status_request import TopicStatusRequest
from bimdata-api-client.model.topic_type import TopicType
from bimdata-api-client.model.topic_type_request import TopicTypeRequest
from bimdata-api-client.model.unit import Unit
from bimdata-api-client.model.unit_request import UnitRequest
from bimdata-api-client.model.user import User
from bimdata-api-client.model.user_invitation import UserInvitation
from bimdata-api-client.model.user_project import UserProject
from bimdata-api-client.model.user_project_id_request import UserProjectIdRequest
from bimdata-api-client.model.version import Version
from bimdata-api-client.model.view_setup_hints import ViewSetupHints
from bimdata-api-client.model.view_setup_hints_request import ViewSetupHintsRequest
from bimdata-api-client.model.viewpoint import Viewpoint
from bimdata-api-client.model.viewpoint_request import ViewpointRequest
from bimdata-api-client.model.visa import Visa
from bimdata-api-client.model.visa_attachment import VisaAttachment
from bimdata-api-client.model.visa_attachment_request import VisaAttachmentRequest
from bimdata-api-client.model.visa_comment import VisaComment
from bimdata-api-client.model.visa_comment_request import VisaCommentRequest
from bimdata-api-client.model.visa_request import VisaRequest
from bimdata-api-client.model.visa_validation import VisaValidation
from bimdata-api-client.model.visa_validation_request import VisaValidationRequest
from bimdata-api-client.model.visa_with_document import VisaWithDocument
from bimdata-api-client.model.visibility import Visibility
from bimdata-api-client.model.visibility_definition import VisibilityDefinition
from bimdata-api-client.model.visibility_request import VisibilityRequest
from bimdata-api-client.model.web_hook import WebHook
from bimdata-api-client.model.web_hook_request import WebHookRequest
from bimdata-api-client.model.write_folder import WriteFolder
from bimdata-api-client.model.write_folder_request import WriteFolderRequest
from bimdata-api-client.model.xkt_file import XktFile
from bimdata-api-client.model.zone import Zone
from bimdata-api-client.model.zone_request import ZoneRequest
from bimdata-api-client.model.zone_space import ZoneSpace
from bimdata-api-client.model.zone_space_relation_request import ZoneSpaceRelationRequest
from bimdata-api-client.model.zone_space_request import ZoneSpaceRequest
