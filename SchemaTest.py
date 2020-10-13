import sys
import os
import json

string schemaJson = @"{
    "$schema": "http://json-schema.org/draft-06/schema#",
	"$id": "https://github.com/gabe7murphy/oeda-json/blob/master/Phoenix.Countries.actors.json",
	"title": "Phoenix.CountriesActors",
	"description": "OEDA dictionary for Countries and Actors",
    "type": "array",
    "items": {
        "$ref": "#/definitions/WelcomeElement"
    },
    "definitions": {
        "WelcomeElement": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "name": {
                    "type": "string"
                },
                "alias": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "codes": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "comments": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            },
            "required": [
                "name",
                "codes"
            ],
            "title": "WelcomeElement"
        }
    }
}";

JsonSchema schema = JsonSchema.Parse(schemaJson);

JObject person = JObject.Parse(@"{
  'name': 'TRUMP',
  'codes': ['USAELI','USAGOV']
}");

bool valid = person.IsValid(schema);