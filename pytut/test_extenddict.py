
class System(dict):
    _keys = "systemId name hardwareProfile os productProfile".split()

    def __init__(self, val = None):
        self['systemId'] = 0
        self['name'] = ""
        self['os'] = OS()

    def __setitem__(self, key, val):
        if key not in self._keys:
            raise KeyError
        dict.__setitem__(self, key, val)
        
class OS(dict):
    _keys = "type version architecture fstype".split()

    def __init__(self, val = None):
        for key in self._keys:
            self[key] = val

    def __setitem__(self, key, val):
        if key not in self._keys:
            raise KeyError
        dict.__setitem__(self, key, val)
        
if __name__ == "__main__":
    system = System()
    print system.__dict__
    
    print system['os']['type']
    system['os']['type'] = base.types.OS.CENTOS
    print system['os']['type']
        
        