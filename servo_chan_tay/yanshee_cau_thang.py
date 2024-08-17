from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
configuration = openadk.Configuration()
configuration.host = 'http://10.220.5.230:9090/v1'
api_instance = openadk.ServosApi(openadk.ApiClient(configuration))

# ---------------------------------------------------------------------------------
b33a = {
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

b34 = {
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

b35 = {
    "runtime": 1000,
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

b36 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 62,
        "LeftHipFB": 117,
        "RightAnkleFB": 97,
        "LeftHipLR": 101,
        "LeftAnkleUD": 99,
        "LeftKneeFlex": 113,
        "RightHipLR": 88,
        "RightAnkleUD": 87,
        "RightKneeFlex": 81,
        "RightHipFB": 55,
    }
}

b37 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 57,
        "LeftHipFB": 109,
        "RightAnkleFB": 97,
        "LeftHipLR": 96,
        "LeftAnkleUD": 104,
        "LeftKneeFlex": 113,
        "RightHipLR": 93,
        "RightAnkleUD": 87,
        "RightKneeFlex": 60,
        "RightHipFB": 38,
    }
}

b38 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 51,
        "LeftHipFB": 80,
        "RightAnkleFB": 97,
        "LeftHipLR": 71,
        "LeftAnkleUD": 109,
        "LeftKneeFlex": 100,
        "RightHipLR": 55,
        "RightAnkleUD": 118,
        "RightKneeFlex": 37,
        "RightHipFB": 31,
    }
}

b39 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 48,
        "LeftHipFB": 69,
        "RightAnkleFB": 97,
        "LeftHipLR": 72,
        "LeftAnkleUD": 109,
        "LeftKneeFlex": 96,
        "RightHipLR": 60,
        "RightAnkleUD": 118,
        "RightKneeFlex": 37,
        "RightHipFB": 20,
    }
}

b40 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 37,
        "LeftHipFB": 48,
        "RightAnkleFB": 65,
        "LeftHipLR": 69,
        "LeftAnkleUD": 107,
        "LeftKneeFlex": 101,
        "RightHipLR": 61,
        "RightAnkleUD": 118,
        "RightKneeFlex": 54,
        "RightHipFB": 27,
    }
}

b41 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 39,
        "LeftHipFB": 73,
        "RightAnkleFB": 65,
        "LeftHipLR": 66,
        "LeftAnkleUD": 106,
        "LeftKneeFlex": 95,
        "RightHipLR": 60,
        "RightAnkleUD": 115,
        "RightKneeFlex": 78,
        "RightHipFB": 19,
    }
}

b42 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 51,
        "LeftHipFB": 105,
        "RightAnkleFB": 41,
        "LeftHipLR": 73,
        "LeftAnkleUD": 91,
        "LeftKneeFlex": 95,
        "RightHipLR": 62,
        "RightAnkleUD": 100,
        "RightKneeFlex": 129,
        "RightHipFB": 16,
    }
}

b43 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 70,
        "LeftHipFB": 126,
        "RightAnkleFB": 27,
        "LeftHipLR": 72,
        "LeftAnkleUD": 91,
        "LeftKneeFlex": 95,
        "RightHipLR": 60,
        "RightAnkleUD": 90,
        "RightKneeFlex": 167,
        "RightHipFB": 12,
    }
}

b44 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 70,
        "LeftHipFB": 124,
        "RightAnkleFB": 47,
        "LeftHipLR": 72,
        "LeftAnkleUD": 91,
        "LeftKneeFlex": 102,
        "RightHipLR": 63,
        "RightAnkleUD": 82,
        "RightKneeFlex": 167,
        "RightHipFB": 38,
    }
}

b45 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 81,
        "LeftHipFB": 147,
        "RightAnkleFB": 51,
        "LeftHipLR": 83,
        "LeftAnkleUD": 101,
        "LeftKneeFlex": 145,
        "RightHipLR": 81,
        "RightAnkleUD": 78,
        "RightKneeFlex": 166,
        "RightHipFB": 49,
    }
}

