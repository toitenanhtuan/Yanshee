from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
configuration = openadk.Configuration()
configuration.host = 'http://10.220.5.230:9090/v1'
api_instance = openadk.ServosApi(openadk.ApiClient(configuration))
api_instance_motion = openadk.MotionsApi(openadk.ApiClient(configuration))

# ---------------------------------------------------------------------------------
b33 = {
    "operation": "start",
    "motion": {
        "name": "walk",
        "direction": "forward",
        "repeat": 4,
        "speed": "slow"
    }
}

# b98 = {
#     "runtime": 1000,
#     "angles": {
#         "RightShoulderRoll": 91,
#         "RightShoulderFlex": 141,
#         "RightElbowFlex": 166,
#         "LeftShoulderRoll": 90,
#         "LeftShoulderFlex": 40,
#         "LeftElbowFlex": 15,
#         "RightHipLR": 90,
#         "LeftHipLR": 90,
#         "RightHipFB": 62,
#         "LeftHipFB": 120,
#         "RightKneeFlex": 76,
#         "LeftKneeFlex": 106,
#         "RightAnkleFB": 111,
#         "LeftAnkleFB": 71,
#         "RightAnkleUD": 90,
#         "LeftAnkleUD": 90,
#     }
# }

# ---------------------------------------------------------------------------------


try:
    pprint(api_instance_motion.put_motions(b33))
    time.sleep(10)

    # pprint(api_instance.put_servos_angles(b98))
except ApiException as e:
    print("Exception when calling ServosApi->put_servos_angles: %s\n" % e)
