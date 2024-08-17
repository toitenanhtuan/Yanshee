from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
configuration = openadk.Configuration()
configuration.host = 'http://10.220.5.230:9090/v1'
api_instance = openadk.ServosApi(openadk.ApiClient(configuration))


b1 = {
    "runtime": 1000,
    "angles": {
        "RightShoulderRoll": 90,
        "RightShoulderFlex": 90,
        "RightElbowFlex": 90,
        "LeftShoulderRoll": 90,
        "LeftShoulderFlex": 90,
        "LeftElbowFlex": 90,
    }
}

b2 = {
    "runtime": 2000,
    "angles": {
        "RightHipLR": 81,
        "LeftHipLR": 89,
        "RightHipFB": 58,
        "LeftHipFB": 121,
        "RightKneeFlex": 73,
        "LeftKneeFlex": 107,
        "RightAnkleFB": 112,
        "LeftAnkleFB": 71,
        "RightAnkleUD": 110,
        "LeftAnkleUD": 103,
    }
}

b3 = {
    "runtime": 2000,
    "angles": {
        "RightHipLR": 78,
        "LeftHipLR": 94,
        "RightHipFB": 55,
        "LeftHipFB": 119,
        "RightKneeFlex": 73,
        "LeftKneeFlex": 97,
        "RightAnkleFB": 112,
        "LeftAnkleFB": 75,
        "RightAnkleUD": 100,
        "LeftAnkleUD": 105,
    }
}

b4 = {
    "runtime": 2000,
    "angles": {
        "RightHipLR": 75,
        "LeftHipLR": 98,
        "RightHipFB": 53,
        "LeftHipFB": 117,
        "RightKneeFlex": 73,
        "LeftKneeFlex": 90,
        "RightAnkleFB": 112,
        "LeftAnkleFB": 79,
        "RightAnkleUD": 97,
        "LeftAnkleUD": 106,
    }
}

b5 = {
    "runtime": 2000,
    "angles": {
        "RightHipLR": 72,
        "LeftHipLR": 103,
        "RightHipFB": 50,
        "LeftHipFB": 116,
        "RightKneeFlex": 73,
        "LeftKneeFlex": 83,
        "RightAnkleFB": 112,
        "LeftAnkleFB": 81,
        "RightAnkleUD": 90,
        "LeftAnkleUD": 106,
    }
}

b6 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 75,
        "LeftHipLR": 103,
        "RightHipFB": 48,
        "LeftHipFB": 110,
        "RightKneeFlex": 70,
        "LeftKneeFlex": 84,
        "RightAnkleFB": 105,
        "LeftAnkleFB": 78,
        "RightAnkleUD": 90,
        "LeftAnkleUD": 106,
    }
}

b7 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 78,
        "LeftHipLR": 103,
        "RightHipFB": 46,
        "LeftHipFB": 108,
        "RightKneeFlex": 68,
        "LeftKneeFlex": 85,
        "RightAnkleFB": 98,
        "LeftAnkleFB": 75,
        "RightAnkleUD": 90,
        "LeftAnkleUD": 103,
    }
}

b8 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 81,
        "LeftHipLR": 103,
        "RightHipFB": 45,
        "LeftHipFB": 104,
        "RightKneeFlex": 67,
        "LeftKneeFlex": 86,
        "RightAnkleFB": 91,
        "LeftAnkleFB": 73,
        "RightAnkleUD": 90,
        "LeftAnkleUD": 103,
    }
}

b9 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 82,
        "LeftHipLR": 103,
        "RightHipFB": 35,
        "LeftHipFB": 96,
        "RightKneeFlex": 67,
        "LeftKneeFlex": 84,
        "RightAnkleFB": 91,
        "LeftAnkleFB": 73,
        "RightAnkleUD": 90,
        "LeftAnkleUD": 103,
    }
}


b10 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 83,
        "LeftHipLR": 103,
        "RightHipFB": 25,
        "LeftHipFB": 94,
        "RightKneeFlex": 67,
        "LeftKneeFlex": 82,
        "RightAnkleFB": 91,
        "LeftAnkleFB": 73,
        "RightAnkleUD": 90,
        "LeftAnkleUD": 103,
    }
}

b11 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 84,
        "LeftHipLR": 103,
        "RightHipFB": 20,
        "LeftHipFB": 90,
        "RightKneeFlex": 67,
        "LeftKneeFlex": 80,
        "RightAnkleFB": 91,
        "LeftAnkleFB": 73,
        "RightAnkleUD": 90,
        "LeftAnkleUD": 100,
    }
}

b12 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 83,
        "LeftHipLR": 103,
        "RightHipFB": 21,
        "LeftHipFB": 87,
        "RightKneeFlex": 67,
        "LeftKneeFlex": 83,
        "RightAnkleFB": 91,
        "LeftAnkleFB": 71,
        "RightAnkleUD": 93,
        "LeftAnkleUD": 100,
    }
}

