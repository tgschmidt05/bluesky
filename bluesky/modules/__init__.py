"""bluesky.modules

This subpackage contains BlueSky modules.  These modules can be implemented
either as python modules or subpackages. All that's required is that the
modules/packages have a run method that can be imported, and that the run
method have the signature:

    def run(fires_manager)

where 'fires_manager' is a bluesky.models.fires.FiresManager obejct

If implemented as a subpackage, the __init__.py just needs to define a run
method or import it from one of it's modules.)
"""

__author__      = "Joel Dubowy"
__copyright__   = "Copyright 2015, AirFire, PNW, USFS"
