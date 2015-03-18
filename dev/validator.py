from jsonschema import Draft4Validator, RefResolver
import os
import json
import urllib.request




if __name__=="__main__":
    # Hack to the extreme for now
    '''
    testdata = {
        'schema': '../schema/mhealth/schema/generic/unit-value-1.0.json',
        'data': [
            '../schema/mhealth/sampleData/generic/unit-value/1.0/shouldFail/empty-document.json',
            '../schema/mhealth/sampleData/generic/unit-value/1.0/shouldFail/number-unit.json',
            '../schema/mhealth/sampleData/generic/unit-value/1.0/shouldFail/string-value.json',
            '../schema/mhealth/sampleData/generic/unit-value/1.0/shouldFail/unit-only.json',
            '../schema/mhealth/sampleData/generic/unit-value/1.0/shouldFail/value-only.json',
            '../schema/mhealth/sampleData/generic/unit-value/1.0/shouldPass/negative-float-value.json',
            '../schema/mhealth/sampleData/generic/unit-value/1.0/shouldPass/negative-integer-value.json',
            '../schema/mhealth/sampleData/generic/unit-value/1.0/shouldPass/positive-float-value.json',
            '../schema/mhealth/sampleData/generic/unit-value/1.0/shouldPass/positive-integer-value.json',
            '../schema/mhealth/sampleData/generic/unit-value/1.0/shouldPass/zero-float-value.json',
            '../schema/mhealth/sampleData/generic/unit-value/1.0/shouldPass/zero-integer-value.json',
        ]
    }
    '''
        
    

    testdata = {
        'schema': 'http://localhost:12000/cmr/patient.json',
        'data': [
            'http://localhost:12100/patient.juhan.json',
            'http://localhost:12100/patient.ben.json',
            'http://localhost:12100/patient.invalid.json',
        ]
    }
    
    
    with urllib.request.urlopen( testdata['schema'] ) as remote_schema:
        schema = json.loads(remote_schema.read().decode('utf-8'))
    
    validator = Draft4Validator(schema)
    

    for test in testdata['data']:
        print("-------------------------------------------")
        with urllib.request.urlopen( test ) as remote_data:
            data = json.loads(remote_data.read().decode('utf-8'))
        
        
        validator.validate(data)
        
        try:
            validator.validate(data)
            print("Successful validation of", test)
        except Exception as inst:
            print("Failed validation of", test)
            print(inst.args[0])

        print("\n")
            