b13 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 82,
        "LeftHipLR": 104,
        "RightHipFB": 23,
        "LeftHipFB": 83,
        "RightKneeFlex": 67,
        "LeftKneeFlex": 85,
        "RightAnkleFB": 91,
        "LeftAnkleFB": 69,
        "RightAnkleUD": 95,
        "LeftAnkleUD": 100,
    }
}

b14 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 80,
        "LeftHipLR": 97,
        "RightHipFB": 28,
        "LeftHipFB": 85,
        "RightKneeFlex": 69,
        "LeftKneeFlex": 90,
        "RightAnkleFB": 92,
        "LeftAnkleFB": 68,
        "RightAnkleUD": 100,
        "LeftAnkleUD": 104,
    }
}

b15 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 73,
        "LeftHipLR": 91,
        "RightHipFB": 24,
        "LeftHipFB": 89,
        "RightKneeFlex": 71,
        "LeftKneeFlex": 95,
        "RightAnkleFB": 92,
        "LeftAnkleFB": 67,
        "RightAnkleUD": 90,
        "LeftAnkleUD": 104,
    }
}

b16 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 80,
        "LeftHipLR": 92,
        "RightHipFB": 20,
        "LeftHipFB": 80,
        "RightKneeFlex": 67,
        "LeftKneeFlex": 99,
        "RightAnkleFB": 92,
        "LeftAnkleFB": 62,
        "RightAnkleUD": 90,
        "LeftAnkleUD": 103,
    }
}

b17 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 90,
        "LeftHipLR": 94,
        "RightHipFB": 17,
        "LeftHipFB": 71,
        "RightKneeFlex": 61,
        "LeftKneeFlex": 103,
        "RightAnkleFB": 92,
        "LeftAnkleFB": 50,
        "RightAnkleUD": 90,
        "LeftAnkleUD": 103,
    }
}

b18 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 88,
        "LeftHipLR": 87,
        "RightHipFB": 20,
        "LeftHipFB": 65,
        "RightKneeFlex": 61,
        "LeftKneeFlex": 136,
        "RightAnkleFB": 92,
        "LeftAnkleFB": 27,
        "RightAnkleUD": 91,
        "LeftAnkleUD": 104,
    }
}

b19 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 89,
        "LeftHipLR": 85,
        "RightHipFB": 25,
        "LeftHipFB": 61,
        "RightKneeFlex": 69,
        "LeftKneeFlex": 147,
        "RightAnkleFB": 72,
        "LeftAnkleFB": 6,
        "RightAnkleUD": 91,
        "LeftAnkleUD": 103,
    }
}

b20 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 88,
        "LeftHipLR": 85,
        "RightHipFB": 19,
        "LeftHipFB": 73,
        "RightKneeFlex": 72,
        "LeftKneeFlex": 131,
        "RightAnkleFB": 58,
        "LeftAnkleFB": 10,
        "RightAnkleUD": 91,
        "LeftAnkleUD": 99,
    }
}

b21 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 93,
        "LeftHipLR": 95,
        "RightHipFB": 24,
        "LeftHipFB": 42,
        "RightKneeFlex": 91,
        "LeftKneeFlex": 92,
        "RightAnkleFB": 54,
        "LeftAnkleFB": 14,
        "RightAnkleUD": 90,
        "LeftAnkleUD": 89,
    }
}

b22 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 91,
        "LeftHipLR": 100,
        "RightHipFB": 26,
        "LeftHipFB": 64,
        "RightKneeFlex": 112,
        "LeftKneeFlex": 76,
        "RightAnkleFB": 50,
        "LeftAnkleFB": 34,
        "RightAnkleUD": 87,
        "LeftAnkleUD": 77,
    }
}

b23 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 93,
        "LeftHipLR": 100,
        "RightHipFB": 25,
        "LeftHipFB": 66,
        "RightKneeFlex": 113,
        "LeftKneeFlex": 78,
        "RightAnkleFB": 53,
        "LeftAnkleFB": 43,
        "RightAnkleUD": 85,
        "LeftAnkleUD": 77,
    }
}

b24 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 93,
        "LeftHipLR": 98,
        "RightHipFB": 21,
        "LeftHipFB": 76,
        "RightKneeFlex": 111,
        "LeftKneeFlex": 78,
        "RightAnkleFB": 61,
        "LeftAnkleFB": 59,
        "RightAnkleUD": 84,
        "LeftAnkleUD": 77,
    }
}

b25 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 88,
        "LeftHipLR": 95,
        "RightHipFB": 23,
        "LeftHipFB": 92,
        "RightKneeFlex": 114,
        "LeftKneeFlex": 96,
        "RightAnkleFB": 69,
        "LeftAnkleFB": 58,
        "RightAnkleUD": 76,
        "LeftAnkleUD": 77,
    }
}

b26 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 77,
        "LeftHipLR": 98,
        "RightHipFB": 27,
        "LeftHipFB": 92,
        "RightKneeFlex": 101,
        "LeftKneeFlex": 96,
        "RightAnkleFB": 81,
        "LeftAnkleFB": 58,
        "RightAnkleUD": 79,
        "LeftAnkleUD": 77,
    }
}