b46 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 81,
        "LeftHipFB": 163,
        "RightAnkleFB": 50,
        "LeftHipLR": 114,
        "LeftAnkleUD": 87,
        "LeftKneeFlex": 143,
        "RightHipLR": 90,
        "RightAnkleUD": 68,
        "RightKneeFlex": 167,
        "RightHipFB": 55,
    }
}

b47 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 81,
        "LeftHipFB": 166,
        "RightAnkleFB": 49,
        "LeftHipLR": 115,
        "LeftAnkleUD": 59,
        "LeftKneeFlex": 119,
        "RightHipLR": 101,
        "RightAnkleUD": 68,
        "RightKneeFlex": 167,
        "RightHipFB": 69,
    }
}

b48 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 87,
        "LeftHipFB": 166,
        "RightAnkleFB": 59,
        "LeftHipLR": 105,
        "LeftAnkleUD": 79,
        "LeftKneeFlex": 112,
        "RightHipLR": 95,
        "RightAnkleUD": 76,
        "RightKneeFlex": 147,
        "RightHipFB": 69,
    }
}

b49 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 71,
        "LeftHipFB": 120,
        "RightAnkleFB": 111,
        "LeftHipLR": 90,
        "LeftAnkleUD": 92,
        "LeftKneeFlex": 107,
        "RightHipLR": 90,
        "RightAnkleUD": 90,
        "RightKneeFlex": 76,
        "RightHipFB": 61,
    }
}

b50 = {
    "runtime": 2000,
    "angles": {
        "LeftAnkleFB": 70,
        "LeftHipFB": 120,
        "RightAnkleFB": 111,
        "LeftHipLR": 105,
        "LeftAnkleUD": 92,
        "LeftKneeFlex": 108,
        "RightHipLR": 92,
        "RightAnkleUD": 73,
        "RightKneeFlex": 76,
        "RightHipFB": 61,
    }
}

b51 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 71,
        "LeftHipFB": 120,
        "RightAnkleFB": 124,
        "LeftHipLR": 105,
        "LeftAnkleUD": 71,
        "LeftKneeFlex": 109,
        "RightHipLR": 81,
        "RightAnkleUD": 76,
        "RightKneeFlex": 76,
        "RightHipFB": 83,
    }
}

b52 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 97,
        "LeftHipFB": 129,
        "RightAnkleFB": 137,
        "LeftHipLR": 94,
        "LeftAnkleUD": 71,
        "LeftKneeFlex": 108,
        "RightHipLR": 84,
        "RightAnkleUD": 76,
        "RightKneeFlex": 72,
        "RightHipFB": 103,
    }
}

b53 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 121,
        "LeftHipFB": 130,
        "RightAnkleFB": 132,
        "LeftHipLR": 93,
        "LeftAnkleUD": 81,
        "LeftKneeFlex": 91,
        "RightHipLR": 87,
        "RightAnkleUD": 72,
        "RightKneeFlex": 79,
        "RightHipFB": 110,
    }
}

b54 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 117,
        "LeftHipFB": 124,
        "RightAnkleFB": 141,
        "LeftHipLR": 95,
        "LeftAnkleUD": 80,
        "LeftKneeFlex": 82,
        "RightHipLR": 87,
        "RightAnkleUD": 78,
        "RightKneeFlex": 77,
        "RightHipFB": 115,
    }
}

b55 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 117,
        "LeftHipFB": 134,
        "RightAnkleFB": 141,
        "LeftHipLR": 95,
        "LeftAnkleUD": 80,
        "LeftKneeFlex": 82,
        "RightHipLR": 87,
        "RightAnkleUD": 83,
        "RightKneeFlex": 77,
        "RightHipFB": 105,
    }
}

b56 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 128,
        "LeftHipFB": 153,
        "RightAnkleFB": 149,
        "LeftHipLR": 95,
        "LeftAnkleUD": 85,
        "LeftKneeFlex": 81,
        "RightHipLR": 88,
        "RightAnkleUD": 90,
        "RightKneeFlex": 76,
        "RightHipFB": 98,
    }
}

