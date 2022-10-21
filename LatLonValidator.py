"""
FelipedelosH

This class is create to validate a integryty of latitude and longitude
"""

class GeoLatLongValidator:
    def __init__(self) -> None:
        pass

    def validates(self, latitude, longitude):
        return self._validatesLatitude(latitude) and self._validatesLongitude(longitude)

    def _validatesLatitude(self, latitude):
        """
        Beetween +-90,90
        """
        try:
            value = float(latitude)
            if value >= -90 and value <= 90:
                return True
            else:
                return False
        except:
            return False 

    def _validatesLongitude(self, longitude):
        """
        Beetween +-180,180
        """
        try:
            value = float(longitude)
            if value >= -180 and value <= 180:
                return True
            else:
                return False
        except:
            return False 

