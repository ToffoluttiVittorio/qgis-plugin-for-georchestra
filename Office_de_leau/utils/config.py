class PluginConfig:
    """
    Classe de configuration pour le plugin Office de l'eau Réunion.
    """
    
    def __init__(self):
        self.title = "Office de l'eau Réunion"
        self.description = "Catalogue de l'Office de l'eau Réunion"
        self.config_data = {
            "title": self.title,
            "description": self.description,
            "type": "folder",
            "children": [
                {
                    "title": "Test titre",
                    "description": "Test descirption de folder",
                    "type": "folder",
                    "children": [
                        {
                            "title": "Plan IGN",
                            "description": "Plan IGN",
                            "metadata_url": "https://geoservices.ign.fr/services-web-essentiels",
                            "type": "wms_layer",
                            "params": {
                                "url": "https://wxs.ign.fr/essentiels/geoportail/r/wms?tiled=true",
                                "name": "GEOGRAPHICALGRIDSYSTEMS.PLANIGNV2",
                                "format": "image/png",
                                "srs": "EPSG:2154"
                            }
                        },
                        {
                            "title": "Scan IGN",
                            "description": "Scans de l'IGN 2017 (scan différent selon l'échelle)",
                            "type": "wms_layer",
                            "metadata_url": "http://www.ign.fr/",
                            "params": {
                                "url": "https://tile.geobretagne.fr/gwc02/service/wms?tiled=true",
                                "name": "carte",
                                "format": "image/png",
                                "srs": "EPSG:2154"
                            }
                        }
                    ]
                }
            ]
        }

    def get_config_data(self):
        """
        Retourne les données de configuration.
        """
        return self.config_data