b57 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 143,
        "LeftHipFB": 171,
        "RightAnkleFB": 147,
        "LeftHipLR": 94,
        "LeftAnkleUD": 90,
        "LeftKneeFlex": 56,
        "RightHipLR": 91,
        "RightAnkleUD": 91,
        "RightKneeFlex": 84,
        "RightHipFB": 75,
    }
}

b58 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 161,
        "LeftHipFB": 158,
        "RightAnkleFB": 141,
        "LeftHipLR": 92,
        "LeftAnkleUD": 105,
        "LeftKneeFlex": 16,
        "RightHipLR": 97,
        "RightAnkleUD": 101,
        "RightKneeFlex": 73,
        "RightHipFB": 69,
    }
}

b59 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 154,
        "LeftHipFB": 161,
        "RightAnkleFB": 141,
        "LeftHipLR": 92,
        "LeftAnkleUD": 106,
        "LeftKneeFlex": 16,
        "RightHipLR": 92,
        "RightAnkleUD": 101,
        "RightKneeFlex": 73,
        "RightHipFB": 73,
    }
}

b60 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 141,
        "LeftHipFB": 143,
        "RightAnkleFB": 141,
        "LeftHipLR": 91,
        "LeftAnkleUD": 106,
        "LeftKneeFlex": 26,
        "RightHipLR": 78,
        "RightAnkleUD": 101,
        "RightKneeFlex": 73,
        "RightHipFB": 62,
    }
}

b61 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 140,
        "LeftHipFB": 139,
        "RightAnkleFB": 144,
        "LeftHipLR": 92,
        "LeftAnkleUD": 112,
        "LeftKneeFlex": 30,
        "RightHipLR": 73,
        "RightAnkleUD": 101,
        "RightKneeFlex": 73,
        "RightHipFB": 59,
    }
}

b62 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 123,
        "LeftHipFB": 121,
        "RightAnkleFB": 115,
        "LeftHipLR": 99,
        "LeftAnkleUD": 107,
        "LeftKneeFlex": 35,
        "RightHipLR": 77,
        "RightAnkleUD": 110,
        "RightKneeFlex": 87,
        "RightHipFB": 58,
    }
}

b63 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 109,
        "LeftHipFB": 100,
        "RightAnkleFB": 115,
        "LeftHipLR": 93,
        "LeftAnkleUD": 107,
        "LeftKneeFlex": 40,
        "RightHipLR": 79,
        "RightAnkleUD": 110,
        "RightKneeFlex": 87,
        "RightHipFB": 58,
    }
}

b64 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 100,
        "LeftHipFB": 110,
        "RightAnkleFB": 115,
        "LeftHipLR": 93,
        "LeftAnkleUD": 100,
        "LeftKneeFlex": 52,
        "RightHipLR": 85,
        "RightAnkleUD": 107,
        "RightKneeFlex": 80,
        "RightHipFB": 58,
    }
}

b65 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleFB": 71,
        "LeftHipFB": 120,
        "RightAnkleFB": 111,
        "LeftHipLR": 90,
        "LeftAnkleUD": 91,
        "LeftKneeFlex": 106,
        "RightHipLR": 90,
        "RightAnkleUD": 90,
        "RightKneeFlex": 76,
        "RightHipFB": 60,
    }
}

b66 = {
    "runtime": 1000,
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

b67 = {
    "runtime": 1000,
    "angles": {
        "RightHipLR": 86,
        "LeftHipLR": 94,
        "RightHipFB": 58,
        "LeftHipFB": 116,
        "RightKneeFlex": 73,
        "LeftKneeFlex": 107,
        "RightAnkleFB": 112,
        "LeftAnkleFB": 63,
        "RightAnkleUD": 100,
        "LeftAnkleUD": 103,
    }
}

b68 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 105,
        "RightAnkleFB": 111,
        "RightKneeFlex": 76,
        "LeftHipFB": 108,
        "LeftAnkleFB": 56,
        "RightHipFB": 61,
        "LeftKneeFlex": 112,
        "LeftHipLR": 101,
        "RightAnkleUD": 90,
        "RightHipLR": 91,
    }
}

