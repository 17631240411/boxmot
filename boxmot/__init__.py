# Mikel Broström 🔥 Yolo Tracking 🧾 AGPL-3.0 license

__version__ = '11.0.2'

from boxmot.postprocessing.gsi import gsi
from boxmot.tracker_zoo import create_tracker, get_tracker_config
from boxmot.trackers.botsort.botsort import BotSort
from boxmot.trackers.bytetrack.byte_tracker import ByteTrack
from boxmot.trackers.deepocsort.deep_ocsort import DeepOcSort
from boxmot.trackers.hybridsort.hybridsort import HybridSort
from boxmot.trackers.ocsort.ocsort import OcSort as OcSort
from boxmot.trackers.strongsort.strong_sort import StrongSort
from boxmot.trackers.imprassoc.impr_assoc_tracker import ImprAssocTrack


TRACKERS = ['bytetrack', 'botsort', 'strongsort', 'ocsort', 'deepocsort', 'hybridsort', 'imprassoc']

__all__ = ("__version__",
           "StrongSort", "OcSort", "ByteTrack", "BotSort", "DeepOcSort", "HybridSort", "ImprAssocTrack"
           "create_tracker", "get_tracker_config", "gsi")
