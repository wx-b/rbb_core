# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class SimulationDetailed(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SimulationDetailed - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'detail_type': 'str',
            'identifier': 'int',
            'description': 'str',
            'created': 'datetime',
            'result': 'int',
            'environment_name': 'str',
            'queued_task_identifier': 'str',
            'queued_task_state': 'int',
            'config': 'object',
            'on_complete_action': 'object',
            'environment': 'SimulationEnvironmentDetailed',
            'runs': 'list[SimulationRunDetailed]',
            'queued_task': 'TaskDetailed'
        }

        self.attribute_map = {
            'detail_type': 'detail_type',
            'identifier': 'identifier',
            'description': 'description',
            'created': 'created',
            'result': 'result',
            'environment_name': 'environment_name',
            'queued_task_identifier': 'queued_task_identifier',
            'queued_task_state': 'queued_task_state',
            'config': 'config',
            'on_complete_action': 'on_complete_action',
            'environment': 'environment',
            'runs': 'runs',
            'queued_task': 'queued_task'
        }

        self._detail_type = None
        self._identifier = None
        self._description = None
        self._created = None
        self._result = None
        self._environment_name = None
        self._queued_task_identifier = None
        self._queued_task_state = None
        self._config = None
        self._on_complete_action = None
        self._environment = None
        self._runs = None
        self._queued_task = None

    @property
    def detail_type(self):
        """
        Gets the detail_type of this SimulationDetailed.


        :return: The detail_type of this SimulationDetailed.
        :rtype: str
        """
        return self._detail_type

    @detail_type.setter
    def detail_type(self, detail_type):
        """
        Sets the detail_type of this SimulationDetailed.


        :param detail_type: The detail_type of this SimulationDetailed.
        :type: str
        """
        self._detail_type = detail_type

    @property
    def identifier(self):
        """
        Gets the identifier of this SimulationDetailed.


        :return: The identifier of this SimulationDetailed.
        :rtype: int
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this SimulationDetailed.


        :param identifier: The identifier of this SimulationDetailed.
        :type: int
        """
        self._identifier = identifier

    @property
    def description(self):
        """
        Gets the description of this SimulationDetailed.


        :return: The description of this SimulationDetailed.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SimulationDetailed.


        :param description: The description of this SimulationDetailed.
        :type: str
        """
        self._description = description

    @property
    def created(self):
        """
        Gets the created of this SimulationDetailed.


        :return: The created of this SimulationDetailed.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this SimulationDetailed.


        :param created: The created of this SimulationDetailed.
        :type: datetime
        """
        self._created = created

    @property
    def result(self):
        """
        Gets the result of this SimulationDetailed.
        0 is scheduled, -1 is prep failed, -100 is sim failed, 100 is sim succeeded

        :return: The result of this SimulationDetailed.
        :rtype: int
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this SimulationDetailed.
        0 is scheduled, -1 is prep failed, -100 is sim failed, 100 is sim succeeded

        :param result: The result of this SimulationDetailed.
        :type: int
        """
        self._result = result

    @property
    def environment_name(self):
        """
        Gets the environment_name of this SimulationDetailed.
        Name of the simulation environment

        :return: The environment_name of this SimulationDetailed.
        :rtype: str
        """
        return self._environment_name

    @environment_name.setter
    def environment_name(self, environment_name):
        """
        Sets the environment_name of this SimulationDetailed.
        Name of the simulation environment

        :param environment_name: The environment_name of this SimulationDetailed.
        :type: str
        """
        self._environment_name = environment_name

    @property
    def queued_task_identifier(self):
        """
        Gets the queued_task_identifier of this SimulationDetailed.
        Identifier of the task associated to this simulation

        :return: The queued_task_identifier of this SimulationDetailed.
        :rtype: str
        """
        return self._queued_task_identifier

    @queued_task_identifier.setter
    def queued_task_identifier(self, queued_task_identifier):
        """
        Sets the queued_task_identifier of this SimulationDetailed.
        Identifier of the task associated to this simulation

        :param queued_task_identifier: The queued_task_identifier of this SimulationDetailed.
        :type: str
        """
        self._queued_task_identifier = queued_task_identifier

    @property
    def queued_task_state(self):
        """
        Gets the queued_task_state of this SimulationDetailed.
        Read only value, taken from associated task

        :return: The queued_task_state of this SimulationDetailed.
        :rtype: int
        """
        return self._queued_task_state

    @queued_task_state.setter
    def queued_task_state(self, queued_task_state):
        """
        Sets the queued_task_state of this SimulationDetailed.
        Read only value, taken from associated task

        :param queued_task_state: The queued_task_state of this SimulationDetailed.
        :type: int
        """
        self._queued_task_state = queued_task_state

    @property
    def config(self):
        """
        Gets the config of this SimulationDetailed.
        Configuration of the simulation.

        :return: The config of this SimulationDetailed.
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this SimulationDetailed.
        Configuration of the simulation.

        :param config: The config of this SimulationDetailed.
        :type: object
        """
        self._config = config

    @property
    def on_complete_action(self):
        """
        Gets the on_complete_action of this SimulationDetailed.
        Action to take when simulation completes.

        :return: The on_complete_action of this SimulationDetailed.
        :rtype: object
        """
        return self._on_complete_action

    @on_complete_action.setter
    def on_complete_action(self, on_complete_action):
        """
        Sets the on_complete_action of this SimulationDetailed.
        Action to take when simulation completes.

        :param on_complete_action: The on_complete_action of this SimulationDetailed.
        :type: object
        """
        self._on_complete_action = on_complete_action

    @property
    def environment(self):
        """
        Gets the environment of this SimulationDetailed.
        Read only value, expanded on request.

        :return: The environment of this SimulationDetailed.
        :rtype: SimulationEnvironmentDetailed
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """
        Sets the environment of this SimulationDetailed.
        Read only value, expanded on request.

        :param environment: The environment of this SimulationDetailed.
        :type: SimulationEnvironmentDetailed
        """
        self._environment = environment

    @property
    def runs(self):
        """
        Gets the runs of this SimulationDetailed.
        Read only value, expanded on request.

        :return: The runs of this SimulationDetailed.
        :rtype: list[SimulationRunDetailed]
        """
        return self._runs

    @runs.setter
    def runs(self, runs):
        """
        Sets the runs of this SimulationDetailed.
        Read only value, expanded on request.

        :param runs: The runs of this SimulationDetailed.
        :type: list[SimulationRunDetailed]
        """
        self._runs = runs

    @property
    def queued_task(self):
        """
        Gets the queued_task of this SimulationDetailed.
        Read only value, expanded on request.

        :return: The queued_task of this SimulationDetailed.
        :rtype: TaskDetailed
        """
        return self._queued_task

    @queued_task.setter
    def queued_task(self, queued_task):
        """
        Sets the queued_task of this SimulationDetailed.
        Read only value, expanded on request.

        :param queued_task: The queued_task of this SimulationDetailed.
        :type: TaskDetailed
        """
        self._queued_task = queued_task

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

