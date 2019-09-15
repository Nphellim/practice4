#encoding=utf-8
# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissiosdfns and
# limitations under the License.

from random import *
import webapp2
import json


class MainPage(webapp2.RequestHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        
        nPoints = 5000000
        sum_in_sample = 0
    
        for i in range(nPoints):
            x_sample_cord =  random()
            y_sample_cord =  random()
            d = x_sample_cord**2 + y_sample_cord**2
            if d <= 1:
                sum_in_sample = sum_in_sample + 1
        t = sum_in_sample        
        
        res = {
            'sum_value': t
        }
        
        self.response.write(json.dumps(res))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)


