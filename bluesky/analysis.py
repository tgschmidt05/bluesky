from bluesky import models, locationutils

class SummarizedFire(dict):

    def __init__(self, fire):
        self.fire = models.fires.Fire(fire)

        self.active_areas = self.fire.active_areas
        self.locations = self.fire.locations
        self.set_lat_lng()
        self.set_flat_summary()

    def set_lat_lng(self):
        lat_lngs = [locationutils.LatLng(l) for l in self.locations]

        def get_min_max(vals):
            return min(vals), max(vals)

        min_lat, max_lat = get_min_max([ll.latitude for ll in lat_lngs])
        min_lng, max_lng = get_min_max([ll.longitude for ll in lat_lngs])

        def format_str(mi, ma):
            return "{} to {}".format(mi, ma) if mi != ma else mi

        self['lat_lng'] = {
            'lat': {
                'min': min_lat,
                'max': max_lat,
                'pretty_str': format_str(min_lat, max_lat),
            },
            'lng': {
                'min': min_lng,
                'max': max_lng,
                'pretty_str': format_str(min_lng, max_lng)
            }
        }

    def set_flat_summary(self):
        self['flat_summary'] = {
            'id': self.fire.get('id'),
            'lat': self['lat_lng']['lat']['pretty_str'],
            'lng':  self['lat_lng']['lng']['pretty_str'],
            'total_consumption': self.fire.consumption['summary']['total'],
            'total_emissions': self.fire.emissions['summary']['total'],
            'PM2.5': self.fire.emissions['summary']['PM2.5'],
            'num_locations': len(self.locations),
            'total_area': sum([l['area'] for l in self.locations]),
            'start': min([aa['start'] for aa in self.active_areas]),
            'end': max([aa['end'] for aa in self.active_areas])
        }