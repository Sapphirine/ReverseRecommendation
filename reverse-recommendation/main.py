#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
# See the License for the specific language governing permissions and
# limitations under the License.
#

# for google app engine
import jinja2
import json
import os
import webapp2

from YelpAPI.YelpSearchAPI import query_result

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        template = jinja_env.get_template(template)
        return template.render(params)

    def render_json(self, json_obj):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(json_obj))

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainHandler(Handler):
    def get(self):
        self.render("index.html")

    def post(self):
        review = self.request.get("review")
        keywords, search_result_jsons = query_result(review)
        # keywords = keywords.replace(' ', ', ')
        for result_json in search_result_jsons:
            result_json["image_url"] = result_json["image_url"].replace("ms", "l")

        # print "search_result_json:"
        # print search_result_json
        # self.render_json(search_result_json)
        self.render("search.html", keywords=keywords,                          \
                                   result_jsons1=search_result_jsons[:3],      \
                                   result_jsons2=search_result_jsons[3:])


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
