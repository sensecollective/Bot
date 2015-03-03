# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteDocumentOrFile
# Permanently deletes the document or file you specify.
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

class DeleteDocumentOrFile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteDocumentOrFile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteDocumentOrFile, self).__init__(temboo_session, '/Library/Google/Documents/DeleteDocumentOrFile')


    def new_input_set(self):
        return DeleteDocumentOrFileInputSet()

    def _make_result_set(self, result, path):
        return DeleteDocumentOrFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteDocumentOrFileChoreographyExecution(session, exec_id, path)

class DeleteDocumentOrFileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteDocumentOrFile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) A Google App-specific password that you've generated after enabling 2-Step Verification.)
        """
        super(DeleteDocumentOrFileInputSet, self)._set_input('Password', value)
    def set_ResourceID(self, value):
        """
        Set the value of the ResourceID input for this Choreo. ((required, string) The resource ID for the document or file to delete.)
        """
        super(DeleteDocumentOrFileInputSet, self)._set_input('ResourceID', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(DeleteDocumentOrFileInputSet, self)._set_input('Username', value)

class DeleteDocumentOrFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteDocumentOrFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (There is no XML response for delete requests.)
        """
        return self._output.get('Response', None)

class DeleteDocumentOrFileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteDocumentOrFileResultSet(response, path)
