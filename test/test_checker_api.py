# coding: utf-8

"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@bimdata.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import bimdata_api_client
from bimdata_api_client.api.checker_api import CheckerApi  # noqa: E501
from bimdata_api_client.rest import ApiException


class TestCheckerApi(unittest.TestCase):
    """CheckerApi unit test stubs"""

    def setUp(self):
        self.api = bimdata_api_client.api.checker_api.CheckerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_checker(self):
        """Test case for create_checker

        Create a checker to a model  # noqa: E501
        """
        pass

    def test_create_checker_result(self):
        """Test case for create_checker_result

        Create a CheckerResult  # noqa: E501
        """
        pass

    def test_create_checkplan(self):
        """Test case for create_checkplan

        Create a Checkplan  # noqa: E501
        """
        pass

    def test_create_rule(self):
        """Test case for create_rule

        Create a Rule  # noqa: E501
        """
        pass

    def test_create_rule_component(self):
        """Test case for create_rule_component

        Create a RuleComponent  # noqa: E501
        """
        pass

    def test_create_ruleset(self):
        """Test case for create_ruleset

        Create a Ruleset  # noqa: E501
        """
        pass

    def test_delete_checker(self):
        """Test case for delete_checker

        Delete a checker of a model  # noqa: E501
        """
        pass

    def test_delete_checker_result(self):
        """Test case for delete_checker_result

        Delete a CheckerResult  # noqa: E501
        """
        pass

    def test_delete_checkplan(self):
        """Test case for delete_checkplan

        Delete a Checkplan  # noqa: E501
        """
        pass

    def test_delete_rule(self):
        """Test case for delete_rule

        Delete a Rule  # noqa: E501
        """
        pass

    def test_delete_rule_component(self):
        """Test case for delete_rule_component

        Delete a RuleComponent  # noqa: E501
        """
        pass

    def test_delete_ruleset(self):
        """Test case for delete_ruleset

        Delete a Ruleset  # noqa: E501
        """
        pass

    def test_full_update_checker(self):
        """Test case for full_update_checker

        Update all fields of a checker of a model  # noqa: E501
        """
        pass

    def test_full_update_checker_result(self):
        """Test case for full_update_checker_result

        Update all fields of a CheckerResult  # noqa: E501
        """
        pass

    def test_full_update_checkplan(self):
        """Test case for full_update_checkplan

        Update all fields of a Checkplan  # noqa: E501
        """
        pass

    def test_full_update_rule(self):
        """Test case for full_update_rule

        Update all fields of a Rule  # noqa: E501
        """
        pass

    def test_full_update_rule_component(self):
        """Test case for full_update_rule_component

        Update all fields of a RuleComponent  # noqa: E501
        """
        pass

    def test_full_update_ruleset(self):
        """Test case for full_update_ruleset

        Update all fields of a Ruleset  # noqa: E501
        """
        pass

    def test_get_checker(self):
        """Test case for get_checker

        Retrieve a checker of a model  # noqa: E501
        """
        pass

    def test_get_checker_result(self):
        """Test case for get_checker_result

        Retrieve one CheckerResult  # noqa: E501
        """
        pass

    def test_get_checker_results(self):
        """Test case for get_checker_results

        Retrieve all CheckerResults  # noqa: E501
        """
        pass

    def test_get_checkers(self):
        """Test case for get_checkers

        Retrieve all checkers of a model  # noqa: E501
        """
        pass

    def test_get_checkplan(self):
        """Test case for get_checkplan

        Retrieve one Checkplan  # noqa: E501
        """
        pass

    def test_get_checkplans(self):
        """Test case for get_checkplans

        Retrieve all Checkplans  # noqa: E501
        """
        pass

    def test_get_rule(self):
        """Test case for get_rule

        Retrieve one Rule  # noqa: E501
        """
        pass

    def test_get_rule_component(self):
        """Test case for get_rule_component

        Retrieve one RuleComponent  # noqa: E501
        """
        pass

    def test_get_rule_components(self):
        """Test case for get_rule_components

        Retrieve all RuleComponents  # noqa: E501
        """
        pass

    def test_get_rules(self):
        """Test case for get_rules

        Retrieve all Rules  # noqa: E501
        """
        pass

    def test_get_ruleset(self):
        """Test case for get_ruleset

        Retrieve one Ruleset  # noqa: E501
        """
        pass

    def test_get_rulesets(self):
        """Test case for get_rulesets

        Retrieve all Rulesets  # noqa: E501
        """
        pass

    def test_launch_new_check(self):
        """Test case for launch_new_check

        Launch a new check on the model  # noqa: E501
        """
        pass

    def test_update_checker(self):
        """Test case for update_checker

        Update some fields of a checker of a model  # noqa: E501
        """
        pass

    def test_update_checker_result(self):
        """Test case for update_checker_result

        Update some fields of a CheckerResult  # noqa: E501
        """
        pass

    def test_update_checkplan(self):
        """Test case for update_checkplan

        Update some fields of a Checkplan  # noqa: E501
        """
        pass

    def test_update_rule(self):
        """Test case for update_rule

        Update some fields of a Rule  # noqa: E501
        """
        pass

    def test_update_rule_component(self):
        """Test case for update_rule_component

        Update some fields of a RuleComponent  # noqa: E501
        """
        pass

    def test_update_ruleset(self):
        """Test case for update_ruleset

        Update some fields of a Ruleset  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