b69 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 110,
        "RightAnkleFB": 111,
        "RightKneeFlex": 76,
        "LeftHipFB": 108,
        "LeftAnkleFB": 37,
        "RightHipFB": 67,
        "LeftKneeFlex": 140,
        "LeftHipLR": 100,
        "RightAnkleUD": 110,
        "RightHipLR": 85,
    }
}

b70 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 110,
        "RightAnkleFB": 111,
        "RightKneeFlex": 76,
        "LeftHipFB": 87,
        "LeftAnkleFB": 41,
        "RightHipFB": 67,
        "LeftKneeFlex": 125,
        "LeftHipLR": 90,
        "RightAnkleUD": 118,
        "RightHipLR": 75,
    }
}

b71 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 108,
        "RightAnkleFB": 111,
        "RightKneeFlex": 76,
        "LeftHipFB": 82,
        "LeftAnkleFB": 37,
        "RightHipFB": 56,
        "LeftKneeFlex": 133,
        "LeftHipLR": 90,
        "RightAnkleUD": 118,
        "RightHipLR": 76,
    }
}

b72 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 113,
        "RightAnkleFB": 111,
        "RightKneeFlex": 76,
        "LeftHipFB": 78,
        "LeftAnkleFB": 13,
        "RightHipFB": 56,
        "LeftKneeFlex": 154,
        "LeftHipLR": 87,
        "RightAnkleUD": 118,
        "RightHipLR": 76,
    }
}

b73 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 113,
        "RightAnkleFB": 111,
        "RightKneeFlex": 61,
        "LeftHipFB": 61,
        "LeftAnkleFB": 11,
        "RightHipFB": 50,
        "LeftKneeFlex": 138,
        "LeftHipLR": 79,
        "RightAnkleUD": 118,
        "RightHipLR": 70,
    }
}

b74 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 108,
        "RightAnkleFB": 103,
        "RightKneeFlex": 59,
        "LeftHipFB": 43,
        "LeftAnkleFB": 11,
        "RightHipFB": 53,
        "LeftKneeFlex": 115,
        "LeftHipLR": 77,
        "RightAnkleUD": 112,
        "RightHipLR": 69,
    }
}

b75 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 98,
        "RightAnkleFB": 87,
        "RightKneeFlex": 52,
        "LeftHipFB": 54,
        "LeftAnkleFB": 9,
        "RightHipFB": 23,
        "LeftKneeFlex": 112,
        "LeftHipLR": 76,
        "RightAnkleUD": 107,
        "RightHipLR": 67,
    }
}

b76 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 84,
        "RightAnkleFB": 54,
        "RightKneeFlex": 106,
        "LeftHipFB": 81,
        "LeftAnkleFB": 29,
        "RightHipFB": 2,
        "LeftKneeFlex": 78,
        "LeftHipLR": 80,
        "RightAnkleUD": 88,
        "RightHipLR": 74,
    }
}

b77 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 82,
        "RightAnkleFB": 53,
        "RightKneeFlex": 123,
        "LeftHipFB": 91,
        "LeftAnkleFB": 46,
        "RightHipFB": 5,
        "LeftKneeFlex": 78,
        "LeftHipLR": 74,
        "RightAnkleUD": 78,
        "RightHipLR": 75,
    }
}

b78 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 82,
        "RightAnkleFB": 53,
        "RightKneeFlex": 138,
        "LeftHipFB": 91,
        "LeftAnkleFB": 56,
        "RightHipFB": 35,
        "LeftKneeFlex": 88,
        "LeftHipLR": 74,
        "RightAnkleUD": 78,
        "RightHipLR": 75,
    }
}

b79 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 82,
        "RightAnkleFB": 48,
        "RightKneeFlex": 168,
        "LeftHipFB": 90,
        "LeftAnkleFB": 33,
        "RightHipFB": 61,
        "LeftKneeFlex": 102,
        "LeftHipLR": 78,
        "RightAnkleUD": 78,
        "RightHipLR": 78,
    }
}

