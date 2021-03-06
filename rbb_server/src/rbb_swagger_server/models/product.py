# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rbb_swagger_server.models.base_model_ import Model
from rbb_swagger_server.models.product_file import ProductFile  # noqa: F401,E501
from rbb_swagger_server.models.topic_mapping import TopicMapping  # noqa: F401,E501
from rbb_swagger_server import util


class Product(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, uid: str=None, plugin: str=None, product_type: str=None, product_data: object=None, created: datetime=None, title: str=None, configuration_tag: str=None, configuration_rule: str=None, topics: List[TopicMapping]=None, files: List[ProductFile]=None):  # noqa: E501
        """Product - a model defined in Swagger

        :param uid: The uid of this Product.  # noqa: E501
        :type uid: str
        :param plugin: The plugin of this Product.  # noqa: E501
        :type plugin: str
        :param product_type: The product_type of this Product.  # noqa: E501
        :type product_type: str
        :param product_data: The product_data of this Product.  # noqa: E501
        :type product_data: object
        :param created: The created of this Product.  # noqa: E501
        :type created: datetime
        :param title: The title of this Product.  # noqa: E501
        :type title: str
        :param configuration_tag: The configuration_tag of this Product.  # noqa: E501
        :type configuration_tag: str
        :param configuration_rule: The configuration_rule of this Product.  # noqa: E501
        :type configuration_rule: str
        :param topics: The topics of this Product.  # noqa: E501
        :type topics: List[TopicMapping]
        :param files: The files of this Product.  # noqa: E501
        :type files: List[ProductFile]
        """
        self.swagger_types = {
            'uid': str,
            'plugin': str,
            'product_type': str,
            'product_data': object,
            'created': datetime,
            'title': str,
            'configuration_tag': str,
            'configuration_rule': str,
            'topics': List[TopicMapping],
            'files': List[ProductFile]
        }

        self.attribute_map = {
            'uid': 'uid',
            'plugin': 'plugin',
            'product_type': 'product_type',
            'product_data': 'product_data',
            'created': 'created',
            'title': 'title',
            'configuration_tag': 'configuration_tag',
            'configuration_rule': 'configuration_rule',
            'topics': 'topics',
            'files': 'files'
        }

        self._uid = uid
        self._plugin = plugin
        self._product_type = product_type
        self._product_data = product_data
        self._created = created
        self._title = title
        self._configuration_tag = configuration_tag
        self._configuration_rule = configuration_rule
        self._topics = topics
        self._files = files

    @classmethod
    def from_dict(cls, dikt) -> 'Product':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Product of this Product.  # noqa: E501
        :rtype: Product
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uid(self) -> str:
        """Gets the uid of this Product.


        :return: The uid of this Product.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid: str):
        """Sets the uid of this Product.


        :param uid: The uid of this Product.
        :type uid: str
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

    @property
    def plugin(self) -> str:
        """Gets the plugin of this Product.

        Plugin that created this product  # noqa: E501

        :return: The plugin of this Product.
        :rtype: str
        """
        return self._plugin

    @plugin.setter
    def plugin(self, plugin: str):
        """Sets the plugin of this Product.

        Plugin that created this product  # noqa: E501

        :param plugin: The plugin of this Product.
        :type plugin: str
        """
        if plugin is None:
            raise ValueError("Invalid value for `plugin`, must not be `None`")  # noqa: E501

        self._plugin = plugin

    @property
    def product_type(self) -> str:
        """Gets the product_type of this Product.

        Type of product  # noqa: E501

        :return: The product_type of this Product.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type: str):
        """Sets the product_type of this Product.

        Type of product  # noqa: E501

        :param product_type: The product_type of this Product.
        :type product_type: str
        """
        if product_type is None:
            raise ValueError("Invalid value for `product_type`, must not be `None`")  # noqa: E501

        self._product_type = product_type

    @property
    def product_data(self) -> object:
        """Gets the product_data of this Product.

        Product data  # noqa: E501

        :return: The product_data of this Product.
        :rtype: object
        """
        return self._product_data

    @product_data.setter
    def product_data(self, product_data: object):
        """Sets the product_data of this Product.

        Product data  # noqa: E501

        :param product_data: The product_data of this Product.
        :type product_data: object
        """
        if product_data is None:
            raise ValueError("Invalid value for `product_data`, must not be `None`")  # noqa: E501

        self._product_data = product_data

    @property
    def created(self) -> datetime:
        """Gets the created of this Product.

        Date and time this product was created.  # noqa: E501

        :return: The created of this Product.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created: datetime):
        """Sets the created of this Product.

        Date and time this product was created.  # noqa: E501

        :param created: The created of this Product.
        :type created: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def title(self) -> str:
        """Gets the title of this Product.

        Some descriptive title  # noqa: E501

        :return: The title of this Product.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Product.

        Some descriptive title  # noqa: E501

        :param title: The title of this Product.
        :type title: str
        """

        self._title = title

    @property
    def configuration_tag(self) -> str:
        """Gets the configuration_tag of this Product.

        Tag of the configuration file that generated this product  # noqa: E501

        :return: The configuration_tag of this Product.
        :rtype: str
        """
        return self._configuration_tag

    @configuration_tag.setter
    def configuration_tag(self, configuration_tag: str):
        """Sets the configuration_tag of this Product.

        Tag of the configuration file that generated this product  # noqa: E501

        :param configuration_tag: The configuration_tag of this Product.
        :type configuration_tag: str
        """

        self._configuration_tag = configuration_tag

    @property
    def configuration_rule(self) -> str:
        """Gets the configuration_rule of this Product.

        Name of the rule that generated this product  # noqa: E501

        :return: The configuration_rule of this Product.
        :rtype: str
        """
        return self._configuration_rule

    @configuration_rule.setter
    def configuration_rule(self, configuration_rule: str):
        """Sets the configuration_rule of this Product.

        Name of the rule that generated this product  # noqa: E501

        :param configuration_rule: The configuration_rule of this Product.
        :type configuration_rule: str
        """

        self._configuration_rule = configuration_rule

    @property
    def topics(self) -> List[TopicMapping]:
        """Gets the topics of this Product.


        :return: The topics of this Product.
        :rtype: List[TopicMapping]
        """
        return self._topics

    @topics.setter
    def topics(self, topics: List[TopicMapping]):
        """Sets the topics of this Product.


        :param topics: The topics of this Product.
        :type topics: List[TopicMapping]
        """
        if topics is None:
            raise ValueError("Invalid value for `topics`, must not be `None`")  # noqa: E501

        self._topics = topics

    @property
    def files(self) -> List[ProductFile]:
        """Gets the files of this Product.


        :return: The files of this Product.
        :rtype: List[ProductFile]
        """
        return self._files

    @files.setter
    def files(self, files: List[ProductFile]):
        """Sets the files of this Product.


        :param files: The files of this Product.
        :type files: List[ProductFile]
        """
        if files is None:
            raise ValueError("Invalid value for `files`, must not be `None`")  # noqa: E501

        self._files = files
