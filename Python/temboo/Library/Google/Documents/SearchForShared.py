# -*- coding: utf-8 -*-

###############################################################################
#
# SearchForShared
# Retrieves a list of all documents shared by the two users you specify.
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

class SearchForShared(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchForShared Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchForShared, self).__init__(temboo_session, '/Library/Google/Documents/SearchForShared')


    def new_input_set(self):
        return SearchForSharedInputSet()

    def _make_result_set(self, result, path):
        return SearchForSharedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchForSharedChoreographyExecution(session, exec_id, path)

class SearchForSharedInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchForShared
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) A Google App-specific password that you've generated after enabling 2-Step Verification.)
        """
        super(SearchForSharedInputSet, self)._set_input('Password', value)
    def set_User1(self, value):
        """
        Set the value of the User1 input for this Choreo. ((required, string) The email address of the first document collaborator.)
        """
        super(SearchForSharedInputSet, self)._set_input('User1', value)
    def set_User2(self, value):
        """
        Set the value of the User2 input for this Choreo. ((required, string) The email address for the second document collaborator.)
        """
        super(SearchForSharedInputSet, self)._set_input('User2', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(SearchForSharedInputSet, self)._set_input('Username', value)

class SearchForSharedResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchForShared Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from the Google Documents API.)
        """
        return self._output.get('Response', None)

class SearchForSharedChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchForSharedResultSet(response, path)