b80 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 83,
        "RightAnkleFB": 68,
        "RightKneeFlex": 148,
        "LeftHipFB": 122,
        "LeftAnkleFB": 45,
        "RightHipFB": 72,
        "LeftKneeFlex": 102,
        "LeftHipLR": 87,
        "RightAnkleUD": 75,
        "RightHipLR": 80,
    }
}

b81 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 82,
        "RightAnkleFB": 66,
        "RightKneeFlex": 168,
        "LeftHipFB": 136,
        "LeftAnkleFB": 62,
        "RightHipFB": 87,
        "LeftKneeFlex": 113,
        "LeftHipLR": 96,
        "RightAnkleUD": 71,
        "RightHipLR": 84,
    }
}

b82 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 82,
        "RightAnkleFB": 64,
        "RightKneeFlex": 168,
        "LeftHipFB": 143,
        "LeftAnkleFB": 62,
        "RightHipFB": 83,
        "LeftKneeFlex": 113,
        "LeftHipLR": 96,
        "RightAnkleUD": 74,
        "RightHipLR": 93,
    }
}

b83 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 82,
        "RightAnkleFB": 74,
        "RightKneeFlex": 138,
        "LeftHipFB": 157,
        "LeftAnkleFB": 72,
        "RightHipFB": 73,
        "LeftKneeFlex": 113,
        "LeftHipLR": 106,
        "RightAnkleUD": 75,
        "RightHipLR": 93,
    }
}

b84 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 90,
        "RightAnkleFB": 110,
        "RightKneeFlex": 76,
        "LeftHipFB": 120,
        "LeftAnkleFB": 71,
        "RightHipFB": 61,
        "LeftKneeFlex": 106,
        "LeftHipLR": 90,
        "RightAnkleUD": 90,
        "RightHipLR": 90,
    }
}

b85 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 106,
        "RightAnkleFB": 111,
        "RightKneeFlex": 77,
        "LeftHipFB": 126,
        "LeftAnkleFB": 73,
        "RightHipFB": 61,
        "LeftKneeFlex": 106,
        "LeftHipLR": 86,
        "RightAnkleUD": 89,
        "RightHipLR": 81,
    }
}

b86 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 107,
        "RightAnkleFB": 111,
        "RightKneeFlex": 77,
        "LeftHipFB": 126,
        "LeftAnkleFB": 61,
        "RightHipFB": 54,
        "LeftKneeFlex": 118,
        "LeftHipLR": 89,
        "RightAnkleUD": 89,
        "RightHipLR": 74,
    }
}

b87 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 110,
        "RightAnkleFB": 93,
        "RightKneeFlex": 76,
        "LeftHipFB": 113,
        "LeftAnkleFB": 41,
        "RightHipFB": 49,
        "LeftKneeFlex": 134,
        "LeftHipLR": 84,
        "RightAnkleUD": 112,
        "RightHipLR": 70,
    }
}

b88 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 107,
        "RightAnkleFB": 93,
        "RightKneeFlex": 76,
        "LeftHipFB": 86,
        "LeftAnkleFB": 26,
        "RightHipFB": 46,
        "LeftKneeFlex": 135,
        "LeftHipLR": 84,
        "RightAnkleUD": 112,
        "RightHipLR": 70,
    }
}

b89 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 101,
        "RightAnkleFB": 93,
        "RightKneeFlex": 76,
        "LeftHipFB": 80,
        "LeftAnkleFB": 11,
        "RightHipFB": 46,
        "LeftKneeFlex": 155,
        "LeftHipLR": 85,
        "RightAnkleUD": 112,
        "RightHipLR": 75,
    }
}

b90 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 92,
        "RightAnkleFB": 65,
        "RightKneeFlex": 82,
        "LeftHipFB": 83,
        "LeftAnkleFB": 3,
        "RightHipFB": 26,
        "LeftKneeFlex": 148,
        "LeftHipLR": 82,
        "RightAnkleUD": 102,
        "RightHipLR": 70,
    }
}

