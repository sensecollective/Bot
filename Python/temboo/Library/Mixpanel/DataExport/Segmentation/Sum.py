# -*- coding: utf-8 -*-

###############################################################################
#
# Sum
# Sums an expression for events per unit time.
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

class Sum(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Sum Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Sum, self).__init__(temboo_session, '/Library/Mixpanel/DataExport/Segmentation/Sum')


    def new_input_set(self):
        return SumInputSet()

    def _make_result_set(self, result, path):
        return SumResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SumChoreographyExecution(session, exec_id, path)

class SumInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Sum
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided my Mixpanel. You can find your Mixpanel API Key in the project settings dialog in the Mixpanel app.)
        """
        super(SumInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) The API Secret provided by Mixpanel. You can find your Mixpanel API Secret in the project settings dialog in the Mixpanel app.)
        """
        super(SumInputSet, self)._set_input('APISecret', value)
    def set_EventName(self, value):
        """
        Set the value of the EventName input for this Choreo. ((required, string) The event that you wish to segment on.)
        """
        super(SumInputSet, self)._set_input('EventName', value)
    def set_Expire(self, value):
        """
        Set the value of the Expire input for this Choreo. ((optional, integer) The amount of minutes past NOW() before the request will expire. Defaults to 1.)
        """
        super(SumInputSet, self)._set_input('Expire', value)
    def set_FromDate(self, value):
        """
        Set the value of the FromDate input for this Choreo. ((required, date) The date in yyyy-mm-dd format from which to begin querying for the event from. This date is inclusive.)
        """
        super(SumInputSet, self)._set_input('FromDate', value)
    def set_On(self, value):
        """
        Set the value of the On input for this Choreo. ((required, string) The expression to sum per unit time. Must be a numeric expression (e.g., number(properties["time"]). See Choreo description for examples.)
        """
        super(SumInputSet, self)._set_input('On', value)
    def set_ToDate(self, value):
        """
        Set the value of the ToDate input for this Choreo. ((required, date) The date in yyyy-mm-dd format from which to stop querying for the event from. This date is inclusive. The date range may not be more than 30 days.)
        """
        super(SumInputSet, self)._set_input('ToDate', value)
    def set_Unit(self, value):
        """
        Set the value of the Unit input for this Choreo. ((optional, string) Determines the buckets into which the property values that you segment on are placed. Valid values are: hour or day.)
        """
        super(SumInputSet, self)._set_input('Unit', value)
    def set_Where(self, value):
        """
        Set the value of the Where input for this Choreo. ((optional, string) An expression to filter events by  (e.g., number(properties["time"]) >= 2000). See Choreo description for examples.)
        """
        super(SumInputSet, self)._set_input('Where', value)

class SumResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Sum Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mixpanel.)
        """
        return self._output.get('Response', None)

class SumChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SumResultSet(response, path)