b27 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 73,
        "LeftHipLR": 95,
        "RightHipFB": 37,
        "LeftHipFB": 99,
        "RightKneeFlex": 93,
        "LeftKneeFlex": 106,
        "RightAnkleFB": 91,
        "LeftAnkleFB": 55,
        "RightAnkleUD": 77,
        "LeftAnkleUD": 77,
    }
}

b28 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 73,
        "LeftHipLR": 95,
        "RightHipFB": 40,
        "LeftHipFB": 101,
        "RightKneeFlex": 83,
        "LeftKneeFlex": 126,
        "RightAnkleFB": 101,
        "LeftAnkleFB": 55,
        "RightAnkleUD": 77,
        "LeftAnkleUD": 77,
    }
}

b29 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 77,
        "LeftHipLR": 93,
        "RightHipFB": 44,
        "LeftHipFB": 106,
        "RightKneeFlex": 73,
        "LeftKneeFlex": 141,
        "RightAnkleFB": 110,
        "LeftAnkleFB": 53,
        "RightAnkleUD": 75,
        "LeftAnkleUD": 77,
    }
}

b30 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 82,
        "LeftHipLR": 110,
        "RightHipFB": 41,
        "LeftHipFB": 122,
        "RightKneeFlex": 59,
        "LeftKneeFlex": 127,
        "RightAnkleFB": 115,
        "LeftAnkleFB": 67,
        "RightAnkleUD": 73,
        "LeftAnkleUD": 76,
    }
}

b31 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 82,
        "LeftHipLR": 90,
        "RightHipFB": 41,
        "LeftHipFB": 132,
        "RightKneeFlex": 59,
        "LeftKneeFlex": 127,
        "RightAnkleFB": 115,
        "LeftAnkleFB": 67,
        "RightAnkleUD": 73,
        "LeftAnkleUD": 82,
    }
}

b32 = {
    "runtime": 1000,
    "angles": {
        "RightShoulderRoll": 91,
        "RightShoulderFlex": 141,
        "RightElbowFlex": 166,
        "LeftShoulderRoll": 90,
        "LeftShoulderFlex": 40,
        "LeftElbowFlex": 15,
        "RightHipLR": 90,
        "LeftHipLR": 90,
        "RightHipFB": 62,
        "LeftHipFB": 120,
        "RightKneeFlex": 76,
        "LeftKneeFlex": 106,
        "RightAnkleFB": 111,
        "LeftAnkleFB": 71,
        "RightAnkleUD": 90,
        "LeftAnkleUD": 90,
    }
}

# ---------------------------------------------------------------------------------


try:
    pprint(api_instance.put_servos_angles(b1))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b2))
    time.sleep(2)
    pprint(api_instance.put_servos_angles(b3))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b4))
    time.sleep(0.7)
    pprint(api_instance.put_servos_angles(b5))
    time.sleep(0.7)
    pprint(api_instance.put_servos_angles(b6))
    time.sleep(0.4)
    pprint(api_instance.put_servos_angles(b7))
    time.sleep(0.3)
    pprint(api_instance.put_servos_angles(b8))
    time.sleep(0.2)
    pprint(api_instance.put_servos_angles(b9))
    time.sleep(0.2)
    pprint(api_instance.put_servos_angles(b10))
    time.sleep(0.2)
    pprint(api_instance.put_servos_angles(b11))
    time.sleep(0.4)
    pprint(api_instance.put_servos_angles(b12))
    time.sleep(0.4)
    pprint(api_instance.put_servos_angles(b13))
    time.sleep(0.2)
    pprint(api_instance.put_servos_angles(b14))
    time.sleep(0.2)
    pprint(api_instance.put_servos_angles(b15))
    time.sleep(0.2)
    pprint(api_instance.put_servos_angles(b16))
    time.sleep(0.7)
    pprint(api_instance.put_servos_angles(b17))
    time.sleep(0.7)
    pprint(api_instance.put_servos_angles(b18))
    time.sleep(0.7)
    pprint(api_instance.put_servos_angles(b19))
    time.sleep(0.7)
    pprint(api_instance.put_servos_angles(b20))
    time.sleep(0.7)
    pprint(api_instance.put_servos_angles(b21))
    time.sleep(0.7)
    pprint(api_instance.put_servos_angles(b22))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b23))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b24))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b25))
    time.sleep(0.7)
    pprint(api_instance.put_servos_angles(b26))
    time.sleep(0.7)
    pprint(api_instance.put_servos_angles(b27))
    time.sleep(0.7)
    pprint(api_instance.put_servos_angles(b28))
    time.sleep(0.7)
    pprint(api_instance.put_servos_angles(b29))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b30))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b31))
    time.sleep(1.2)
    pprint(api_instance.put_servos_angles(b32))
    time.sleep(1)
except ApiException as e:
    print("Exception when calling ServosApi->put_servos_angles: %s\n" % e)