b91 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 88,
        "RightAnkleFB": 62,
        "RightKneeFlex": 91,
        "LeftHipFB": 98,
        "LeftAnkleFB": 10,
        "RightHipFB": 2,
        "LeftKneeFlex": 121,
        "LeftHipLR": 82,
        "RightAnkleUD": 95,
        "RightHipLR": 75,
    }
}

b92 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 84,
        "RightAnkleFB": 49,
        "RightKneeFlex": 135,
        "LeftHipFB": 103,
        "LeftAnkleFB": 36,
        "RightHipFB": 10,
        "LeftKneeFlex": 87,
        "LeftHipLR": 81,
        "RightAnkleUD": 84,
        "RightHipLR": 81,
    }
}

b93 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 84,
        "RightAnkleFB": 53,
        "RightKneeFlex": 136,
        "LeftHipFB": 121,
        "LeftAnkleFB": 55,
        "RightHipFB": 18,
        "LeftKneeFlex": 102,
        "LeftHipLR": 77,
        "RightAnkleUD": 78,
        "RightHipLR": 76,
    }
}

b94 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 84,
        "RightAnkleFB": 62,
        "RightKneeFlex": 136,
        "LeftHipFB": 119,
        "LeftAnkleFB": 55,
        "RightHipFB": 34,
        "LeftKneeFlex": 116,
        "LeftHipLR": 77,
        "RightAnkleUD": 72,
        "RightHipLR": 73,
    }
}

b95 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 74,
        "RightAnkleFB": 63,
        "RightKneeFlex": 143,
        "LeftHipFB": 137,
        "LeftAnkleFB": 55,
        "RightHipFB": 46,
        "LeftKneeFlex": 120,
        "LeftHipLR": 86,
        "RightAnkleUD": 73,
        "RightHipLR": 66,
    }
}

b96 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 74,
        "RightAnkleFB": 70,
        "RightKneeFlex": 143,
        "LeftHipFB": 142,
        "LeftAnkleFB": 56,
        "RightHipFB": 68,
        "LeftKneeFlex": 120,
        "LeftHipLR": 86,
        "RightAnkleUD": 77,
        "RightHipLR": 70,
    }
}

b97 = {
    "runtime": 1000,
    "angles": {
        "LeftAnkleUD": 74,
        "RightAnkleFB": 76,
        "RightKneeFlex": 150,
        "LeftHipFB": 134,
        "LeftAnkleFB": 55,
        "RightHipFB": 90,
        "LeftKneeFlex": 126,
        "LeftHipLR": 90,
        "RightAnkleUD": 78,
        "RightHipLR": 85,
    }
}

b98 = {
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
    pprint(api_instance.put_servos_angles(b33a))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b34))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b35))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b36))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b37))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b38))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b39))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b40))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b41))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b42))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b43))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b44))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b45))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b46))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b47))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b48))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b49))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b50))
    time.sleep(1.2)
    pprint(api_instance.put_servos_angles(b51))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b52))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b53))
    time.sleep(0.9)
    pprint(api_instance.put_servos_angles(b54))
    time.sleep(0.9)
    pprint(api_instance.put_servos_angles(b55))
    time.sleep(0.9)
    pprint(api_instance.put_servos_angles(b56))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b57))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b58))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b59))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b60))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b61))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b62))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b63))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b64))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b65))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b66))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b67))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b68))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b69))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b70))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b71))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b72))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b73))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b74))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b75))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b76))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b77))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b78))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b79))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b80))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b81))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b82))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b83))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b84))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b85))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b86))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b87))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b88))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b89))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b90))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b91))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b92))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b93))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b94))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b95))
    time.sleep(0.8)
    pprint(api_instance.put_servos_angles(b96))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b97))
    time.sleep(1)
    pprint(api_instance.put_servos_angles(b98))
    time.sleep(1)
except ApiException as e:
    print("Exception when calling ServosApi->put_servos_angles: %s\n" % e)
