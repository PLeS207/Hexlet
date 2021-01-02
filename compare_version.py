def compare_version(version1, version2):
    ver1 = version1.split('.')
    ver2 = version2.split('.')
    if ver1[0] > ver2[0]:
        return 1
    elif ver1[0] < ver2[0]:
        return -1
    if int(ver1[1]) > int(ver2[1]):
        return 1
    elif int(ver1[1]) < int(ver2[1]):
        return -1
    return 0
