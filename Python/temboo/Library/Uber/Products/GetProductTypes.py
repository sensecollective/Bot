# -*- coding: utf-8 -*-

###############################################################################
#
# GetProductTypes
# Returns information about the Uber products offered at a given location.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetProductTypes(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetProductTypes Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetProductTypes, self).__init__(temboo_session, '/Library/Uber/Products/GetProductTypes')


    def new_input_set(self):
        return GetProductTypesInputSet()

    def _make_result_set(self, result, path):
        return GetProductTypesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetProductTypesChoreographyExecution(session, exec_id, path)

class GetProductTypesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetProductTypes
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude coordinate for the location e.g., 40.71863.)
        """
        super(GetProductTypesInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude coordinate for the location e.g., -74.005584.)
        """
        super(GetProductTypesInputSet, self)._set_input('Longitude', value)
    def set_ServerToken(self, value):
        """
        Set the value of the ServerToken input for this Choreo. ((required, string) The Sever Token provided by Uber.)
        """
        super(GetProductTypesInputSet, self)._set_input('ServerToken', value)

class GetProductTypesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetProductTypes Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Uber.)
        """
        return self._output.get('Response', None)

class GetProductTypesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetProductTypesResultSet(response, path)